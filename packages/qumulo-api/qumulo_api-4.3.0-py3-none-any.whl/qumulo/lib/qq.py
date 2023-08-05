# Copyright (c) 2015 Qumulo, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

# XXX: Please add types to the functions in this file. Static type checking in
# Python prevents bugs!
# mypy: ignore-errors


import argparse
import logging
import os
import socket
import sys
import warnings

import qumulo.commands
import qumulo.lib.auth
import qumulo.lib.opts as opts
import qumulo.lib.request

from qumulo.lib import log

VERSION = 1.0
USER_AGENT = 'qq'


def main_options(parser, endpoint_args=True):
    parser.add_argument(
        '--chunked',
        action='store_true',
        default=qumulo.lib.request.DEFAULT_CHUNKED,
        help='Force chunked transfer encoding for requests',
    )
    parser.add_argument(
        '--chunk-size',
        type=int,
        default=qumulo.lib.request.DEFAULT_CHUNK_SIZE_BYTES,
        help=(
            'Set chunk size in bytes for chunked '
            'transfer encoding (default: %d)' % qumulo.lib.request.DEFAULT_CHUNK_SIZE_BYTES
        ),
    )
    parser.add_argument(
        '--credentials-store',
        default=qumulo.lib.auth.credential_store_filename(),
        help='Write credentials to a custom path',
    )
    parser.add_argument('--debug', action='store_true', default=False)
    parser.add_argument(
        '--no-credentials', action='store_true', default=False, help=argparse.SUPPRESS
    )
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('--version', action='version', version=('%(prog)s ' + str(VERSION)))
    parser.add_argument(
        '--timeout', type=int, default=None, help='Time (in seconds) to wait for response'
    )
    if endpoint_args:
        # simnode/qq_internal wants these arguments omitted
        parser.add_argument('--host', default='localhost')
        parser.add_argument('--port', type=int, default=8000)


def main(args):
    if not logging.root.handlers:
        logging.basicConfig(format='%(message)s')

    if args.debug or args.verbose > 1:
        log.setLevel(level=logging.DEBUG)
    elif args.verbose == 1:
        log.setLevel(level=logging.INFO)

    # Allow DeprecationWarnings to be printed when using qq.
    warnings.simplefilter('default', DeprecationWarning)

    conninfo = qumulo.lib.request.Connection(
        args.host,
        args.port,
        chunked=args.chunked,
        chunk_size=args.chunk_size,
        timeout=args.timeout,
        user_agent=USER_AGENT,
    )

    credentials = qumulo.lib.auth.get_credentials(args.credentials_store)

    # qq help commands are not REST wrappers, and therefore do not need
    # @p conninfo or @p credentials
    if issubclass(args.subcommand, qumulo.lib.opts.HelpCommand):
        args.subcommand.main(args)
    elif args.subcommand:
        args.subcommand.main(conninfo, credentials, args)


def qq_main(argz=None, argv=None):
    if argv is None:
        argv = sys.argv

    try:
        parzer = argparse.ArgumentParser(
            description='Qumulo CLI', add_help=True, prog=os.path.basename(argv[0])
        )
        main_options(parzer)
        argz = opts.parse_options(parzer, argv[1:])

        # If no subcommand is specified, the Namespace object is returned but it is
        # missing the subcommand attribute. See https://bugs.python.org/issue9253
        if not hasattr(argz, 'subcommand'):
            parzer.print_usage()
            print('qq: error: too few arguments; try --help to find a list of usable subcommands.')
            return 1
        main(argz)

    except KeyboardInterrupt:
        print('\nCommand interrupted')
        return 1

    except qumulo.lib.request.RequestError as e:
        # When using QQ RequestError is common and expected. Only print out a
        # terse message about the error by calling pretty_str.
        print(e.pretty_str())
        return 1

    except ValueError as e:
        if os.getenv('DEBUG_CLI') or (argz is not None and argz.debug):
            print('Command error: %s' % str(e))
            raise

        print('Command error: %s' % str(e))
        return 1

    except socket.error as e:
        print('Connection error: %s' % str(e))
        return 1

    return 0


# XXX cwallace: hack to fix DE3114. When a user installs `qq` via pip, the `qq`
# executable they invoke is a short, autogenerated Python script which invokes
# an entry point specified by us. Python-argcomplete < 1.10.1 requires the magic
# string PYTHON_ARGCOMPLETE_OK to be within the first 1024 bytes of an
# executable to perform completion. The easiest way to inject that string into
# the auto-generated `qq` executable is by including it in the entry point name.
#
# python-argcomplete 1.10.1 is able to traverse through the entry point call to
# find an annotation in the original source (e.g. here), but most OS's ship
# older versions (e.g. Ubuntu 20.04 ships 1.8.1).
qq_main_PYTHON_ARGCOMPLETE_OK = qq_main

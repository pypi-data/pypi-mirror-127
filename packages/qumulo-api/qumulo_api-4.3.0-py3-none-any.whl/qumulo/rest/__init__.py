# Copyright (c) 2014 Qumulo, Inc.
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


from qumulo.rest import (
    ad,
    analytics,
    audit,
    auth,
    cluster,
    dns,
    encryption,
    fs,
    ftp,
    groups,
    kerberos,
    ldap,
    network,
    nfs,
    node_state,
    object_replication,
    object_replication_v2,
    quota,
    replication,
    roles,
    shutdown,
    smb,
    snapshot,
    support,
    time_config,
    tree_delete,
    unconfigured_node_operations,
    upgrade,
    upgrade_v2,
    users,
    version,
)

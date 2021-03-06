# Copyright 2014 NEC Corporation.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest.api_schema.compute import parameter_types

create_server = {
    'status_code': [202],
    'response_body': {
        'type': 'object',
        'properties': {
            'server': {
                'type': 'object',
                'properties': {
                    # NOTE: Now the type of 'id' is uuid, but here allows
                    # 'integer' also because old OpenStack uses 'integer'
                    # as a server id.
                    'id': {'type': ['integer', 'string']},
                    'security_groups': {'type': 'array'},
                    'links': parameter_types.links,
                    'adminPass': {'type': 'string'},
                    'OS-DCF:diskConfig': {'type': 'string'}
                },
                # NOTE: OS-DCF:diskConfig is API extension, and some
                # environments return a response without the attribute.
                # So it is not 'required'.
                'required': ['id', 'security_groups', 'links', 'adminPass']
            }
        },
        'required': ['server']
    }
}

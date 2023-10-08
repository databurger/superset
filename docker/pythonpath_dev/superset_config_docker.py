#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# This is an example "local" configuration file. In order to set/override config
# options that ONLY apply to your local environment, simply copy/rename this file
# to docker/pythonpath/superset_config_docker.py
# It ends up being imported by docker/superset_config.py which is loaded by
# superset/config.py
#
import os

from flask_appbuilder.security.manager import AUTH_OAUTH

AUTH_TYPE = AUTH_OAUTH

AZURE_TENANT_ID = os.environ.get("AZURE_TENANT_ID")
# app registration -> overview -> application (client) id
AZURE_CLIENT_ID = os.environ.get("AZURE_CLIENT_ID")
# app registration -> Certificates & secrets -> Client Secrets  -> Value
AZURE_CLIENT_SECRET = os.environ.get("AZURE_CLIENT_SECRET")
# app registration -> overview -> application (client) id
AZURE_RESOURCE = os.environ.get("AZURE_CLIENT_ID")

OAUTH_PROVIDERS = [
    {
        "name": "azure",
        "icon": "fa-windows",
        "token_key": "access_token",
        "remote_app": {
            "client_id": AZURE_CLIENT_ID,
            "client_secret": AZURE_CLIENT_SECRET,
            "api_base_url": f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/oauth2",
            "client_kwargs": {
                "scope": "User.read name preferred_username email profile upn groups",
                "resource": AZURE_RESOURCE,
            },
            "request_token_url": None,
            "access_token_url": f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/oauth2/token",
            "authorize_url": f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/oauth2/authorize",
        },
    },
]

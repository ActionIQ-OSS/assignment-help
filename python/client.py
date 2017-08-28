# Copyright 2016 ActionIQ Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Here's a sample of using Requests
# (http://docs.python-requests.org/en/master/) to make HTTP calls
# to a server. This example assumes that you're calling the server
# defined in server.py

import requests

# Call the /date route with two parameters:
#
# http://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls

date_params = { 'start': '2017/02/02', 'end': '2017/02/03' }
r = requests.post('http://localhost:5000/date', params=date_params)
print("code:{} body:{}".format(r.status_code, r.text))

# Call the /grep route with a body:
#
# http://docs.python-requests.org/en/master/user/quickstart/#make-a-request

pattern = '.*'
r = requests.post('http://localhost:5000/grep', data=pattern)
print("code:{} body:{}".format(r.status_code, r.text))


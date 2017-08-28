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


# For the server we recommend you use Flask: http://flask.pocoo.org/
#
# We have supplied two example routes (/date and /grep) for you below,
# as well as example cURL calls.
#
# To run this server:
#     export FLASK_APP=server.py
#     python -m flask run
#
# If you'd like to use JSON in your requests, we suggest you use the
# built-in JSON library: https://docs.python.org/2/library/json.html

from flask import Flask, request

app = Flask(__name__)

# route example: curl -XPOST "http://127.0.0.1:5000/date?start=2017/02/02&end=2017/02/03"
@app.route("/date", methods=['POST'])
def date():
    date_start = request.args.get('start')
    date_end = request.args.get('end')
    return "search log files between {} and {}".format(date_start, date_end)

# route example: curl -XPOST "http://127.0.0.1:5000/grep" -d ".*"
@app.route("/grep", methods=['POST'])
def grep():
    pattern = request.get_data()
    return "search log files for pattern {}".format(pattern)


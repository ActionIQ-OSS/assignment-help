Read lines from a file:

f = (open(‘foo’), ‘r’)
for line in f:
  print line

https://docs.python.org/2/tutorial/inputoutput.html

List files in a directory:

import os.path
files = [f for f in os.listdir(“foo”) if os.path.isfile(f)]

https://docs.python.org/2/library/os.html

Match a line against a regex:

matches = re.search(‘.*’, ‘line to search’)
matches.group(0)

https://docs.python.org/2/library/re.html

Build an http-based client/server:

JSON: https://docs.python.org/2/library/json.html
WebApp: http://flask.pocoo.org/
Http Library: http://docs.python-requests.org/en/master/

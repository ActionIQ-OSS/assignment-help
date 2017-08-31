#################################
####  SUGGESTED BASIC APIS   ####
#### (no downloads required) ####
#################################

# Basic CLI API : https://docs.python.org/2/library/argparse.html
import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
print args.accumulate(args.integers)


# List files in a directory : https://docs.python.org/2/library/os.html
import os
dir = '/Users/you/aiq/'
files = (f for f in os.listdir(dir) if os.path.isfile(dir+f))
for f in files:
  print f


# Reading lines from a file : https://docs.python.org/2/tutorial/inputoutput.html
onefile = 'foo'
with open(onefile) as f:
  for line in f:
    print line


# Match a line against a regex : https://docs.python.org/2/library/re.html
import re
matches = re.search('a.*q', 'my actioniq test')
print matches.group(0)


# Simple client/server API:
# --- there are a handful of options here.  the builtin framework (SimpleSocket) is okay, but a little verbose
### SimpleSocket : http://www.bogotobogo.com/python/python_network_programming_socketserver_framework_for_network_servers.php
### Easier External APIs (download required, no preference from us)
###### HTTP Requests : http://docs.python-requests.org/en/master/
###### Flask  = http://flask.pocoo.org/ , https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask


# Other helpful docs
# JSON: https://docs.python.org/2/library/json.html

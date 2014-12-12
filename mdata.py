#!/usr/bin/python
import json
import sys
from pprint import pprint
if len(sys.argv) < 2:
	sys.stderr.write('Usage: ' + sys.argv[0] + ' /path/to/json_data_file\n\n')
	sys.exit(1)
file = open(sys.argv[1])
data = json.load(file)
pprint(data[-1]) 
for x in data:
	print '[' + str(x['longitude']) + ' , ' + str(x['latitude']) + ' , ' + str(x['msg_count']) + '],'


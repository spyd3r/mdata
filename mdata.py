#!/usr/bin/python
import json
import sys
from pprint import pprint
file = open(sys.argv[1])
data = json.load(file)
pprint(data[-1]) 
for x in data:
	print '[' + str(x['longitude']) + ' , ' + str(x['latitude']) + ' , ' + str(x['msg_count']) + '],'


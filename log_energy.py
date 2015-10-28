#!/usr/bin/env python

import httplib, urllib
with open('lwrf_electricity_kwh.ak') as f:
	ak = f.read().strip()

#params = urllib.urlencode({'api_key': ak, 'field1':2.5, 'created_at':'2015-12-28 10:29:17'})
params = urllib.urlencode({'api_key': ak, 'field1':3.5})
f = urllib.urlopen("https://api.thingspeak.com/update", data=params)
print f.read()

'''
url = "https://api.thingspeak.com/update?key=%s&field1=7"%ak
print url
f = urllib.urlopen(url)
print f.read()

'''


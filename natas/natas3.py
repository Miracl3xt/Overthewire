

import re
import requests

username='natas3'
password='sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

url='http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' %username
#url structure .so whenerver we change the username the link will automatically change

response =requests.get(url,auth=(username,password))

context=response.text
#storing the response text in context(variable)

#print (context)

print re.findall('natas4:(.*)',context)[0]

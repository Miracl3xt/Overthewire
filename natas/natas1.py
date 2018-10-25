
#!/usr/bin/env python

import re    #re library
import requests #reqquest library to play with HTTP

username='natas2'
password='ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

url= 'http://%s.natas.labs.overthewire.org/' %username
#url structure .so whenerver we change the username the link will automatically change

response=requests.get(url ,auth=(username, password))
# auth to input the username and password

context=response.text
#storing the response text in context(variable)


print (response.text)
#print re.findall('The password for natas3 is (.*)-->', context)[0]
#above code will output only the required string (password) that is specified in (.*) and [0]to scrape
# remember if the context is not present in the webpage then code wont run properly..
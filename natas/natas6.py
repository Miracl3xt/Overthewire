

import re            #regual expression library
import requests 

username='natas6'
password='aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url='http://%s.natas.labs.overthewire.org/' %username

response =requests.post(url, auth=(username,password),data={'secret':'FOEIUWGHFEEUHOFUOIU','submit':'submit'})
#ull find the value for secret in the /index-source.html put this in data make sure to include submit button also

content=response.text

#print (content)

print re.findall("natas7 is (.*)",content)[0]
#re.findall to find specific string in (.*) place.
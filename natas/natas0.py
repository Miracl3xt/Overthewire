
#!/usr/bin/env python

import requests
import re

username ='natas0'
password =username

url ='http://%s.natas.labs.overthewire.org' % username

response = requests.get(url , auth =(username, password))



print (response.text.strip())
import requests
import sys
# this will turn off cert verification

#requests.get('https://localhost:8443/', verify=False)

# disable warning messages
sys.stderr=None

r=requests.get('https://justme.localdomain:8443/', verify='./cert.pem')
print (r.text)

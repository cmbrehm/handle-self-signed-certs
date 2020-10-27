import requests

def lambda_handler(event, context):
    r=requests.get('https://justme.localdomain:8443/', verify='cert.pem')
    print (r.text)
    return r.text

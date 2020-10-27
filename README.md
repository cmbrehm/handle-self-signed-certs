# Overview
This example shows how to connect a Python 3.7 client to an HTTPS server with a self-signed cert

## 1. Start Server
```
cd server
docker build -t ss-httpd .
docker run -p 8443:443 -d ss-httpd:latest
```

To test
`curl --insecure https://localhost:8443`

The cert generated will use a hostname of `justme.localdomain`.  You can add to your `/etc/hosts` file

## 2. Export Cert
The below command will export the certificate to a PEM file
Replace `localhost:8443` with the host:port combo
```
cd client
echo | openssl s_client -connect justme.localdomain:8443 2>&1 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > cert.pem
pip3 install -r requirements.txt
python client.py
```

## 3. Lambda
Install AWS SAM CLI if you haven't yet.
```
cd lambda
cp ../client/cert.pem .
sam build
sam local invoke --docker-network host
```

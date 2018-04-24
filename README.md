# poster

This app uses ssl, to generate a self signed certificate for your system, run this command:
```
openssl req -x509 -newkey rsa:4096 -days 365 -nodes -keyout key.pem -out cert.pem
```
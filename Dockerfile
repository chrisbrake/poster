FROM python:3-jessie
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY . .
RUN openssl req -x509 -newkey rsa:4096 -days 365 -nodes \
    -keyout key.pem -out cert.pem \
    -subj "/C=CA/ST=AB/L=Calgary/O=none/OU=none/CN=none"
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "httpd.py"]

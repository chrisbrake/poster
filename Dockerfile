FROM python:3-jessie
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "httpd.py"]

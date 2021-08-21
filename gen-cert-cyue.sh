#!/usr/bin/env bash

openssl genrsa -out cyue.key 2048

openssl req -new -key cyue.key -out cyue.csr \
  -subj "/C=UN/ST=Cyber/L=Web/O=Engineering Sociaty/OU=Development/CN=cyue.box"

openssl x509 -req -in cyue.csr -CA devca.pem -CAkey devca.key -CAcreateserial \
  -out cyue.crt -days 3650 -sha256 -extfile cyue.ext

# already .crt already in pem format, no need seems
# openssl x509 -in cyue.crt -out cyue.pem

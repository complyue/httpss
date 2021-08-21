#!/usr/bin/env bash

openssl genrsa -out devca.key 2048

openssl req -x509 -new -nodes -key devca.key -sha256 -days 3650 -out devca.pem \
  -subj "/C=UN/ST=Cyber/L=Web/O=Engineering Sociaty/OU=Development/CN=ca.development"

openssl x509 -outform der -in devca.pem -out devca.crt

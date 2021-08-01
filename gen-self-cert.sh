#!/usr/bin/env bash

openssl req -nodes -new -x509 -keyout localdev.pem -out localdev.pem -subj "/C=UN/ST=Cyber/L=Web/O=Engineering Sociaty/OU=Development/CN=localhost"

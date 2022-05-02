@echo off
"C:\Program Files\OpenSSL-Win64\bin\openssl.exe" genrsa -out privkey.pem 4096
"C:\Program Files\OpenSSL-Win64\bin\openssl.exe" req -new -x509 -key privkey.pem -out cacert.pem -days 1095
pause
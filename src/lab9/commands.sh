# Signing and verifying python file
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem

openssl dgst -sha256 -sign private.pem -out main.py.sha256 main.py
openssl enc -base64 -in main.py.sha256 -out main.py.sha256.base64

openssl enc -base64 -d -in main.py.sha256.base64 -out main.py.sha256
openssl dgst -sha256 -verify public.pem -signature main.py.sha256 main.py



# Signing and verifying exe file
openssl req -x509 -newkey rsa:4096 -sha256 -keyout openssl.key -out openssl.crt -days 365
osslsigncode sign -certs openssl.crt -key openssl.key -pass 123456 -n "LAB9" -i http://zozulia.vlad/ -in File.exe -out File_signed.exe
osslsigncode verify -in ne_tanki_signed.exe

# openssl pkcs12 -export -out keyStore.p12 -inkey openssl.key -in openssl.crt
# osslsigncode sign -pkcs12 keyStore.p12 -pass dimASS -n "NE TANKI" -i http:/www.dimass.cum/ -in ne_tanki.exe -out ne_tanki_signed.exe
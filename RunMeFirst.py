from Crypto.PublicKey import RSA
key = RSA.generate(4096)
f = open('my_rsa_public.pem', 'wb')
f.write(key.publickey().exportKey('PEM'))
f.close()
f = open('my_rsa_private.pem', 'wb')
f.write(key.exportKey('PEM'))
f.close()
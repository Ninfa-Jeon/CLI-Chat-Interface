import socket	
from Crypto.PublicKey import RSA
from datetime import datetime

def logger(stat,insert):
    log = open('server log.txt','a')
    if insert=='Thank you for the help':
        log.writelines(stat+': '+insert+'\nClient disconnected\n')
    else:
        log.writelines(stat+': '+insert+'\n')
    log.close()

def encrypted(message):    
    now = datetime.now()
    logger('['+now.strftime("%d/%m/%Y %H:%M:%S")+'] sent',message)
    f = open('my_rsa_public.pem', 'rb')
    key = RSA.importKey(f.read())
    message=message.encode()
    x = key.encrypt(message,32)
    return x
    
def decrypted(encrypted_text):
    f1 = open('my_rsa_private.pem', 'rb')
    key1 = RSA.importKey(f1.read())
    z = key1.decrypt(encrypted_text)
    z=z.decode()
    logger('['+now.strftime("%d/%m/%Y %H:%M:%S")+'] received',z)
    return z

s = socket.socket()		 
print("Socket successfully created")

port = 12345				

s.bind(('127.0.0.1', port))		 
print("socket bound to ",port) 

s.listen(19)	 
print("socket is listening")		

while True: 
    try:
        c, addr = s.accept()	 
        print('Got connection from', addr ) 
        now = datetime.now()
        timelog=str(addr)+' at '+now.strftime("%d/%m/%Y %H:%M:%S")
        logger('\nclient', timelog)
        greeting = 'Thank you for connecting'
        greeting = encrypted(greeting)
        c.send(greeting[0])    
        while True:
            z=decrypted(c.recv(1024))   
            print(z)
            if z=='Thank you for the help':
                print('Client disconnected\n')
                break
            x=input('>>>')
            x=encrypted(x)
            c.send(x[0]) 
        c.close()
    except:
        print('Socket logging out')
        break
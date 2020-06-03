# Import socket module 
import socket			 
from Crypto.PublicKey import RSA
import random
nums = 2
from datetime import datetime

def logger(stat,insert):
    log = open('client2 log.txt','a')
    if insert=='Thank you for the help':
        log.writelines(stat+': '+insert+'\nConnection closed\n')
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
    now = datetime.now()
    f1 = open('my_rsa_private.pem', 'rb')
    key1 = RSA.importKey(f1.read())
    z = key1.decrypt(encrypted_text)
    z=z.decode()
    logger('['+now.strftime("%d/%m/%Y %H:%M:%S")+'] received',z)
    return z

def fileCall():
    global nums
    if nums == 0:
        return 'Thank you for the help'
    n = random.randint(0,9)
    f = open('message.txt','r')
    ls=f.readlines()
    nums-=1
    f.close()
    retrieved = ls[n]
    retrieved = retrieved[:len(retrieved)-1]
    return(retrieved) 
# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12345			

# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
now = datetime.now()
timelog=' at '+now.strftime("%d/%m/%Y %H:%M:%S")
logger('\nConnected to server', timelog)
# receive data from the server 
greeting= s.recv(1024)
print(decrypted(greeting))
while True:
    z=fileCall()
    print('>>>'+z)
    msg=encrypted(z)
    s.sendall(msg[0]) 
    if z=='Thank you for the help':
        print('Connection closed') 
        s.close()	 
        break
    print(decrypted(s.recv(1024)))
# close the connection


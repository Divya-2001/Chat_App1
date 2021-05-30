
import socket
import os
import threading
import pyfiglet
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
IP = input("Enter your ip:-")
Port=1021
ReceiverIp = input("Enter Receiver's Ip:-")
s.bind((IP,Port))
print("\n\n")
print("Welcome to Chat App")


def Receive():
       os.system("tput setaf 2")
       while True:
         Input=s.recvfrom(1021)
         Client=Input[1][0]
         Msg=Input[0]
         print("\t\t" + Msg.decode())
         if(Msg.decode() == "exit"):
              os.system("tput setaf 7")
              exit (0) 

def Send():
    while True:
        Msg=input("")
        s.sendto(Msg.encode(), (ReceiverIp,1024))  
        if (Msg.encode() == "exit"):
            os.system("tpuf setaf 8")
            exit(0)
    
z1=threading.Thread(target=Receive)
z2=threading.Thread(target=Send)

z1.start()
z2.start()

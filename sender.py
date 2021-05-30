import socket
import os
import threading
import pyfiglet
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
IP="192.168.1.23"
Port=1024
s.bind((IP,Port))

print("\n\n")
print(pyfiglet.figlet_format("Welcome to Chat App!",font="digital"))

def Send():
     while True:
        Msg=input("")
        s.sendto(Msg.encode(), ("192.168.1.51",1021))
        if (Msg.encode() == "exit"):
            os.system("tput setaf 8")
            exit(0)
            
def Receive():
      os.system("tput setaf 4")
      while True:
        Input=s.recvfrom(1024)
        Client=Input[1][0]
        Msg=Input[0]
        print("\t\t"+ Msg.decode())
        if (Msg.decode() == "exit"):
            os.system("tput setaf 7")
            exit (0)



T1=threading.Thread(target=Send)
T2=threading.Thread(target=Receive)

T1.start()
T2.start()


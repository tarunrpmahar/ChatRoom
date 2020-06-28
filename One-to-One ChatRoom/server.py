import socket
import sys
import time

## end of imports

###init
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host= socket.gethostname()
print("server will start on host: ",host)
port= 8080
s.bind((host, port))
print("")
print("server done binding to host and port successfully")
print("")
print("server is waiting for incoming connections")
print("")
s.listen(1)
conn, addr= s.accept()
print(addr, "has connected to the server and is now online...")
print("")
while 1:
    message= input(str(">>"))
    message= message.encode()
    conn.send(message)
    print("message has been sent...")
    print("")
    incoming_message= conn.recv(1024)
    incoming_message= incoming_message.decode()
    print("client: ", incoming_message)
    print("")



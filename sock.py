import socket
import os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",5000))

errcnt = 0

while True:
    try:
        rcv = s.recvfrom(1024)
        print("> "+rcv[0].decode("utf-8"))
        c = os.popen(rcv[0].decode("utf-8"))
        cm = c.read(2048)
        print(cm)
        print(rcv[1])
        s.sendto(cm.encode("utf-8"),rcv[1])
    except:
        print("Err.")
        errcnt+=1
        print(errcnt)
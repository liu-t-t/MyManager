#!python3
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

a = socket.gethostbyname("cn-cd-txy-1.starryah.com")

addr=(a,5000)
ipt = ""

while True:
    try:
        ipt = input("> ")
#        if ipt=="^D":
#            break
        s.sendto(ipt.encode("utf-8"),addr)
        rcv = s.recvfrom(1024)
        print(rcv[0].decode("utf-8"))
        print(rcv[1])
    except KeyboardInterrupt:
        print("Abort.")
        break
    except ConnectionError:
        print("Server Shutdown!")
    except:
        print("Other Error!")
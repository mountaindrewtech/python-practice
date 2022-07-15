#Drew Schmidt 7/15/22
#Python practice from TCM Security's Python for Behginners Course
#Terrible port scanner

import sys
import socket
from datetime import datetime

#Define our target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate to ipv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
#print("Scanning target: " + target)
#print("Time started: " + str(datetime.now()))

#python 3 new method

print(f"Scanning Target {target}.")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    for port in range(50,85): #only a few since this unthreaded script and bad
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()
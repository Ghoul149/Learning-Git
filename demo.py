
from time import sleep
from threading import Thread
import time
import win32api
import sys
snooziness = int(input('Enter the amount of seconds you want to run this: '))
stdoutOrigin=sys.stdout 
sys.stdout = open("log.txt", "w")
def some_task():
    while True:
        a=win32api.GetKeyState(0x42)
        if a<0:
            print("B is Pressed")
            time.sleep(0.2)
    
    
timet = Thread(target=some_task)
timet.daemon = True
timet.start()
print("*****************************************")
print("This is the Python keywoard sniffing tool")
print("*****************************************")

sleep(snooziness)
sys.stdout.close()
sys.stdout=stdoutOrigin
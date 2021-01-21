import os
lib = input("""
[1] Download lib & update
[2] pass

[+] Please Choice >> """)

if lib == "1":
    os.system('pip install socket')
    os.system('pip install colorama')
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

import socket
import threading
import time
from queue import Queue
from colorama import *

queue = Queue()
open_ports = []
os.system('color')

banner = (Fore.YELLOW + """
[!] - instagram : @sac.hk 
[!] - Free By : @AB_A3 on Telegram

 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓     ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒   ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░    ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░      ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░       ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░       ░ ░ ░ ▒    ░░   ░   ░         ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
             ░ ░     ░                       ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
"""+Style.RESET_ALL)
print(banner)
print(Fore.YELLOW + '========================================='+ Style.RESET_ALL)
target = input(Fore.CYAN +"[+] Enter The Url (like : example.com) >> "+ Style.RESET_ALL)

if target =="":
    print('[!] I didnt find this URL')
    time.sleep(3)
    exit()
else:
    pass

nport = input(Fore.CYAN +'[+] Range Of Ports (Default : 1024) >> '+ Style.RESET_ALL)

if nport == "":
    nport = 1024
else:
    nport = nport

thr = input(Fore.CYAN +'[+] Thread (Default : 100) >> '+ Style.RESET_ALL)

if thr =="":
    thr = 100
else:
    thr = thr


def getIP():
    global target
    global hostIP
    try:
        hostIP = socket.gethostbyname(target)
    except socket.gaierror:
        print('[!] The Url is not valid ..')
        what = input(Fore.CYAN + '[+] Enter [t] to try again or press Enter to get out >> '+ Style.RESET_ALL)
        if what == 't':
            target = input(Fore.CYAN +'[+] Enter The Url (like : example.com) >> '+ Style.RESET_ALL)
            if target =="":
                print('[!] I didnt find this URL')
                time.sleep(3)
                exit()
            else:
                target = target
                hostIP = socket.gethostbyname(target)
        elif what == "":
            time.sleep(3)
            exit()
        else:
            time.sleep(3)
            exit()
        
        return(hostIP)
getIP()

def portscan(port):
    global hostIP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((hostIP, port))
        return True
    except:
        #print(Fore.RED + '[!] Error in Connect'+Style.RESET_ALL)
        return False
    
def fill(port_list):
    for port in port_list:
        queue.put(port)

def scan():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(Fore.GREEN + f'[-] Port {port} is open'+Style.RESET_ALL)
            open_ports.append(port)

port_list = range(1,int(nport))
fill(port_list)

thread_list = []
for t in range(int(thr)):
    thread = threading.Thread(target=scan)
    thread_list.append(thread)
    
for thread in thread_list:
    thread.start()
    
for thread in thread_list:
    thread.join()
    
#Coded By: @o_7ay || insta : @o.7ay

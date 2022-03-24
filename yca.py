from io import BytesIO 
import pycurl 
import os 
import requests 
import threading 
from multiprocessing.dummy import Pool,Lock 
from bs4 import BeautifulSoup 
import time 
import smtplib,sys,ctypes 
from random import choice 
from colorama import Fore 
from colorama import Style 
from colorama import init 
import socket 
from requests.adapters import HTTPAdapter 
import sys 
import random 
import requests, threading, os 
import os.path 
import json 
init(autoreset=True) 
fr = Fore.RED 
gr = Fore.BLUE 
fc = Fore.CYAN 
fw = Fore.WHITE 
fy = Fore.YELLOW 
fg = Fore.GREEN 
sd = Style.DIM 
sn = Style.NORMAL 
sb = Style.BRIGHT 
from random import choice 
 
headers = {} 
print('''
dP    dP  88888888b              dP     dP   .d888888   a88888b. dP     dP 
Y8.  .8P  88                     88     88  d8'    88  d8'   `88 88   .d8' 
 Y8aa8P  a88aaaa                 88aaaaa88a 88aaaaa88a 88        88aaa8P'  
   88     88                     88     88  88     88  88        88   `8b. 
   88     88                     88     88  88     88  Y8.   .88 88     88 
   dP     88888888P              dP     dP  88     88   Y88888P' dP     dP 
                    oooooooooooo                                           
\033[2;37;40m\033[1;37;41m coded by ye_hack  
\033[2;37;40m\033[1;37;41m  Mass Windows Server Detector''') 
 
def display_header(header_line): 
    header_line = header_line.decode('utf-8') 
    if ':' not in header_line: 
        return 
    h_name, h_value = header_line.split(':', 1) 
    h_name = h_name.strip() 
    h_value = h_value.strip() 
    headers[h_name] = h_value 
 
def main(site): 
    b_obj = BytesIO() 
    ip = socket.gethostbyname(site) 
    crl = pycurl.Curl() 
    crl.setopt(crl.URL, site) 
    crl.setopt(crl.HEADERFUNCTION, display_header) 
    crl.setopt(crl.WRITEDATA, b_obj) 
    crl.perform() 
    if "Microsoft" in headers["Server"]: 
        print(fg+'-' * 60) 
        print(fy+"*Hostname    : " + site) 
        print(fy+"*IIS Version : " + headers["Server"]) 
        print(fy+"*Powered By  : " + headers["X-Powered-By"]) 
        print(fy+"*IP    : " + ip) 
        print(fg+'-' * 60) 
        open('windows_detected.txt', 'a').write("http://"+site+'\n') 
        open('windows_ip.txt', 'a').write(ip+'\n') 
    else: 
        print(fw+"["+fc+"YE_HACK-1337"+fw+"] "+ site +fc+" >> "+fr+"not windows") 
 
def overthinker(): 
    file_name = open(input(Fore.WHITE+'Website List : '),'r').read().replace('http://', '').replace('https://', '').replace('/', '').splitlines() 
    TEXTList = [list.strip() for list in file_name] 
    p = Pool(int(input('Thread : '))) 
    p.map(main, TEXTList) 
    main(site) 
 
overthinker()
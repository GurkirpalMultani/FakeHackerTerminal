import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def typing(word):
    for char in word:
        time.sleep(.1)
        print(char, end='')
    print("")

def dump_password(username,password):
    print(Fore.CYAN+username+":"+Fore.RED+password+Fore.WHITE)    

def dump_hash(username,hash):
    print(Fore.CYAN+username+":500:aad3b435b51404eeaad3b435b51404ee:"+Fore.RED+hash+Fore.CYAN+":::")    

def typing(command):
    for char in command:
        time.sleep(.1)
        print(char, end='')
    print("")

def meterpreter(command):
    print(Fore.GREEN+"meterpreter > ", end="", flush=True)
    for char in command:
        time.sleep(.1)
        print(char, end='')
    print("")

def meterpreter_rdp(command):
    print(Fore.GREEN+"meterpreter post("+Fore.RED+"enable_rdp"+Fore.GREEN+") > ", end="", flush=True)
    for char in command:
        time.sleep(.1)
        print(char, end='')
    print("")

# Start

print("")
time.sleep(1)
print(Fore.GREEN + "[msf]("+Fore.YELLOW+"Jobs:"+Fore.GREEN+"0 "+Fore.LIGHTBLUE_EX+"Agents:"+Fore.GREEN+"0) exploit("+Fore.RED+"multi/handler"+Fore.GREEN+") >> ", end="", flush=True)
time.sleep(1)
typing("exploit")
time.sleep(1)
print(Fore.LIGHTBLUE_EX+"[*]"+Fore.GREEN+" Started reverse TCP handler on 10.0.2.15:4444")
time.sleep(3)
print(Fore.LIGHTBLUE_EX+"[*]"+Fore.GREEN+" Sending stage (980808 bytes) to 10.10.146.10")
time.sleep(1)
print(Fore.LIGHTBLUE_EX+"[*]"+Fore.GREEN+" Meterpreter session 1 opened (10.0.2.15:4444 → 10.10.146.10:33396)")
print("")
time.sleep(1)
meterpreter("getuid")
time.sleep(1)
print(Fore.CYAN+"Server username: LAPTOP-67FLDS23U\JoeBlogs")
print("")
time.sleep(1)
meterpreter("ipconfig")
time.sleep(1)
print(Fore.CYAN+"""
MS TCP Loopback interface
Hardware MAC: 00:00:00:00:00:00
IP Address  : 127.0.0.1
Netmask     : 255.0.0.0

AMD PCNET Family PCI Ethernet Adapter - Packet Scheduler Miniport
Hardware MAC: 00:0c:29:10:f5:15
IP Address  : 10.10.146.10
Netmask     : 255.255.0.0
""")
print("")
time.sleep(1)
meterpreter("getsystem")
time.sleep(2)
print(Fore.CYAN+"... got system via technique 1 (Named Pipe Impresonation (In Memory/Admin)).")
print("")
time.sleep(1)
meterpreter("run post/windows/gather/hashdump")
time.sleep(3)
print(Fore.LIGHTBLUE_EX+"[*]"+Fore.GREEN+" Obtaining the user list and keys...")
time.sleep(.5)
print(Fore.LIGHTBLUE_EX+"[*]"+Fore.GREEN+" Decrypting user keys...")
time.sleep(.5)
print(Fore.LIGHTBLUE_EX+"[*]"+Fore.GREEN+" Dumping cleartext passwords...")
time.sleep(2)
print("")
dump_password("Administrator","1234567890")
dump_password("JoeBlogs","password123!")
print("")
time.sleep(.5)
print(Fore.LIGHTBLUE_EX+"[*]"+Fore.GREEN+" Dumping password hashes...")
print("")
time.sleep(2)
dump_hash("Administrator","8AF326AA4850225B75C592D4CE19CCF5")
dump_hash("JoeBlogs","8119935C5F7FA5F57135620C8073AACA")
print("")
time.sleep(1)
meterpreter("run post/windows/manage/enable_rdp")
time.sleep(1)
meterpreter_rdp("set SESSION 1")
time.sleep(.5)
print(Fore.GREEN+"SESSION => 1")
time.sleep(1)
meterpreter_rdp("exploit")
print("")
time.sleep(2)
print(Fore.LIGHTBLUE_EX+"[*]"+Fore.GREEN+" Enabling Remote Desktop")
time.sleep(.5)
print(Fore.LIGHTBLUE_EX+"[*]"+Fore.GREEN+" Opening port on local firewall...")
time.sleep(.5)
print(Fore.LIGHTBLUE_EX+"[*]"+Fore.GREEN+" Module Completed Successfully")
time.sleep(1)

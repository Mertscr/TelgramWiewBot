from configparser import ConfigParser
from threading import active_count
from time import sleep as swait
from os import system, name
from telegram import Api
from re import search
from sys import exit


THREADS = 400
LOGO = '''
   ~ Telegram Auto Views V3 ~
   
  



 | \  /|  |-  |---|     _____
 |  \/ |  |_  | - |       |
 |     |  |_  | \         |
              |  \        |
 

                                
BU TOOL MERT TARAFINDAN YAPILMIŞTIR 🔥


                          
                                         
          ~ Telegram:@Merttzzt ~
         ~                       ~
'''

error_file = open('errors.txt', 'a+', encoding='utf-8')
logger = lambda error: error_file.write(f'{error}\n')


def config_loader():
    try: 
        cfg = ConfigParser(interpolation=None)
        cfg.read("config.ini", encoding="utf-8")
        return (
            cfg["HTTP"].get("Sources").splitlines(), 
            cfg["SOCKS4"].get("Sources").splitlines(), 
            cfg["SOCKS5"].get("Sources").splitlines()
        )
    except KeyError: 
        print(' [ Error ] config.ini not found!')
        swait(3)
        exit()


def input_loader():
    url_input = search(r'(https?:\/\/t\.me\/)?([^/]+)/(\d+)', input(' [ INPUT ] Paylaşımın linkini qeyd edin!: '))
    if url_input: 
        _, channel, post = url_input.groups()
        return channel, post
    else: 
        print(' [ ERROR ] Kanal veya Post Tapılmadı!')
        swait(3)
        exit()


def display():
    print(' [ OUTPUT ] Started ( 10,20 saniyə ərzində başladılır!)');swait(7)
    while int(active_count()) < THREADS-100: swait(0.05)
    system('cls' if name == 'nt' else 'clear')
    
    def inner():
        print(LOGO)
        print(f'''
    [ Live Views ]: {Api.real_views}

    [ Token Errors ]:   {Api.token_errors}
    [ Proxies Errors ]: {Api.proxy_errors}

    [ Threads ]: {active_count()}
        ''')
    
    return inner

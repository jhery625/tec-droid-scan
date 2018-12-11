#!/usr/bin/env python
from urllib2 import *
from platform import system
import sys
def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
banner = '''
	\033[93m
 _____  ___    ___       ___    ___    _____  _  ___   
(_   _)(  _`\ (  _`\    (  _`\ |  _`\ (  _  )(_)(  _`\ 
  | |  | (_(_)| ( (_)   | | ) || (_) )| ( ) || || | ) |
  | |  |  _)_ | |  _    | | | )| ,  / | | | || || | | )
  | |  | (_( )| (_( )   | |_) || |\ \ | (_) || || |_) |
  (_)  (____/'(____/'   (____/'(_) (_)(_____)(_)(____/'                                                                  
\033[96m       ============= TEC DROID ===========
'''
print banner
def menu():
   print'''
\033[91m 1 \033[93m)\033[94m SCANNER DE PUERTOS

\033[91m 2 \033[93m)\033[94m STATUS 

\033[91m 3 \033[93m)\033[94m BUSCADO DE HOST

\033[91m 4 \033[93m)\033[94m CREDITOS!!!

\033[91m 0 \033[93m)\033[94m Salir
'''
slowprint("\033[1;91m   PACK DE UTILITARIOS PARA  SCANNEAR SUBDOMINIOS")
slowprint("\033[1;92m     MENU:")

menu()
def ext():
    ex = raw_input ('\033[94mContinuar/Salir [C/S] ====> ')
    if ex[0].upper() == 'S' :
           print 'Saliendo!!!'
           exit()
    else:
           clear()
           print banner
           menu()
           select()

def  select():
  try:
    joker = input("\033[91mPresiona \033[92m0/\033[93m4 ====>  ")
    if joker == 1:
      dz = raw_input('\033[96mPon la url de la pagina web : \033[92m')
      port = "http://api.hackertarget.com/nmap/?q=" + dz
      scan = urlopen(port).read()
      print (scan)
      ext()
    elif joker == 2:
      dz = raw_input('\033[91mPon la url de la pagina web :\033[93m')
      hea = "http://api.hackertarget.com/httpheaders/?q=" + dz
      der =  urlopen(hea).read()
      print (der)
      ext()
    elif joker == 3:
      dz = raw_input('\033[94mPon la url de la pagina web :\033[92m')
      host = "http://api.hackertarget.com/hostsearch/?q=" + dz
      finder = urlopen(host).read()
      print (finder)
      ext()
    elif joker == 4:
      slowprint("TEC DROID \033[92m")
      slowprint("********************************")
      slowprint("SCRIPT NUNCA DEJES DE APRENDER \033[96m")
      slowprint("*****************************************")
      slowprint("CANAL DE YOUTUBE: https://www.youtube.com/c/TECDROIDPE \033[91m")
      slowprint("**********************")
      slowprint("WHATSAPP : +51926504432 \033[96m ")
	  slowprint("CANAL DE TELEGRAM : t.me/tecdroidp \033[96m ")
	  slowprint("TELEGRAM : @jhere \033[96m ")
      slowprint("********************** ")
      ext() 
    elif joker == 0:
      print "Saliendo!!"
      ext()
  except(KeyboardInterrupt):
    print "\nCtrl + C -> Exiting!!"
select()

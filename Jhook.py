import sys
import requests
import os
import time
from pystyle import Colors, Colorate , Write, Colors
from colorama import Fore
from pyotp import TOTP
os.system(f'cls & mode 85,20 & title Jhook! Version 1.3!')

def main():
   menu()

def menu():
   choices = Write.Input("""
   /$$$$$       /$$   /$$                     /$$            
   |__  $$      | $$  | $$                    | $$            
      | $$      | $$  | $$  /$$$$$$   /$$$$$$ | $$   /$$      
      | $$      | $$$$$$$$ /$$__  $$ /$$__  $$| $$  /$$/      
 /$$  | $$      | $$__  $$| $$  \ $$| $$  \ $$| $$$$$$/       
| $$  | $$      | $$  | $$| $$  | $$| $$  | $$| $$_  $$       
|  $$$$$$/      | $$  | $$|  $$$$$$/|  $$$$$$/| $$ \  $$      
 \______/       |__/  |__/ \______/  \______/ |__/  \__/                   

    Made By Josè#0001,TheSoap1#9870                                                                                                                  
[1] Webhook Checker
[2] Webhook Sender/Deleter
[3] Webhook Spammer
[4] Webhook Protector Spammer
[5] Exit
Enter A Option ->""",Colors.white_to_red, interval=0.0)
   if choices == "1":
    checker()
   elif choices =="2":
        sender()
   elif choices =="3":
        spammer()
   elif choices == "4":
    apis()
   elif choices =="5":
        sys.exit
   else:
         print("Enter The Right Option!")
         time.sleep(3)
         menu()



def checker():
    webhook = Write.Input("Enter Your Webhook Url:",Colors.white_to_red, interval=0.01)
    r = requests.get(webhook)
    if r.status_code == 200:
         Write.Print("Webhook Is Working",Colors.white_to_green, interval=0.01)
         time.sleep(2)
         os.system("cls")
         menu()
    else:
       Write.Print("Webhook Is Not Working",Colors.white_to_green, interval=0.01)
       time.sleep(2)
       os.system("cls")
       menu()
      
def sender():
    webhook = Write.Input("Enter Your Webhook Url:",Colors.white_to_red, interval=0.01)
    name =  Write.Input("Enter Username For Webhook Url:",Colors.white_to_red, interval=0.01)
    avatar = Write.Input("Enter Avatar Url For Webhook Url:",Colors.white_to_red, interval=0.01)
    message = Write.Input("Enter Your Message Here:",Colors.white_to_red, interval=0.01)
    send = requests.post(webhook, json={"content" : message, "username": name, "avatar_url": avatar})
    time.sleep(2)
    r = requests.get(webhook)
    if r.status_code == 404:
            Write.Print(f"Webhook Fail To Delete And Failed To Send",Colors.white_to_blue, interval=0.01)
            time.sleep(2)
            os.system('cls')
            menu()
    else:
        requests.delete(webhook)
        Write.Print("Message Sent Sucessfully And Webhook Was Sucessfully Deleted",Colors.white_to_green, interval=0.01)
        time.sleep(2)
        os.system('cls')
        menu()

def apis():
     api = Write.Input("Enter Your Api Url:",Colors.white_to_red, interval=0.01)
     pass32 = Write.Input("Enter The Apis Password:",Colors.white_to_red, interval=0.01)
     name =  Write.Input("Enter Username:",Colors.white_to_red, interval=0.01)
     avatar = Write.Input("Enter Avatar Url:",Colors.white_to_red, interval=0.01)
     message = Write.Input("Enter Your Message Here:",Colors.white_to_red, interval=0.01)
     amount = int(Write.Input("Enter The Amount Of Messages Here:",Colors.white_to_red, interval=0.01))
     key = TOTP(pass32).now()
     for i in range(amount):
        r = requests.post(api,headers={"Authorization": key}, json={"content" : message, "username": name, "avatar_url": avatar})
        session = {200,204}
        if r.status_code in session:
            Write.Print(f"Sent Message Sucessfully\n",Colors.white_to_green, interval=0.0)
        elif r.status_code == 429:
            print(f"{Fore.MAGENTA}You Are Being Rate Limited ({r.json()['retry_after']}ms){Fore.RESET}")
            time.sleep(r.json()["retry_after"] / 1000)
        else:
            Write.Print(f'Api Dosent Exist',Colors.white_to_red, interval=0.01)
            time.sleep(2)
            os.system('cls')
            menu()
                


def spammer():
   webhook = Write.Input("Enter Your Webhook Url:",Colors.white_to_red, interval=0.01)
   name =  Write.Input("Enter Username For Webhook Url:",Colors.white_to_red, interval=0.01)
   avatar = Write.Input("Enter Avatar Url For Webhook Url:",Colors.white_to_red, interval=0.01)
   message = Write.Input("Enter Your Message Here:",Colors.white_to_red, interval=0.01)
   amount = int(Write.Input("Enter The Amount Of Messages Here:",Colors.white_to_red, interval=0.01))
   for i in range(amount):
    r = requests.post(webhook, json={"content" : message, "username": name, "avatar_url": avatar})
    session = {200,204}
    if r.status_code in session:
        Write.Print(f"Sent Message Sucessfully\n",Colors.white_to_green, interval=0.0)
        
    elif r.status_code == 429:
        print(f"{Fore.MAGENTA}You Are Being Rate Limited ({r.json()['retry_after']}ms){Fore.RESET}")
        time.sleep(r.json()["retry_after"] / 1000)

    else:
      Write.Print(f'Webhook Deleted',Colors.white_to_red, interval=0.01)
      time.sleep(2)
      os.system('cls')
      menu()
    

main()

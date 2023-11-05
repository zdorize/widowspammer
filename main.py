import requests
import time
from colorama import Fore
import os
from func.clear import clear
from func.loading import loading
from func.title import setTitle

os.system('cls')
banner = fr'''{Fore.LIGHTRED_EX}   +--------------[{Fore.RED}Widow Spammer {Fore.LIGHTRED_EX}v1.0{Fore.LIGHTRED_EX}]------------------------------------
   :". /  /  /
   :.-". /  /
   : _.-". /
   :"  _.-".
   :-""     ".
   :
   :
 ^.-.^
'^\+/^`
'/`"'\`

                        ┌──────────────────────┐
                        │ [{Fore.RED}1{Fore.LIGHTRED_EX}] {Fore.RESET} Spam Webhook    {Fore.LIGHTRED_EX}│
                        │ [{Fore.RED}2{Fore.LIGHTRED_EX}] {Fore.RESET} Delete Webhook  {Fore.LIGHTRED_EX}│
                        └──────────────────────┘
{Fore.LIGHTRED_EX}┌──(widow㉿{os.getlogin()})-[~]'''

def main():
    clear()
    print(banner)
    choice = input(
        f'{Fore.LIGHTRED_EX}└─$ {Fore.RED}')

    if choice == "1":
        clear()
        print(banner)
        webhook = input(f'{Fore.LIGHTRED_EX}┝ Webhook: {Fore.LIGHTRED_EX}')
        message = input(f'{Fore.LIGHTRED_EX}└─ Message: {Fore.LIGHTRED_EX}')
        data = {
            "content" : f"{message}",
        }
        def spam():
            time.sleep(0.2)
            sendmessage = requests.post(webhook, json = data)
            try:
                sendmessage.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print(fr'{Fore.RED}└─ Webhook is invalid!')
                time.sleep(1)
                main()
            else:
                print(fr'{Fore.LIGHTRED_EX}└─ Successfully sent "{message}" to the webhook!')
            spam()
        spam()

    elif choice == "2":
        time.sleep(0.5)
        webhook = input(f'{Fore.LIGHTRED_EX}└─ Webhook: {Fore.LIGHTRED_EX}')
        sendmessage = requests.delete(webhook)
        try:
            sendmessage.exceptions.raise_fore_status()
        except requests.exceptions.HTTPError as e:
            print(fr'{Fore.RED}└─ This webhook has already been deleted.')
            time.sleep(1)
            main()
        else:
            print(fr'{Fore.LIGHTRED_EX}Successfully deleted {webhook}!')
    else:
        main()

setTitle("Widow Spammer v1.0")
clear()
loading()
time.sleep(1.5)
main()          
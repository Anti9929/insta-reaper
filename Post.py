import requests
import sys
from bs4 import BeautifulSoup
import json

url = "https://help.instagram.com/ajax/help/contact/submit/page"

print(""" ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄ 
█   █   █ █      █ █ █   ▐ █    █  ▐ 
▐  █▀▀▀▀  █      █    ▀▄   ▐   █     
   █      ▀▄    ▄▀ ▀▄   █     █      
 ▄▀         ▀▀▀▀    █▀▀▀    ▄▀       
█                   ▐      █         
▐                          ▐         
---------------------------------------
1 - Report on a photo ?
2 - Report on a Video ? 

    """)
ghost = input ("-> ")
if ghost == '1':
    ss = input ('Enter the URL of the photo  -> ')
    ss1 = input('Please type the exact comment as it appears on Instagram -> ')
    ss2 = input ('A description of why this comment is abusive -> ')
    payload = """
jazoest=2975&lsd=AVoTJSxOoMU&Field838322882850639=yes&Field666972826719090=photo&Field218593448349930="""+ss+"""&Field746802935372128=&exactcomment="""+ss1+"""&Field256548277850457="""+ss2+"""&Field1435723373333548_iso2_country_code=&Field1435723373333548=sa&sneaky=&support_form_id=424745097661047&support_form_hidden_fields=%7B%22838322882850639%22%3Afalse%2C%22666972826719090%22%3Afalse%2C%22290540267769404%22%3Atrue%2C%22218593448349930%22%3Afalse%2C%22746802935372128%22%3Atrue%2C%221421990228055493%22%3Afalse%2C%22537927836328053%22%3Afalse%2C%22256548277850457%22%3Afalse%2C%221435723373333548%22%3Afalse%2C%22755709437786995%22%3Afalse%7D&support_form_fact_false_fields=[]&__user=0&__a=1&__dyn=7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEy58ogbUuw9-3K4o1j8hwem0nCq1ewcG0KEswaq3a2W2y0umUS1kyE1e42C220gG0D87u1zw9O0RE2Jw8W0hC&__csr=&__req=c&__beoa=0&__pc=PHASED%3ADEFAULT&dpr=1&__ccg=GOOD&__rev=1002880359&__s=w4onwn%3Aov25hx%3A2c6bry&__hsi=6887565373536777664-0&__comet_req=0&__spin_r=1002880359&__spin_b=trunk&__spin_t=1603636279"""
    headers = {
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "help.instagram.com",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://help.instagram.com/contact/424745097661047",
        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
        "Content-Length": "1057",
        "Cookie":"datr=rXuVXyeOlvJlzTAgpOPnnpUi"

           }

    response = requests.post (url, data=payload, headers=headers)
    if 'for' in response.text:
        print(' -'* 15)
        print (whiteB_color +'The report was sent successfully ( ok )')
    elif "payload" in response.text:
        print('Sorry, there is an error')

    print ("")
    print (" -" * 15)
    exit ()

# _______________________________________

if falah == '2':
        ss = input ('Enter the URL of the Video  -> ')
        ss1 = input ('Please type the exact comment as it appears on Instagram -> ')
        ss2 = input ('A description of why this comment is abusive -> ')
        payload = """
    jazoest=2975&lsd=AVoTJSxOoMU&Field838322882850639=yes&Field666972826719090=Video&Field218593448349930=""" + ss + """&Field746802935372128=&exactcomment=""" + ss1 + """&Field256548277850457=""" + ss2 + """&Field1435723373333548_iso2_country_code=&Field1435723373333548=sa&sneaky=&support_form_id=424745097661047&support_form_hidden_fields=%7B%22838322882850639%22%3Afalse%2C%22666972826719090%22%3Afalse%2C%22290540267769404%22%3Atrue%2C%22218593448349930%22%3Afalse%2C%22746802935372128%22%3Atrue%2C%221421990228055493%22%3Afalse%2C%22537927836328053%22%3Afalse%2C%22256548277850457%22%3Afalse%2C%221435723373333548%22%3Afalse%2C%22755709437786995%22%3Afalse%7D&support_form_fact_false_fields=[]&__user=0&__a=1&__dyn=7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEy58ogbUuw9-3K4o1j8hwem0nCq1ewcG0KEswaq3a2W2y0umUS1kyE1e42C220gG0D87u1zw9O0RE2Jw8W0hC&__csr=&__req=c&__beoa=0&__pc=PHASED%3ADEFAULT&dpr=1&__ccg=GOOD&__rev=1002880359&__s=w4onwn%3Aov25hx%3A2c6bry&__hsi=6887565373536777664-0&__comet_req=0&__spin_r=1002880359&__spin_b=trunk&__spin_t=1603636279"""
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Connection": "close",
            "Host": "help.instagram.com",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://help.instagram.com/contact/424745097661047",
            "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
            "Content-Length": "1057",
            "Cookie": "datr=rXuVXyeOlvJlzTAgpOPnnpUi"

        }

        response = requests.post (url, data=payload, headers=headers)
        if 'for' in response.text:
            print (' -' * 15)
            print (whiteB_color +'The report was sent successfully ( ok )')
        elif "payload" in response.text:
            print ('Sorry, there is an error')

        print ("")
        print (" -" * 15)
        exit ()

import requests
import uuid
import threading
import re
print("""
░░░░░░░░███████████████░░░░░░░░
░░░░░█████████████████████░░░░░
░░░░████████████████████████░░░
░░░██████████████████████████░░
░░█████████████████████████████
░░███████████▀░░░░░░░░░████████
░░███████████░░░░░░░░░░░░░░░███
░████████████░░░░░░░░░░░░░░░░██
░█░░███████░░░░░░░░░░░▄▄░░░░░██
█░░░░█████░░░░░░▄███████░░██░░█
█░░█░░░███░░░░░██▀▀░░░░░░░░██░█
█░░░█░░░░░░░░░░░░▄██▄░░░░░░░███
█░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██
█░░░░░░░░░░░░░░░░░░░░░░█░░░░██░
░███░░░░░░░░░░░░░░░░░░░█░░░░█░░
░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░
░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░
░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░
░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░
░░░██░░░░░░░█░░▀████████░░█░░░░
░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░
░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░
░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░
░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░
░░░░░░░░░░░░░░░░████████░░░░░░░
 
 
                                     """)
u = str(uuid.uuid4())
req = requests.session()
userandpass = open('login.txt', 'r').read().splitlines() #making a list of user and pass
target = input('Entere1+ Target Username:')
gettargetuserid = req.get(f'https://www.instagram.com/{target}/?__a=1').text #geting target userId
id1 = re.findall('"logging_page_id":"profilePage_(.*?)"', gettargetuserid)
useridasstring = " ".join(id1)
print(f"{target} User Id >>"+ useridasstring)
threadz = int(input('Enter Threads:'))
print('1. Spam')
print('2. Harassment Or Bullying')
print('3. Sale Or Promotion Of Drugs')
print('4. Violence Or Threat Of Violence')
print('5. Nudity Or Pornography')
print('6. Hate Speech Or Symbols')
print('7. Self Injury')
while True:
    for i in userandpass:
        username = i.split(':')[0]
        password = i.split(':')[1]
        print(username+':'+ password)
    head = {
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTBw==',
        'User-Agent': 'Instagram 35.0.0.20.96 Android (26/8.0.0; 320dpi; 768x1184; unknown/Android; Li0N; vbox86p; vbox86; en_US; 95414347)',
        'Accept-Language': 'en-US',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'i.instagram.com',
        'Connection': 'keep-alive',
        'Accept': '*/*'
    }
    insta = 'https://i.instagram.com/api/v1/accounts/login/'
    data1 = {
        'password': password,
        'username': username,
        'device_id': u,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_count': '0'
    }
    rq = req.post(insta, data=data1, headers=head).text
    report = int(input('Enter Your Report Type:'))
    def Report():
        if report == 1:
            if ('"logged_in_user"') in rq:
                inst1 = f'https://i.instagram.com/api/v1/users/{useridasstring}/flag_user/'
                data = {
                    '_uid': u,
                    '_csrftoken': 'missing',
                    '_uuid': u,
                    'reason_id': '1',
                    'source_name': 'profile'
                }
                while True:
                    r = req.post(inst1, data=data, headers=head).text
                    if ('"status": "ok"') in r:
                        print(f'\u001b[31mDone Spam On >> {target}')
                    elif ('"message": "Please wait a few minutes before you try again."') in r:
                        logout = 'https://i.instagram.com/api/v1/accounts/logout/'
                        logout2 = req.post(logout, headers=head).text
                        if ('"status": "ok"') in logout2:
                            print('Done Logout')
                            break
                    else:
                        print(r)
            else:
                print(rq)
                print('Fail To Login')
        elif report == 2:
            if ('"logged_in_user"') in rq:
                inst1 = f'https://i.instagram.com/api/v1/users/{useridasstring}/flag_user/'
                data = {
                    '_uid': u,
                    '_csrftoken': 'missing',
                    '_uuid': u,
                    'reason_id': '7',
                    'source_name': 'profile'
                }
                while True:
                    r = req.post(inst1, data=data, headers=head).text
                    if ('"status": "ok"') in r:
                        print(f'\u001b[31mDone Harassment Or Bullying >> {target}')
                    elif ('"message": "Please wait a few minutes before you try again."') in r:
                        logout = 'https://i.instagram.com/api/v1/accounts/logout/'
                        logout2 = req.post(logout, headers=head).text
                        if ('"status": "ok"') in logout2:
                            print('Done Logout')
                            break
            else:
                print('Fail To Login')
        elif report == 3:
            if ('"logged_in_user"') in rq:
                inst1 = f'https://i.instagram.com/api/v1/users/{useridasstring}/flag_user/'
                data = {
                    '_uid': u,
                    '_csrftoken': 'missing',
                    '_uuid': u,
                    'reason_id': '3',
                    'source_name': 'profile'
                }
                while True:
                    r = req.post(inst1, data=data, headers=head).text
                    if ('"status": "ok"') in r:
                        print(f'\u001b[31mDone Sale Or Promotion Of Drugs >> {target}')
                    elif ('"message": "Please wait a few minutes before you try again."') in r:
                        logout = 'https://i.instagram.com/api/v1/accounts/logout/'
                        logout2 = req.post(logout, headers=head).text
                        if ('"status": "ok"') in logout2:
                            print('Done Logout')
                            break
            else:
                print('Fail To Login')
        elif report == 4:
            if ('"logged_in_user"') in rq:
                inst1 = f'https://i.instagram.com/api/v1/users/{useridasstring}/flag_user/'
                data = {
                    '_uid': u,
                    '_csrftoken': 'missing',
                    '_uuid': u,
                    'reason_id': '5',
                    'source_name': 'profile'
                }
                while True:
                    r = req.post(inst1, data=data, headers=head).text
                    if ('"status": "ok"') in r:
                        print(f'\u001b[31mDone Violence Or Threat Of Violence >> {target}')
                    elif ('"message": "Please wait a few minutes before you try again."') in r:
                        logout = 'https://i.instagram.com/api/v1/accounts/logout/'
                        logout2 = req.post(logout, headers=head).text
                        if ('"status": "ok"') in logout2:
                            print('Done Logout')
                            break
            else:
                print('Fail To Login')
        elif report == 5:
            if ('"logged_in_user"') in rq:
                inst1 = f'https://i.instagram.com/api/v1/users/{useridasstring}/flag_user/'
                data = {
                    '_uid': u,
                    '_csrftoken': 'missing',
                    '_uuid': u,
                    'reason_id': '4',
                    'source_name': 'profile'
                }
                while True:
                    r = req.post(inst1, data=data, headers=head).text
                    if ('"status": "ok"') in r:
                        print(f'\u001b[31mDone Nudity Or Pornography >> {target}')
                    elif ('"message": "Please wait a few minutes before you try again."') in r:
                        logout = 'https://i.instagram.com/api/v1/accounts/logout/'
                        logout2 = req.post(logout, headers=head).text
                        if ('"status": "ok"') in logout2:
                            print('Done Logout')
                            break
            else:
                print('Fail To Login')
        elif report == 6:
            if ('"logged_in_user"') in rq:
                inst1 = f'https://i.instagram.com/api/v1/users/{useridasstring}/flag_user/'
                data = {
                    '_uid': u,
                    '_csrftoken': 'missing',
                    '_uuid': u,
                    'reason_id': '6',
                    'source_name': 'profile'
                }
                while True:
                    r = req.post(inst1, data=data, headers=head).text
                    if ('"status": "ok"') in r:
                        print(f'\u001b[31mDone Hate Speech Or Symbols >> {target}')
                    elif ('"message": "Please wait a few minutes before you try again."') in r:
                        logout = 'https://i.instagram.com/api/v1/accounts/logout/'
                        logout2 = req.post(logout, headers=head).text
                        if ('"status": "ok"') in logout2:
                            print('Done Logout')
                            break
            else:
                print('Fail To Login')
        elif report == 7:
            if ('"logged_in_user"') in rq:
                inst1 = f'https://i.instagram.com/api/v1/users/{useridasstring}/flag_user/'
                data = {
                    '_uid': u,
                    '_csrftoken': 'missing',
                    '_uuid': u,
                    'reason_id': '2',
                    'source_name': 'profile'
                }
                while True:
                    r = req.post(inst1, data=data, headers=head).text
                    if ('"status": "ok"') in r:
                        print(f'\u001b[31mDone Self Injury >> {target}')
                    elif ('"message": "Please wait a few minutes before you try again."') in r:
                        logout = 'https://i.instagram.com/api/v1/accounts/logout/'
                        logout2 = req.post(logout, headers=head).text
                        if ('"status": "ok"') in logout2:
                            print('Done Logout')
                            break
            else:
                print('Fail To Login')
    Report()
    threads1 = []
    for i in range(threadz):
        thread1 = threading.Thread(target=Report)
        thread2 = threading.Thread(target=Report)
        thread2.start()
        thread1.start()
        threads1.append(thread1)
        threads1.append(thread2)
    for thread in threads1:
        thread.join()
    for thread23 in threads1:
        thread23.join()
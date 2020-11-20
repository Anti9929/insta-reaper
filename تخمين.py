import random
import sys
import os


print("اداة صنع ايميلات من اجل سحب متاحات")
print("reaper")
print("الفوضى")
#================================================

#(hotmail.com)
#(gmail.com)
#(outlook.sa)
#(Yahoo.com)
#================================================
user = 'abcdefgjidjsndxjsiakn' #اليوزر المراد التخمين عليه بين النقطتين اكتبه 
chars2 = '123456' #ارقام واحرف لو ترغب
email = '@hotmail.com'#اختار نطاق معين مثل هوتميل او جميل 
print('=========================================')
amount = input('كم عدد كلمات المرور؟')
amount = int(amount)
length2 = input('ما طول كلمة المرور التي تريدها؟')
length2 = int(length2)

print('==================================')

for password in range(amount):
    password = ''
    
    
    for item in range(length2):
         password = ''
    for item in range(length2):
        password += random.choice(chars2)
          
                  
        
    
        password += random.choice(user)



    print (user+password+email)
    with open('email.txt', 'a') as x:
     x.write(user + password + email + '\n')

import argparse, json
from requests import get
import random
import sys
import os
import time


fa = print ('''
-------------------------------
.:: Brute force phone Instagram / twitter and information extraction ::.
    by chaos - reaper       
    instagram - 05.t1_     
-------------------------------
instagram / twitter ..
سحب م
''')

########

a = input ('ماهو مفتاح الدوله ؟')
k = input ('ماهو اخر رقمين ؟')

uesr = '' + a + ''
chars2 = '1234567890'

print ('==================================')
amount = input ('كم عدد الارقام تريد ؟')
amount = int (amount)
length2 = input ('كم عدد الارقام بدون ذكر مفتاح الدوله و اخر رقمين ؟')
length2 = int (length2)

print ('==================================')
print ('تخمين علي الرقم المرتبط بتويتر ')
print ('')
print ('')
for password in range (amount):
    password = ''

    for item in range (length2):
        password = ''
    for item in range (length2):
        password += random.choice (chars2)
    print ( uesr + password + k )
    with open ('number.txt', 'a') as x:
        x.write ( uesr + password + k  + '\n')

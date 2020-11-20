#!/usr/bin/env python



from __future__ import absolute_import
from __future__ import print_function
import sys, os, time, signal,socket ,webbrowser,platform, subprocess
from six.moves import input


def signal_handler(signal, frame):
		KURO()
		LOGO()
		print('\033[1;m [\033[1;31mX\033[1;m] You pressed Ctrl+C!')
		time.sleep(2)
		EXITMENU()


def KURO():
	if os.name == 'nt':
            os.system('cls')
	else:
            os.system('clear')


def LOGO():
	KURO()
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
	
def menu():

	LOGO()
	time.sleep(1) 
	print("""
	1. Reverse image search |البحث عن الصور 
	2. IP | تحديد الايبي
	3. Geolocation API |تحديد الموقع
	4. Forensically | الطب الشرعي لصورة
	5. Remove background | إزالة الخلفية
	6. analysis Files | تحليل الملفات 
	7. imageidentify | وصف الصور 
	8. Convert files | تحويل صيغ الملفات
	9. Compare Images | صور مقارنة
	10. SnapMap | خريطة السناب 
	11. Explore Google | استكشاف جوجل
	12. Advanced Twitter | المتقدم تويتر
	13. Search simulation| البحث في المدن
	14. knowem | البحث عن اليوزر للمستخدم
	15. intelx | الاستخبارات عامة
	""")

	OPT = input("  Select: ")
	if OPT == "1":
         DEAD()
	elif OPT == "2":
		 PHONE()
	elif OPT == "3":
		KURO()
		webbrowser.open('https://browserleaks.com/geo')

		menu()
	elif OPT == "4":
		KURO()
		webbrowser.open('https://29a.ch/photo-forensics/#level-sweep')
		menu()
	elif OPT == "5":
		KURO()
		webbrowser.open('https://www.remove.bg')
		menu()
	elif OPT == "6":
		KURO()
		webbrowser.open('https://www.get-metadata.com')
		menu()
	elif OPT == "7":
		KURO()
		webbrowser.open('https://www.imageidentify.com')
		menu()
	elif OPT == "8":
		KURO()
		webbrowser.open('https://www.online-convert.com')
		menu()
	elif OPT == "9":
		KURO()
		webbrowser.open('https://www.diffchecker.com/image-diff')
		menu()
	elif OPT == "10":
		KURO()
		webbrowser.open('https://map.snapchat.com/@50.958500,6.924390,12.00z')
	elif OPT == "11":
		KURO()
		webbrowser.open('https://trends.google.com/trends/?geo=US')
		menu()
	elif OPT == "12":
		KURO()
		webbrowser.open('https://mobile.twitter.com/search-advanced')
		menu()
	elif OPT == "13":
		KURO()
		webbrowser.open('http://isearchfrom.com')
		menu()
	elif OPT == "14":
		KURO()
		webbrowser.open('https://knowem.com/checksocialnames.php?u=Ghost&submit=')
		menu()
	elif OPT == "15":
		KURO()
		webbrowser.open('https://intelx.io/tools?tab=general')
		menu()
	
	else:
		KURO()
		LOGO()
		print("selection invalid! / ! اختيار غير صالح")
		time.sleep(3)
		menu()


	Tracker = input(" ")

	if Tracker == "1":
		KURO()
print('تم فتح نافذة لشرح استخدام الاداة')

webbrowser.open('https://www.youtube.com/channel/UCj0HIJav-BM0MvZbbNHOg0Q')

def DEAD():
	KURO()
	LOGO()
	
	print("""
 
  1. yandex  
  2. bing
  3. labnol 
=============================

		""")
	Tracker = input(" ")
	if Tracker == "1":
		KURO()
		webbrowser.open('https://www.yandex.com/images/')
		time.sleep(2)
		menu()
	elif Tracker == "2":
		KURO()
		webbrowser.open('https://www.bing.com/visualsearch?FORM=IDPSBC')
		time.sleep(2)
		menu()
	elif Tracker == "3":
		KURO()
		webbrowser.open('https://www.labnol.org/internet/mobile-reverse-image-search/29014/')
		time.sleep(2)
		menu()
	elif Tracker == "00":
		KURO()
		time.sleep(2)
		webbrowser.open('http://www.libramemoria.com/avis/?Nom='+Name+'&Prenom='+F_name)
		time.sleep(2)
		webbrowser.open('https://www.avis-de-deces.net/avis/par-nom/?lastname='+Name+'&firstname='+F_name)
		time.sleep(2)
		webbrowser.open('http://enmemoria.lavanguardia.com/buscar?keywords='+Name+'+'+F_name+'&type=death&_fstatus=search')
		time.sleep(2)
		menu()
	elif Tracker == "99":
		KURO()
		menu()
	elif Tracker == "0":
		KURO()
		EXITMENU()
	else:
		KURO()
		LOGO()
		print(" selection invalid!")
		time.sleep(3)
		menu()

def PHONE():
	KURO()
	LOGO()
	ip = input(" Ip:")

	print("""
 
  1. G-force 
  2. whatismyipaddress
  3. Whois

==============================

		""")	
	Tracker = input(" ")
	if Tracker == "1":
		KURO()
		webbrowser.open('https://www.g-force.ca/en/hosting/ip-whois?ip='+ip)
		time.sleep(2)
		menu()
	elif Tracker == "2":
		KURO()
		webbrowser.open('http://whatismyipaddress.com/ip/'+ip)
		time.sleep(2)
		menu()
	elif Tracker == "3":
		KURO()
		webbrowser.open('https://dig.whois.com.au/ip/'+ip)
		time.sleep(2)
		menu()
	elif Tracker == "00":
		KURO()
		time.sleep(2)
		webbrowser.open('https://www.g-force.ca/en/hosting/ip-whois?ip='+ip)
		time.sleep(2)
		webbrowser.open('http://whatismyipaddress.com/ip/'+ip)
		time.sleep(2)
		webbrowser.open('https://dig.whois.com.au/ip/'+ip)
		time.sleep(2)
		menu()
	elif Tracker == "99":
		KURO()
		menu()
	else:
		KURO()
		LOGO()
		print(" selection invalid!")
		time.sleep(3)
		menu()











#~~~~ خروج ~~~~
def EXITMENU():
	KURO()
	LOGO()
	time.sleep(1)
	print("\033[1;m Thanks for using DoxTracker\033[1;m")
	time.sleep(2)
	print()
	print("...Closing")
	time.sleep(1)
	KURO()
	sys.exit()
		
menu()

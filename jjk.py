#-*- coding:utf-8 -*-
import os, sys, time
print ('''\033[1;31m
        ▄▀▀▀▄
        █   █
       ███████ 
       ███ ███     
       ███▄███ 
    
L  O  C  K  E  D  ◕‿◕ ''')
print ""
print ("\033[1;34m>Input code verifikasi< ")
print ("\033[1;31m>Enter untuk hubungi mbest via messenger >>> ")

key = 'h'
jjk = ''

def oke():
        os.system('termux-open https://m.facebook.com/profile.php?id=100032075620241')
def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():

        uname = raw_input("\033[1;34m>>>> ")

        if uname == key:
                print "\033[1;31mSABAR.."
                time.sleep(2)
                os.system('lolcat app.txt -a -d 45 -s 20 -F 0.1 -p 2.0')

        elif uname == jjk:
                oke()
                os.system('clear')
                restart()

        else:
                print "\033[1;31mUp gan ...!!"
                time.sleep(2);os.system('clear')
                restart()

try:
        main()
except KeyboardInterrupt:
        time.sleep(1)
        print "Kho_Thank's.."
        exit()

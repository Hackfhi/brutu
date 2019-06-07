import os
import re
import sys
from .app import *
from robobrowser import RoboBrowser


class facebook(object):
    def __init__(self, freemode=False):
        super(facebook, self).__init__()

        self.authenticated = False
        self.fullname = ''
        self.username = ''
        self.users = []

        self.facebook = 'https://mbasic.facebook.com' if freemode == False else 'https://free.facebook.com'
        self.facebook_home = self.facebook+'/home.php'
        self.facebook_friend_list = '/{}/friends'
        self.user_agent = 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'
        self.browser = RoboBrowser(user_agent=self.user_agent, parser='html.parser')

    def signin(self, username, password):
        while True:
            try:
                if self.authenticated == True:
                    lol('[C1]...\n')
                    break
                lol_replace('Login...')
                self.browser.open(self.facebook)
                form = self.browser.get_form(id='login_form')
                form["email"] = username
                form["pass"] = password
                self.browser.submit_form(form)
                if 'save-device' in self.browser.url or 'm_sess' in self.browser.url:
                    self.authenticated = True
                    lol('[W1]Login berhasil... ')
                    lol_replace('memindai ...')
                    self.browser.open(self.facebook_home)
                    self.fullname = re.findall(r'\((.*?)\)', self.browser.find(id='mbasic_logout_button').string)[0]
                    self.username = re.findall(r'/(.*?)\?', self.browser.find(string=self.fullname).find_parent('a')['href'])[0]
                    lol('okey...')
                    os.system('clear')
                    lol('[C1]{} [P1]{}'.format(self.fullname, self.username))
                elif 'checkpoint' in self.browser.url:
                    lol('[Y1]Upps... checkpoint\nferivikasi akun anda terlebih dahulu')
                else:
                    lol('[R1]Login gagal...')
                lol()
                break
            except Exception as exception:
                lol('[R1]Exception [R2]{}\n'.format(exception))
                lol('[R2]Koneksi Gagal'+' '*12+'\n')
                if opt_input('Coba ulang?? y/n', ['y','n'], enter=True) == 'n':
                    break
            except KeyboardInterrupt:
                exit()

    def take_users_from_friend_list(self, username=''):
        if self.authenticated == False or username == '':
            return False
        self.users = []
        url = self.facebook_friend_list.format(username)
        confirm_next = True
        while True:
            try:
                file_users_all = list(filter(None, open(os.path.dirname(os.path.abspath(__file__))+'/../txt/users-all.txt', 'r').read().splitlines()))
                self.browser.open(self.facebook+url)
                if 'home.php' in self.browser.url or 'Page Not Found' in self.browser.find('title'):
                    lol('[Y1]Halaman tidak ditemukan\n')
                    return
                response = str(self.browser.parsed)
                table_data = self.browser.find(id='root').find_all('table', attrs={'role':'presentation'})
                for data in table_data:
                    data = data.find('a')
                    if sys.version[0] == '3':
                        user_name = data.string
                    else:
                        user_name = data.string.encode('utf-8')
                    while True:
                        result = re.findall(r'/(.*?)\?fref', data['href'])
                        if len(result):
                            user_id = result[0]
                            user = '{} - {}'.format(user_id, user_name)
                            self.users.append(user)
                            if user in file_users_all:
                                lol('[C2]> [W2]{} [D1]{}'.format(user_name, user_id))
                            else:
                                lol('[C2]> [P1]{} [P2]{}'.format(user_name, user_id))
                                with open(os.path.dirname(os.path.abspath(__file__))+'/../txt/users-all.txt', 'a') as text_file:
                                    text_file.write('{}\n'.format(user))
                            break
                        result = re.findall(r'\?id=(.*?)&fref', data['href'])
                        if len(result):
                            user_id = result[0]
                            lol('[C2]> [R1]{} [R2]{}'.format(user_name, user_id))
                            break
                        result = re.findall(r'\?uid=(.*?)&', data['href'])
                        if len(result):
                            user_id = result[0]
                            lol('[C2]> [R1]{} [R2]{}'.format(user_name, user_id))
                            break
                        user_id = data['href']
                        lol('[C2]> [R1]{} [R2]{}'.format(user_name, user_id))
                        break 
                url = self.browser.find(id='m_more_friends').find('a')['href']
                if confirm_next == True and len(self.users):
                    result = opt_input('>Ambil semua? y/n', ['y','n',''])
                    if result == 'y':
                        lol()
                        confirm_next = False
                    elif result == 'n':
                        break
                    else:
                        lol()
            except AttributeError:
                break
            except Exception as exception:
                lol('\n[R2]...: {}'.format(exception))
            except KeyboardInterrupt:
                lol('[R1]Berhenti\n')
                break
        if len(self.users):
            lol('\n[Y1]{} user telah dipindai\n'.format(len(self.users)))
            open(os.path.dirname(os.path.abspath(__file__))+'/../txt/users-temp.txt', 'w').write('\n'.join(self.users))
            return True

    def save_users(self):
        if len(self.users):
            if opt_input('lanjut y/n' , ['n','y'], enter=True) == 'y':
                try:
                    open(os.path.dirname(os.path.abspath(__file__))+'/../txt/users.txt', 'w').write('\n'.join(self.users))
                    lol('[G1]Okey..')
                    os.system('clear')
                    main()
                except Exception as exception:
                    lol('[R1]..')
                    return
            else:
                lol('[R1]....')
            lol()

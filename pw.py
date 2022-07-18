import re
import subprocess

class pw_windows:
    def __init__(self):
        self.user = []
        self.pw = []
        self.get_user()
        self.get_pw()
        self.print_hasil()
        
    def get_user(self):
        cmd = re.findall(r':\s.+', subprocess.run(['netsh', 'wlan', 'show', 'profile'], shell=False, capture_output=True).stdout.decode('utf-8'))
        for i in cmd:
            self.user.append(i.replace(': ', '').strip())
    def get_pw(self):
        for usern in self.user:
            try: cmd = re.search(r'Content            :\s.+', subprocess.run(['netsh', 'wlan', 'show', 'profile', usern, 'key=clear'], shell=False, capture_output=True).stdout.decode('utf-8')).group(0).replace('Content            : ', '')
            except: cmd = 'none'
            self.pw.append(cmd.strip())
    def print_hasil(self):
        x = 0
        for i in range(len(self.user)):
            x += 1
            print(f'{x}. {self.user[x-1]}')
        a = int(input('pilih nomer berapa: '))
        if 'none' in self.pw[a-1]: print(f'\nUsername "{self.user[a-1]}" Tidak menggunakan kata sandi')
        else: print(f'\nKatasandi dari username "{self.user[a-1]}" adalah "{self.pw[a-1]}"')
# a = []
# cmd = re.findall(r':\s.+', subprocess.run(['netsh', 'wlan', 'show', 'profile'], shell=False, capture_output=True).stdout.decode('utf-8'))
# for i in cmd:
#     a.append(i.replace(': ', ''))
if __name__ == '__main__':
    pw_windows()
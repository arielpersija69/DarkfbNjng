   # -*- coding: utf-8 -*-
import os, sys
print '\x1b[1;33mLogin Dulu Boss Qu'
print '\x1b[1;32mID : . Password : .'
import os, sys

def wa():
    os.system('xdg-open https://api.whatsapp.com/send?phone=6283103023425&text=Assalamualaikum')


def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


user = raw_input('ID: ')
import getpass
sandi = raw_input('Password: ')
if user == '.' and sandi == '.':
    print 'Login Berhasil'
    sys.exit
else:
    print 'Login GAGAL, Silahkan hubungi ADMIN'
    wa()
    restart()

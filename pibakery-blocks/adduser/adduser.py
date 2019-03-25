#!/usr/bin/python
import subprocess,crypt,random, sys

login = sys.argv[1]
password = sys.argv[2]

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./"
salt = ''.join(random.choice(ALPHABET) for i in range(16))

shadow_password = crypt.crypt(password,'$6$'+salt+'$')

r = subprocess.call(('useradd', '-m', '-p', shadow_password, '-s', '/bin/bash', login))

if r != 0:
    print 'Error creating user ' + login

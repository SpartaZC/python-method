# python-method
# 
import requests,uuid,secrets 
from time import sleep
print('Created By ~ ose')
uid = uuid.uuid4()
r = requests.Session()
cookie = secrets.token_hex(8)*2
print('(Welcome To Free Bot Spam)')
print(" ")
print(" ")

print('#'"   " '####################################')
print('#'"   " "--Spam Bot By:Telegram/@AB_A3" "     " '#')
print('#'"   " "--Coded ByYosuf insta-@SAC.HK" "     " '#')
print('#'"   " "-- Programing lang Python--" "       " '#')
print("# " "  " '###################################')
print(" ")
print(" ")
print("_______________________")
print(" ")
print("Login In Instagram Account")
print(" ")
username = input('Your UserName:')
password = input('Your PassWord:')
target = input('User TarGet:')
sle = int(input('Sleep:'))
def login():
    global username
    global password
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36', 'x-csrftoken': 'missing', 'mid': cookie}
    data = {'username':username,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false',}
    req_login = r.post(url,headers=headers,data=data)
    if ("userId") in req_login.text:
        r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
        print('login True')
        url_id = 'https://www.instagram.com/{}/?__a=1'.format(target)
        req_id = r.get(url_id).json()
        user_id = str(req_id['logging_page_id'])
        idd = user_id.split('_')[1]
        done = 1
        while True:
            url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
            datas = {'source_name':'','reason_id':1,'frx_context':''} #spam
            report = r.post(url_report,data=datas)
            print('done spam {}'.format(done))
            sleep(sle)
            done += 1
    else:
        print('login false')
        exit()
login()












import os
import requests
import re
import time
import sendNotify


def shenyu(user,password):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://www.acg088.com/',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    data = {
        'action': 'user_login',
        'username': user,
        'password': password,
        'rememberme': '1',
    }
    session =requests.session()
    response = session.post('http://www.acg088.com/wp-admin/admin-ajax.php', headers=headers, data=data)

    response=session.get('http://www.acg088.com/user/vip',headers=headers,cookies=response.cookies,verify=False)
    bb=re.findall('<button class="btn btn-sm btn-info w-100 mt-3 go-user-qiandao" data-nonce="(.*?)"',response.text)
    try:
        nonce=bb[0]
        print(nonce)
    except IndexError:
        nonce='0'


    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://www.acg088.com/user/vip',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }


    data = {
        'action': 'user_qiandao',
        'nonce': nonce,
    }

    response = session.post('http://www.acg088.com/wp-admin/admin-ajax.php', cookies=response.cookies,headers=headers, data=data)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    response = session.get('http://www.acg088.com/user/coin', cookies=response.cookies, headers=headers, verify=False)
    coin=re.findall('<p class="small m-0">(.*?)</p>',response.text)
    
    try:
        print(coin[0])
        message='账号：'+user+coin[0]
    except IndexError:
        message="出错啦，请检查"
    sendNotify.send("绝对神域签到结果：\n"+message)


if __name__ == '__main__':
    USER1=os.environ['USER1']
    PW1=os.environ['PW1']
    USER2=os.environ['USER2']
    PW2=os.environ['PW2']
    USER3=os.environ['USER3']
    PW3=os.environ['PW3']
    account=[[USER1,PW1],[USER2,PW2],[USER3,PW3]]
    for user,password in account:
        shenyu(user,password)
        time.sleep(5)
        

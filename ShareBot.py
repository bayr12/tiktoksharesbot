from logging import error
import ssl, os, requests, pyfiglet, time
from threading import active_count, Thread
from pystyle import Colorate, Colors, Write
from random import randint, choice
from urllib3.exceptions import InsecureRequestWarning
from http import cookiejar
from Data.UserAgent import UserAgent

DeviceTypes = ["iPhone1,1","iPhone1,2","iPhone2,1","iPhone3,1","iPhone3,2","iPhone3,3","iPhone4,1","iPhone5,1","iPhone5,2","iPhone5,3","iPhone5,4","iPhone6,1","iPhone6,2","iPhone7,1","iPhone7,2","iPhone8,1","iPhone8,2","iPhone8,4","iPhone9,1","iPhone9,2","iPhone9,3","iPhone9,4","iPhone10,1","iPhone10,2","iPhone10,3","iPhone10,4","iPhone10,5","iPhone10,6","iPhone11,2","iPhone11,4","iPhone11,6","iPhone11,8","iPhone12,1","iPhone12,3","iPhone12,5","iPhone12,8","iPhone13,1","iPhone13,2","iPhone13,3","iPhone13,4","iPhone14,2","iPhone14,3","iPhone14,4","iPhone14,5","iPod1,1","iPod2,1","iPod3,1","iPod4,1","iPod5,1","iPod7,1","iPod9,1","iPad1,1","iPad1,2","iPad2,1","iPad2,2","iPad2,3","iPad2,4","iPad3,1","iPad3,2","iPad3,3","iPad2,5","iPad2,6","iPad2,7","iPad3,4","iPad3,5","iPad3,6","iPad4,1","iPad4,2","iPad4,3","iPad4,4","iPad4,5","iPad4,6","iPad4,7","iPad4,8","iPad4,9","iPad5,1","iPad5,2","iPad5,3","iPad5,4","iPad6,3","iPad6,4","iPad6,7","iPad6,8","iPad6,11","iPad6,12","iPad7,1","iPad7,2","iPad7,3","iPad7,4","iPad7,5","iPad7,6","iPad7,11","iPad7,12","iPad8,1","iPad8,2","iPad8,3","iPad8,4","iPad8,5","iPad8,6","iPad8,7","iPad8,8","iPad8,9","iPad8,10","iPad8,11","iPad8,12","iPad11,1","iPad11,2","iPad11,3","iPad11,4","iPad11,6","iPad11,7","iPad12,1","iPad12,2","iPad14,1","iPad14,2","iPad13,1","iPad13,2","iPad13,4","iPad13,5","iPad13,6","iPad13,7","iPad13,8","iPad13,9","iPad13,10","iPad13,11","Watch1,1","Watch1,2","Watch2,6","Watch2,7","Watch2,3","Watch2,4","Watch3,1","Watch3,2","Watch3,3","Watch3,4","Watch4,1","Watch4,2","Watch4,3","Watch4,4","Watch5,1","Watch5,2","Watch5,3","Watch5,4","Watch5,9","Watch5,10","Watch5,11","Watch5,12","Watch6,1","Watch6,2","Watch6,3","Watch6,4","Watch6,6","Watch6,7","Watch6,8","Watch6,9","SM-G9900", "sm-g950f", "SM-A136U1", "SM-M225FV", "SM-E426B", "SM-M526BR", "SM-M326B", "SM-A528B", "SM-F711B", "SM-F926B", "SM-A037G", "SM-A225F", "SM-M325FV", "SM-A226B", "SM-M426B", "SM-A525F"]
Platforms   = ["android", "windows", "iphone", "web"]
Channel     = ["tiktok_web", "googleplay", "App%20Store"]
ApiDomain   = ["api19.tiktokv.com", "api.toutiao50.com", "api19.toutiao50.com", "api19-core-c-alisg.tiktokv.com"]

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
r = requests.Session()
ThreadCount = 0
Sent = 0
Failed = 0

class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

r.cookies.set_policy(BlockCookies())

#Set title and update it
def Title(Content):
    os.system(f"title {Content}")

#SendShares
def SendShares(item_id):
    global Sent, Failed
    platform = choice(Platforms)
    apiDomain = choice(ApiDomain)
    channelLol = choice(Channel)
    DeviceType = choice(DeviceTypes)
    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": choice(UserAgent)
    }
    appName = choice(["tiktok_web", "musically_go"])
    osVersion = randint(1, 12)
    Device_ID = randint(1000000000000000000, 9999999999999999999)
    URI = f"https://{apiDomain}/aweme/v1/aweme/stats/?channel={channelLol}&device_type={DeviceType}&device_id={Device_ID}&os_version={osVersion}&version_code=220400&app_name={appName}&device_platform={platform}&aid=1988"
    Data = f"item_id={item_id}&share_delta=1"

    try:
        req = r.post(URI, headers=headers, data=Data, stream=True, verify=False)
        try:
            if req.json()["status_code"] == 0:
                Sent += 1
                print(Colorate.Horizontal(Colors.green_to_white, f"[+] Share sent > {Sent}"))
                Title(f"Thread :{active_count()} - Hit :{Sent} - Fail :{Failed}")
            else:
                pass
        except:
            Failed += 1
            Title(f"Thread :{active_count()} / Hit :{Sent} / Fail :{Failed}")
    except:
        pass

#Run script, inputs and then function
if __name__ == "__main__":
    Title("[TIKTOK SHARE BOT]")
    Write.Print(pyfiglet.figlet_format('k e n z o'), Colors.red_to_white, interval=0.000001)
    print(Colorate.Horizontal(Colors.red_to_white, 'Used as reference: https://github.com/Wizz1337/TikTokMassBotting'))
    print('')
    Error = True
    while Error:
        videoLink = Write.Input("[?] Video Link > ", Colors.red_to_white)
        try:
            itemID = videoLink.split("/")[5].split("?", 1)[0]
        except:
            print(Colorate.Horizontal(Colors.red_to_white, '[!] Invalid Link'))
            print('')
        else:
            Error = False
    print('')
    amount = Write.Input("[?] Amount (0=inf) > ", Colors.red_to_white)
    print('')
    print(Colorate.Horizontal(Colors.red_to_white, '[!] Highly advise to maintain <= 1000'))
    ThreadAmount = Write.Input("[?] Thread Amount > ", Colors.red_to_white)
    print('')
    print(Colorate.Horizontal(Colors.red_to_white, '[+] Starting!!!'))
    print('')
    time.sleep(1.5)

    if int(amount) == 0:
        while active_count() <= int(ThreadAmount):
            try:
                Thread(target=SendShares, args=(itemID,)).start()
            except:
                pass
    else:
        while Sent < int(amount):
            if active_count() <= int(ThreadAmount):
                try:
                    Thread(target=SendShares, args=(itemID,)).start()
                except:
                    pass
import urllib3
import os 
import requests
import time

'''
anime photo 

'''
myid = os.getenv("TARGET_CHAT_ID")
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

img_url = os.getenv("IMG_URL")
img_api = os.getenv("IMG_API")


def sendText(msg):
    send_text = msg.strip()
    sendMSGAPI = rf"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={myid}&text={send_text}"
    http = urllib3.PoolManager()
    rsp = http.request('GET', sendMSGAPI) 
    print(rsp.status)
    # print(rsp.data)

def sendText2(msg):
    send_text = msg.strip()
    sendMSGAPI = rf"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={myid}&text={send_text}"
    r = requests.get(sendMSGAPI)
    print(r.status_code)    

def get_img_list():
    headers = {  
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "X-Directive": "api",
        "Connection": "keep-alive" 
    }
    r0 = requests.get(url=img_url,headers=headers)
    cookies = {}
    if r0.status_code == 200:
        for each in r0.cookies.keys():
            cookies[each] = r0.cookies.get(each)
    else:
        return []

    r0 = requests.get(url=img_api,headers=headers,cookies=cookies)
    if r0.status_code == 200:
        return [item["canonical_url"] for item in r0.json()["data"]]
    else:
        return [] 
  
def sendFile(fileUrl):
    ## sending by URL will currently only work for gif, pdf and zip files
    send_doc = fileUrl.strip()
    sendDOCAPI = rf"https://api.telegram.org/bot{bot_token}/sendDocument?chat_id={myid}&document={send_doc}"
    r = requests.get(sendDOCAPI)
    print("File" ,r.status_code) 

def sendPhoto(fileUrl):
    ## sending by URL will currently only work for gif, pdf and zip files
    send_photo = fileUrl.strip()
    sendPHOTOAPI = rf"https://api.telegram.org/bot{bot_token}/sendPhoto?chat_id={myid}&photo={send_photo}" 
    r = requests.get(sendPHOTOAPI)
    print("Photo", r.status_code) 
    return r.status_code == 200

if __name__ == '__main__':
    #sendText("In function....")
    #sendText2("https://www.google.com")
    li = get_img_list()

    # #sendText2(f"Action start....,get len is {len(li)}")
    
    if len(li) != 0:
        for each in li:
            if each is not None and "." in each:
                sub_ext = each.split(".")[-1]
            else:
                sub_ext = None 

            if each is not None:
                if sub_ext not in ["mp4","gif","webm"] and sendPhoto(each.strip()):
                    pass
                else:
                    sendFile(each.strip())   # sendText2(each.strip())
                time.sleep(1)
    sendText2(f"Get len is {len(li)} at {time.ctime()}")               
    # #sendText2(f"Action Finish, {time.ctime()}")

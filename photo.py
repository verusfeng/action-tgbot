import json 
import os 
import requests
import time


target_id = os.getenv("BLBCPID")
main_page_api = os.getenv("BLBCPAPI")

token = os.getenv("TELEGRAM_BOT_TOKEN")

## {"ok":false,"error_code":400,"description":"Bad Request: group send failed"}

# send media group 
proxies = None

def bot_send_message(msg):
    text =msg.strip()
    r = requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={target_id}&text={text}",proxies=proxies)
    print("bot_send_message", r.status_code)
    return 

def get_photo_list():
    r = requests.get(main_page_api)
    kl = []
    if r.status_code == 200:
        for ei in r.json()["data"]["items"]:
            for url in ei["item"]["pictures"]:
                # print(url["img_src"])
                kl.append(url["img_src"])
        return kl
    else:
        return []  ## error return empty list .


def sendFile(fileUrl):
    ## sending by URL will currently only work for gif, pdf and zip files
    send_doc = fileUrl.strip()
    sendDOCAPI = rf"https://api.telegram.org/bot{token}/sendDocument?chat_id={target_id}&document={send_doc}"
    r = requests.get(sendDOCAPI,proxies= proxies)
    print(r.status_code) 


def sendPhoto(fileUrl):
    ## sending by URL will currently only work for gif, pdf and zip files
    send_photo = fileUrl.strip()
    sendPHOTOAPI = rf"https://api.telegram.org/bot{bot_token}/sendPhoto?chat_id={target_id}&photo={send_photo}" 
    r = requests.get(sendPHOTOAPI)
    print("Photo", r.status_code) 
    return r.status_code == 200





'''

'''

def bot_send_media_group(media):
    try_times = 0 
    while True:      
        r= requests.get(rf"https://api.telegram.org/bot{token}/sendMediaGroup?chat_id={target_id}&media={media}",proxies=proxies)
        print("bot_send_media_group", r.status_code, "times is", try_times)
        time.sleep(1)
        if r.status_code == 200 or try_times > 2 :
            ## send ok , return ; retry 3 times return .
            return
        else:
            try_times+=1  

    return 

def send_list(url_list):
    if len(url_list) == 0:
        bot_send_message("list len is 0...")
        return 
    loop_end = len(url_list) // 9
    for i in range(0,loop_end):
        img_array = []
        for each in url_list[i*9:9*(i+1)]:
            img_item = {
            "type":"photo",
            "media":each
            }
            img_array.append(img_item)
        send_data = json.dumps(img_array)
        bot_send_media_group(send_data)
    return 

###################################################
def main():
    l = get_photo_list()  ## ok
    bot_send_message(f"Action start! {time.ctime()} url len {len(l)}")  # ok
    #   ## send files. 
    # for each in l[:40]:
    #     if sendPhoto(each):
    #         pass
    #     else:
    #         sendFile(each)
    #     time.sleep(1/10)
    send_list(l)
    bot_send_message(f"Action Finish!")   

    exit(0)

    
main()
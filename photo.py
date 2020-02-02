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

# def bot_send_media_group(media):
#     r= requests.get(f"https://api.telegram.org/bot{token}/sendMediaGroup?chat_id={target_id}&media={media}",proxies=proxies)
#     print("bot_send_media_group", r.status_code)
#     print(r.text)
#     return 
# ## Fail while testing...


# def send_list(url_list):
#     if len(url_list) == 0:
#         bot_send_message("list len is 0...")
#         return 
#     for i in range(0,3):
#         img_array = []
#         for each in url_list[i*10:10*(i+1)]:
#             img_item = {
#             "type":"photo",
#             "media":each
#             }
#             img_array.append(img_item)
#         send_data = json.dumps(img_array)
#         bot_send_media_group(send_data)
#     return 

def sendFile(fileUrl):
    ## sending by URL will currently only work for gif, pdf and zip files
    send_doc = fileUrl.strip()
    sendDOCAPI = rf"https://api.telegram.org/bot{token}/sendDocument?chat_id={target_id}&document={send_doc}"
    r = requests.get(sendDOCAPI,proxies= proxies)
    print(r.status_code) 


def sendPhoto(fileUrl):
    ## sending by URL will currently only work for gif, pdf and zip files
    send_photo = fileUrl.strip()
    sendPHOTOAPI = rf"https://api.telegram.org/bot{bot_token}/sendPhoto?chat_id={myid}&photo={send_photo}" 
    r = requests.get(sendPHOTOAPI)
    print("Photo", r.status_code) 
    return r.status_code == 200


def main():
    l = get_photo_list()  ## ok
    bot_send_message(f"Action start! {time.ctime()} url len {len(l)}")  # ok

    for each in l[:40]:
        if sendPhoto(each):
            pass
        else:
            sendFile(each)
        time.sleep(1/10)

    bot_send_message(f"Action Finish!")   

    exit(0)

    
main()
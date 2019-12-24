import urllib3
import os 
import requests

myid = os.getenv("TARGET_CHAT_ID")
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

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


if __name__ == '__main__':
    sendText("In function....")
    sendText2("Use requests....")
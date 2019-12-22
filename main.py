import urllib3
import os 
myid = os.getenv("TARGET_CHAT_ID")
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

send_text = "send text ...."
sendMSGAPI = rf"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={myid}&text={send_text}"
http = urllib3.PoolManager()
rsp = http.request('GET', sendMSGAPI) 
print(rsp.status)
# print(rsp.data)
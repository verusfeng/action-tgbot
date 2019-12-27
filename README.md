# Action-tgbot
Try action with tg bot

## Create a bot 
1. [@BotFather](https://t.me/BotFather)
2. [Tg API](https://core.telegram.org/bots/api#making-requests)  


## Set Secrets Data
1. Current Repository Setting -> Secrets -> Add a new secret
2. Add bot token Name BOT1_TOKEN
3. Add test chat id Name CHAT_ID

### Action yml configuration
1. In yml file 
    - This will set OS env variable
    - env:  
        - TOKEN: ${{ secrets.BOT1_TOKEN}}
        - ID: ${{ secrets.CHAT_ID }}
2. In source code 
    - Get env variable from OS
    - myid = os.getenv("ID")
    - bot_token = os.getenv("TOKEN")

## About telegram API
1. Send <sendMediaGroup>. Required arguments
    - chat_id
    - media, list to json object 
        - type: photo 
        - media: url 
2. Max count in album is 10 photos.

# My Actions
1. Get photo from webAPI and send with telegram bot to target ID
    - Schedule is every hour on hour.
    - Required data
        - bot token 
        - target id 
        - web url 
        - web api 
2. Get photo from webAPI and send to target group with bot
    - Schedul runs on every 30th minute
    - Required secrets
        - bot token
        - group id - alias BLBCPID
        - photoAPI - alias BLBCPAPI
# action-tgbot
Try action with tg bot

## create a bot 
1. [@BotFather](https://t.me/BotFather)
2. [Tg API](https://core.telegram.org/bots/api#making-requests)  


## set SecretsData
1. Current Repository Setting -> Secrets -> Add a new secret
2. Add bot token Name BOT1_TOKEN
3. Add test chat id Name CHAT_ID

### action yaml configuration
1. in yaml file 
    - env:  
        TOKEN: ${{ secrets.BOT1_TOKEN}}
        ID: ${{ secrets.CHAT_ID }}
2. in source code 
    myid = os.getenv("ID")
    bot_token = os.getenv("TOKEN")

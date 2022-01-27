# PyroFilesStoreBot
NOTE: full source code is written by Abir hasan, i just changed some codes and made it easy to deploy

* **Language:** [Python3](https://www.python.org)
* **Library:** [Pyrogram](https://docs.pyrogram.org)

### Features:
- In PM Just Forward or Send any file it will save on Database & give you the Access Link.
- In Channel Add Bot as Admin with Edit Rights. When you will send any file or media in Channel it will Edit the Broadcast Message with Saved Link Button.
- You can also Broadcast anythings via this Bot.
- You can also Do Force Sub to a Channel to allow access the Bot.

## Configs:
- `API_ID` - Get this from [@TeleORG_Bot](https://t.me/TeleORG_Bot)
- `API_HASH` - Get this from [@TeleORG_Bot](https://t.me/TeleORG_Bot)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)
- `BOT_USERNAME` - You Bot Username. *(Without [@])*
- `DB_CHANNEL` - A Telegram Channel ID.
	- Make a Channel for Storing Files. We will use that as Database. Channel must be Private! Else you will be Copyright by [Telegram DMCA](https://t.me/dmcatelegram)!
- `BOT_OWNER` - Bot Owner UserID
	- Put your Telegram UserID for doing Broadcast.
- `DATABASE_URL` - MongoDB Database URI
	- This for Saving UserIDs. When you will Broadcast, bot will forward the Broadcast to DB Users.
- `UPDATES_CHANNEL` - Force Sub Channel ID *(Optional)*
	- ID of a Channel which you want to do Force Sub to use the bot. 
- `LOG_CHANNEL` - Logs Channel ID
	- This for some getting user info. If any new User added to DB, Bot will send Log to that Logs Channel. You can use same DB Channel ID.
- `FORWARD_AS_COPY` - Value can be `True` or `False` *(Optional)*
	- If `True` all messages will be forwarder *As Copy*. If `False` all messages will be forwarder with Forward Tag.
- `BANNED_USERS` - Banned unwanted members
         - Put all banned user IDs & Separate with space.
- `BANNED_CHAT_IDS` - All Banned Channel IDs *(Optional)*
	- Put all banned channel IDs & Separate with space.
- `UR_CHANNEL` - Your channel username.
	- to set your channel in start button.
- `UR_GROUP` - yur group username.
	-  to set your group in start button.

### Deploy Now:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Commands:
```
start - start the bot
status - Show number of users in DB
```

### Credits:
* **Abir Hasan:** [Abir Hasan](https:/github.com/abirhasan2005)
* **Library:** [me](https:/github.com/pyrogramers)

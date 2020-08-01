# b0ttime
a smol twitch bot

## Requirements

* `pipenv`

On Arch Linux it's as simple as:     
```
# pacman -S python-pipenv
```

Inside the folder, install the packages

* `twitchio`
* `pydub`

like this:
```bash
$ pipenv lock
$ pipenv install twitchio
$ pipenv install pydub
``` 

## Create the `.env` file

You have to create a file named `.env`. Inside this file, write the following:
```env
# .env
TMI_TOKEN=<YOUR TWITCH TMI TOKEN>
CLIENT_ID=<YOUR TWITCH BOT CLIENT ID>
BOT_NICK=<YOUR TWITCH BOT CHANNEL NAME>
BOT_PREFIX=!
CHANNEL=<YOUR STREAMING CHANNEL NAME>
```

[Twitch TMI token](https://twitchapps.com/tmi/)    
[Twitch Client ID](https://dev.twitch.tv/console/apps/create)

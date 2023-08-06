## Logging-Telegram

[Telegram](https://telegram.org/) handler for python logging.


## Installation

...


## Usage from console

``` python

from logging import getLogger
from logging_telegram.handlers import TelegramHandler

# Setup logger
logger = getLogger()
logger.addHandler(TelegramHandler(token='<bot-token-here>', chat_id='<chat-id-here>'))

# Send some logs to telegram
logger.warning("Hello there")
logger.warning("There is an warning from logger!")

```


## Usage with django

``` python

LOGGING = {
    'version': 1,
    'handlers': {
        'telegram': {
            'class': 'logging_telegram.handlers.TelegramHandler',
            'token': '<bot-token-here>',
            'chat_id': '<chat-id-here>'
        }
    },
    'loggers': {
        '<logger-name>': {
            'handlers': ['telegram'],
            'level': 'DEBUG'
        }
    }
}

```


## How to obtain token?

Follow bot creation instructions [here](https://core.telegram.org/bots#6-botfather).


## How to find chat_id?

1. Open Telegram and start a chat with your bot.

2. Write him a message like "Hello there".

3. Get bot updates by following link
   
   ``` python
      "https://api.telegram.org/bot{token}/getUpdates".format(token=your_bot_token)
   ```

4. Find chat_id in json response:

    ``` json
    {
        "ok": true,
        "result": [
            {
                "update_id": 349933642,
                "message": {
                    "message_id": 2,
                    "from": {
                    "id": 912588819,
                    "is_bot": false,
                    "first_name": "Artiom",
                    "last_name": "Rotari",
                    "language_code": "en"
                },
                "chat": {
                    "id": 912588819,
                    "first_name": "Artiom",
                    "last_name": "Rotari",
                    "type": "private"
                },
                "date": 1635235337,
                "text": "Hello there"
                }
            }
        ]
    }
    ```

    There is our chat_id `912588819`.

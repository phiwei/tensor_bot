# tensor_bot
## Keras callbacks for Twitter and Telegram messaging bots

This repository provides you with some code examples on how to live tweet or message model optimization results. 
The callbacks should work out of the box both for keras and tensorflow keras / tf.keras, although I only tested with tf.keras.

Below, I will point you towards the resources required to set up a Telegram or Twitter bot. You need to get API tokens for each, but the process is pretty straight forward and should only take a couple of minutes. 

## Twitter 
Setting up the Twitter bot worked more smoothly for me than Telegram. 

1. Install the `Twython` package with 

    $ pip install twython

2. Follow the steps as described [in this explanation](https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api) to get developer access and to get the required API tokens. 

3. Save the tokens to `auth.py` if you want to run the example attached. Adhere to the variable names that are already set. 

## Telegram
Telegram was a bit trickier to set up, mainly recovering the `chat_id`. I will elaborate on that later. 

First, install `python-telegram-bot` with

    $ pip install python-telegram-bot --upgrade

Then, you have to message the BotFather [as described here](https://core.telegram.org/bots#6-botfather) to set up a new bot. 

Basically, you just need to message `/newbot` in the chat that pops up upon clicking [this link](https://telegram.me/botfather). 

You will then receive a token for your bot. Save this to `auth.py`. 

You will also receive a link to your bot similar as for the BotFather. If you click it, a chat with your bot will start. Send it a message. 

Now this part proved a bit tricky. Next, you need to obtain the `chat_id` of this conversation. This can in theory be done by messaging the bot once and then opening
	https://api.telegram.org/bot<bot_token>_/getUpdates
where you replace `<bot_token>` by the token you got from the BotFather. For me, following this link at first displayed a link with a true request message but nothing else. 
After approximately two hours, it displayed the messages that I sent to the bot and I could read the `id` field, as e.g. described [here.](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id). 
However, I got a bit frustrated at this step because I initially could not see any reason why the `id` didn't show as described. Probably it is best to be a bit patient. 

Once you got the `id`, add it as `chat_id` to `auth.py` to run the example. 


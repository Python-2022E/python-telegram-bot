import telegram
import os

TOKEN = os.environ['TOKEN']

bot = telegram.Bot(TOKEN)
update = bot.getUpdates()[-1]
chat_id = update.message.chat.id
text = update.message.text
img = 'https://c.ndtvimg.com/2020-08/h5mk7js_cat-generic_625x300_28_August_20.jpg'

bot.sendPhoto(chat_id, photo=img)
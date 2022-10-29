import telegram
import os

TOKEN = os.environ['TOKEN']

bot = telegram.Bot(TOKEN)
update = bot.getUpdates()[-1]
chat_id = update.message.chat.id
text = update.message.text
photo = update.message.photo
# img = 'https://c.ndtvimg.com/2020-08/h5mk7js_cat-generic_625x300_28_August_20.jpg'
f = open('requirements.txt','rb')

bot.sendDocument(chat_id, document=f)
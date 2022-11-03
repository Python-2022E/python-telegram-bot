import telegram
from telegram import KeyboardButton, ReplyKeyboardMarkup

TOKEN='5559122728:AAERqDDQSGzmbuY0jZklQBawNd3Bt0m5xqc'
bot = telegram.Bot(TOKEN)

button = KeyboardButton(text='BUTTON')
keyboard = ReplyKeyboardMarkup([[button]])

update = bot.getUpdates()[-1]
chat_id = update.message.chat.id
text = update.message.text

bot.sendMessage(chat_id, text, reply_markup=keyboard)
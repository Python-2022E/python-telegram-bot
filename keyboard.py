from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
from telegram import KeyboardButton, ReplyKeyboardMarkup
def start(update, context):
    chat_id = update.message.chat.id
    bot = context.bot

    bot.sendMessage(chat_id, 'Welcome!')

def echo(update, context):
    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot
    button1 = KeyboardButton(text='Cat')
    button2 = KeyboardButton(text='Dog')

    reply_markup =ReplyKeyboardMarkup(
        [
            [button1, button2]
        ],
        resize_keyboard=True)

    bot.sendMessage(chat_id, text, reply_markup=reply_markup)

updater = Updater("5559122728:AAERqDDQSGzmbuY0jZklQBawNd3Bt0m5xqc")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()

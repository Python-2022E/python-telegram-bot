from telegram.ext import (
    Updater,
    CommandHandler, 
    MessageHandler, 
    Filters,
    InlineQueryHandler,
    CallbackQueryHandler
)
from pprint import pprint
import json
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
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
    button3 = KeyboardButton(text='Inline')

    reply_markup =ReplyKeyboardMarkup(
        [
            [button1, button2],
            [button3]
        ],
        resize_keyboard=True)

    bot.sendMessage(chat_id, text, reply_markup=reply_markup)

def inlinekeyboard(update, context):
    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot
    botton = InlineKeyboardButton(text='Your Channel', callback_data='channel_link_callback')
    keyboard = InlineKeyboardMarkup([[botton]])

    bot.sendMessage(chat_id, text, reply_markup = keyboard)

def callback_inline(update, context):
    callback = update.callback_query
    callback_data = callback.message.reply_markup.inline_keyboard[0][0].callback_data
    print(callback_data)
updater = Updater("5559122728:AAERqDDQSGzmbuY0jZklQBawNd3Bt0m5xqc")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Inline'), inlinekeyboard))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.dispatcher.add_handler(CallbackQueryHandler(callback_inline))
updater.start_polling()
updater.idle()

from email import message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    chat_id = update.message.chat.id
    bot = context.bot

    bot.sendMessage(chat_id, 'Welcome!')

def echo(update, context):
    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot

    bot.sendMessage(chat_id, f"LIKE 5: 👍 DISLIKE 5: 👎")

updater = Updater("5559122728:AAERqDDQSGzmbuY0jZklQBawNd3Bt0m5xqc")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()
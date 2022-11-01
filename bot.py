from email import message
from telegram.ext import Updater, CommandHandler

def start(update, context):
    chat_id = update.message.chat.id
    # text = update.message.text

    bot = context.bot
    
    bot.sendMessage(chat_id, 'Welcome!')


updater = Updater("5559122728:AAERqDDQSGzmbuY0jZklQBawNd3Bt0m5xqc")

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
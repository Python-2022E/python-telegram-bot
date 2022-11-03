from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
def start(update, context):
    chat_id = update.message.chat.id
    bot = context.bot

    bot.sendMessage(chat_id, 'Welcome!')

def echo(update, context):
    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot

    f = open('like_dislike.json', 'r').read()
    data = json.loads(f)

    like = data.get('LIKE')
    dislike = data.get('DISLIKE')

    if text == '👍':
        like += 1

    if text == '👎':
        dislike += 1

    data['LIKE'] = like
    data['DISLIKE'] = dislike
    data = json.dumps(data)
    print(data)
    f = open('like_dislike.json','w')
    f.write(data)
    f.close()
    bot.sendMessage(chat_id, f"👍 - {like}\n\n👎 - {dislike}")

updater = Updater("5559122728:AAERqDDQSGzmbuY0jZklQBawNd3Bt0m5xqc")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()

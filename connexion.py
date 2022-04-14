from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import os
archiv = ''
files = [['/help']]
markup = ReplyKeyboardMarkup(files, one_time_keyboard=False)
chat_id = '1303744874'


def show(update, context):
    global archiv, chat_id
    format = ' '.join(context.args).lower().split('.')[-1]
    if format == 'txt':
        with open(f'{archiv}/{" ".join(context.args)}', 'r', encoding='utf-8') as f:
            data = f.read()
            update.message.reply_text(data)
    elif format in ['jpg', 'jpeg', 'png']:
        context.bot.send_photo(chat_id=chat_id, photo=open(f'{archiv}/{" ".join(context.args)}', 'rb'))


def start(update, context):
    begin = [['/help']]
    beginning = ReplyKeyboardMarkup(begin, one_time_keyboard=True)
    update.message.reply_text('Welcome to the "Connexion" service! '
                              'Find out about available commands by writing "/help"', reply_markup=beginning)


def connect(update, context):
    global archiv, files, markup
    try:
        archiv = context.args[0]
        files = [[f'/show {k}' for k in os.listdir(context.args[0])]]
        markup = ReplyKeyboardMarkup(files, one_time_keyboard=False)
        update.message.reply_text('We are ready to work! Choose file', reply_markup=markup)
    except IndexError:
        update.message.reply_text('You need to write name of the directory')
    except FileNotFoundError:
        update.message.reply_text('You need to write correct name of the directory')


def disconnect(update, context):
    global archiv, files, markup
    archiv = ''
    files = [['/help']]
    markup = ReplyKeyboardMarkup(files, one_time_keyboard=False)
    update.message.reply_text("Directory is disconnected. Check our service's commands", reply_markup=markup)


def help(update, context):
    update.message.reply_text('/start - starts working with service\n/help - shows available commands\n'
                              '/connect {your directory} - choosing directory to work with\n'
                              '/disconnect - disconnection with directory\n/show {your file} - shows you chosen file')


def main():
    updater = Updater('5170844453:AAFtKrDwRUmbQHYP-JHHi2OzQN_BfP2hMzc', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('show', show))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('connect', connect))
    dp.add_handler(CommandHandler('disconnect', disconnect))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
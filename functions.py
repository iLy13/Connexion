from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import os


def start(update, context):
    begin = [['/help']]
    beginning = ReplyKeyboardMarkup(begin, one_time_keyboard=True)
    update.message.reply_text('Welcome to the "Connexion" service! '
                              'Find out about available commands by writing "/help"', reply_markup=beginning)


def help(update, context):
    update.message.reply_text('/start - starts working with service\n/help - shows available commands\n'
                              '/connect {your directory} - choosing directory to work with\n'
                              '/disconnect - disconnection with directory\n/show {your file} - shows you chosen file')



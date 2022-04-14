from telegram import ReplyKeyboardMarkup


def start(update, context):
    begin = [['/help']]
    beginning = ReplyKeyboardMarkup(begin, one_time_keyboard=True)
    update.message.reply_text('Welcome to the "Connexion" service! '
                              'Find out about available commands by writing "/help"', reply_markup=beginning)


def help(update, context):
    update.message.reply_text('/start - starts working with service\n/help - shows available commands\n'
                              '/connect {your directory} - choosing directory to work with\n'
                              '/disconnect - disconnection with directory\n/show {your file} - shows you chosen file')


def create_kb(spisok):
    kb = []
    while len(spisok) > 0:
        if len(spisok) > 15:
            keys = [[f'/show {k}' for k in spisok[:8]], [f'/show {n}' for n in spisok[8:15]].append('/next_page')]
            kb.append(keys)
            del spisok[:15]
        else:
            kb.append([[f'/show {k}' for k in spisok[:(len(spisok) // 2)]],
                      [f'/show {m}' for m in spisok[(len(spisok) // 2):]]])
            spisok.clear()
    return kb

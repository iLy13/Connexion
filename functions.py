from telegram import ReplyKeyboardMarkup
import sqlite3


def start(update, context):
    begin = [['/help']]
    beginning = ReplyKeyboardMarkup(begin, one_time_keyboard=True)
    update.message.reply_text('Welcome to the "Connexion" service! '
                              'Find out about available commands by writing "/help"', reply_markup=beginning)


def help(update, context):
    update.message.reply_text('/start - starts working with service\n/help - shows available commands\n'
                              '/connect {your directory} - choosing directory to work with\n'
                              '/disconnect - disconnection with directory\n'
                              '/get {your file} - shows you chosen file\n'
                              '/next_page - changing page of your directory\n'
                              '/new_text - starts recording of a new file\n'
                              '/stop - stops recording of a new file')


def create_kb(spisok):
    kb = []
    spisok = sorted(spisok)
    while len(spisok) > 0:
        if len(spisok) > 10:
            keys = [[f'/get {k}' for k in spisok[:5]], [f'/get {n}' for n in spisok[5:9]]]
            keys[1].append('/next_page')
            kb.append(keys)
            del spisok[:10]
        else:
            spisok = [f'/get {k}' for k in spisok]
            spisok.append('/next_page')
            keys = [spisok[:(len(spisok) // 2)],
                    spisok[(len(spisok) // 2):]]
            kb.append(keys)
            spisok.clear()
    return kb


def write_history(event, file, date, month, year, time):
    con = sqlite3.connect('Database.db')
    cur = con.cursor()
    cur.execute("""INSERT INTO History(Event, File, Date, Month, Year, Time) 
                VALUES (?, ?, ?, ?, ?, ?)""", (event, file, date, month, year, time,))
    con.commit()
    con.close()

import random
import datetime
import telebot
# 5468434717:AAEAiUSNhioP9v7Xvu8mUp_OP2Fn1tpa58M

bot = telebot.TeleBot("5468434717:AAEAiUSNhioP9v7Xvu8mUp_OP2Fn1tpa58M")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Доброго ранку, ми з України! Я поки вмію просто відповідати тим, що ти пишеш")
spisok = ['що?', 'я мабуть піду', 'ого-го', 'ну таке...', 'ти так вважаєш?', 'маєш рацію', 'мабуть в цьому є сенс', 'можливо і так', 'я хз', 'що тобі відповісти?']
random_mes = random.choice(spisok)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'хеллоу':
        bot.reply_to(message, 'Ну драсьтє! Напиши мені слово "bot"')
    elif message.text == 'bot':
        bot.reply_to(message, 'А ти слухняний! :-) Добре, іди займись справами бо мій словарний запас скінчився')
    elif message.text == 'привіт':
        bot.reply_to(message, 'Привіт, чо нада?')
    elif message.text == 'бай':
        bot.reply_to(message, 'Ага, щезни швиденько і не відволікай!')
    elif message.text == 'як справи?':
        bot.reply_to(message, 'Тебе це не повинно турбувати! Йди заробляй гроші і не видєлуйса!')
    elif message.text == '300' or message.text == 'триста':
        bot.reply_to(message, 'Атсасі у трактаріста!')
    elif message.text == 'синій кіт' or message.text == 'синий кит' or message.text == 'синий кот':
        bot.reply_to(message, 'ТОБІ ПІЗДА!')
    elif message.text == 'хз' or message.text == 'не знаю' or message.text == 'иди':
        bot.reply_to(message, 'Ну ти вже доросла людина, а не знаєш що тобі треба!')
    else:
        today = datetime.datetime.now()
        spisok = ['яка в тебе гучна клавіатура', 'що ж ти так', 'піди може каву зроби', 'ти ж розумієш про що ти?', 'тобі самому не смішно?', 'що то було?', 'день сьогодні гарний', 'усе буде добре', 'ого-го', 'ну таке...', 'ти так вважаєш?', 'маєш рацію', 'мабуть в цьому є сенс', 'можливо і так',
                  'я хз', 'що тобі відповісти?', 'ти щось не те кажеш', 'так!!!', 'о ноу!', 'ти знову за старе?!', 'мені треба подумати', 'ти ще тут? міцний горішок )))', 'з тобою кумедно', 'ой дурне...', 'іди похрумкай барбарисок']
        time_print = (f'створено: {today: %d-%m-%Y  %H:%M:%S}')
        random_mess = random.choice(spisok)

        random_mes = time_print + '\n\n' + random_mess
        bot.reply_to(message, random_mes)


bot.polling()
from библиотеки import *
from check import *

@bot.message_handler(commands=['start'])
def start_checking(message):
    bot.send_message('490500128', 'Начало проверки фандинга...')
    check_all_funding()
    bot.send_message('490500128', 'Проверка фандинга завершена. Для новой проверки используйте команду /start')

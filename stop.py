from библиотеки import *
from check import *

# конец
@bot.message_handler(commands=['stop'])
def stop_checking(message):
    bot.send_message('490500128', 'Проверка фандинга остановлена')
    exit()

bot.polling(none_stop=stop_checking)
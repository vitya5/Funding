from библиотеки import *
bot = telebot.TeleBot('6153381262:AAEvB2ScH2N3QU9YXJnE6ybgy5p-hJ2abRM')
def check_all_funding():
    #  список всех пар
    response = requests.get('https://api.binance.com/api/v3/exchangeInfo')
    pairs = response.json()['symbols']



    for pair in pairs:
        symbol = pair['symbol']

        #  пара заканчивается на 'USDT' и фьючерс
        if symbol.endswith('quoteAsset')=="USDT" and pair['contractType'] == 'MARGIN':
            #  данные о фандинге для каждой пары
            response = requests.get(f'https://fapi.binance.com/fapi/v1/fundingRate?symbol={symbol}')
            funding_data = response.json()

            #  ответ содержит значение фандинга
            if isinstance(funding_data, list) and len(funding_data) > 0:
                # наличие значения фандинга
                funding_rate = float(funding_data[0].get('fundingRate', 0))

                if -1 < funding_rate < 1:
                    interesting_pairs.append(f"{symbol}: Нет интересного фандинга")
                else:
                    interesting_pairs.append(f"{symbol}: {funding_rate}")
            else:
                interesting_pairs.append(f"{symbol}: Ошибка получения данных")

    if interesting_pairs:
        bot.send_message('490500128', '\n'.join(interesting_pairs))
    else:
        bot.send_message('490500128', 'Нет интересного фандинга')

    bot.send_message('490500128', 'Проверка фандинга завершена')

interesting_pairs = []

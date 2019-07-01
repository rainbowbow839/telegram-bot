import telebot
import pyowm

owm = pyowm.OWM('2b4cfa219b1cec81db2e1546b6061f4b', language = 'uk')
bot = telebot.TeleBot("834747499:AAH_ci9fnHECJhbBFdQd1gSfpS3iws2xwSA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    obs = owm.weather_at_place(message.text)
    w = obs.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer = 'в місті ' + message.text + " зараз " + w.get_detailed_status() + '\n'
    answer +='температура зараз в районі ' + str(temp) + '\n\n'


    if -50 < temp < 10:
        answer +=('зараз холодно, вдягнись як бот ;3')
    elif 10 < temp <20:
        answer +=('нічого особливого, вдягни штани')
    elif 20 < temp < 35:
        answer +=('зарaз нормально, можна вдягнуть шорти') 
    else:
        answer +=('побігай в трусах по під^їзду')


    bot.send_message(message.chat.id, answer)
bot.polling (none_stop = True)
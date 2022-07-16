import requests
import telebot 
import json



bot = telebot.TeleBot(token_telega)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hi, {message.from_user.first_name}. I am the weather bot. Please, enter your city.'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(content_types=["text"])
def finish(message):
    city = message.text
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_weather}&units=metric')
    data = r.json()
    with open('data.txt', 'w+') as outfile:
        json.dump(r.json(), outfile)
    temp = data['main']['temp']
    bot.reply_to(message, f'Temperature in {city} is {temp}')





bot.polling(none_stop=True)

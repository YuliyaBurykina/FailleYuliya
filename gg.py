import telebot

token = "5846873146:AAFQ9-2ySS0eZldiFb3_iSEO_C-rFH3JvGU"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def echo(message):
    print(message)
    bot.send_message(message.chad.id, message.text)


bot.poolling()
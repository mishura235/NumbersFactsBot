import telebot
import Service

TOKEN = "токен"
bot = telebot.TeleBot(TOKEN)
wait_number = False


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Command /fact 'number' -> bot returns fact about number \n"
                          "Command /randomFact -> bot returns fact about random fact")


@bot.message_handler(commands=['randomFact'])
def random(message):
    text = Service.getRandomFact()
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def fact(message):
    try:
        number = int(message.text)
        text = Service.getFact(number)
        bot.reply_to(message, text)
    except:
        bot.reply_to(message, "Send NUMBER or /randomFact")


if __name__ == "__main__":
    bot.infinity_polling()

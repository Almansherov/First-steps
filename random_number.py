from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import random

updater = Updater(token='671136765:AAEIneEgzN0o0pbrSG6iVbWAl7zR3FkMHjc')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def name(bot, input):
    bot.send_message(chat_id=Updater.message.chat_id, text="Please indicate your name: ")

def question(bot, input):
    bot.send_message(chat_id=Updater.message.chat_id, text="All right, " + name + ", feel free to ask me about 
your future: ")
    return question



ran_number = random.randint(1, 100)

if ran_number <= 20:
    print("Impossible")
elif 20 < ran_number <= 40:
    print("Maybe")
elif 40 < ran_number <= 60:
    print("Highly possible")
else:
    print("Definitely")

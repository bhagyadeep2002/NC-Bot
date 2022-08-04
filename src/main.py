from asyncore import dispatcher
import telegram
import logging
import requests
from dotenv import load_dotenv
import os
from telegram import Update
from telegram import ParseMode
from telegram.ext import MessageHandler, Filters
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import CommandHandler
from commands.weather import get_weather
from commands.animals import getCat
from commands.animals import getDog
from commands.animals import getHamster
load_dotenv()

updater = Updater(token=os.environ["TG_BOT"])
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="bot will be abandoned because of lack of confidence")



def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(text="Sorry I did not recognise that command")

cat_handler = CommandHandler('cat',getCat)
hamster_handler = CommandHandler('hamster',getHamster)
dog_handler = CommandHandler('dog',getDog)
weather_handler = CommandHandler('weather',get_weather)
start_handler = CommandHandler('start',start)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(hamster_handler)
dispatcher.add_handler(dog_handler)
dispatcher.add_handler(cat_handler)
dispatcher.add_handler(weather_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()


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
load_dotenv()

updater = Updater(token=os.environ["TG_BOT"])
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="bot will be abandoned because of lack of confidence")

def get_weather(update: Update, context: CallbackContext):
    cityname = context.args[0]
    api_string = f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={os.environ["WEATHER_API"]}&units=metric'
    r = requests.get(api_string)
    data = r.json()
    cityname = cityname.capitalize()
    curr_weather = f"<b> 🌎 {cityname} </b> \n\n"
    curr_weather += f"<b> 🌡 Temperature: </b> {data['main']['temp']}°C \n"
    curr_weather += f"<b> 😶‍🌫️ Feels like: </b> {data['main']['feels_like']}°C \n"
    curr_weather += f"<b> 💨 Wind Speed: </b> {data['wind']['speed']} m/s\n"
    update.message.reply_text(text=curr_weather, parse_mode=ParseMode.HTML)

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(text="Sorry I did not recognise that command")

weather_handler = CommandHandler('weather',get_weather)
start_handler = CommandHandler('start',start)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(weather_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()


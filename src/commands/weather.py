import telegram
from dotenv import load_dotenv
import os
from telegram import Update
from telegram import ParseMode
from telegram.ext import MessageHandler, Filters
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import CommandHandler
load_dotenv()
import requests

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
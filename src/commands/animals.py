import telegram
import requests
from telegram import Update
from telegram import ParseMode
from telegram.ext import MessageHandler, Filters
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import CommandHandler
from serpapi import GoogleSearch
import os

def getCat(update: Update, callback: CallbackContext):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    data = r.json()
    image_url = data[0]["url"]
    update.message.reply_photo(image_url)

def getDog(update: Update, callback: CallbackContext):
    r = requests.get("https://api.thedogapi.com/v1/images/search")
    data = r.json()
    image_url = data[0]["url"]
    update.message.reply_photo(image_url)

def getHamster(update: Update, callback: CallbackContext):
    params = {
    "q": "Hamster",
    "tbm": "isch",
    "ijn": "0",
    "api_key": str(os.environ["SERP_API"])
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results["images_results"]
    image_url = images_results[0]["original"]
    update.message.reply_photo(image_url)
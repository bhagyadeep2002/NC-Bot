import telegram
from dotenv import load_dotenv
import os
import requests
from telegram import Update
from telegram import ParseMode
from telegram.ext import MessageHandler, Filters
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import CommandHandler
import os
load_dotenv()

def getPrice(update: Update, context: CallbackContext):
    try:
        crypto = context.args[0].upper()
        url = f"https://rest.coinapi.io/v1/exchangerate/{crypto}/INR"
        headers = {'X-CoinAPI-Key' : str(os.environ["CRYPTO_API"])}
        response = requests.get(url, headers=headers)
        temp = response.json()
        price = temp["rate"]
        res = "{:.2f}".format(price)
        currPrice = f"<b>💸 {crypto} 💸</b>\n"
        currPrice += f"<b> Price (INR): </b>{res} "
        update.message.reply_text(text=currPrice, parse_mode=ParseMode.HTML)
    except:
        update.message.reply_text(text="<b> Please enter a valid crypto Token </b>", parse_mode=ParseMode.HTML)
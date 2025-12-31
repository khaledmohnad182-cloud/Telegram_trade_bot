from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import datetime

TOKEN = "Here is the token for bot alftnah trader @alftnah2025bot:

8356379468:AAGLuUh5BuR7rUOcKLB7tXCVo-dGPxqgd3A"

async def signal_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pair = update.message.text.upper()
    hour = datetime.datetime.utcnow().hour

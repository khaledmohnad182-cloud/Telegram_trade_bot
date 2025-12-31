from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import datetime

# التوكن الخاص بالبوت
TOKEN = "8356379468:AAGLuUh5BuR7rUOcKLB7tXCVo-dGPxqgd3A"

async def signal_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pair = update.message.text.upper()
    hour = datetime.datetime.utcnow().hour

    # منطق بسيط لإشارات التداول
    if "AED" in pair or "CNY" in pair:
        signal = "⬇️ هبوط"
    elif hour % 2 == 0:
        signal = "⬆️ صعود"
    else:
        signal = "⬇️ هبوط"

    await update.message.reply_text(f"{signal} لمدة 2 دقيقة")

# إنشاء تطبيق البوت وتشغيله
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, signal_bot))
app.run_polling()

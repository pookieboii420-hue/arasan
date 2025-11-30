from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8074141108:AAFVFDp8fBdn6obWQH_S-7i-Uhh82GGaDRg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Movie: ARASAN\nAudio: Tamil\nQuality: 480p | 720p | 1080p\nJoin our channel!"
    buttons = [[InlineKeyboardButton("JOIN CHANNEL", url="https://t.me/+pe9xc8ZmsK82ZDc1")]]
    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(text, reply_markup=reply_markup)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot started…")
app.run_polling()

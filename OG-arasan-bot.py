from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔑 Replace with your BOT_TOKEN from BotFather
BOT_TOKEN = "8074141108:AAFVFDp8fBdn6obWQH_S-7i-Uhh82GGaDRg"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """📽️ Movie: ARASAN
🎧 Audio: Tamil
🎞️ Quality: 480p | 720p | 1080p (HD)

👇 Join our channel
"""
    buttons = [[InlineKeyboardButton("JOIN CHANNEL", url="https://t.me/+pe9xc8ZmsK82ZDc1")]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.message.reply_text(text, parse_mode="HTML", reply_markup=reply_markup)

# Echo handler for other messages
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

# Build the bot application
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("🚀 Bot started… Waiting for messages!")
app.run_polling()

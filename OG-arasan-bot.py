from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# --- VERY IMPORTANT ---
# Replace with your BOT token from BotFather
BOT_TOKEN = "8074141108:AAFVFDp8fBdn6obWQH_S-7i-Uhh82GGaDRg"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """📽️ *ᴍᴏᴠɪᴇ* : ᴀʀᴀꜱᴀɴ  
🎧 *ᴀᴜᴅɪᴏ* : ᴛᴀᴍɪʟ (ᴏꜰꜰɪᴄɪᴀʟ)  
🎞️ *Qᴜᴀʟɪᴛʏ* : 480ᴘ | 720ᴘ | 1080ᴘ (HD)

👇 ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ
"""
    buttons = [
        [InlineKeyboardButton("JOIN CHANNEL", url="https://t.me/+pe9xc8ZmsK82ZDc1")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        text,
        parse_mode="MarkdownV2",
        reply_markup=reply_markup
    )

# Echo for other messages
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

# Build app
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("🚀 Bot started successfully… Waiting for messages!")
app.run_polling()

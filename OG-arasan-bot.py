from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- VERY IMPORTANT ---
# Replace with your NEW bot token from BotFather
BOT_TOKEN = "8074141108:AAFVFDp8fBdn6obWQH_S-7i-Uhh82GGaDRg"


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
        parse_mode="Markdown",
        reply_markup=reply_markup
    )


# Build the bot application
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Add commands
app.add_handler(CommandHandler("start", start))

print("🚀 Bot started successfully… Waiting for messages!")
app.run_polling()
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 MediaOlami botiga xush kelibsiz!\n\n"
        "🎥 Kino\n🧸 Multik\n🎌 Anime\n\n"
        "Kino yoki multik nomini yozing 🔍"
    )

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(
        f"🔍 '{text}' bo‘yicha qidirilmoqda...\n\n"
        "❗ Hozircha test rejim.\n"
        "Keyin haqiqiy bazani ulaymiz."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))
    app.run_polling()

if __name__ == "__main__":
    main()

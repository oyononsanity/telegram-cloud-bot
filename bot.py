import os
import telebot
from telebot.types import MenuButtonWebApp, WebAppInfo
import threading
from flask import Flask

TOKEN = os.getenv("BOT_TOKEN")
WEB_URL = os.getenv("WEB_APP_URL")

bot = telebot.TeleBot(TOKEN)

bot.set_chat_menu_button(
    menu_button=MenuButtonWebApp(
        type="web_app",
        text="🍿 Watch Videos",
        web_app=WebAppInfo(url=WEB_URL)
    )
)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👇")

# ---- Dummy Flask app to bind port for Render Web Service ----
app = Flask("")

@app.route("/")
def home():
    return "Bot is running..."

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ---- Run bot and Flask together ----
threading.Thread(target=run_flask).start()
print("Bot running...")
bot.infinity_polling()

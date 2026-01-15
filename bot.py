import os
import telebot
from telebot.types import MenuButtonWebApp, WebAppInfo

TOKEN = os.getenv("BOT_TOKEN")  # 🔐 cloud থেকে আসবে
bot = telebot.TeleBot(TOKEN)

bot.set_chat_menu_button(
    menu_button=MenuButtonWebApp(
        type="web_app",
        text="🍿 Watch Videos",
        web_app=WebAppInfo(url="https://google.com")
    )
)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👇")

print("Bot running...")
bot.infinity_polling()

import telebot
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.first_name
    bot.reply_to(message,
f"""اهلا {user} 👋
💰 مرحبا بك في بوت الربح الاحترافي
رصيدك: 0.00$
اختر من القائمة:
🎯 المهام
👥 دعوة الاصدقاء
💳 سحب الارباح
🏆 المتصدرين
""")

bot.infinity_polling()

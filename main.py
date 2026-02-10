import telebot
import google.generativeai as genai

TELEGRAM_TOKEN = "944892092:AAFCtq05u_gxa82r-szQrHXUPXFPkjjYdfY"
GEMINI_KEY = "AIzaSyCzlLyyybzvGtxtvUaJXYIbJo78JGUx4HI"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom Doik Mirabror aka! Bot ishga tushdi.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Xatolik: API kalitni tekshiring.")

bot.infinity_polling()
    

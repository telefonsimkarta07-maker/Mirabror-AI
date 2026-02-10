import telebot
import google.generativeai as genai

# 1. Siz yuborgan Telegram Bot Token
TELEGRAM_TOKEN = "944892092:AAFCtq05u_gxa82r-szQrHXUPXFPkjjYdfY"

# 2. Siz yuborgan Gemini API kaliti
GEMINI_KEY = "AIzaSyDXRVtOBr6ze8fKc_1Nb5Mq2_QbNKko0o8"

# Gemini AI sozlamalari
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom Doik Mirabror aka! Mirabror-AI botingiz ishga tushdi. Men tayyorman, savolingizni bering.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        # Sun'iy intellektdan javob olish
        response = model.generate_content(f"Sen aqlli o'zbek tilidagi yordamchisan. Foydalanuvchi: {message.text}")
        bot.reply_to(message, f"Mirabrorning o'ylashicha: \n{response.text}")
    except Exception as e:
        bot.reply_to(message, "Kichik xatolik bo'ldi, qayta urinib ko'ring yoki API kalitni tekshiring.")

print("Bot ishga tushdi...")
bot.infinity_polling()

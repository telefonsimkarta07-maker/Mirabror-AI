import telebot
import google.generativeai as genai
import os
from flask import Flask
from threading import Thread

# 1. MA'LUMOTLAR
TOKEN = "7901300440:AAEg--9ejI2fWKxj9aEPwoNT1Mi333VmoT8"
GEMINI_KEY = "AIzaSyAXvm1viAtu20KNsSmdgxuFc4S_tf5iZ1w"

# Gemini va Bot sozlamalari
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)

# Render uchun kichik "Veb-sayt" qismi
app = Flask('')

@app.route('/')
def home():
    return "Bot tirik va ishlamoqda!"

def run():
    # Render beradigan PORT-ni eshitib turadi
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# Bot buyruqlari
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum, Doik Mirabror aka! Endi botingiz o'chib qolmaydi.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Xato: {e}")
        bot.reply_to(message, "Mirabror aka, Gemini ulanishida xato. Biroz kuting.")

if __name__ == "__main__":
    # Render-ni aldash uchun Flask-ni alohida oqimda yurgizamiz
    Thread(target=run).start()
    bot.remove_webhook()
    print("Bot muvaffaqiyatli ishga tushdi...")
    bot.infinity_polling()
    

import telebot
from telebot import types
import google.generativeai as genai

# 1. YANGI MA'LUMOTLAR
TOKEN = "7901300440:AAEg--9ejI2fWKxj9aEPwoNT1Mi333VmoT8"
GEMINI_KEY = "AIzaSyAXvm1viAtu20KNsSmdgxuFc4S_tf5iZ1w"

# Gemini sozlamalari
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)

# Start buyrug'i (Tugmalar bilan)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🤖 AI bilan suhbat")
    btn2 = types.KeyboardButton("💡 Maslahat")
    markup.add(btn1, btn2)
    
    bot.reply_to(message, "Assalomu alaykum, Doik Mirabror aka! Yangi botingiz ishga tushdi. Savolingizni yozing.", reply_markup=markup)

# Xabarlarni qayta ishlash
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Bot "yozmoqda..." holatini ko'rsatadi
        bot.send_chat_action(message.chat.id, 'typing')
        
        # Sun'iy intellektdan javob olish
        response = model.generate_content(message.text)
        
        # Javobni qaytarish
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Xato: {e}")
        bot.reply_to(message, "Mirabror aka, ulanishda xato bo'ldi. Render'da 'Manual Deploy'ni bosing.")

if __name__ == "__main__":
    # Webhookni tozalash (xatolar oldini olish uchun)
    bot.remove_webhook()
    print("Bot muvaffaqiyatli ishga tushdi...")
    bot.infinity_polling()
    bot.infinity_polling()

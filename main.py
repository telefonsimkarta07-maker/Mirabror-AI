import telebot
import google.generativeai as genai

# 1. Telegram Bot Token
TOKEN = "944892092:AAFCtq05u_gxa82r-szQrHXUPXFPkjjYdfY"

# 2. Gemini API Key (Siz yuborgan yangi kalit)
GEMINI_KEY = "AIzaSyCzlLyyybzvGtxtvUaJXYIbJo78JGUx4HI"

# Sozlamalar
genai.configure(api_key=GEMINI_KEY)

# Render serveri qiynalmasligi uchun eng tezkor modelni tanladik
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Ismingizni talabingizga binoan "Doik"siz to'g'irladik
    bot.reply_to(message, "Salom Mirabror aka! Bot ishga tushdi. Savolingizni yuboring.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        # Gemini javobini olish
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        # Xatoni Render loglarida ko'rish uchun
        print(f"Xatolik: {e}")
        bot.reply_to(message, "Hozircha javob bera olmayman, qayta urinib ko'ring.")

# Webhook to'sig'ini avtomatik yechish
if __name__ == "__main__":
    bot.remove_webhook()
    print("Bot muvaffaqiyatli ishga tushdi...")
    bot.infinity_polling()

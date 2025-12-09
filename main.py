import telebot
import google.generativeai as genai

# ==========================================
# НАСТРОЙКИ (Вставь свои токены сюда)
# ==========================================
TELEGRAM_TOKEN = "7927640953:AAHWA1uxVxxhQR9VMNsMaVxiSpax6yUyXt8"
GEMINI_API_KEY = "AIzaSyCUvrV7VspTaxtIhfXuJd4gnngOV9c7SzI"

# Настройка Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash-lite')

# Настройка Telegram бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я подключен к Gemini. Спроси меня о чем угодно.")

# Обработчик любого текста
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Отправляем боту сообщение "Печатает...", чтобы пользователь видел активность
        bot.send_chat_action(message.chat.id, 'typing')

        # Отправляем запрос в Gemini
        response = model.generate_content(message.text)

        # Отправляем ответ пользователю
        # response.text содержит готовый ответ нейросети
        bot.reply_to(message, response.text)

    except Exception as e:
        # Если возникла ошибка (например, фильтр безопасности Gemini), сообщаем об этом
        bot.reply_to(message, f"Произошла ошибка или сработал фильтр безопасности.\nДетали: {e}")

# Запуск постоянного опроса серверов Telegram
if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()

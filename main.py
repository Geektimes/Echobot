import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Включим логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен вашего бота (замените на свой)
TOKEN = "7927640953:AAHWA1uxVxxhQR9VMNsMaVxiSpax6yUyXt8"

# Функция-обработчик для всех текстовых сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Повторяет сообщение пользователя."""
    # Отправляем обратно тот же текст, что прислал пользователь
    await update.message.reply_text(update.message.text)

def main() -> None:
    """Запуск бота."""
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик для текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

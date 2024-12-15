from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from weather import get_weather_emoji
from config import TELEGRAM_TOKEN, WEBAPP_URL
import json

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Создаем кнопку с WebApp
    keyboard = [
        [
            InlineKeyboardButton(
                "Открыть мини-приложение", web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите статус через мини-приложение:", reply_markup=reply_markup)

# Обработка данных от мини-приложения
async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Получаем данные из WebApp
    data = json.loads(update.message.web_app_data.data)
    emoji = data.get("emoji", "🌍")
    description = data.get("description", "Неизвестно")

    # Ответ пользователю
    await update.message.reply_text(f"Вы выбрали эмодзи-статус: {emoji} ({description})")

    # Здесь можно добавить код для обновления эмодзи-статуса через API (если у пользователя Telegram Premium)

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))

    print("Бот запущен!")
    application.run_polling()

if __name__ == "__main__":
    main()

from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import json

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Создаем кнопку, которая откроет Mini App
    keyboard = [[KeyboardButton(
        text="Открыть меню услуг",
        web_app=WebAppInfo(url="ВАША_ССЫЛКА_НА_MINI_APP")
    )]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "Добро пожаловать! Нажмите на кнопку ниже, чтобы открыть меню услуг:",
        reply_markup=reply_markup
    )

async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Обработка данных, отправленных из Mini App
    data = json.loads(update.effective_message.web_app_data.data)
    services = {
        "mortgage": "ИПОТЕКА",
        "visa": "ВИЗА",
        "bank": "СЧЕТ В БАНКЕ",
        "lawyer": "ВАШ ЮРИСТ",
        "company": "ОТКРЫТЬ КОМПАНИЮ",
        "consultation": "КОНСУЛЬТАЦИЯ"
    }
    
    service_name = services.get(data["service"], "Неизвестная услуга")
    await update.message.reply_text(f"Вы выбрали: {service_name}\nНаш специалист свяжется с вами!")

def main():
    application = Application.builder().token("ВАШ_ТОКЕН_БОТА").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))

    application.run_polling()

if __name__ == "__main__":
    main()
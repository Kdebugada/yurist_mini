import logging
import os
import asyncio
from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
API_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher(storage=MemoryStorage())
router = Router()

# URL вашего мини-приложения
WEBAPP_URL = os.getenv('WEBAPP_URL')

# Создание клавиатуры с кнопкой для запуска мини-приложения
def get_webapp_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏢 Открыть мини-приложение", web_app={"url": WEBAPP_URL})]
    ])
    return keyboard

# Обработчик команды /start
@router.message(Command("start"))
async def send_welcome(message: types.Message):
    # Отправляем только инлайн-кнопку для запуска приложения
    await message.answer(
        f"👋 Здравствуйте, {message.from_user.first_name}!\n\n"
        "Я бот-помощник по юридическим услугам в ОАЭ.\n"
        "Нажмите на кнопку ниже, чтобы открыть мини-приложение:",
        reply_markup=get_webapp_keyboard()
    )

# Обработчик для всех остальных сообщений
@router.message()
async def handle_text(message: types.Message):
    if not message.web_app_data:
        # Отправляем только кнопку для входа в мини-приложение
        await message.answer(
            "Для получения информации о наших услугах, пожалуйста, воспользуйтесь мини-приложением:",
            reply_markup=get_webapp_keyboard()
        )
    else:
        # Получаем данные из веб-приложения
        data = message.web_app_data.data
        
        # Отправляем подтверждение получения данных
        await message.answer(
            f"✅ Данные из мини-приложения получены!\n\n"
            f"Мы обработаем вашу заявку и свяжемся с вами в ближайшее время.",
            reply_markup=get_webapp_keyboard()
        )
        
        # Здесь можно добавить логику обработки данных из веб-приложения
        logging.info(f"Получены данные из веб-приложения: {data}")

# Запуск бота
async def main():
    # Регистрация обработчиков
    dp.include_router(router)
    
    # Запуск бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main()) 
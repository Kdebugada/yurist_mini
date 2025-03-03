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
        "",
        reply_markup=get_webapp_keyboard()
    )

# Обработчик для всех остальных сообщений
@router.message()
async def handle_text(message: types.Message):
    # Отправляем только кнопку для входа в мини-приложение
    await message.answer(
        "",
        reply_markup=get_webapp_keyboard()
    )

# Запуск бота
async def main():
    # Регистрация обработчиков
    dp.include_router(router)
    
    # Запуск бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main()) 
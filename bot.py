import logging
import asyncio
from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
API_TOKEN = '7691650728:AAHZj6V35OPoq8qh5Ke3CgquHu5XA6sK1js'
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher(storage=MemoryStorage())
router = Router()

# URL мини-приложения
WEBAPP_URL = 'https://kdebugada.github.io/yurist_mini/'

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
        "Добро пожаловать! Нажмите на кнопку ниже, чтобы открыть мини-приложение.",
        reply_markup=get_webapp_keyboard()
    )

# Обработчик для всех остальных сообщений
@router.message()
async def handle_text(message: types.Message):
    # Отправляем только кнопку для входа в мини-приложение
    await message.answer(
        "Используйте кнопку ниже для доступа к мини-приложению.",
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
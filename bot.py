import logging
import os
import asyncio
from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
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

# Создание основной клавиатуры
def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="📱 Открыть приложение", web_app={"url": WEBAPP_URL})],
        [KeyboardButton(text="ℹ️ Информация"), KeyboardButton(text="❓ Помощь")],
        [KeyboardButton(text="📞 Контакты")]
    ], resize_keyboard=True)
    return keyboard

# Обработчик команды /start
@router.message(Command("start"))
async def send_welcome(message: types.Message):
    # Отправляем приветственное сообщение с кнопкой
    await message.answer(
        f"👋 Здравствуйте, {message.from_user.first_name}!\n\n"
        "Я бот-помощник по юридическим услугам в ОАЭ.\n"
        "Нажмите на кнопку ниже, чтобы открыть мини-приложение и получить консультацию:",
        reply_markup=get_main_keyboard()
    )
    
    # Отправляем инлайн-кнопку для запуска приложения
    await message.answer(
        "Вы также можете использовать эту кнопку для запуска приложения:",
        reply_markup=get_webapp_keyboard()
    )

# Обработчик команды /help
@router.message(Command("help"))
async def send_help(message: types.Message):
    help_text = (
        "🔍 *Как пользоваться ботом:*\n\n"
        "• Нажмите кнопку \"📱 Открыть приложение\" для запуска мини-приложения\n"
        "• В мини-приложении вы можете:\n"
        "   - Узнать о юридических услугах в ОАЭ\n"
        "   - Получить консультацию по ипотеке\n"
        "   - Оставить заявку на обратную связь\n\n"
        "• Используйте команды:\n"
        "   /start - запустить бота\n"
        "   /help - получить помощь\n"
        "   /info - информация о услугах\n"
        "   /contact - контактная информация"
    )
    
    await message.answer(help_text, reply_markup=get_main_keyboard())
    await message.answer("Открыть мини-приложение:", reply_markup=get_webapp_keyboard())

# Обработчик команды /info
@router.message(Command("info"))
async def send_info(message: types.Message):
    info_text = (
        "🏢 *Наши услуги в ОАЭ:*\n\n"
        "• *Юридические консультации*\n"
        "• *Ипотечное кредитование*\n"
        "• *Открытие банковских счетов*\n"
        "• *Оформление виз*\n"
        "• *Регистрация компаний*\n\n"
        "Для получения подробной информации воспользуйтесь нашим мини-приложением."
    )
    
    await message.answer(info_text, reply_markup=get_main_keyboard())
    await message.answer("Открыть мини-приложение:", reply_markup=get_webapp_keyboard())

# Обработчик команды /contact
@router.message(Command("contact"))
async def send_contact(message: types.Message):
    contact_text = (
        "📞 *Контактная информация:*\n\n"
        "• *Телефон:* +971 XX XXX XXXX\n"
        "• *Email:* info@example.com\n"
        "• *Адрес:* Dubai, UAE\n\n"
        "Вы также можете оставить заявку через мини-приложение, и мы свяжемся с вами."
    )
    
    await message.answer(contact_text, reply_markup=get_main_keyboard())

# Обработчик для текстовых сообщений
@router.message()
async def handle_text(message: types.Message):
    if not message.web_app_data:
        text = message.text.lower() if message.text else ""
        
        if text == "ℹ️ информация" or text == "информация":
            await send_info(message)
        elif text == "❓ помощь" or text == "помощь":
            await send_help(message)
        elif text == "📞 контакты" or text == "контакты":
            await send_contact(message)
        else:
            # Отправляем сообщение с кнопкой
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
            reply_markup=get_main_keyboard()
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
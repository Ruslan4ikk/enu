import logging
import json
import os
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.utils.executor import start_polling
from bot_sections_logic import main_menu, services_menu, interactive_menu, settings_menu, extras_menu
from platonus_webview import open_platonus
import google.generativeai as genai

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Константы
TELEGRAM_API_KEY = "7249084291:AAHtZKO4oj5m81fR9F-ey_KPGRjBNI_rMUo"
GEMINI_API_KEY = "AIzaSyA443fdvjgwe4qoTosJDUqapzAp30qWL_Y"
ADMIN_ID = 568010963
DATA_FILE = 'data.json'

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_API_KEY, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

genai.configure(api_key=GEMINI_API_KEY)

# Функция загрузки истории сообщений
def load_chat_history(user_id):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get(str(user_id), [])
    return []

# Функция сохранения истории сообщений
def save_chat_history(user_id, message):
    data = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    
    user_history = data.get(str(user_id), [])
    user_history.append(message)
    data[str(user_id)] = user_history[-20:]  # Ограничиваем историю до 20 сообщений
    
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Генерация ответа с учётом памяти
def generate_gemini_response(user_id, user_message):
    try:
        history = load_chat_history(user_id)
        context = "\n".join(history)
        
        system_message = (
            "Ты — интеллектуальный помощник Евразийского национального университета (ЕНУ). "
            "Отвечай подробно, логично и по-человечески. "
            "Используй информацию из базы знаний, если она есть, иначе отвечай на основе общих знаний. "
            "Контекст переписки: " + context
        )

        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(f"{system_message}\nПользователь: {user_message}\nОтвет:")
        
        save_chat_history(user_id, user_message)
        save_chat_history(user_id, response.text)
        
        return response.text.replace('*', '').replace('**', '')
    except Exception as e:
        logging.error(f"Ошибка генерации ответа Gemini: {e}")
        return "Извините, произошла ошибка при обработке запроса. Попробуйте позже."

# Обработчики разделов
@dp.message_handler(commands=['menu'])
async def cmd_menu(message: types.Message):
    await message.reply("📌 <b>Главное меню</b>\nВыберите нужный раздел:", reply_markup=main_menu(), parse_mode=types.ParseMode.HTML)

@dp.message_handler(lambda message: message.text == "🔗 Полезные сервисы")
async def show_services_menu(message: types.Message):
    await message.reply("🔗 <b>Полезные сервисы</b>\nВыберите нужный сервис:", reply_markup=services_menu(), parse_mode=types.ParseMode.HTML)

@dp.message_handler(lambda message: message.text == "🎯 Интерактивные функции")
async def show_interactive_menu(message: types.Message):
    await message.reply("🎯 <b>Интерактивные функции</b>\nВыберите нужный раздел:", reply_markup=interactive_menu(), parse_mode=types.ParseMode.HTML)

@dp.message_handler(lambda message: message.text == "⚙ Персональные настройки")
async def show_settings_menu(message: types.Message):
    await message.reply("⚙ <b>Персональные настройки</b>\nВыберите нужную настройку:", reply_markup=settings_menu(), parse_mode=types.ParseMode.HTML)

@dp.message_handler(lambda message: message.text == "📢 Дополнительные возможности")
async def show_extras_menu(message: types.Message):
    await message.reply("📢 <b>Дополнительные возможности</b>\nВыберите нужный раздел:", reply_markup=extras_menu(), parse_mode=types.ParseMode.HTML)

@dp.message_handler(lambda message: message.text == "🔑 Platonus")
async def open_platonus_menu(message: types.Message):
    await open_platonus(message)

@dp.message_handler(lambda message: message.text == "🔙 Назад")
async def go_back(message: types.Message):
    await message.reply("📌 <b>Главное меню</b>", reply_markup=main_menu(), parse_mode=types.ParseMode.HTML)

# Обработка обычных сообщений с памятью
@dp.message_handler()
async def handle_messages(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    gemini_response = generate_gemini_response(message.from_user.id, message.text)
    await message.reply(gemini_response, parse_mode=types.ParseMode.HTML)

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    start_polling(dp, skip_updates=True)

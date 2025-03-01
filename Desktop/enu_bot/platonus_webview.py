from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types, Dispatcher

# Создаём WebView-кнопку для входа в Platonus
def platonus_button():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔑 Войти в Platonus", url="https://platonus.enu.kz"))
    return keyboard

# Обработчик кнопки Platonus
async def open_platonus(message: types.Message):
    await message.reply("🔹 Нажмите на кнопку ниже, чтобы войти в Platonus:", reply_markup=platonus_button())

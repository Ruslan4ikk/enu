from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# Главное меню
def main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton("📜 О университете"), KeyboardButton("🎓 Факультеты"))
    keyboard.row(KeyboardButton("📝 Поступление"), KeyboardButton("☎ Контакты"))
    keyboard.row(KeyboardButton("🔗 Полезные сервисы"), KeyboardButton("🎯 Интерактивные функции"))
    keyboard.row(KeyboardButton("⚙ Персональные настройки"), KeyboardButton("📢 Дополнительные возможности"))
    keyboard.row(KeyboardButton("🔑 Platonus", web_app=WebAppInfo(url="https://edu.enu.kz/")))  # WebApp кнопка
    return keyboard

# Полезные сервисы
def services_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton("📆 Расписание"), KeyboardButton("📚 Библиотека"))
    keyboard.row(KeyboardButton("🍽 Столовая"), KeyboardButton("📌 Новости"))
    keyboard.row(KeyboardButton("🔙 Назад"))
    return keyboard

# Интерактивные функции
def interactive_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton("❓ Задать вопрос"), KeyboardButton("🏆 Рейтинг студентов"))
    keyboard.row(KeyboardButton("👥 Курсы и кружки"), KeyboardButton("🔗 Полезные ссылки"))
    keyboard.row(KeyboardButton("🔙 Назад"))
    return keyboard

# Персональные настройки
def settings_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton("⚙ Изменить профиль"), KeyboardButton("🔔 Уведомления"))
    keyboard.row(KeyboardButton("🏠 Личный кабинет"), KeyboardButton("🌍 Выбор языка"))
    keyboard.row(KeyboardButton("🔙 Назад"))
    return keyboard

# Дополнительные возможности
def extras_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton("💼 Карьера"), KeyboardButton("🎤 Мероприятия"))
    keyboard.row(KeyboardButton("📢 Объявления"), KeyboardButton("💬 Чаты и сообщества"))
    keyboard.row(KeyboardButton("🔙 Назад"))
    return keyboard

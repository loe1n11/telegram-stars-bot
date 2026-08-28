import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Bot Configuration
BOT_NAME = "Telegram Stars Bot"
BOT_VERSION = "0.1.0"

# Messages
MESSAGES = {
    'welcome': """
🌟 <b>Добро пожаловать в Telegram Stars Bot!</b>

Здесь вы можете найти информацию о продаже Telegram Stars.

Выберите опцию из меню ниже:
    """,
    'info': """
📋 <b>Информация о сервисе</b>

Мы предоставляем возможность приобретения Telegram Stars через различные способы оплаты:
• WATA
• TON (Toncoin)

<i>Функционал покупки находится в разработке и будет доступен позже.</i>
    """,
    'faq': """
❓ <b>Часто задаваемые вопросы</b>

<b>Что такое Telegram Stars?</b>
Это встроенная валюта Telegram, которая используется для покупки услуг и контента в приложении.

<b>Какие способы оплаты доступны?</b>
В настоящий момент разрабатываются способы оплаты через WATA и TON.

<b>Когда будет доступна покупка?</b>
Функционал будет включен в следующем обновлении.
    """,
    'contact': """
📧 <b>Свяжитесь с нами</b>

По вопросам и предложениям обращайтесь в поддержку.
    """,
    'error': """
❌ <b>Ошибка</b>

К сожалению, что-то пошло не так. Пожалуйста, повторите попытку.
    """,
    'not_available': """
🚫 <b>Функция недоступна</b>

Покупка Telegram Stars находится в стадии разработки. Пожалуйста, вернитесь позже.
    """
}

# Button Labels
BUTTONS = {
    'info': '📋 Информация',
    'faq': '❓ Часто задаваемые вопросы',
    'profile': '👤 Профиль',
    'contact': '📧 Поддержка',
    'back': '◀️ Назад',
    'buy_stars': '💰 Купить звезды',
}

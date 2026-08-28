from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import BUTTONS, STAR_PACKAGES, get_package_button_text

def get_main_keyboard():
    """Get main menu keyboard"""
    keyboard = [
        [KeyboardButton(BUTTONS['buy_stars'])],
        [KeyboardButton(BUTTONS['profile']), KeyboardButton(BUTTONS['history'])],
        [KeyboardButton(BUTTONS['faq']), KeyboardButton(BUTTONS['contact'])],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_back_keyboard():
    """Get back button keyboard"""
    keyboard = [[KeyboardButton(BUTTONS['back'])]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_main_menu_keyboard():
    """Get main menu button keyboard"""
    keyboard = [[KeyboardButton(BUTTONS['main_menu'])]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_buy_stars_inline_keyboard():
    """Get inline keyboard for buying stars with different packages"""
    keyboard = []
    for i, package in enumerate(STAR_PACKAGES):
        keyboard.append([
            InlineKeyboardButton(
                text=get_package_button_text(package),
                callback_data=f"buy_stars_{i}"
            )
        ])
    keyboard.append([InlineKeyboardButton(text=BUTTONS['back'], callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

def get_payment_method_keyboard():
    """Get inline keyboard for payment methods"""
    keyboard = [
        [InlineKeyboardButton("💳 Карта (Visa/Mastercard)", callback_data="pay_card")],
        [InlineKeyboardButton("🏦 Яндекс.Касса", callback_data="pay_yandex")],
        [InlineKeyboardButton("📱 Киви кошелёк", callback_data="pay_kiwi")],
        [InlineKeyboardButton("💎 TON Crypto", callback_data="pay_ton")],
        [InlineKeyboardButton("💰 WATA", callback_data="pay_wata")],
        [InlineKeyboardButton(BUTTONS['back'], callback_data="back_to_stars")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_referral_keyboard():
    """Get keyboard for referral code actions"""
    keyboard = [
        [KeyboardButton("📋 Копировать реферальный код")],
        [KeyboardButton("👥 Статистика рефералов")],
        [KeyboardButton(BUTTONS['back'])]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_profile_detail_keyboard():
    """Get keyboard for profile details"""
    keyboard = [
        [KeyboardButton("🔗 Реферальный код")],
        [KeyboardButton("💰 История платежей")],
        [KeyboardButton(BUTTONS['back'])]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

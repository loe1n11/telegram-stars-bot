from telegram import ReplyKeyboardMarkup, KeyboardButton
from config import BUTTONS

def get_main_keyboard():
    """Get main menu keyboard"""
    keyboard = [
        [KeyboardButton(BUTTONS['info'])],
        [KeyboardButton(BUTTONS['faq'])],
        [KeyboardButton(BUTTONS['profile'])],
        [KeyboardButton(BUTTONS['contact'])],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_back_keyboard():
    """Get back button keyboard"""
    keyboard = [
        [KeyboardButton(BUTTONS['back'])],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_buy_keyboard():
    """Get buy stars keyboard (currently disabled)"""
    keyboard = [
        [KeyboardButton(BUTTONS['buy_stars'])],
        [KeyboardButton(BUTTONS['back'])],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

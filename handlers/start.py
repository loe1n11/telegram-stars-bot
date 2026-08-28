from telegram import Update
from telegram.ext import ContextTypes
from config import MESSAGES, BOT_NAME, BOT_VERSION
from keyboards.main import get_main_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command"""
    user = update.effective_user
    welcome_message = f"{MESSAGES['welcome']}\n\n<i>v{BOT_VERSION}</i>"
    
    await update.message.reply_html(
        welcome_message,
        reply_markup=get_main_keyboard()
    )

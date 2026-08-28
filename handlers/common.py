from telegram import Update
from telegram.ext import ContextTypes
from config import MESSAGES, BUTTONS
from keyboards.main import get_main_keyboard
from handlers.info import info, faq, contact
from handlers.profile import profile

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle text messages based on button presses"""
    text = update.message.text
    
    if text == BUTTONS['info']:
        await info(update, context)
    elif text == BUTTONS['faq']:
        await faq(update, context)
    elif text == BUTTONS['profile']:
        await profile(update, context)
    elif text == BUTTONS['contact']:
        await contact(update, context)
    elif text == BUTTONS['back']:
        await back_to_main(update, context)
    elif text == BUTTONS['buy_stars']:
        await buy_stars(update, context)
    else:
        await unknown_command(update, context)

async def back_to_main(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Return to main menu"""
    from handlers.start import start
    await start(update, context)

async def buy_stars(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle buy stars request (currently not available)"""
    await update.message.reply_html(
        MESSAGES['not_available'],
        reply_markup=get_main_keyboard()
    )

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle unknown commands"""
    await update.message.reply_html(
        "❓ Пожалуйста, используйте меню ниже.",
        reply_markup=get_main_keyboard()
    )

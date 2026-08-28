from telegram import Update
from telegram.ext import ContextTypes
from config import MESSAGES, BUTTONS
from keyboards.main import get_back_keyboard

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle info request"""
    await update.message.reply_html(
        MESSAGES['info'],
        reply_markup=get_back_keyboard()
    )

async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle FAQ request"""
    faq_message = MESSAGES['faq']
    await update.message.reply_html(
        faq_message,
        reply_markup=get_back_keyboard()
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle contact request"""
    await update.message.reply_html(
        MESSAGES['contact'],
        reply_markup=get_back_keyboard()
    )

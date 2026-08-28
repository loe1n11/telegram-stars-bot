from telegram import Update
from telegram.ext import ContextTypes
from config import MESSAGES, BOT_VERSION, BOT_NAME
from keyboards.main import get_main_keyboard
from models.database import get_user, create_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command"""
    user = update.effective_user
    
    # Get or create user in database
    db_user = get_user(user.id)
    if not db_user:
        db_user = create_user(
            user.id,
            user.first_name,
            user.last_name,
            user.username
        )
    
    welcome_message = f"{MESSAGES['welcome']}\n\n<i>v{BOT_VERSION}</i>"
    
    await update.message.reply_html(
        welcome_message,
        reply_markup=get_main_keyboard()
    )

async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show main menu"""
    await update.message.reply_html(
        "🏠 <b>Главное меню</b>",
        reply_markup=get_main_keyboard()
    )

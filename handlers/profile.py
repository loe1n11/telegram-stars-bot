from telegram import Update
from telegram.ext import ContextTypes
from keyboards.main import get_back_keyboard

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle profile request"""
    user = update.effective_user
    
    profile_message = f"""
👤 <b>Ваш профиль</b>

<b>ID:</b> <code>{user.id}</code>
<b>Имя:</b> {user.first_name}
{f"<b>Фамилия:</b> {user.last_name}" if user.last_name else ""}
{f"<b>Username:</b> @{user.username}" if user.username else ""}

<i>Дополнительная информация будет доступна в следующих обновлениях.</i>
    """
    
    await update.message.reply_html(
        profile_message,
        reply_markup=get_back_keyboard()
    )

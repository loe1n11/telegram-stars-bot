from telegram import Update
from telegram.ext import ContextTypes
from config import MESSAGES, BUTTONS
from keyboards.main import get_back_keyboard
from models.database import get_user, save_user

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle profile request"""
    user = update.effective_user
    db_user = get_user(user.id)
    
    if not db_user:
        await update.message.reply_html(
            "❌ Профиль не найден. Пожалуйста, начните с команды /start",
            reply_markup=get_back_keyboard()
        )
        return
    
    # Update level based on spending
    db_user.update_level()
    save_user(db_user)
    
    last_name_info = f"\n👨‍👩‍👧‍👦 Фамилия: <b>{db_user.last_name}</b>" if db_user.last_name else ""
    username_info = f"\n💬 Username: <b>@{db_user.username}</b>" if db_user.username else ""
    
    profile_message = MESSAGES['profile'].format(
        user_id=db_user.user_id,
        first_name=db_user.first_name,
        last_name_info=last_name_info,
        username_info=username_info,
        joined_date=db_user.get_joined_date(),
        total_spent=db_user.total_spent,
        purchase_count=db_user.purchase_count,
        balance=db_user.balance,
        ref_code=db_user.referral_code,
        referral_count=db_user.referral_count,
        referral_earning=db_user.referral_earning,
        level=db_user.level,
        achievements=len(db_user.achievements)
    )
    
    await update.message.reply_html(
        profile_message,
        reply_markup=get_back_keyboard()
    )

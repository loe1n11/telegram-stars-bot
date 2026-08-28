from telegram import Update
from telegram.ext import ContextTypes
from config import MESSAGES, BUTTONS, STAR_PACKAGES, get_package_button_text
from keyboards.main import (
    get_main_keyboard, 
    get_back_keyboard, 
    get_buy_stars_inline_keyboard,
    get_payment_method_keyboard
)
from models.database import get_user, save_user, get_user_transactions, add_transaction
from models.user import Transaction
import uuid
from datetime import datetime

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle text messages based on button presses"""
    text = update.message.text
    
    if text == BUTTONS['buy_stars']:
        await buy_stars_menu(update, context)
    elif text == BUTTONS['profile']:
        from handlers.profile import profile
        await profile(update, context)
    elif text == BUTTONS['history']:
        await show_history(update, context)
    elif text == BUTTONS['faq']:
        from handlers.info import faq
        await faq(update, context)
    elif text == BUTTONS['contact']:
        from handlers.info import contact
        await contact(update, context)
    elif text == BUTTONS['back'] or text == BUTTONS['main_menu']:
        await back_to_main(update, context)
    else:
        await unknown_command(update, context)

async def buy_stars_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show star packages for purchase"""
    packages_list = ""
    for package in STAR_PACKAGES:
        packages_list += f"• {get_package_button_text(package)}\n"
    
    buying_message = MESSAGES['buying_stars'].format(packages_list=packages_list)
    
    await update.message.reply_html(
        buying_message,
        reply_markup=get_buy_stars_inline_keyboard()
    )

async def show_history(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show purchase history"""
    user = update.effective_user
    db_user = get_user(user.id)
    
    if not db_user:
        await update.message.reply_html(
            "❌ Профиль не найден",
            reply_markup=get_back_keyboard()
        )
        return
    
    transactions = get_user_transactions(user.id)
    
    if not transactions:
        await update.message.reply_html(
            MESSAGES['empty_history'],
            reply_markup=get_back_keyboard()
        )
        return
    
    # Format transaction history
    history_content = "<b>📋 Ваши покупки:</b>\n\n"
    total_spent = 0
    total_stars = 0
    
    for trans in transactions:
        status_emoji = trans.get_status_emoji()
        history_content += (
            f"{status_emoji} <b>{trans.get_formatted_date()}</b>\n"
            f"   ⭐ Звёзд: {trans.stars} | 💰 Цена: {trans.price}₽\n"
            f"   💳 Метод: {trans.payment_method}\n\n"
        )
        if trans.status == 'completed':
            total_spent += trans.price
            total_stars += trans.stars
    
    history_message = MESSAGES['history'].format(
        history_content=history_content,
        total_spent=total_spent,
        total_stars=total_stars,
        transactions_count=len(transactions)
    )
    
    await update.message.reply_html(
        history_message,
        reply_markup=get_back_keyboard()
    )

async def back_to_main(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Return to main menu"""
    from handlers.start import start
    await start(update, context)

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle unknown commands"""
    await update.message.reply_html(
        "❓ Пожалуйста, используйте меню ниже.",
        reply_markup=get_main_keyboard()
    )

async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle inline button clicks"""
    query = update.callback_query
    await query.answer()
    
    if query.data.startswith('buy_stars_'):
        # Extract package index
        try:
            package_idx = int(query.data.split('_')[2])
            if 0 <= package_idx < len(STAR_PACKAGES):
                package = STAR_PACKAGES[package_idx]
                context.user_data['selected_package'] = package
                
                message = (
                    f"💳 <b>Выбран пакет: {package['name']}</b>\n\n"
                    f"⭐ Звёзд: {package['stars']}\n"
                    f"💰 Цена: {package['price']}₽\n\n"
                    f"<b>Выберите способ оплаты:</b>"
                )
                
                await query.edit_message_text(
                    text=message,
                    parse_mode='HTML',
                    reply_markup=get_payment_method_keyboard()
                )
        except (ValueError, IndexError):
            pass
    
    elif query.data.startswith('pay_'):
        # Handle payment method selection
        payment_method_map = {
            'card': 'Карта (Visa/Mastercard)',
            'yandex': 'Яндекс.Касса',
            'kiwi': 'Киви кошелёк',
            'ton': 'TON Crypto',
            'wata': 'WATA'
        }
        payment_method = query.data.split('_')[1]
        payment_method_name = payment_method_map.get(payment_method, payment_method)
        package = context.user_data.get('selected_package')
        
        if package:
            # Create transaction
            transaction = Transaction(
                transaction_id=str(uuid.uuid4()),
                user_id=update.effective_user.id,
                stars=package['stars'],
                price=package['price'],
                payment_method=payment_method_name,
                status='completed'
            )
            add_transaction(transaction)
            
            # Update user data
            db_user = get_user(update.effective_user.id)
            if db_user:
                db_user.purchase_count += 1
                db_user.total_spent += package['price']
                db_user.balance += package['stars']
                db_user.update_level()
                save_user(db_user)
            
            success_message = (
                f"✅ <b>Заказ успешно обработан!</b>\n\n"
                f"🆔 ID заказа: <code>{transaction.transaction_id}</code>\n"
                f"⭐ Звёзд: {package['stars']}\n"
                f"💰 Сумма: {package['price']}₽\n"
                f"💳 Метод: {payment_method_name}\n\n"
                f"✨ Спасибо за покупку! 🎉\n\n"
                f"Звезды уже на вашем аккаунте Telegram!"
            )
            
            await query.edit_message_text(
                text=success_message,
                parse_mode='HTML'
            )
    
    elif query.data == 'back_to_main':
        from handlers.start import start
        await start(update, context)
    
    elif query.data == 'back_to_stars':
        packages_list = ""
        for package in STAR_PACKAGES:
            packages_list += f"• {get_package_button_text(package)}\n"
        
        buying_message = MESSAGES['buying_stars'].format(packages_list=packages_list)
        
        await query.edit_message_text(
            text=buying_message,
            parse_mode='HTML',
            reply_markup=get_buy_stars_inline_keyboard()
        )

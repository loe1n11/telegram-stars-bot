#!/usr/bin/env python3
"""
Telegram Stars Bot - Main entry point with beautiful UI
"""

import logging
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)
from config import TELEGRAM_BOT_TOKEN, LOG_LEVEL
from handlers.start import start
from handlers.common import handle_text, handle_callback_query

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=LOG_LEVEL
)
logger = logging.getLogger(__name__)

def main():
    """Start the bot"""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN not set in environment variables")
        return
    
    # Create the Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_callback_query))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    
    # Start the Bot
    logger.info("🤖 Starting Telegram Stars Bot...")
    logger.info("✅ Bot is running! Send /start to begin.")
    application.run_polling()

if __name__ == '__main__':
    main()

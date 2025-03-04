import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Update
from user_manager import UserManager
from proxy_manager import ProxyManager
from registration import register_account
from logging_config import configure_logging

# Configure logging
configure_logging()

# Initialize Managers
user_manager = UserManager()
proxy_manager = ProxyManager()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome to the Grass Bot!')

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await update.message.reply_text('Usage: /register email:password [refer_code]')
        return
    
    email_password = context.args[0]
    try:
        email, password = email_password.split(':')
    except ValueError:
        await update.message.reply_text('Invalid email:password format.')
        return
    
    refer_code = context.args[1] if len(context.args) > 1 else None
    result = await register_account(email, password, refer_code)
    await update.message.reply_text(result)

async def assign_proxy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text('Usage: /assign_proxy email proxy')
        return
    
    email = context.args[0]
    proxy = context.args[1]
    result = proxy_manager.assign_proxy(email, proxy)
    await update.message.reply_text(result)

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status_message = proxy_manager.get_status()
    await update.message.reply_text(status_message)

def main():
    # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
    application = ApplicationBuilder().token('YOUR_TELEGRAM_BOT_TOKEN').build()

    start_handler = CommandHandler('start', start)
    register_handler = CommandHandler('register', register)
    assign_proxy_handler = CommandHandler('assign_proxy', assign_proxy)
    status_handler = CommandHandler('status', status)

    application.add_handler(start_handler)
    application.add_handler(register_handler)
    application.add_handler(assign_proxy_handler)
    application.add_handler(status_handler)

    application.run_polling()

if __name__ == '__main__':
    main()

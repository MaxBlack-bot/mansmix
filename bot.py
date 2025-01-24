import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Your bot's token
BOT_TOKEN = '7535027604:AAG4n3dHwfcdfRpgggTAlILh9Zwwy4T_t40'

# Your Web App and GitHub URLs
WEB_APP_URL = 'https://prod-rnd-frontend-php.100hp.app/mines/?exitUrl=https%253A%252F%252F1win.com%252Fcasino&language=en&b=demo'
GITHUB_URL = 'https://maxblack-bot.github.io/mansmix/'  # Replace with your GitHub URL

# Your 1win ID
WIN_ID = '97745262'  # Replace this with the actual ID for 1win

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /start command.
    Sends a welcome message with buttons for the Web App, GitHub, and the 1win ID.
    """
    keyboard = [
        [InlineKeyboardButton("Start Game", web_app={"url": WEB_APP_URL})],
        [InlineKeyboardButton("GitHub Repository", url=GITHUB_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Include the 1win ID in the message
    message_text = (
        f"Welcome to MineGames! Your 1win ID is: **{WIN_ID}**.\n"
        "Click a button below to get started."
    )

    await update.message.reply_text(
        text=message_text,
        reply_markup=reply_markup,
        parse_mode="Markdown"  # To format the ID in bold
    )

def main() -> None:
    """
    Main function to run the bot.
    """
    # Ensure the bot token is available
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing! Please check your environment or code settings.")

    # Create the bot application using the token
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add a handler for the /start command
    app.add_handler(CommandHandler("start", start))

    # Start the bot
    print("Bot is running... You can now interact with it!")
    app.run_polling()

# Run the bot
if __name__ == '__main__':
    main()

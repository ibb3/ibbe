import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.getenv('TOKEN')  # Retrieve bot token from environment variable

# Function to handle /start command
def start(update: telegram.Update, context: telegram.ext.CallbackContext):
    update.message.reply_text("Hello! I'm your bot. Send me a video link from YouTube, TikTok, or Instagram and I will download it for you.")

# Function to handle text messages (URLs)
def handle_message(update: telegram.Update, context: telegram.ext.CallbackContext):
    # Check if the message contains a URL
    if update.message.text.startswith('http://') or update.message.text.startswith('https://'):
        download_video(update.message.text.strip(), update.message.chat_id)
    else:
        update.message.reply_text("Please send a valid video URL.")

# Function to download video based on URL type (YouTube, TikTok, Instagram)
def download_video(url: str, chat_id: int):
    # Implement your video downloading logic here
    if 'youtube.com' in url:
        # Handle YouTube video download
        pass  # Placeholder for YouTube download logic
    elif 'tiktok.com' in url:
        # Handle TikTok video download
        pass  # Placeholder for TikTok download logic
    elif 'instagram.com' in url:
        # Handle Instagram video download
        pass  # Placeholder for Instagram download logic
    else:
        # Handle unrecognized URL
        update.message.reply_text("Sorry, I can only download videos from YouTube, TikTok, or Instagram.")

# Function to handle unknown commands
def unknown(update: telegram.Update, context: telegram.ext.CallbackContext):
    update.message.reply_text("Sorry, I didn't understand that command.")

# Function to greet user on bot start
def greet_user():
    return "Welcome to the video downloader bot!"

def main():
    # Initialize Telegram bot updater
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    # Start greeting message
    updater.bot.send_message(chat_id=updater.dispatcher.user_data['chat_id'], text=greet_user())

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
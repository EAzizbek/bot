import asyncio
import logging
from aiogram import Bot, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties  # Add this import

# Your bot token from BotFather
TOKEN = "7865303820:AAFh9xBZ1gcCVzaKfUYcoKBdKCGqK2rdlG4"

# Initialize bot and dispatcher
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))  # Fixed this line
dp = Dispatcher()

# Start command handler
@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}! Welcome to my bot!")

# Echo handler - repeats any message sent to the bot
@dp.message()
async def echo_handler(message: Message) -> None:
    await message.send_copy(chat_id=message.chat.id)

# Main function to run the bot
async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

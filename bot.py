import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Бот работает 🚀")


async def main():
    await dp.start_polling(bot)


if name == "__main__":
    import asyncio
    asyncio.run(main())

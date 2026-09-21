import asyncio
import sqlite3
import logging
from dotenv import load_dotenv
from os import getenv
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.formatting import Bold, Italic, Text, TextLink, Code

con = sqlite3.connect("database.db")
db = con.cursor()

db.execute("CREATE TABLE IF NOT EXISTS users")

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp =  Dispatcher()

@dp.message(CommandStart)
async def command_start_handler(message: Message) -> None:
    text = Text(
        "Привіт, ",
        TextLink(Bold(message.from_user.first_name), url=f"tg://openmessage?user_id={message.from_user.id}")
    )
    await message.answer(text.as_markdown())

async def main() -> None:
    print("Бот запущений!")

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

con.close()
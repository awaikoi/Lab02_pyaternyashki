import asyncio
import logging
from dotenv import load_dotenv
from os import getenv
import sys

from aiogram import Bot, Dispatcher, html
from aiogram import Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import *
from aiogram.utils.formatting import Bold, Italic, Text, TextLink, Code

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp =  Dispatcher()
router = Router(name=__name__)


@router.message(CommandStart)
async def command_start_handler(message: Message) -> None:
    text = Text(
        "Привіт, ",
        TextLink(Bold(message.from_user.first_name), url=f"tg://openmessage?user_id={message.from_user.id}"),
        "!"
    )
    await message.answer(text.as_markdown())

@router.error()
async def error_handler(event: ErrorEvent):
    logging.critical("[CRITICAL ERROR] Caused by %s", event.exception, exc_info=True)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))

    await dp.start_polling(bot)
    print("Бот запущений!")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
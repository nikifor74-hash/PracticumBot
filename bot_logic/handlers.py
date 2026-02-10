
from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message

from bot_logic.ai_tool import get_gigachat_response

handlers_router=Router()

@handlers_router.message(Command(commands=["start"]))
async def start_handler(message:  Message):
    await message.answer(text="Привет!\n\nЯ бот для важных переговоров!\n\nПросто отправь мне свой текст...")

@handlers_router.message()
async def ai_hendler(messadge: Message):
    ai_response = await get_gigachat_response(user_text=messadge.text)

    await messadge.answer(text=ai_response)
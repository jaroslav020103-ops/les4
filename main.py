import asyncio
import os
from  dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Вітаю в мому боті! Якщо є питання пиши /help")

@dp.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer("мене звати ярослав я вчу пайтон")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("команди мого бота:\n"
                         "/start запуск бота \n"
                         "/help список команд \n"
                         "/about про мене \n"
                         "/seals інфа про тюленів")

@dp.message(Command("seals"))
async def cmd_seals(message: Message):
    await message.answer("Тюлені — це ластоногі морські ссавці, які ідеально адаптовані до холодних вод завдяки обтічній формі тіла, товстому шару жиру та здатності тривалий час перебувати під водою, виходячи на сушу або лід лише для відпочинку та розмноження.")

@dp.message(Command('me'))
async def cmd_me(message: Message):
    user = message.from_user
    await message.answer(
        f"Твій профіль: \n"
        f"Iмʼя: {user.first_name}\n"
        f"Username: @{user.username}\n"
        f"ID: {user.id}"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

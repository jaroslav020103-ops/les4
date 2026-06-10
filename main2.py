import asyncio
import os
from  dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(messege: Message):
    await messege.answer("Я бот папуга. Напиши що небудь!")

#повторювання 
# @dp.message(F.text)
# async def echo(messege: Message):
#     await message.answer(message.text)

#те саме но капс
# @dp.message(F.text)
# async def shout(messege: Message):
#     await message.answer(message.text.upper())

#уно реверс
# @dp.message(F.text)
# async def reverse(message: Message):
#     reversed_text = message.text[::-1]
#     await message.answer(reversed_text)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
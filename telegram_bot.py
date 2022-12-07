import asyncio
import requests
import datetime
from config import tg_bot_token, tg_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название любого города и я пришлю тебе погоду☺")

asyncio.run(start_command())
if __name__ == '__main__':
    executor.start_polling(dp)

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

@dp.message_handler()
async def get_weather(message: types.Message):
    weather_conditions = {
        "Clear": "Ясно☀",
        "Clouds": "Облачно☁",
        "Windy": "Ветрено🍃",
        "Rain": "Дождливо🌂",
        "Thunderstorm": "Гроза⚡",
        "Mist": "Туман🌫",
        "Snow": "Снег❄",
        "Tornado": "Торнадо🌪"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={tg_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        current_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in weather_conditions:
            wd = weather_conditions[weather_description]
        else:
            wd = "Ого! Что-то необычное! Выгляни в окно и попробуй это описать"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        await message.reply(f"Дата и время: {datetime.datetime.now().strftime('%Y-%m-%d — %H:%M')}\n"
              f"\n"
              f"Погода в городе: {city}\nТемпература: {current_weather}°C, Описание погоды: {wd}\n" # \n - символ новой строки
              f"Влажность: {humidity}%\nДавление: {pressure} мм рт.ст\n"
              f"Скорость ветра: {wind} м/с\nРассвет: {sunrise}\n"
              f"Закат: {sunset}\n"
              f"Хорошего дня!💗"
              )

    except:
        await message.reply("Город не найден❗")

if __name__ == '__main__':
    executor.start_polling(dp)

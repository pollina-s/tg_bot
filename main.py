import requests
import datetime
from config import tg_token

def get_weather(city, tg_token):

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

    try:  #  делаем get-запрос, где получаем и обрабатываем данные
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={tg_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        current_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in weather_conditions:
            wd = weather_conditions[weather_description]
        else:
            wd = "Ого! Что-то необычное! Выгляни в окно и попробуй это описать"

        humidity = data["main"]["humidity"]  # влажность
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        print(f"Дата и время: {datetime.datetime.now().strftime('%Y-%m-%d — %H:%M')}\n"
              f"\n"
              f"Погода в городе: {city}\nТемпература: {current_weather}°C, Описание погоды: {wd}\n" # \n - символ новой строки
              f"Влажность: {humidity}%\nДавление: {pressure} мм рт.ст\n"
              f"Скорость ветра: {wind} м/с\nРассвет: {sunrise}\n"
              f"Закат: {sunset}\n"
              f"Хорошего дня!💗"
              )

    except Exception as ex:  #  сообщение об ошибке
        print("Пожалуйста, проверьте правильность написания города!")

def main():  # запрос города у пользователя
    city = input("Введите название города: ")
    get_weather(city, tg_token)

if __name__ == '__main__':
    main()

import requests
import datetime
from config import tg_token

def get_weather(city, tg_token):
    try:  #  делаем get-запрос, где получаем и обрабатываем данные
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={tg_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        current_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]  # влажность
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        print(f"Погода в городе: {city}\nТемпература: {current_weather}°C\n" # \n - символ новой строки
              f"Влажность: {humidity}%\nДавление: {pressure} мм рт.ст\n"
              f"Скорость ветра: {wind} м/с\nРассвет: {sunrise}\n"
              f"Закат: {sunset}\n"
              f"Хорошего дня! :)"
              )

    except Exception as ex:  #  сообщение об ошибке
        print("Пожалуйста, проверьте правильность написания города!")

def main():  # запрос города у пользователя
    city = input("Введите название города: ")
    get_weather(city, tg_token)

if __name__ == '__main__':
    main()

import requests
from pprint import pprint
from config import tg_token

def get_weather(city, tg_token):
    try:  #  делаем get-запрос, где получаем и обрабатываем данные
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={tg_token}&units=metric"
        )
        data = r.json()
        pprint(data)
    except Exception as ex:  #  сообщение об ошибке
        print(ex)  #  выводим саму ошибку
        print("Пожалуйста, проверьте правильность написания города!")

def main():  # запрос города у пользователя
    city = input("Введите название города: ")
    get_weather(city, tg_token)

if __name__ == '__main__':
    main()

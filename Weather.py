import requests
import Current_weather
import keyboard


def display_current_weather(url: str, api_key: str):
    """Формирует HTTP-запрос на сайт с погодой с заданными параметрами
    
    Параметры функции:
    url: URL-адрес
    api_key: API-ключ
    """
    
    city_name = input("Введите название населенного пункта: \n")
    response = requests.get(url, params={"q":city_name, "appid": api_key, "lang": "RU"})
    try:
        print()
        
        # Вывод информации о прогнозе погоды в указанном населенном пункте
        Current_weather.Weather(response.json()).display_current_weather()
    except:
        print("Неизвестный населенный пункт")

# Указываем собственный API-ключ (это пример)
api_key = "b1b15e88fa797225412429c1c50c122a1"
url = "https://api.openweathermap.org/data/2.5/weather"

display_current_weather(url, api_key)
while True:
    print("\nДля продолжения просмотра прогнозов погоды нажмите клавишу 'Ctrl'," \
                " для завершения программы нажмите клавишу 'Esc': ")
    if keyboard.read_key() == "esc":
        break
    if keyboard.read_key() == "ctrl":
        print()
        display_current_weather(url, api_key)

print("Завершение программы")
input()

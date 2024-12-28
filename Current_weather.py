class Weather:
    
    def __init__(self, json: dict):
        """Принимает JSON-объект и создает на основе его атрибут класса"""
        self.json = json
        
    def get_name(self):
        """Возвращает название населенного пункта"""
        return self.json['name']
    
    def get_temperature(self):
        """Возвращает температуру в градусах Цельсия в текущем населенном пункте"""
        return round(self.json['main']['temp'] - 273, 1)
    
    def get_feels_like_temp(self):
        """Возвращает температуру в градусах Цельсия по человеческому восприятию погоды"""
        return round(self.json['main']['feels_like'] - 273, 1)
    
    def get_pressure(self):
        """Возвращает показание давления в мм рт. ст."""
        return round(self.json['main']['pressure'] * 0.750063755419211)
    
    def get_humidity(self):
        """Возвращает показание влажности в %"""
        return self.json['main']['humidity']
    
    def get_wind(self):
        """Возвращает показания о ветре (скорость, направление)"""
        directions = ['↑ С', 'СВ', '→ В', 'ЮВ', '↓ Ю', 'ЮЗ', '← З', 'СЗ']
        degrees = self.json['wind']['deg']
        return round(self.json['wind']['speed']), directions[round(degrees / 45) % 8]
    
    def get_cloudiness(self):
        """Возвращает показания об облачности в %"""
        return self.json["clouds"]["all"]
    
    def get_rain(self):
        """Возвращает объем осадков в виде дождя за последний час в мм"""
        return self.json['rain']['1h'] if 'rain' in self.json.keys() else 0
    
    def get_snow(self):
        """Возвращает объем осадков в виде снега за последний час в мм"""
        return self.json['snow']['1h'] if 'snow' in self.json.keys() else 0
    
    def get_weather_conditions(self):
        """Возвращает описание погодных условий"""
        return self.json['weather'][0]['description']

    def display_current_weather(self):
        """Выводит краткие необходимые сведения о погоде на текущий момент"""
        
        print(f"<<<Сведения о погоде в {self.get_name()}>>>")
        print(f"Погодные условия: {self.get_weather_conditions()}")
        print(f"Текущая температура: {self.get_temperature()} °С")
        print(f"По ощущению: {self.get_feels_like_temp()} °С")
        print(f"Давление: {self.get_pressure()} мм рт. ст.")
        print(f"Влажность: {self.get_humidity()}%")
        print(f"Ветер: {self.get_wind()[0]} м/с, {self.get_wind()[1]}")
        print(f"Облачность: {self.get_cloudiness()}%")
        print(f"Осадки (дождь): {self.get_rain()} мм за последний час")
        print(f"Осадки (снег): {self.get_snow()} мм за последний час")
        
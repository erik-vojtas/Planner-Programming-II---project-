import requests
import json
import pytemperature
import easygui #message box

#api.openweathermap.org

class Weather:
        def __init__(self, city, country_abbreviation):
            self.city = city
            self.country_abbreviation = country_abbreviation
            self.list_of_data = []

        def getCurrentWeather(self):
            try:
                response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={self.city},{self.country_abbreviation}&appid=dd11e44d0bf849b66556e486a385c647')
                json_data = json.loads(response.text) #convert string to json object - dictionary
                weather_description = json_data['weather'][0]['main'] # weather description
                temp_in_kelvin = json_data['main']['temp'] # temp in Kelvins
                temp_in_celsius = "temperature: "+str(round(pytemperature.k2c(json_data['main']['temp'])))+"°C" # temp Kelvin to Celsius
                humidity = "humudity: "+str(json_data['main']['humidity'])+"%"# humidity in %
                wind_speed = "wind: "+str(json_data['wind']['speed'])+"km/h" # wind speed in km/h
                self.list_of_data.append(self.city)
                self.list_of_data.append(weather_description)
                self.list_of_data.append(temp_in_celsius)
                self.list_of_data.append(humidity)
                self.list_of_data.append(wind_speed)
                return self.list_of_data
            except:
                self.handleError(self.getCurrentWeather, "Weather can not be retrieved...")

        def handleError(self, funct, msg):
            title = "'Oops, something is wrong'"
            if easygui.ccbox(msg, title):  # show a Try Again/Cancel dialog
                funct.__call__()  # user chose Try Again

# Linz_weather = Weather("Linz", "AT")
# print(Linz_weather.getCurrentWeather())


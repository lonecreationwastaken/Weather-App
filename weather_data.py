import requests, json, sys

api_key = "" # Please enter your API key here
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = sys.argv[1] 

complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
response = requests.get(complete_url) 

x = response.json() 

def check_weather():
    global weather_description
    if x["cod"] != "404": 

        y = x["main"] 
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 
      
        details = (" Temperature (in celsius) = " +
                        str(current_temperature) + 
              "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
              "\n humidity (in percentage) = " +
                        str(current_humidiy) +
              "\n description = " +
                        str(weather_description))

    else: 
        print(" City Not Found ") 
    return details

current_temperature = check_weather()

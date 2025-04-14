import requests

def get_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            
            city = data['name']
            country = data['sys']['country']
            temp = data['main']['temp']
            weather = data['weather'][0]['description']
            humidity = data['main']['humidity']

            print(f'Condition in {city}, {country}: {weather}')
            print(f'Temperature: {temp} degrees fahrenheit')
            print(f'Humidity: {humidity} %')

        else:
            print(f'Error recieved status code: {response.status_code}. Unable to retrieve data.')

    except Exception as e:
        print(f'Something went wrong: {e}')

get_weather('Orlando', '2929bc316dec43e90381babcf6c4f026')
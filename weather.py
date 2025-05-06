import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Replace with your OpenWeatherMap API key
API_KEY = 'API_Key'
CITY = 'Tokyo'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

def fetch_weather_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def extract_temperature_and_time(data):
    temps = []
    times = []
    for entry in data['list']:
        temp = entry['main']['temp']
        time = datetime.fromtimestamp(entry['dt'])
        temps.append(temp)
        times.append(time)
    return times, temps

def plot_temperature(times, temps, city):
    plt.figure(figsize=(10,5))
    plt.plot(times, temps, marker='o', linestyle='-', color='b')
    plt.title(f'Temperature Forecast for {city}')
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    data = fetch_weather_data(URL)
    times, temps = extract_temperature_and_time(data)
    plot_temperature(times, temps, CITY)

if __name__ == '__main__':
    main()

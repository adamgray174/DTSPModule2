from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'e4c1bb5a78c6a1d455a289eb9bc47bef'
API_URL = 'https://api.openweathermap.org/data/2.5/forecast?'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(API_URL, params=params)
    weather_data = response.json()
    print('Start of Results:')

    print('Temperature over the Day in 3 hour intervals:')
    print('Wednesday, 8 February 2024 07:00:00 (UTC):' + str(weather_data['list'][1]['main']['temp'])) #GMT: Wednesday, 4 February 2024 07:00:00 (UTC)
    print('Wednesday, 8 February 2024 10:00:00 (UTC):' + str(weather_data['list'][2]['main']['temp'])) #GMT: Wednesday, 4 February 2024 10:00:00 (UTC)
    print('Wednesday, 8 February 2024 13:00:00 (UTC):' + str(weather_data['list'][3]['main']['temp'])) #GMT: Wednesday, 4 February 2024 13:00:00 (UTC)
    print('Wednesday, 8 February 2024 16:00:00 (UTC):' + str(weather_data['list'][4]['main']['temp'])) #GMT: Wednesday, 4 February 2024 16:00:00 (UTC)
    print('Wednesday, 8 February 2024 19:00:00 (UTC):' + str(weather_data['list'][5]['main']['temp'])) #GMT: Wednesday, 4 February 2024 19:00:00 (UTC)
    
    print('Humidity over the Day in 3 hour intervals:')
    print('Wednesday, 8 February 2024 07:00:00 (UTC):' + str(weather_data['list'][1]['main']['humidity']))
    print('Wednesday, 8 February 2024 10:00:00 (UTC):' + str(weather_data['list'][2]['main']['humidity']))
    print('Wednesday, 8 February 2024 13:00:00 (UTC):' + str(weather_data['list'][3]['main']['humidity']))
    print('Wednesday, 8 February 2024 16:00:00 (UTC):' + str(weather_data['list'][4]['main']['humidity']))
    print('Wednesday, 8 February 2024 19:00:00 (UTC):' + str(weather_data['list'][5]['main']['humidity']))
    
    print('Temperature it feels like over the day in 3 hour intervals:')
    print('Wednesday, 8 February 2024 07:00:00 (UTC):' + str(weather_data['list'][1]['main']['feels_like']))
    print('Wednesday, 8 February 2024 10:00:00 (UTC):' + str(weather_data['list'][2]['main']['feels_like']))
    print('Wednesday, 8 February 2024 13:00:00 (UTC:' + str(weather_data['list'][3]['main']['feels_like']))
    print('Wednesday, 8 February 2024 16:00:00 (UTC):' + str(weather_data['list'][4]['main']['feels_like']))
    print('Wednesday, 8 February 2024 19:00:00 (UTC):' + str(weather_data['list'][5]['main']['feels_like']))
    
    print('End of Results.')

    if response.status_code == 200:
        return render_template('index.html', city=city, weather_data=weather_data)
    else:
        error_message = f"Error: {weather_data['message']}"
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)

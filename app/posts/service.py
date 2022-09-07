import requests
from decouple import config


def get_weather_data():
    """날씨 데이터 가져오기"""
    api = config("WEATHER_API_KEY")
    try:
        data = requests.get(api).json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    return data

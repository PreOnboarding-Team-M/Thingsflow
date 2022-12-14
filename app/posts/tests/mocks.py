def create_mock_weather_data():
    return {
        "location": {
            "name": "Seoul",
            "region": "",
            "country": "South Korea",
            "lat": 37.57,
            "lon": 127.0,
            "tz_id": "Asia/Seoul",
            "localtime_epoch": 1662528458,
            "localtime": "2022-09-07 14:27",
        },
        "current": {
            "last_updated_epoch": 1662527700,
            "last_updated": "2022-09-07 14:15",
            "temp_c": 28.0,
            "temp_f": 82.4,
            "is_day": 1,
            "condition": {
                "text": "대체로 맑음",
                "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                "code": 1003,
            },
            "wind_mph": 6.9,
            "wind_kph": 11.2,
            "wind_degree": 300,
            "wind_dir": "WNW",
            "pressure_mb": 1018.0,
            "pressure_in": 30.05,
            "precip_mm": 0.0,
            "precip_in": 0.0,
            "humidity": 33,
            "cloud": 25,
            "feelslike_c": 27.0,
            "feelslike_f": 80.5,
            "vis_km": 10.0,
            "vis_miles": 6.0,
            "uv": 7.0,
            "gust_mph": 4.7,
            "gust_kph": 7.6,
        },
    }

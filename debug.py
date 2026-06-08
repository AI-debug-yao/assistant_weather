#!/usr/bin/env python3
"""调试天气API"""

import requests

gaode_api_key = "dc6f10d1c0b5d4af2b2bc87d5385acbf"
base_url = "https://restapi.amap.com/v3/weather/weatherInfo"

cities = ["北京", "上海", "深圳"]

for city in cities:
    print(f"\n{'='*60}")
    print(f"查询城市: {city}")
    print(f"{'='*60}")
    
    params = {
        "key": gaode_api_key,
        "city": city,
        "extensions": "base",
    }
    
    response = requests.get(base_url, params=params)
    print(f"状态码: {response.status_code}")
    print(f"完整URL: {response.url}")
    print(f"\n原始响应:")
    print(response.json())

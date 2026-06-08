import requests
from typing import Optional

weather_tool = {
    "type": "function",
    "function": {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city name, e.g. 北京",
                },
                "adcode": {
                    "type": "string",
                    "description": "The city code, e.g. 110000 (北京)",
                }
            },
            "required": ["location"],
        },
    },
}


def get_weather_from_gaode(location: str, adcode: Optional[str] = None):
    """调用高德地图API查询天气"""
    gaode_api_key = "58fa1b02f183bdcad7cef9b29f9360c1"
    base_url = "https://restapi.amap.com/v3/weather/weatherInfo"
    
    params = {
        "key": gaode_api_key,
        "city": adcode if adcode else location,
        "extensions": "base",
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch weather: {response.status_code}"}


def get_current_weather(location: str, adcode: Optional[str] = None) -> str:
    """获取当前天气信息的友好格式"""
    result = get_weather_from_gaode(location, adcode)
    
    if "error" in result:
        return result["error"]
    
    if result.get("status") == "1" and result.get("lives"):
        weather = result["lives"][0]
        return (
            f"城市: {weather['city']}\n"
            f"天气: {weather['weather']}\n"
            f"温度: {weather['temperature']}°C\n"
            f"风向: {weather['winddirection']}\n"
            f"风力: {weather['windpower']}级\n"
            f"湿度: {weather['humidity']}%\n"
            f"发布时间: {weather['reporttime']}"
        )
    else:
        error_info = result.get('info', '未知错误')
        infocode = result.get('infocode', '')
        return f"查询失败 - 城市: {location}, 错误: {error_info} (代码: {infocode})"

#!/usr/bin/env python3
"""Qwen-Agent 天气工具使用示例"""

from weather_tool import weather_tool, get_current_weather


def test_weather_tool():
    """测试天气工具"""
    print("测试天气工具...")
    print("=" * 50)
    
    cities = ["北京", "上海", "深圳"]
    
    for city in cities:
        print(f"\n查询 {city} 的天气:")
        print("-" * 30)
        result = get_current_weather(city)
        print(result)


if __name__ == "__main__":
    test_weather_tool()

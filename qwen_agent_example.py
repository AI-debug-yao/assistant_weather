#!/usr/bin/env python3
"""Qwen-Agent 天气工具集成示例"""

from weather_tool import weather_tool, get_current_weather
from typing import Dict, Any


class WeatherAgent:
    """天气查询Agent"""
    
    def __init__(self):
        self.tools = {
            "get_current_weather": get_current_weather
        }
        self.tool_definitions = [weather_tool]
    
    def run(self, user_query: str) -> str:
        """
        处理用户查询，模拟Qwen-Agent的工作流程
        实际项目中这里应该使用真实的Qwen-Agent SDK
        """
        print(f"用户查询: {user_query}")
        print("=" * 60)
        
        # 简单的城市名称提取（实际项目中应由LLM处理）
        city = self._extract_city(user_query)
        
        if city:
            print(f"识别到城市: {city}")
            print("调用天气工具...\n")
            
            # 调用天气工具
            result = self.tools["get_current_weather"](city)
            return result
        else:
            return "请告诉我你想查询哪个城市的天气？"
    
    def _extract_city(self, query: str) -> str:
        """简单的城市提取逻辑（仅用于演示）"""
        cities = ["北京", "上海", "深圳", "广州", "杭州", "成都", "武汉", "南京"]
        for city in cities:
            if city in query:
                return city
        return ""


def main():
    print("Qwen-Agent 天气查询助手")
    print("=" * 60)
    
    agent = WeatherAgent()
    
    # 示例查询
    queries = [
        "今天北京天气怎么样？",
        "上海现在温度多少？",
        "深圳的天气如何？"
    ]
    
    for query in queries:
        print("\n" + "=" * 60)
        response = agent.run(query)
        print(response)


if __name__ == "__main__":
    main()

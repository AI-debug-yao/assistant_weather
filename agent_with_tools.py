#!/usr/bin/env python3
"""使用Qwen-Agent SDK的天气工具集成"""

from weather_tool import weather_tool, get_current_weather
import json


def create_weather_agent():
    """
    创建集成天气工具的Qwen-Agent
    注意：这是一个框架示例，需要根据实际的Qwen-Agent SDK进行调整
    """
    # 工具映射
    tool_map = {
        "get_current_weather": get_current_weather
    }
    
    def agent(query: str):
        """
        Agent的主函数
        在真实的Qwen-Agent中，这里会调用LLM来决定是否使用工具
        """
        print(f"用户: {query}")
        print("-" * 60)
        
        # 这是一个简化的模拟，真实Qwen-Agent会自动：
        # 1. 理解用户意图
        # 2. 决定是否调用工具
        # 3. 解析工具参数
        # 4. 执行工具调用
        # 5. 生成最终回答
        
        # 简单模拟：直接尝试查询天气
        # 实际应用中，这里应该集成Qwen-Agent的FunctionCall能力
        
        cities = ["北京", "上海", "深圳", "广州", "杭州", "成都", "武汉", "南京", "重庆", "天津"]
        found_city = None
        
        for city in cities:
            if city in query:
                found_city = city
                break
        
        if found_city:
            print(f"Agent: 我来帮你查询{found_city}的天气...\n")
            weather_info = tool_map["get_current_weather"](found_city)
            return f"好的，这是{found_city}的天气信息：\n\n{weather_info}"
        else:
            return "请问你想查询哪个城市的天气呢？"
    
    return agent


def main():
    print("Qwen-Agent 天气查询助手 (带工具调用)")
    print("=" * 60)
    
    agent = create_weather_agent()
    
    # 测试对话
    test_queries = [
        "北京今天天气怎么样？",
        "我想知道上海现在的温度",
        "深圳会下雨吗？"
    ]
    
    for query in test_queries:
        print("\n" + "=" * 60)
        response = agent(query)
        print(f"\nAgent: {response}")


if __name__ == "__main__":
    main()

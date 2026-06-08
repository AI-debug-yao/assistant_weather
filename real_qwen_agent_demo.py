#!/usr/bin/env python3
"""真正使用Qwen-Agent的天气工具集成示例"""

import os
from dotenv import load_dotenv
from weather_tool_qwen import WeatherTool
from qwen_agent.agents import FnCallAgent

# 加载环境变量
load_dotenv()


def main():
    print("=" * 60)
    print("Qwen-Agent 天气查询助手 (完整版)")
    print("=" * 60)
    
    # 1. 配置LLM (需要设置API密钥)
    # 这里需要配置实际的Qwen API密钥
    # 请设置环境变量 DASHSCOPE_API_KEY 或在下面直接配置
    
    api_key = os.environ.get('DASHSCOPE_API_KEY', '')
    
    if not api_key:
        print("\n警告: 未设置DASHSCOPE_API_KEY环境变量")
        print("无法演示完整的LLM+工具调用功能")
        print("\n但我们可以演示工具本身的功能...")
        print("\n" + "=" * 60)
        
        # 演示工具的直接使用
        weather_tool = WeatherTool()
        
        # 测试工具
        test_cities = ['北京', '上海', '深圳']
        for city in test_cities:
            print(f"\n查询 {city} 的天气:")
            print("-" * 40)
            result = weather_tool.call({'location': city})
            print(result)
        
        print("\n" + "=" * 60)
        print("要使用完整的LLM+工具调用功能:")
        print("1. 获取DASHSCOPE API密钥: https://dashscope.console.aliyun.com/")
        print("2. 设置环境变量: export DASHSCOPE_API_KEY='your-api-key'")
        print("3. 重新运行此脚本")
        return
    
    # 2. 创建带有天气工具的Agent
    llm_cfg = {
        'model': 'qwen-turbo',
        'api_key': api_key,
        'model_server': 'dashscope',
    }
    
    agent = FnCallAgent(
        function_list=[WeatherTool()],
        llm=llm_cfg,
        system_message='你是一个天气查询助手，可以帮助用户查询各个城市的天气信息。'
    )
    
    # 3. 演示对话
    messages = [{'role': 'user', 'content': '北京今天天气怎么样？'}]
    
    print("\n用户: 北京今天天气怎么样？")
    print("-" * 60)
    
    for responses in agent.run(messages):
        last_response = responses[-1]
        if last_response.role == 'assistant' and last_response.content:
            print(f"\n助手: {last_response.content}")
        elif last_response.role == 'function':
            print(f"\n[工具调用结果: {last_response.name}]")
            print(last_response.content)


if __name__ == '__main__':
    main()

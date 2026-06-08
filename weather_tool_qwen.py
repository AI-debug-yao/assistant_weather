#!/usr/bin/env python3
"""符合Qwen-Agent标准的天气工具实现"""

import os
from typing import Dict, Optional, Union
import requests
from dotenv import load_dotenv
from qwen_agent.tools.base import BaseTool, register_tool

# 加载环境变量
load_dotenv()


@register_tool('get_current_weather')
class WeatherTool(BaseTool):
    description = '获取对应城市的天气数据'
    parameters = {
        'type': 'object',
        'properties': {
            'location': {
                'description': '城市名称，如`北京`、`上海`',
                'type': 'string',
            },
            'adcode': {
                'description': '城市代码，如`110000`（北京）',
                'type': 'string',
            }
        },
        'required': ['location'],
    }

    def __init__(self, cfg: Optional[Dict] = None):
        super().__init__(cfg)
        # 优先从配置中读取，其次从环境变量读取，最后使用默认值
        self.gaode_api_key = self.cfg.get(
            'api_key',
            os.getenv('GAODE_API_KEY', '58fa1b02f183bdcad7cef9b29f9360c1')
        )
        self.base_url = 'https://restapi.amap.com/v3/weather/weatherInfo'

    def call(self, params: Union[str, dict], **kwargs) -> str:
        params = self._verify_json_format_args(params)
        
        location = params.get('location')
        adcode = params.get('adcode')
        
        city_param = adcode if adcode else location
        
        request_params = {
            'key': self.gaode_api_key,
            'city': city_param,
            'extensions': 'base',
        }
        
        try:
            response = requests.get(self.base_url, params=request_params)
            response.raise_for_status()
            data = response.json()
            
            if data.get('status') == '1' and data.get('lives'):
                weather = data['lives'][0]
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
                error_info = data.get('info', '未知错误')
                infocode = data.get('infocode', '')
                return f"查询天气失败 - {error_info} (代码: {infocode})"
                
        except Exception as e:
            return f"查询天气时出错: {str(e)}"

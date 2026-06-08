#!/usr/bin/env python3
"""
天气查询工具 - 可视化界面
使用 Streamlit 构建
"""

import os
import requests
from dotenv import load_dotenv
import streamlit as st
from datetime import datetime

# 加载环境变量
load_dotenv()

# 配置页面
st.set_page_config(
    page_title="天气查询助手",
    page_icon="🌤️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 侧边栏 - 配置
with st.sidebar:
    st.title("⚙️ 设置")
    st.markdown("---")
    
    st.markdown("### 常用城市")
    quick_cities = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉", "南京"]
    
    st.markdown("---")
    st.markdown("### 关于")
    st.info("基于高德地图API和Qwen-Agent构建的天气查询工具")

# 从环境变量读取API密钥
gaode_api_key = os.getenv("GAODE_API_KEY", "")


# 主界面
st.title("🌤️ 天气查询助手")
st.markdown("查询中国主要城市的实时天气信息")
st.markdown("---")


def get_weather(city, api_key):
    """调用高德天气API"""
    base_url = "https://restapi.amap.com/v3/weather/weatherInfo"
    params = {
        "key": api_key,
        "city": city,
        "extensions": "base",
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") == "1" and data.get("lives"):
            return data["lives"][0]
        else:
            return None
    except Exception as e:
        st.error(f"查询出错: {str(e)}")
        return None


def get_weather_icon(weather):
    """根据天气状况返回对应的emoji"""
    weather = weather.lower()
    if "晴" in weather:
        return "☀️"
    elif "多云" in weather or "少云" in weather:
        return "⛅"
    elif "阴" in weather:
        return "☁️"
    elif "雨" in weather:
        if "雷" in weather:
            return "⛈️"
        elif "小" in weather:
            return "🌦️"
        else:
            return "🌧️"
    elif "雪" in weather:
        return "❄️"
    elif "雾" in weather or "霾" in weather:
        return "🌫️"
    else:
        return "🌡️"


def display_weather(weather_data):
    """显示天气信息"""
    if not weather_data:
        return
    
    city = weather_data.get("city", "未知")
    weather = weather_data.get("weather", "未知")
    temp = weather_data.get("temperature", "")
    wind_dir = weather_data.get("winddirection", "")
    wind_power = weather_data.get("windpower", "")
    humidity = weather_data.get("humidity", "")
    report_time = weather_data.get("reporttime", "")
    
    # 显示卡片
    with st.container():
        # 城市名称和天气状态
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(f"### 🏙️ {city}")
        with col2:
            icon = get_weather_icon(weather)
            st.markdown(f"<h2 style='text-align: right;'>{icon}</h2>", unsafe_allow_html=True)
        
        st.markdown(f"#### {weather}")
        
        # 温度和详细信息
        col_temp, col_details = st.columns([1, 1])
        with col_temp:
            st.metric(label="温度", value=f"{temp}°C")
        with col_details:
            st.write(f"💨 风向: {wind_dir}")
            st.write(f"🌬️ 风力: {wind_power}级")
            st.write(f"💧 湿度: {humidity}%")
        
        # 发布时间
        st.markdown("---")
        st.caption(f"⏰ 发布时间: {report_time}")


# 主界面 - 查询区域
st.subheader("🔍 查询天气")

# 选择查询方式
query_method = st.radio(
    "选择查询方式",
    ["输入城市名", "从常用城市选择"],
    horizontal=True
)

city = ""
if query_method == "输入城市名":
    city = st.text_input("请输入城市名称", placeholder="例如：北京、上海、深圳")
else:
    city = st.selectbox("选择城市", quick_cities, index=None)

# 查询按钮
if st.button("查询天气", type="primary", use_container_width=True):
    if not city:
        st.warning("请先输入或选择城市")
    elif not gaode_api_key:
        st.error("请在.env文件中配置GAODE_API_KEY")
    else:
        with st.spinner("正在查询天气..."):
            weather_data = get_weather(city, gaode_api_key)
            if weather_data:
                st.success("查询成功！")
                display_weather(weather_data)
            else:
                st.error("未找到该城市的天气信息，请检查城市名称或API密钥配置")

st.markdown("---")

# 页脚
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p>数据来源：高德地图 | 最后更新: {}</p>
    </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    unsafe_allow_html=True
)

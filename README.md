# 🌤️ 天气查询助手

基于高德地图API和Qwen-Agent构建的天气查询工具，提供简洁美观的可视化界面。

## 🌟 功能特性

- **实时天气查询** - 获取中国主要城市的实时天气信息
- **Qwen-Agent集成** - 符合Qwen-Agent标准的工具集成
- **可视化界面** - 使用Streamlit构建的现代化用户界面
- **灵活配置** - 支持.env文件管理API密钥

## 📁 项目结构

```
assistant_weather/
├── app.py                      # Streamlit 可视化界面
├── weather_tool_qwen.py        # 符合Qwen-Agent标准的天气工具
├── weather_tool.py             # 原始天气工具实现
├── real_qwen_agent_demo.py     # Qwen-Agent集成示例
├── qwen_weather_integration_demo.py  # 集成演示
├── example.py                  # 简单使用示例
├── debug.py                    # 调试脚本
├── .env                        # 环境变量配置 (需自行创建)
├── .env.example                # 环境变量示例文件
├── .gitignore                  # Git忽略文件
├── requirements.txt            # Python依赖
└── README.md                   # 项目文档
```

## 🚀 快速开始

### 1. 克隆/下载项目

```bash
cd assistant_weather
```

### 2. 创建虚拟环境（推荐）

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate  # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

复制示例配置文件并填写真实的API密钥：

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```env
# 高德地图API密钥 (用于天气查询)
GAODE_API_KEY=your-gaode-api-key

# 阿里云DashScope API密钥 (用于Qwen-Agent)
DASHSCOPE_API_KEY=your-dashscope-api-key
```

### 5. 运行可视化界面

```bash
streamlit run app.py
```

浏览器会自动打开 `http://localhost:8501`

## 📖 使用说明

### 可视化界面使用

1. 确保已在 `.env` 文件中配置好 `GAODE_API_KEY`
2. 在主界面输入城市名称或从常用城市列表选择
3. 点击「查询天气」按钮
4. 查看天气信息卡片

### Qwen-Agent工具使用

```python
from weather_tool_qwen import WeatherTool
from qwen_agent.agents import FnCallAgent

# 创建带有天气工具的Agent
agent = FnCallAgent(
    function_list=[WeatherTool()],
    llm={
        'model': 'qwen-turbo',
        'api_key': 'your-dashscope-api-key',
        'model_server': 'dashscope',
    },
    system_message='你是一个天气查询助手。'
)

# 与Agent对话
messages = [{'role': 'user', 'content': '北京今天天气怎么样？'}]
for responses in agent.run(messages):
    print(responses[-1].content)
```

## 🔑 API密钥获取

### 高德地图API密钥

1. 访问 [高德开放平台](https://lbs.amap.com/)
2. 注册并登录账号
3. 创建应用，选择「Web服务」类型
4. 获取API Key

### 阿里云DashScope API密钥

1. 访问 [阿里云DashScope控制台](https://dashscope.console.aliyun.com/)
2. 注册并登录账号
3. 创建API-KEY

## 📦 依赖说明

- `requests` - HTTP请求库
- `qwen-agent` - Qwen-Agent框架
- `python-dotenv` - 环境变量管理
- `streamlit` - 可视化界面框架

## 🛠️ 开发说明

### 天气工具集成原理

Qwen-Agent的工具需要遵循以下标准：

1. 继承 `BaseTool` 基类
2. 使用 `@register_tool()` 装饰器注册
3. 实现 `call()` 方法
4. 定义 `description` 和 `parameters` 属性

### 项目文件说明

| 文件 | 说明 |
|------|------|
| `weather_tool_qwen.py` | 符合Qwen-Agent标准的实现 |
| `weather_tool.py` | 原始实现，供参考 |
| `app.py` | Streamlit可视化界面 |
| `real_qwen_agent_demo.py` | 完整的Qwen-Agent集成示例 |

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📮 联系方式

如有问题或建议，欢迎通过Issue反馈。

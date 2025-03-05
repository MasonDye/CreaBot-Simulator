# CreaBot 模拟器

一个用于 CreaBot 机器人控制和测试的 Python 模拟器。该模拟器提供了一个虚拟环境，用于测试机器人控制功能，而无需实际的硬件设备。

[**English**](https://chatgpt.com/c/README.md)     [**中文简体**](https://chatgpt.com/c/README_CN.md)

## 功能特点

- 机器人移动与导航模拟
- 门禁与灯光控制
- 语音交互（TTS/ASR）
- 摄像头模拟与拍照功能
- 紫外线消毒控制
- 地图管理
- 充电桩模拟
- 位置追踪
- 彩色控制台输出的状态反馈

## 使用方法

### 基本初始化

```python
from creabot_simulator import Creabot
# 或者
# import creabot_simulator as creabot

# 使用 IP 地址初始化机器人
bot = Creabot("192.168.1.100")
# 或者
# bot.creabot.Creabot("192.168.1.100")
```

### 运动控制

```python
# 以指定速度移动机器人
bot.chassis_move(x_speed=0.5, y_speed=0, rotate_speed=0)  # 向前移动
bot.stop_push()  # 停止移动
```

### 地图操作

```python
# 获取可用地图列表
maps = bot.list_map()

# 设置当前地图
bot.set_map("map_id")

# 获取地图点位
points = bot.list_map_point("map_id")
```

### 设备控制

```python
# 门禁控制
bot.door_ctrl(1)  # 打开门
bot.door_ctrl(0)  # 关闭门

# 灯光控制
bot.light_ctrl(1)  # 开灯
bot.light_ctrl(0)  # 关灯

# 紫外线消毒控制
bot.uv_ctrl(level=1)  # 设置紫外线消毒等级
```

### 摄像头功能

```python
# 拍照
photo_data = bot.take_photo()  # 返回 Base64 编码的图片数据

# 保存照片
bot.save_base64_as_image(photo_data, "path/to/save/photo.jpg")
```

## 依赖要求

- Python 3.6+
- `requests` 库
- `typing` 支持

## 备注

该模拟器仅用于开发和测试目的，实际机器人的行为可能与模拟器的响应有所不同。

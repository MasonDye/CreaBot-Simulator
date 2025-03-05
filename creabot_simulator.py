# creabot_simulator.py
import time
import random
from typing import Optional, List, Dict, Any
import requests
import base64

door_status = False


def colored_print(text: str, action_type: str):
    """Print colored text based on action type"""
    reset = '\033[0m'
    colors = {
        'door_light': '\033[6;30;47m',  # Yellow bg
        'voice': '\033[6;30;45m',  # Purple bg
        'movement': '\033[6;30;44m',  # Blue bg
        'default': '\033[6;30;42m'  # Green bg
    }
    color = colors.get(action_type, colors['default'])
    print(color + text + reset)


class Creabot:
    def __init__(self, ip: str):
        self.ip = ip
        colored_print(f"[CreaBot Sim] 初始化机器人 [IP地址: {ip}]", "default")
        self.position = {"x": 0, "y": 0, "theta": 0}
        self.current_map = None
        self.uv_level = 0

        self._maps = [{
            "id": "097d0b65-094a-43f9-99ed-b08e4fab7b92",
            "name": "default_map",
            "points": [
                {"id": "c9b58f24-b15c-461d-bd37-639fefc0eb3d", "name": "center", "x": 0, "y": 0, "theta": 1.1},
                {"id": "db3f7dd4-bfc4-4f5d-911c-8ae3918662ed", "name": "changer", "x": 1, "y": 1, "theta": 1.12},
                {"id": "db3f7dd4-bfc4-4f5d-911c-8ae3918662ed", "name": "Point1", "x": 2, "y": 2, "theta": 1.12},
                {"id": "eac8d40c-6683-4631-9791-3e1fa8a68736", "name": "Point2", "x": 3, "y": 3, "theta": 1.13},
                {"id": "98467ab6-7415-4d7b-a469-2c5e89bdce46", "name": "Point3", "x": 4, "y": 4, "theta": 1.14},
                {"id": "15ba0e94-a305-426a-96e7-3270b7332ca8", "name": "Point4", "x": 5, "y": 5, "theta": 1.15}
            ]
        }]

    def list_map(self) -> List[Dict[str, Any]]:
        colored_print("[CreaBot Sim] 获取地图列表", "default")
        return self._maps

    def list_map_point(self, map_id: str) -> List[Dict[str, Any]]:
        map_data = next((m for m in self._maps if m["id"] == map_id), None)
        return map_data["points"] if map_data else []

    def set_map(self, map_id: str) -> None:
        colored_print(f"[CreaBot Sim] 设置地图: {map_id}", "default")
        self.current_map = map_id

    def relocate_sync(self, x: float, y: float, theta: float) -> None:
        colored_print(f"[CreaBot Sim] 重定位至: ({x}, {y}, {theta})", "movement")
        time.sleep(1)
        self.position = {"x": x, "y": y, "theta": theta}

    def start_navigation_sync(self, x: float, y: float, theta: float, speed: float) -> None:
        colored_print(f"[CreaBot Sim] 开始导航: 目标({x}, {y}, {theta}), 速度{speed}", "movement")
        time.sleep(2)
        self.position = {"x": x, "y": y, "theta": theta}

    def show_media(self, media_type: str, content: str) -> None:
        colored_print(f"[CreaBot Sim] 显示{media_type}: {content}", "default")
        try:
            responses = requests.get(content)
            if responses.status_code == 200:
                colored_print("[CreaBot Sim] 测试文件状态正常，状态码 " + str(responses.status_code), "default")
            else:
                colored_print("[CreaBot Sim] 测试文件 HTTP 状态码异常", "default")
        except Exception as error:
            colored_print(f"[CreaBot Sim] 测试文件状态异常 {error}", "default")

    def tts_sync(self, text: str) -> None:
        colored_print(f"[CreaBot Sim] TTS {text}", "voice")
        time.sleep(1)

    def asr_sync(self, timeout: int) -> str:
        colored_print(f"[CreaBot Sim] 等待语音输入 (超时{timeout}秒)...", "voice")
        return input("请输入模拟的语音命令: ")

    def dock_charge_on_sync(self, map_id: str, x: float, y: float, theta: float) -> None:
        colored_print(f"[CreaBot Sim] 开始对接充电桩: ({x}, {y}, {theta})", "movement")
        time.sleep(2)

    def dock_charge_off_sync(self) -> None:
        colored_print("[CreaBot Sim] 脱离充电桩", "movement")
        time.sleep(1)

    def uv_ctrl(self, level: int) -> None:
        colored_print(f"[CreaBot Sim] UV消毒级别设置为: {level}", "default")
        self.uv_status = level

    def chassis_move(self, x_speed: float, y_speed: float, rotate_speed: float = 0.0) -> None:
        self.position["x"] += x_speed * 0.1
        self.position["y"] += y_speed * 0.1
        self.position["theta"] += rotate_speed * 0.1

        movement_type = []
        if x_speed > 0:
            movement_type.append("前进")
        elif x_speed < 0:
            movement_type.append("后退")

        if y_speed > 0:
            movement_type.append("左移")
        elif y_speed < 0:
            movement_type.append("右移")

        if rotate_speed != 0:
            rotation = "逆时针" if rotate_speed > 0 else "顺时针"
            movement_type.append(f"{rotation}旋转")

        movement_str = "和".join(movement_type) if movement_type else "静止"
        colored_print(
            f"[CreaBot Sim] 底盘运动: {movement_str} (x={x_speed:.1f}, y={y_speed:.1f}, r={rotate_speed:.1f})",
            "movement")

    def stop_push(self):
        colored_print("[CreaBot Sim] 已停止运动", "movement")

    def exist_object(self, *exist):
        if exist is bool and exist != None:
            return exist
        else:
            return random.choice([True, False])

    def door_ctrl(self, status: int):
        global door_status
        if status == 1 and not door_status:
            colored_print("[CreaBot Sim] 开门", "door_light")
            door_status = 1
        elif status == 0 and door_status:
            colored_print("[CreaBot Sim] 关门", "door_light")
            door_status = 0
        elif status == 1 and door_status:
            colored_print("[CreaBot Sim] 执行操作受阻 门已经打开", "door_light")
        elif status == 0 and not door_status:
            colored_print("[CreaBot Sim] 执行操作受阻 门已经关闭", "door_light")

    def is_door_open(self):
        return door_status

    def light_ctrl(self, status: int):
        if status == 1:
            colored_print("[CreaBot Sim] 开灯", "door_light")
        else:
            colored_print("[CreaBot Sim] 关灯", "door_light")

    def take_photo(self):
        try:
            response = requests.get("https://acbox.app/f/jOBzU6/family.jpg")  # Example URL for fetching an image
            if response.status_code == 200:
                image_base64 = base64.b64encode(response.content).decode('utf-8')
                return image_base64
            else:
                colored_print("[CreaBot Sim] 获取图片失败", "default")
                return None
        except Exception as error:
            colored_print(f"[CreaBot Sim] 获取图片时发生错误: {error}", "default")
            return None

    def save_base64_as_image(self, photo, file_path):
        with open(file_path, "wb") as f:
            f.write(base64.b64decode(photo))
        colored_print(f"[CreaBot Sim - Local] 保存图片到 {file_path}", "default")
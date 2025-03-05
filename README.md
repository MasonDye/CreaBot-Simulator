# CreaBot Simulator

A Python simulator for CreaBot robot control and testing. This simulator provides a virtual environment for testing robot control functions without requiring physical hardware.

[**English**](README.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**中文简体**](README_CN.md)

## Features

- Robot movement and navigation simulation
- Door and light control
- Voice interaction (TTS/ASR)
- Camera simulation with photo capture
- UV disinfection control
- Map management
- Charging dock simulation
- Position tracking
- Status feedback with colored console output

## Usage

### Basic Initialization

```python
from creabot_simulator import Creabot
# or
# import creabot_simulator as creabot

# Initialize robot with IP address
bot = Creabot("192.168.1.100")
# or
#bot.creabot.Creabot("192.168.1.100")
```

### Movement Control

```python
# Move robot with speed parameters
bot.chassis_move(x_speed=0.5, y_speed=0, rotate_speed=0)  # Move forward
bot.stop_push()  # Stop movement
```

### Map Operations

```python
# Get available maps
maps = bot.list_map()

# Set current map
bot.set_map("map_id")

# Get map points
points = bot.list_map_point("map_id")
```

### Device Control

```python
# Door control
bot.door_ctrl(1)  # Open door
bot.door_ctrl(0)  # Close door

# Light control
bot.light_ctrl(1)  # Turn on lights
bot.light_ctrl(0)  # Turn off lights

# UV control
bot.uv_ctrl(level=1)  # Set UV disinfection level
```

### Camera Functions

```python
# Take photo
photo_data = bot.take_photo()  # Returns base64 encoded image

# Save photo
bot.save_base64_as_image(photo_data, "path/to/save/photo.jpg")
```

## Requirements

- Python 3.6+
- `requests` library
- `typing` support

## Note

This is a simulator intended for development and testing purposes. Actual robot behavior may differ from the simulated responses.


# AI Aim Assist Pro

Professional AI Aim Assist system with modular architecture, multi-GPU support, and real-time configurable GUI.

## Overview

This project provides an AI-powered aim assist system for games, featuring:

- Screen capture with GPU acceleration
- AI inference using YOLOv8 with ONNX/TensorRT
- Target selection algorithms
- Aim control with configurable smoothness and delay
- Visualization overlay with OpenCV
- Real-time GUI with PyQt5
- Config management and profile support
- Stealth mode and logging
- OTA updates support

## Project Structure

- core/: Core pipeline modules (capturer, detector, aimer, visualizer)
- gui/: GUI implementation with PyQt5
- configs/: Configuration files (settings.json)
- models/: AI models (yolov8n.onnx)
- utils/: Utility modules (hotkeys)
- main.py: Entry point
- requirements.txt: Python dependencies

## Technologies

- Python 3.8+
- PyQt5, OpenCV, PyTorch, ONNX Runtime, TensorRT
- mss, pyautogui, numpy

## Usage

Run the main application:

```bash
python main.py
```

Configure settings in `configs/settings.json`.

## License

MIT License

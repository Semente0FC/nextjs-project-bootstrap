from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton, QSlider, QLabel,
    QComboBox, QHBoxLayout, QGroupBox, QGridLayout
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Aim Assist Pro")
        self.setGeometry(100, 100, 400, 300)
        self._init_ui()

    def _init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # ON/OFF Button
        self.toggle_button = QPushButton("Toggle Aim Assist")
        layout.addWidget(self.toggle_button)

        # Sliders Group
        sliders_group = QGroupBox("Settings")
        sliders_layout = QGridLayout()

        # Smoothness Slider
        self.smoothness_slider = QSlider(Qt.Horizontal)
        self.smoothness_slider.setMinimum(1)
        self.smoothness_slider.setMaximum(100)
        self.smoothness_slider.setValue(50)
        self.smoothness_label = QLabel("Smoothness: 0.5")
        sliders_layout.addWidget(self.smoothness_label, 0, 0)
        sliders_layout.addWidget(self.smoothness_slider, 0, 1)

        # FOV Slider
        self.fov_slider = QSlider(Qt.Horizontal)
        self.fov_slider.setMinimum(10)
        self.fov_slider.setMaximum(180)
        self.fov_slider.setValue(90)
        self.fov_label = QLabel("FOV: 90")
        sliders_layout.addWidget(self.fov_label, 1, 0)
        sliders_layout.addWidget(self.fov_slider, 1, 1)

        # Delay Slider
        self.delay_slider = QSlider(Qt.Horizontal)
        self.delay_slider.setMinimum(0)
        self.delay_slider.setMaximum(500)
        self.delay_slider.setValue(100)
        self.delay_label = QLabel("Delay: 100 ms")
        sliders_layout.addWidget(self.delay_label, 2, 0)
        sliders_layout.addWidget(self.delay_slider, 2, 1)

        sliders_group.setLayout(sliders_layout)
        layout.addWidget(sliders_group)

        # Dropdown for AI Models
        model_layout = QHBoxLayout()
        model_label = QLabel("AI Model:")
        self.model_dropdown = QComboBox()
        self.model_dropdown.addItems(["yolov8n.onnx", "yolov8s.onnx", "custom.onnx"])
        model_layout.addWidget(model_label)
        model_layout.addWidget(self.model_dropdown)
        layout.addLayout(model_layout)

        central_widget.setLayout(layout)

        # Connect slider signals
        self.smoothness_slider.valueChanged.connect(self.update_smoothness_label)
        self.fov_slider.valueChanged.connect(self.update_fov_label)
        self.delay_slider.valueChanged.connect(self.update_delay_label)

    def update_smoothness_label(self, value):
        self.smoothness_label.setText(f"Smoothness: {value / 100:.2f}")

    def update_fov_label(self, value):
        self.fov_label.setText(f"FOV: {value}")

    def update_delay_label(self, value):
        self.delay_label.setText(f"Delay: {value} ms")

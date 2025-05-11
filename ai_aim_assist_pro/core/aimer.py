import time
import pyautogui
import math

class AimController:
    def __init__(self, smoothness=0.5, fov=90, delay=100):
        self.smoothness = smoothness
        self.fov = fov
        self.delay = delay / 1000.0  # convert ms to seconds

    def move_mouse(self, x, y):
        pyautogui.moveRel(x, y, duration=self.smoothness)

    def aim_at(self, target_x, target_y, screen_center_x, screen_center_y):
        dx = target_x - screen_center_x
        dy = target_y - screen_center_y
        distance = math.sqrt(dx*dx + dy*dy)
        if distance > self.fov:
            return  # target out of FOV
        self.move_mouse(dx, dy)
        time.sleep(self.delay)

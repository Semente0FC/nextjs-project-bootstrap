from pynput import keyboard

class HotkeyManager:
    def __init__(self):
        self.hotkeys = {}
        self.listener = keyboard.GlobalHotKeys(self.hotkeys)

    def add_hotkey(self, hotkey, callback):
        self.hotkeys[hotkey] = callback
        self.listener = keyboard.GlobalHotKeys(self.hotkeys)

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()

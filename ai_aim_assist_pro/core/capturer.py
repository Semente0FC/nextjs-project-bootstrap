import mss
import numpy as np

class ScreenCapturer:
    def __init__(self, monitor=1, region=None):
        self.sct = mss.mss()
        self.monitor = self.sct.monitors[monitor]
        self.region = region  # region = {'top': int, 'left': int, 'width': int, 'height': int}

    def capture(self):
        if self.region:
            bbox = {
                "top": self.region.get("top", self.monitor["top"]),
                "left": self.region.get("left", self.monitor["left"]),
                "width": self.region.get("width", self.monitor["width"]),
                "height": self.region.get("height", self.monitor["height"]),
            }
        else:
            bbox = self.monitor
        img = self.sct.grab(bbox)
        img_np = np.array(img)
        # Convert BGRA to BGR
        img_np = img_np[:, :, :3]
        return img_np

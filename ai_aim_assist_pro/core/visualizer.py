import cv2

class Visualizer:
    def __init__(self):
        pass

    def draw_boxes(self, image, detections):
        for det in detections:
            x1, y1, x2, y2, conf, cls = det[:6]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{cls}: {conf:.2f}"
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)
        return image

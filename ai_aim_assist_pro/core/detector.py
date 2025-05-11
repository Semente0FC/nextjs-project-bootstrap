import onnxruntime as ort
import numpy as np

class Detector:
    def __init__(self, model_path, providers=None):
        if providers is None:
            providers = ['CUDAExecutionProvider', 'CPUExecutionProvider']
        self.session = ort.InferenceSession(model_path, providers=providers)
        self.input_name = self.session.get_inputs()[0].name

    def preprocess(self, image):
        # Resize and normalize image for YOLOv8 input
        import cv2
        img = cv2.resize(image, (640, 640))
        img = img.astype('float32') / 255.0
        img = np.transpose(img, (2, 0, 1))
        img = np.expand_dims(img, axis=0)
        return img

    def infer(self, image):
        input_tensor = self.preprocess(image)
        outputs = self.session.run(None, {self.input_name: input_tensor})
        return outputs

    def postprocess(self, outputs, conf_threshold=0.25):
        # Simplified postprocessing to filter detections by confidence
        detections = []
        pred = outputs[0]
        for det in pred[0]:
            conf = det[4]
            if conf > conf_threshold:
                detections.append(det)
        return detections

    def detect(self, image):
        outputs = self.infer(image)
        detections = self.postprocess(outputs)
        return detections

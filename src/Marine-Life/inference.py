import cv2
import glob
import numpy as np
import torch
import yolov5
from typing import Dict, Tuple, Union, List, Optional


# -----------------------------------------------------------------------------
# Configs
# -----------------------------------------------------------------------------

model_path = "./models/Marine-life-ID.pt"


# -----------------------------------------------------------------------------
# YOLOv5 class
# -----------------------------------------------------------------------------

class YOLO:
    """Wrapper class for loading and running YOLO model"""

    def __init__(self, model_path: str, device: Optional[str] = None):

        # load model
        self.model = yolov5.load(model_path, device=device)

    def __call__(
            self,
            img: Union[str, np.ndarray],
            conf_threshold: float = 0.25,
            iou_threshold: float = 0.45,
            image_size: int = 720,
            classes: Optional[List[int]] = None) -> torch.Tensor:
        self.model.conf = conf_threshold
        self.model.iou = iou_threshold

        if classes is not None:
            self.model.classes = classes

        # pylint: disable=not-callable
        detections = self.model(img, size=image_size)

        return detections


def run_inference(image_path):
    """Helper function to execute the inference."""

    predictions = model(image_path)

    return predictions


# -----------------------------------------------------------------------------
# Model Creation
# -----------------------------------------------------------------------------
model = YOLO(model_path, device='cpu')

if __name__ == "__main__":
    print("Done.")

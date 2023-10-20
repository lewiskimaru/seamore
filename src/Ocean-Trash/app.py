from ultralytics import YOLO
import gradio as gr

MODEL_PATH = "trashdetector_yolov8.pt"
trash_detector_model = YOLO(MODEL_PATH)

PREDICTION_SETTINGS = {
    "classes": 0,
    "conf_threshold": 0.4,
}


def detect_trash(image_path):
    results = trash_detector_model.predict(image_path, **PREDICTION_SETTINGS)
    return results[0].plot()[:, :, ::-1]  # Reverse channels for Gradio


title = "Trash Detector"
description = (
    ""
)

interface = gr.Interface(
    detect_trash,
    inputs=[gr.inputs.Image(type="filepath")],
    outputs=gr.outputs.Image(type="numpy"),
    title=title,
    description=description,
)

interface.launch()

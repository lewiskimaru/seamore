import glob
import gradio as gr
from ultralytics import YOLO

model_path = "trashdetector_yolov8.pt"
model = YOLO(model_path)


PREDICT_KWARGS = {
    "classes": 0,
    "conf": 0.4,
}


def run(image_path):
    results = model.predict(image_path, **PREDICT_KWARGS)
    return results[0].plot()[:, :, ::-1]  # reverse channels for gradio


title = "Trash Detector"
description = (
    ""
)

examples = glob.glob("images/*.png")

interface = gr.Interface(
    run,
    inputs=[gr.components.Image(type="filepath")],
    outputs=gr.components.Image(type="numpy"),
    title=title,
    description=description,
    examples=examples,
)

interface.queue().launch()

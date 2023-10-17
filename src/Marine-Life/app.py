import glob
import gradio as gr
from inference import *
from PIL import Image


def gradio_app(image_path):
    """A function that send the file to the inference pipeline, and filters
    some predictions before outputting to gradio interface."""

    predictions = run_inference(image_path)

    out_img = Image.fromarray(predictions.render()[0])

    return out_img


Title = "Marine Life Identification"
description = (
    ""
)

examples = glob.glob("images/*.png")

gr.Interface(gradio_app,
             inputs=[gr.inputs.Image(type="filepath")],
             outputs=gr.outputs.Image(type="pil"),
             enable_queue=True,
             title=Title,
             description=description,
             examples=examples).launch()

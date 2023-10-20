import gradio as gr
from inference import *
from PIL import Image


def gradio_app(image_path):
    """A function that sends the file to the inference pipeline, and applies filters to certain 
        predictions before displaying the output on the Gradio interface."""

    predictions = run_inference(image_path)

    out_img = Image.fromarray(predictions.render()[0])

    return out_img


Title = "Marine Life Identification"
description = (
    ""
)

gr.Interface(gradio_app,
             inputs=[gr.inputs.Image(type="filepath")],
             outputs=gr.outputs.Image(type="pil"),
             enable_queue=True,
             title=Title,
             description=description).launch()

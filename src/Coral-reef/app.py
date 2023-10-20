import gradio as gr
import tensorflow as tf
import numpy as np 
from PIL import Image

model_path = "models"
model = tf.saved_model.load(model_path)

classes = [ "bleached" ,  "healthy" , ]

def run(image_path):
    img = Image.open(image_path).convert('RGB')
    img = img.resize((300, 300 * img.size[1] // img.size[0]), Image.ANTIALIAS)
    inp_numpy = np.array(img)[None]
    inp = tf.constant(inp_numpy, dtype='float32')
    class_scores = model(inp)[0].numpy()
    print(class_scores)
    state = classes[class_scores.argmax()]
    return state

title = "Coral Health"
description = (
    ""
)


interface = gr.Interface(
    run,
    inputs=[gr.components.Image(type="filepath")],
    outputs="text",
    #outputs=gradio.outputs.Label(num_top_classes=3),
    title=title,
    description=description,
)

interface.queue().launch()

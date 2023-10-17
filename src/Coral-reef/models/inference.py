import tensorflow
import numpy
from PIL import Image

model = tensorflow.saved_model.load('./')
classes = [ "bleached" ,  "healthy" , ]

img = Image.open("image.jpg").convert('RGB')
img = img.resize((300, 300 * img.size[1] // img.size[0]), Image.ANTIALIAS)
inp_numpy = numpy.array(img)[None]


inp = tensorflow.constant(inp_numpy, dtype='float32')

class_scores = model(inp)[0].numpy()


print("")
print("class_scores", class_scores)
print("Class : ", classes[class_scores.argmax()])

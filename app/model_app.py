import numpy as np
from PIL import Image
from skimage import transform
import tensorflow as tf
model = tf.keras.models.load_model("model/my_model.h5")

def loadImage(filename):
    print(filename)
    image = Image.open(filename)
    image = np.array(image).astype('float32')
    image = transform.resize(image, (224, 224, 3))
    image = np.expand_dims(image, axis=0)
    return image

def predict(input):
    image = loadImage(input)
    predicted_label=int(np.round(model.predict(image)))
    return predicted_label
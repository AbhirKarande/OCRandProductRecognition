from tensorflow import keras
model = keras.models.load_model('whole_foods_model.h5')

#call the model on test_image.py
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing import image
test_image = image.load_img('daves.jpg', target_size = (224, 224))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)
print(result)
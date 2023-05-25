from chassisml import framework
model = framework.load('whole_foods_model.h5')
def process(input_bytes):
    import numpy as np
    from tensorflow import keras
    from tensorflow.keras.preprocessing import image
    test_image = image.load_img(input_bytes, target_size = (224, 224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict(test_image)
    #add a dictionary of the index of probabilities to class name: 0: 'Daves Killer Bread', 1: 'Gotham Greens Basil', 2: 'Labelle Patrimoine Heritage Eggs', 3: 'Whole Foods Market Brown Butter Chocolate Chunk Cookie'
    #print the index of the highest probability
    classDict = {0: 'Daves Killer Bread', 1: 'Gotham Greens Basil', 2: 'Labelle Patrimoine Heritage Eggs', 3: 'Whole Foods Market Brown Butter Chocolate Chunk Cookie'}
    result = classDict[np.argmax(result)]
    return result

#set up the chassis client
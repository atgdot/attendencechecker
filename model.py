import os
import numpy as np
import cv2
import os
import queryimage
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from sklearn.neighbors import NearestNeighbors

folder_path = 'image_data'

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(folder_path, filename)  # Get the full path of the image
        img = cv2.imread(image_path)  # Read the image using cv2.imread()

        # Process the image as needed
        # Example: Display the image
        #cv2.imshow('Image', img)
        cv2.waitKey(0)  # Wait for a key press to move to the next image

# After processing all images, close any open windows
cv2.destroyAllWindows()


# Function to extract features from images using pre-trained CNN model
def extract_features(directory, model):
    features = {}
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        image = load_img(path, target_size=(224, 224))
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image = preprocess_input(image)
        feature = model.predict(image).flatten()
        features[filename] = feature
    return features

# Function to identify if a person is the same as the dataset
def identify_person(image_path, features, model, threshold=0.6):
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    query_feature = model.predict(image).flatten()

    distances, indices = nn.kneighbors([query_feature])
    if distances[0][0] <= threshold:
        return "Same person"
    else:
        return "Different person"

# Path to the dataset directory
dataset_directory = 'image_data'

# Load pre-trained VGG16 model without the top (fully connected) layer
base_model = VGG16(weights="imagenet", include_top=False)
model = Model(inputs=base_model.input, outputs=base_model.output)

# Extract features from dataset images
dataset_features = extract_features(dataset_directory, model)

# Convert features to an array
features_array = np.array(list(dataset_features.values()))

# Create nearest neighbors model
nn = NearestNeighbors(n_neighbors=1, metric="cosine")
nn.fit(features_array)

image_dot = queryimage.capture_image()
# Example usage
query_image_path = image_dot
result = identify_person(query_image_path, dataset_features, model)
print(result)

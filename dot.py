import cv2
import os

folder_path = 'image_data'

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(folder_path, filename)  # Get the full path of the image
        img = cv2.imread(image_path)  # Read the image using cv2.imread()

        # Process the image as needed
        # Example: Display the image
        cv2.imshow('Image', img)
        cv2.waitKey(0)  # Wait for a key press to move to the next image

# After processing all images, close any open windows
cv2.destroyAllWindows()

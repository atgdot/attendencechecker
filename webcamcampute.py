import cv2
import os
import time
import uuid

# Function to save images to a directory with labels and generate a random UUID
def save_images_with_uuid(directory, num_images, label):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Generate a random UUID for this run
    run_id = str(uuid.uuid4())[:8]
    
    # Open the webcam
    cap = cv2.VideoCapture(0)
    
    count = 0 
    while count < num_images:
        # Capture frame from the webcam
        ret, frame = cap.read()
        
        # Display the captured frame
        cv2.imshow('Capture Images', frame)
        
        # Save the frame as an image file with label and run ID
        image_path = os.path.join(directory, 'image{}_{}_{}.jpg'.format(count, label, run_id))
        cv2.imwrite(image_path, frame)
        
        count += 1
        
        time.sleep(0.5)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the webcam and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

    # Return the generated UUID
    return run_id

# Save images from webcam with labels and get the random UUID
label = input("Enter the label for the captured images: ")
uuid = save_images_with_uuid('image_data', 10, label)
print("Random UUID:", uuid)

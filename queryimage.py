import cv2

def capture_image():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Failed to open the webcam")
        return

    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if not ret:
        print("Failed to capture frame")
        cap.release()
        return

    # Display the captured frame
    cv2.imshow("Captured Image", frame)

    # Save the captured frame as an image file
    image_path = "captured_image.jpg"
    cv2.imwrite(image_path, frame)
    #print(f"Image saved as {image_path}")
    return image_path

    # Release the webcam and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

# Call the function to capture an image
capture_image()

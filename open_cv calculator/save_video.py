#Saving video
import cv2

# Initialize video capture and video writer
cap = cv2.VideoCapture(0)  # Use the appropriate camera index or video file path
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for video
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Output file name, codec, frame rate, frame size

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the frame
    cv2.imshow('Frame', frame)

    # Write the frame to the output video file
    out.write(frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()

import cv2
import numpy as np

# Start video capture
cap = cv2.VideoCapture(0)

# Define color ranges (HSV)
colors = {
    'red': [
        (np.array([0, 120, 70]), np.array([10, 255, 255])),
        (np.array([170, 120, 70]), np.array([180, 255, 255]))
    ],
    'green': [(np.array([36, 25, 25]), np.array([86, 255,255]))],
    'blue': [(np.array([94, 80, 2]), np.array([126, 255, 255]))]
}

detect_color = 'red'  # change to 'green' or 'blue'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = None
    for lower, upper in colors[detect_color]:
        partial_mask = cv2.inRange(hsv, lower, upper)
        mask = partial_mask if mask is None else mask + partial_mask

    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Optional: Draw contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow('Original', frame)
    cv2.imshow('Detected Color', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

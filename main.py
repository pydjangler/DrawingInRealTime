import cv2

def Draw(image):
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_blure = cv2.GaussianBlur(image_grey, (3, 3), 0)
    edges = cv2.Canny(image_blure, 10, 80)

    match, mask = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY_INV)
    return mask


cap = cv2.VideoCapture(0)
while True:
    match, frame = cap.read()
    cv2.imshow('stream_sketch', Draw(frame))

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
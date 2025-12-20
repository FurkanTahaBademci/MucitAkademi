import cv2

ilk_x, ilk_y = None, None
x_son, y_son = None, None
sart = False
# mouse event callback function


def mouse_event(event, x, y, flags, param):
    global ilk_x, ilk_y, x_son, y_son, sart

    if event == cv2.EVENT_LBUTTONDOWN:
        x_son = None
        y_son = None
        sart = True
        ilk_x = x
        ilk_y = y
        print(f"Left button down at ({x}, {y})")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right button down at ({x}, {y})")
    elif event == cv2.EVENT_MBUTTONDOWN:
        print(f"Middle button down at ({x}, {y})")
    elif event == cv2.EVENT_MOUSEMOVE:
        if sart:
            x_son = x
            y_son = y

        # print(f"Mouse move at ({x}, {y})")
    elif event == cv2.EVENT_LBUTTONUP:
        x_son = x
        y_son = y
        sart = False
        print(f"Left button up at ({x}, {y})")
    elif event == cv2.EVENT_RBUTTONUP:
        print(f"Right button up at ({x}, {y})")
    elif event == cv2.EVENT_MBUTTONUP:
        print(f"Middle button up at ({x}, {y})")


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if ilk_x is not None and ilk_y is not None and x_son is not None and y_son is not None:
        print(
            f"Drawing rectangle from ({ilk_x}, {ilk_y}) to ({x_son}, {y_son})")
        cv2.rectangle(frame, (ilk_x, ilk_y), (x_son, y_son), (0, 255, 0), 2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('Webcam', frame)
    cv2.setMouseCallback('Webcam', mouse_event)

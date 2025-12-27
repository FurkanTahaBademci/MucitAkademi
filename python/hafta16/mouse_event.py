import cv2

ilk_x, ilk_y = None, None
x_son, y_son = None, None
sart = False

kareler = []

mavi = (255, 0, 0)
yesil = (0, 255, 0)
kirmizi = (0, 0, 255)

renk = mavi
# mouse event callback function


def mouse_event(event, x, y, flags, param):
    global ilk_x, ilk_y, x_son, y_son, sart, renk

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
        kareler.append((ilk_x, ilk_y, x_son, y_son, renk))
        x_son = x
        y_son = y
        sart = False
        print(f"Left button up at ({x}, {y})")
    elif event == cv2.EVENT_RBUTTONUP:
        print(f"Right button up at ({x}, {y})")
    elif event == cv2.EVENT_MBUTTONUP:
        print(f"Middle button up at ({x}, {y})")


cap = cv2.VideoCapture(0)
cv2.namedWindow('Webcam')
cv2.setMouseCallback('Webcam', mouse_event)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Kaydedilen dikdörtgenleri çiz
    for (x1, y1, x2, y2, rect_renk) in kareler:
        cv2.rectangle(frame, (x1, y1), (x2, y2), rect_renk, 2)
    
    # Gerçek zamanlı çizim (sürükleme sırasında)
    if sart and ilk_x is not None and ilk_y is not None and x_son is not None and y_son is not None:
        cv2.rectangle(frame, (ilk_x, ilk_y), (x_son, y_son), renk, 2)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('d'):
        print("Clearing rectangles")
        kareler.clear()
    elif key == ord('a'):
        print("Changing color to red")
        renk = kirmizi
    elif key == ord('b'):
        print("Changing color to green")
        renk = yesil
    elif key == ord('c'):
        print("Changing color to blue")
        renk = mavi


    cv2.imshow('Webcam', frame)

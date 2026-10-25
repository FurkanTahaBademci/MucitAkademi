import cv2
import requests
import numpy as np

url = "http://192.168.5.82:8080/shot.jpg"


while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)

    cv2.imshow("IP Camera", img)
    cv2.waitKey(1)
    

    if cv2.waitKey(30) == 27:
        break


    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
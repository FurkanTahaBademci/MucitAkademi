import cv2
import numpy as np

# Boş bir beyaz tuval oluştur
canvas = 255 * np.ones((750, 750, 3), dtype="uint8")

cv2.line(canvas,(50,50),(700,50),(255,0,0),5)
## canvas üzerindeki (50,50) noktasından (700,50) noktasına mavi renkli ve 5 pixel kalınlığında bir çizgi çizer.

cv2.rectangle(canvas,(100,100),(200,600),(0,255,0),3)
cv2.rectangle(canvas,(100,250),(150,300),(0,255,0),3)

cv2.circle(canvas, (325,325), 75, (0,0,255), -1)

cv2.putText(canvas,"Furkan",(400,700),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),3)

cv2.namedWindow("Drawing Canvas")
cv2.imshow("Drawing Canvas", canvas)
cv2.waitKey(0)

cv2.destroyAllWindows()
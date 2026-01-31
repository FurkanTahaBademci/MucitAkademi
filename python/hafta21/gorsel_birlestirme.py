import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Görselleri yükle
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

# Renkleri düzelt (OpenCV BGR okur, Matplotlib RGB bekler)
img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# 2. ORB ve Eşleştirme (Senin kodun)
orb = cv2.ORB_create(nfeatures=2000)
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = sorted(bf.match(des1, des2), key=lambda x: x.distance)

# 3. Homografi Hesaplama
# En iyi eşleşen noktaların koordinatlarını al
src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# RANSAC algoritması ile hatalı eşleşmeleri ayıkla ve matrisi bul
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# 4. Perspektif Dönüşümü ve Birleştirme
h, w, _ = img2.shape
# img1'i img2'nin perspektifine göre bük (warp)
# Genişliği iki resmin toplamı kadar yaparak yer açıyoruz
dst = cv2.warpPerspective(img1, M, (img1.shape[1] + img2.shape[1], img2.shape[0]))

# img2'yi (referans resim) sol tarafa yerleştir
dst[0:img2.shape[0], 0:img2.shape[1]] = img2

# 5. Görselleştirme
plt.figure(figsize=(20, 10))
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title('Birleştirilmiş Görsel (Panorama)')
plt.axis('off')
plt.show()
import cv2
import numpy as np
import matplotlib.pyplot as plt


def get_homography(img1, img2):
    orb = cv2.ORB_create(nfeatures=2000)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = sorted(bf.match(des1, des2), key=lambda x: x.distance)

    src_pts = np.float32(
        [kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32(
        [kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    return M


# 1. Görselleri yükle
img1 = cv2.imread('1.jpg')  # Sol
img2 = cv2.imread('2.jpg')  # Orta (Referans)
img3 = cv2.imread('3.jpg')  # Sağ

# 2. Homografi Matrislerini Hesapla
# img1'i img2'ye, img3'ü img2'ye uyduracağız
M1 = get_homography(img1, img2)
M3 = get_homography(img3, img2)

# 3. Geniş Bir Kanvas Oluştur (3 resmin toplam genişliği kadar)
width = img1.shape[1] + img2.shape[1] + img3.shape[1]
height = img2.shape[0]

# 4. Resimleri Yerleştir
# Önce img1'i orta resmin koordinat sistemine göre sağa kaydırarak büküyoruz
# (Burada matrisi biraz modifiye ederek sola yer açabiliriz ama en basit yol sırayla eklemektir)
# Bu örnekte img2'yi merkeze koyup diğerlerini warp ediyoruz:

# img1 -> img2 perspektifine
result = cv2.warpPerspective(img1, M1, (width, height))

# img3 -> img2 perspektifine (Önce geçici bir değişkene atayalım)
res3 = cv2.warpPerspective(img3, M3, (width, height))

# Katmanları Birleştir (Siyah olmayan pikselleri üst üste koy)
result[0:img2.shape[0], 0:img2.shape[1]] = img2
result = np.maximum(result, res3)  # Basit birleştirme yöntemi

# 5. Görselleştirme
plt.figure(figsize=(20, 10))
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title('3 Görsel Panorama')
plt.axis('off')
plt.show()

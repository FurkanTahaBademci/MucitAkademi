import cv2
import numpy as np


def thresh_tozero(gray, thresh):

	#THRESH_TOZERO: pixels greater than `thresh` keep their original value,
	#pixels less than or equal to `thresh` become 0.

	#Returns a tuple `(dst_cv, dst_manual)` where `dst_cv` is the result from
	#OpenCV's `cv2.threshold(..., cv2.THRESH_TOZERO)` and `dst_manual` is a
	#NumPy-based manual implementation for clarity and testing.
	
	_, dst_cv = cv2.threshold(gray, thresh, 255, cv2.THRESH_TOZERO)
	dst_manual = np.where(gray > thresh, gray, 0).astype(np.uint8)
	return dst_cv, dst_manual


def thresh_mask(gray, thresh):
	
#THRESH_MASK: `thresh` değerinden büyük piksellerin sıfırdan farklı 
#(genellikle 255) ve diğerlerinin 0 olduğu ikili bir maske (8 bit tek kanallı) üretir.
#OpenCV'nin `cv2.THRESH_MASK` fonksiyonu, hedef görüntüyü maskeyle doldurur.
#Ayrıca, gösterim amacıyla manuel bir maske döndürüyoruz.
	
	# Note: OpenCV's threshold returns the same image size mask for THRESH_MASK
	_, dst_cv = cv2.threshold(gray, thresh, 255, cv2.THRESH_MASK)
	dst_manual = (gray > thresh).astype(np.uint8) * 255
	return dst_cv, dst_manual


def thresh_otsu(gray):
	
	#THRESH_OTSU: Otsu'nun yöntemini kullanarak otomatik eşik seçimi.

#Otsu'nun yöntemi, bimodal bir histogram için sınıf içi varyansı en aza indiren 
#(eşdeğer olarak sınıflar arası varyansı en üst düzeye çıkaran) bir eşik bulur.
#OpenCV, `cv2.THRESH_OTSU` bayrağını kullanırken eşik değeri olarak 0 geçilmesini gerektirir.
# `(otsu_thresh, binary_image)` değerini döndürürüz; burada `otsu_thresh` hesaplanan eşik değeri
#  ve `binary_image`, `cv2.THRESH_BINARY` kullanılarak ikili hale getirilmiş sonuçtur.
	
	otsu_thresh, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	return otsu_thresh, binary


if __name__ == '__main__':
	# Örnek kullanım bloğu: mevcut resim dosyanızı ayarlayın
	img_path = 'C:\\Users\\furkan\\Desktop\\MucitAkademi\\python\\hafta12\\klon.jpg'
	image = cv2.imread(img_path)
	if image is None:
		raise FileNotFoundError(f"Resim bulunamadı: {img_path}")

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# THRESH_TOZERO örneği
	tozero_cv, tozero_manual = thresh_tozero(gray, thresh=127)

	# THRESH_MASK örneği
	mask_cv, mask_manual = thresh_mask(gray, thresh=127)

	# THRESH_OTSU örneği
	otsu_thresh, otsu_bin = thresh_otsu(gray)

	print(f"Otsu tarafından bulunan eşik değeri: {otsu_thresh}")

	# Görüntüleme (kapatmak için herhangi bir tuşa basın)
	cv2.imshow('Original Image', image)
	cv2.imshow('Gray Image', gray)
	cv2.imshow('TOZERO (cv)', tozero_cv)
	cv2.imshow('TOZERO (manual)', tozero_manual)
	cv2.imshow('MASK (cv)', mask_cv)
	cv2.imshow('MASK (manual)', mask_manual)
	cv2.imshow('OTSU Binary', otsu_bin)

	cv2.waitKey(0)
	cv2.destroyAllWindows()
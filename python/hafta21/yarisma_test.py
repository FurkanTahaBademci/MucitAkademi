import cv2
import numpy as np
import os

# --- AYARLAR ---
folder_path = 'yarisma'
RESIZE_FACTOR = 0.5  # RAM dostu olması için 0.5 kalsın

def read_and_resize(path, factor):
    img = cv2.imread(path)
    if img is None: return None
    if factor < 1.0:
        img = cv2.resize(img, (0,0), fx=factor, fy=factor)
    return img

def crop_black_borders(img):
    """Görselin etrafındaki siyah boşlukları otomatik kırpar."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        x, y, w, h = cv2.boundingRect(contours[0])
        return img[y:y+h, x:x+w]
    return img

# 1. Dosyaları Listele
image_files = sorted([f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))])
print(f"Toplam {len(image_files)} görsel işleniyor...")

# 2. İlk Resim ve Dev Kanvas Hazırlığı
first_img = read_and_resize(os.path.join(folder_path, image_files[0]), RESIZE_FACTOR)
h, w = first_img.shape[:2]

# Kanvası 15 kat daha büyük başlatıyoruz (Hata almamak için)
canvas_h, canvas_w = h * 25, w * 25
panorama = np.zeros((canvas_h, canvas_w, 3), dtype=np.uint8)

# Başlangıç noktası (Tam merkez)
start_x, start_y = canvas_w // 2, canvas_h // 2
panorama[start_y:start_y+h, start_x:start_x+w] = first_img

current_x, current_y = float(start_x), float(start_y)
prev_img_gray = cv2.cvtColor(first_img, cv2.COLOR_BGR2GRAY).astype(np.float32)

# 3. Döngü
for i in range(1, len(image_files)):
    curr_img = read_and_resize(os.path.join(folder_path, image_files[i]), RESIZE_FACTOR)
    if curr_img is None: continue
    
    curr_img_gray = cv2.cvtColor(curr_img, cv2.COLOR_BGR2GRAY).astype(np.float32)

    # Kayma hesaplama
    hann = cv2.createHanningWindow((w, h), cv2.CV_32F)
    shift, _ = cv2.phaseCorrelate(prev_img_gray, curr_img_gray, window=hann)
    
    dx, dy = shift[0], shift[1]
    
    # Koordinat güncelleme
    current_x -= dx
    current_y -= dy
    
    ix, iy = int(round(current_x)), int(round(current_y))

    # Sınır Kontrolü ve Yerleştirme
    if 0 <= ix < canvas_w - w and 0 <= iy < canvas_h - h:
        # Mevcut panorama ile yeni resmi harmanla (üst üste binmeyi yumuşatır)
        existing_area = panorama[iy:iy+h, ix:ix+w]
        mask = (curr_img > 0)
        existing_area[mask] = curr_img[mask]
        panorama[iy:iy+h, ix:ix+w] = existing_area
        
        print(f"[{i+1}/{len(image_files)}] Yerleştirildi: {image_files[i]}")
    else:
        print(f"!!! KRİTİK: {image_files[i]} kanvas dışına taştı, bu kare atlanıyor.")

    prev_img_gray = curr_img_gray

    # Ara aşama gösterimi (Her 5 karede bir güncellemek hızı artırır)
    if i % 5 == 0:
        temp_show = cv2.resize(panorama, (1000, 700))
        cv2.imshow('Dron Haritalama - Adim Adim', temp_show)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

# 4. Final: Kırpma ve Kaydetme
print("İşlem bitti, siyah alanlar temizleniyor...")
final_map = crop_black_borders(panorama)

cv2.imwrite('dron_buyuk_harita_final.jpg', final_map)
print("Başarıyla kaydedildi: dron_buyuk_harita_final.jpg")

cv2.imshow('Final Harita', cv2.resize(final_map, (1200, 800)))
cv2.waitKey(0)
cv2.destroyAllWindows()
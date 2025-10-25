import imageio.v3 as iio
from PIL import Image
import numpy as np
import os

# PNG dosyalarını bul
filenames = [f for f in os.listdir() if f.lower().endswith('.png')]
filenames.sort()

images = []

# Tüm resimleri aynı boyutta olacak şekilde ortala
# Önce maksimum genişlik ve yüksekliği bul
max_width = 0
max_height = 0
for filename in filenames:
    img = Image.open(filename)
    max_width = max(max_width, img.width)
    max_height = max(max_height, img.height)

# Şimdi her resmi max boyuta ortalayıp array'e çevir
for filename in filenames:
    try:
        img = Image.open(filename).convert("RGBA")  # RGBA ile şeffaflık dahil
        canvas = Image.new("RGBA", (max_width, max_height), (255, 255, 255, 0))  # boş arka plan
        offset = ((max_width - img.width) // 2, (max_height - img.height) // 2)
        canvas.paste(img, offset)
        images.append(np.array(canvas))
    except Exception as e:
        print(f"{filename} okunamadı: {e}")

# GIF oluştur
if images:
    iio.imwrite('team.gif', images, duration=0.5, loop=0)
    print(f"GIF oluşturuldu: team.gif ({len(images)} kare)")
else:
    print("Hiç PNG dosyası bulunamadı.")

import imageio.v3 as iio
import os

folder = 'gif'  # klasör adı
filenames = ['team-pic1.png', 'team-pic2.png']

images = []
for filename in filenames:
    path = os.path.join(folder, filename)  # klasör + dosya
    if os.path.exists(path):
        images.append(iio.imread(path))
    else:
        print(f"Dosya bulunamadı: {path}")

if images:
    iio.imwrite('team.gif', images, duration=0.5, loop=0)
    print("GIF oluşturuldu: team.gif")
else:
    print("Hiç dosya bulunamadı.")

import os.path
from PIL import Image

img_dir = r'C:/Path/To/Images/'
sized_dir = r'C:/Path/To/Put/Resized/Images'

print('Bulk images resizing started...')

for img in os.listdir(img_dir):
	img_name = img
  print(img_name)
  f_img = img_dir + img
  f, e = os.path.splitext(img_dir + img)
  img = Image.open(f_img)
  img = img.resize((128, 128), Image.ANTIALIAS)
  without_ext = img_name.split(".")[0]
  img.save(sized_dir + without_ext + ".png", 'png', quality=90)

print('Bulk images resizing finished...')

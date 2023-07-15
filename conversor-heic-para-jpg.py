import glob
from PIL import Image
from pillow_heif import register_heif_opener
import os

register_heif_opener()

folder = r"C:\Users\david\Downloads\pai"

os.chdir(folder)

# searching .heic images in existing folder
for heic_pic_name in glob.glob("*.heic"):
    my_pic = Image.open(heic_pic_name)  # opening .heic images
    # creating new names for .jpg images
    jpg_pic_name = heic_pic_name.split('.')[0]+'.jpg'
    my_pic.save(jpg_pic_name, format="JPEG",
                optimize=True, quality=100)  # saving

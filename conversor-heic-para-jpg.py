#importação das bibliotecas necessárias para 
# a tarefa
import glob
from PIL import Image
from pillow_heif import register_heif_opener
import os

register_heif_opener()

#atribuir a variavel folder a url do diretorio onde estão as fotos
folder = r"C:\Users\user\diretorio-das-fotos"

# configurar o diretório das fotos como o diretório de trabalho
os.chdir(folder)

# searching .heic images in existing folder
for heic_pic_name in glob.glob("*.heic"):
    my_pic = Image.open(heic_pic_name)  # opening .heic images
    # creating new names for .jpg images
    jpg_pic_name = heic_pic_name.split('.')[0]+'.jpg'
    my_pic.save(jpg_pic_name, format="JPEG",
                optimize=True, quality=100)  # saving

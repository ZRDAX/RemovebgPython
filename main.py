# instale [ pip install rembg ]
# faz pelo terminal

from rembg import remove
from PIL import Image

# importe sua img e no output troque de jpgpara png

input_img = 'ChikipiWar.JPG'
output_img = 'ChikipiWar.PNG'

input = Image.open(input_img)
output = remove(input)
output.save(output_img)

# acho que vai funcionar no teu trabalho
# é bem simples o codigo.

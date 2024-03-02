# instale [ pip install rembg ]
# faz pelo terminal

from rembg import remove
from PIL import image

# importe sua img e no output troque de jpgpara png

input_img = 'ChikipiWar.JPG'
output_img = 'ChikipiWar.PNG'

input = image.open(input_img)
output = remove(input)
output.save(output_img)

# acho que vai funcionar no teu trabalho
# é bem simples o codigo.

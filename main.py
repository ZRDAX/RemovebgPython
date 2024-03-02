# instale [ pip install rembg ]
# faz pelo terminal

from rembg import remove
from PIL import Image
from tkinter import filedialog
from ImgImport import import_Img

inputImg = import_Img()

if inputImg:
    input_img = Image.open(inputImg)

    outputImg = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

    if outputImg:
        output_img = remove(input_img)

        # Salva a imagem de saída
        output_img.save(outputImg)
        print(f'Diretorio da imagem: {outputImg}')
        print("Salvo!")
    else:
        print('Erro! Nenhum diretório selecionado. Vlw!')
else:
    print('Erro! Nenhum arquivo selecionado. Vlw!.')

# acho que vai funcionar no teu trabalho
# é bem simples o codigo.

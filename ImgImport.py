
import tkinter as tk
from tkinter import filedialog


def import_Img():
    root = tk.Tk()
    root.withdraw()

    pasta_arq = filedialog.askopenfilename()

    return pasta_arq

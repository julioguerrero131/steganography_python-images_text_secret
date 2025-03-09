from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
root.title("Esteganografía - Oculta Mensajes de Texto en una Imagen")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#2f4155")

# icon
image_icon = PhotoImage(file="logo.jpg") 
root.iconphoto(False, image_icon)

# logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)

root.mainloop()
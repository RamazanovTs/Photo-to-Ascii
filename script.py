from PIL import Image, ImageOps
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

replace = ['.', ':', '+', '*', '%', 'S', '#', '@']

file_path = filedialog.askopenfilename()

while not file_path:
    file_path = filedialog.askopenfilename()

image = Image.open(file_path)
image = ImageOps.grayscale(image)
image = image.resize((100, 100))

width, height = image.size

ascii_art = []

for i in range(height):
    row = ""
    for j in range(width):
        value = image.getpixel((j, i)) 

        if value <= 31:
            row += replace[7]
        elif 32 <= value <= 63:
            row += replace[6]
        elif 64 <= value <= 95:
            row += replace[5]
        elif 96 <= value <= 127:
            row += replace[4]
        elif 128 <= value <= 159:
            row += replace[3]
        elif 160 <= value <= 191:
            row += replace[2]
        elif 192 <= value <= 223:
            row += replace[1]
        else:
            row += replace[0]

    ascii_art.append(row)

with open("ascii_output.txt", "w") as f:
    f.write("\n".join(ascii_art))

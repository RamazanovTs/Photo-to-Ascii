from PIL import Image
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

while not file_path:
    file_path = filedialog.askopenfilename()


image = Image.open(file_path)
image = image.resize((100, 100))

width, height = image.size

ascii_art = []

for i in range(height):
    row = ""
    for j in range(width):
        pixel_val = image.getpixel((j, i))
        if pixel_val[0] == 255 and pixel_val[1] == 255 and pixel_val[2] == 255:
            row += "*"
        else:
            row += "#"
    ascii_art.append(row)

with open("ascii_output.txt", "w") as f:
    f.write("\n".join(ascii_art))

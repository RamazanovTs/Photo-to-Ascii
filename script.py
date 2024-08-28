from PIL import Image

image =Image.open("photo.jpg")
ascii_art=[]

width=image.width
height=image.height
pixels=width*height

for i in range(height):
    row=""
    for j in range(width):
        pixel_val=image.getpixel((j,i))
        if pixel_val[0]==255 and pixel_val[1]==255 and pixel_val[2]==255:
            row+="*"
        else:
            row+="#"
    with open("ascii_output.txt", "a") as f:
        f.write(f'{row}\n')


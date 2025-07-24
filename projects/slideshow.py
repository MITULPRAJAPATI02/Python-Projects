from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# Path of images
image_paths = [
    r"C:\Users\mitul\Desktop\post instra\IMG_2515.jpg",
    r"C:\Users\mitul\Desktop\post instra\IMG_2517.jpg",
    r"C:\Users\mitul\Desktop\post instra\IMG_2527.jpg",
    r"C:\Users\mitul\Desktop\post instra\IMG_2635.jpg",
    r"C:\Users\mitul\Desktop\post instra\IMG_2656.jpg",
]

# Resize images to 1080x1080
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

slideshow = cycle(photo_images)

def update_image():
    photo_image = next(slideshow)
    label.config(image=photo_image)
    root.after(3000, update_image)  # 3000 ms = 3 seconds

def start_slideshow():
    update_image()

play_button = tk.Button(root, text="Start Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import tkinter as tk
from tkinter import ttk
from os.path import join

def change_image(_):
    global image_tk
    print(f'color:{color_int.get()} blur:{blur_int.get()}')
    # blur
    blur_image = image.filter(
        ImageFilter.BoxBlur(radius=blur_int.get())
    )
    
    # vibrance
    color_enhancer = ImageEnhance.Color(blur_image)
    new_image = color_enhancer.enhance(color_int.get())
    
    image_tk = ImageTk.PhotoImage(new_image)
    canvas.create_image(0,0, 
                        image=image_tk,
                        anchor='nw')

# create the window
window = tk.Tk()

window.geometry('600x400')
window.title('Image Editor')

# image import
image = Image.open(join('resources', 'images', 'raccoon.jpg'))
image_width, image_height = image.size
image = image.resize(size = (image_width // 3, image_height // 3))
image_tk = ImageTk.PhotoImage(image)

# canvas
canvas = tk.Canvas(window,
                   background='black',
                   bd=0,
                   highlightthickness=0,
                   relief='ridge')
canvas.create_image(0, 0, 
                    image=image_tk,
                    anchor='nw')
canvas.pack(fill='both', 
            expand=True)

# sliders
blur_int = tk.IntVar(value = 0)
blur_slider = ttk.Scale(window, 
                        from_=0, 
                        to=100, 
                        variable=blur_int,
                        orient='horizontal',
                        length=200, 
                        command=change_image)
blur_slider.pack()

# sliders
color_int = tk.IntVar(value = 1)
color_slider = ttk.Scale(window, 
                        from_=0, 
                        to=100, 
                        variable=color_int,
                        orient='horizontal',
                        length=200, 
                        command=change_image)
color_slider.pack()

window.mainloop()

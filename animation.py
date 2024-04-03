from PIL import Image
from os.path import isfile, join
from glob import glob

paths = glob(join("resources", "animation", "*.png"))  
images = [Image.open(path) for path in paths]

print(paths)
# def create_gif(image_folder, output_gif):

images[0].save("animation.gif", 
               save_all=True, 
               append_images=images[1:],
               duration=100, 
               loop=0)    
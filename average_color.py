from PIL import Image
import numpy as np
from os.path import join

image = Image.open(join('resources', 'images','cat.jpg'))

red_array = np.asarray(image.getchannel('R'))
green_array = np.asarray(image.getchannel('G'))
blue_array = np.asarray(image.getchannel('B'))

print(red_array.shape)

average_color = (
    int(np.average(red_array)),
    int(np.average(green_array)),
    int(np.average(blue_array))
)

print(average_color)
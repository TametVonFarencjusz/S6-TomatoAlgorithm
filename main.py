import cv2 
import numpy as np
import myfunctions as mf

tomatos = [[760, 267, 869, 366, 1],
        [138, 593, 138+89, 593+76, 0.8]]

stems = [[796, 226, 796+19, 226+45, 0.6],
        [724, 265, 724+32, 265+43, 0.6],
        [786, 361, 786+41, 361+39, 0.5],
        [851, 255, 851+23, 255+39, 0.2],
        [185, 311, 185+84, 311+186, 0.9],
        [305, 611, 305+20, 611+40, 0.01]]

path = r"tomato.png"


for i,tomato in enumerate(tomatos):
    image = cv2.imread(path)
    mf.full_tomato(image, tomato)
    for stem in stems:
        mf.full_draw(image, stem, tomato)
    window_name = "Image" + str(i)
    cv2.imshow(window_name, image) 
    cv2.imwrite(f"./out/{window_name}.png", image)
cv2.waitKey(0)
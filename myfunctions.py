import cv2 
import numpy as np

def get_center(obj):
    return [(obj[0]+obj[2])//2, (obj[1]+obj[3])//2]

def get_radius(obj):
    return (((obj[0]-obj[2])//2)**2+((obj[1]-obj[3])//2)**2)**.5

def dist(obj, obj2):
    return ((obj[0]-obj2[0])**2+(obj[1]-obj2[1])**2)**.5

def angle(obj1, obj2):
    x = get_center(obj1)[0] - get_center(obj2)[0]
    y = get_center(obj1)[1] - get_center(obj2)[1]
    norm = (x**2+y**2)**0.5
    x /= norm
    y /= norm
    val = abs(np.angle(-y+x*1j, deg=True))
    return (180-val)/180

def full_draw(image, obj, tomato):
    draw(image, obj, 1)
    calc_value(image, obj, tomato)

def draw(image, obj, type):
    color = (0,0,255) if type == 0 else (0,255,0)
    image = cv2.rectangle(image, (obj[0], obj[1]), (obj[2], obj[3]), color, 2)
    image = cv2.circle(image, get_center(obj), 2, color, 2)
    image = cv2.putText(image, str(obj[4]), (obj[2], obj[3]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 2, cv2.LINE_AA)
    image = cv2.putText(image, str(obj[4]), (obj[2], obj[3]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (150,150,150), 1, cv2.LINE_AA)

def full_tomato(image, obj):
    draw(image, obj, 0)
    image = cv2.circle(image, get_center(obj), int(get_radius(obj)), (0,0,255), 1)

def calc_value(image, obj, tomato):
    val_d = get_radius(tomato) / (dist(get_center(tomato), get_center(obj)))
    val_a = angle(obj, tomato)
    value = (val_a)*(val_d**2)*(obj[4]**2)
    
    image = cv2.putText(image, f"{value:.3f}", get_center(obj), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
    image = cv2.putText(image, f"{value:.3f}", get_center(obj), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)


from PIL import Image, ImageGrab
from pynput.keyboard import Key, Controller
import time

screen_pic_px = ImageGrab.grab(bbox=(885, 200, 1035, 705)).load()
screen_pic = ImageGrab.grab(bbox=(885, 200, 1035, 705))
screen_pic.show()
wood = [161, 116, 56]

tree = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

wood_px_left = []
wood_px_right = []
'''
#right
for y in range(505):

    #left
    if screen_pic_px[15,y][0]==wood[0]:
        wood_px_left.append(y)
    #right
    if screen_pic_px[115,y][0]==wood[0]:
        wood_px_right.append(y)
'''        
print("Ende")    

if  screen_pic_px[15,75][0]==wood[0]:
    tree[10] = 1
elif screen_pic_px[115,75][0]==wood[0]:
    tree[10] = 2
else:
    tree[10] = 2

if  screen_pic_px[15,118][0]==wood[0]:
    tree[9] = 1
elif screen_pic_px[115,118][0]==wood[0]:
    tree[10] = 2
else: tree[10] = 2

if  screen_pic_px[15,159][0]==wood[0]:
    tree[8] = 1
elif screen_pic_px[115,159][0]==wood[0]:
    tree[10] = 2
else: tree[10] = 2

if  screen_pic_px[15,200][0]==wood[0]:
    tree[7] = 1
elif screen_pic_px[115,200][0]==wood[0]:
    tree[10] = 2
else: tree[10] = 2

if  screen_pic_px[15,242][0]==wood[0]:
    tree[6] = 1
elif screen_pic_px[115,242][0]==wood[0]:
    tree[10] = 2
else: tree[10] = 2

if  screen_pic_px[15,283][0]==wood[0]:
    tree[5] = 1
elif screen_pic_px[115,283][0]==wood[0]:
    tree[10] = 2
else: tree[10] = 2

if  screen_pic_px[15,325][0]==wood[0]:
    tree[4] = 1
elif screen_pic_px[115,325][0]==wood[0]:
    tree[10] = 2
else: tree[10] = 2

if  screen_pic_px[15,368][0]==wood[0]:
    tree[3] = 1
elif screen_pic_px[115,368][0]==wood[0]:
    tree[10] = 2
else: tree[10] = 2

if  screen_pic_px[15,408][0]==wood[0]:
    tree[2] = 1
elif screen_pic_px[115,408][0]==wood[0]:
    tree[10] = 2
else: tree[10] = 2


if  screen_pic_px[15,451][0]==wood[0]:
    tree[1] = 1
elif screen_pic_px[115,451][0]==wood[0]:
    tree[10] = 2
else: tree[10] = 2

if  screen_pic_px[15,492][0]==wood[0]:
    tree[0] = 1
elif screen_pic_px[115,492][0]==wood[0]:
    tree[10] = 2
else: tree[10] = 2


for ctrl in tree:

    if ctrl == 0:
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    elif ctrl == 1:
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    elif ctrl == 2:
        keyboard.press(Key.left)
        keyboard.release(Key.left) 
           
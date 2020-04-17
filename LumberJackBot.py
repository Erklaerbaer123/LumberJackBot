
# IDEAS

# Pixel am Rand oben tracken um schneller zu reagieren


from PIL import Image, ImageGrab
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
wood = [161, 116, 56]

inp = input("Start: ")

time.sleep(3)
keyboard.press(Key.space)
keyboard.release(Key.space)

flag = 0
tree = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

pics = []
prev = 0

i=0
while  i<1:
# i<=19
    time.sleep(0.5)

    #Variante 1: --------------------
    #screen_px = ImageGrab.grab(bbox=(660, 70, 1260, 800 )).load()
    #screen_pic = ImageGrab.grab(bbox=(660, 70, 1260, 800 ))   # left, upper, right, lower

    #cropped_left = screen_pic.crop(box = (225, 590, 275, 625))
    #cropped_left_px = screen_pic.crop(box = (225, 590, 275, 625)).load()

    #cropped_right = screen_pic.crop(box = (325, 590, 375, 625))
    #cropped_right_px = screen_pic.crop(box = (325, 590, 375, 625)).load()


    #cropped_left_px = ImageGrab.grab(bbox=(885, 660, 935, 695)).load()
    #cropped_right_px = ImageGrab.grab(bbox=(985, 660, 1035, 695)).load()
    
    #cropped_left = ImageGrab.grab(bbox = (885, 660, 935, 695))
    #cropped_right = ImageGrab.grab(bbox = (985, 660, 1035, 695))
    '''
    flag = 0 # 1-left , 2-right, 0-nothing
    for y in range(35): 
        for x in range(25):
            if cropped_left_px[x,y][0]==wood[0]:
                flag = 1
                #cropped_right.show()
                #cropped_left.show()

    for y in range(35): 
        for x in range(50):
            if cropped_right_px[x,y][0]==wood[0]:
                flag = 2
                #cropped_right.show()
                #cropped_left.show()
    

    # Variante 2: --------------------
    screen_pic = ImageGrab.grab(bbox=(885, 660, 1035, 695)).load()
    for y in range(35):
        if screen_pic[15,y][0]==wood[0]:
            flag = 1
    for y in range(35):
        if screen_pic[115,y][0]==wood[0]:
            flag = 2

     if flag == 0:
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    elif flag == 1:
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    elif flag == 2:
        keyboard.press(Key.left)
        keyboard.release(Key.left) 
    '''
    #Variante 3: ------------------------
    time.sleep(0.015)
    screen_pic_px = ImageGrab.grab(bbox=(885, 200, 1035, 705)).load()
    '''
    if  screen_pic_px[15,75][0]==wood[0]:
        tree[10] = 1
    elif screen_pic_px[115,75][0]==wood[0]:
        tree[10] = 2
    else:
        tree[10] = 0
    '''

    if  screen_pic_px[15,118][0]==wood[0]:
        tree[9] = 1
    elif screen_pic_px[115,118][0]==wood[0]:
        tree[9] = 2
    else: tree[9] = 0

    if  screen_pic_px[15,159][0]==wood[0]:
        tree[8] = 1
    elif screen_pic_px[115,159][0]==wood[0]:
        tree[8] = 2
    else: tree[8] = 0

    if  screen_pic_px[15,200][0]==wood[0]:
        tree[7] = 1
    elif screen_pic_px[115,200][0]==wood[0]:
        tree[7] = 2
    else: tree[7] = 0

    if  screen_pic_px[15,242][0]==wood[0]:
        tree[6] = 1
    elif screen_pic_px[115,242][0]==wood[0]:
        tree[6] = 2
    else: tree[6] = 0

    if  screen_pic_px[15,283][0]==wood[0]:
        tree[5] = 1
    elif screen_pic_px[115,283][0]==wood[0]:
        tree[5] = 2
    else: tree[5] = 0

    if  screen_pic_px[15,325][0]==wood[0]:
        tree[4] = 1
    elif screen_pic_px[115,325][0]==wood[0]:
        tree[4] = 2
    else: tree[4] = 0

    if  screen_pic_px[15,368][0]==wood[0]:
        tree[3] = 1
    elif screen_pic_px[115,368][0]==wood[0]:
        tree[3] = 2
    else: tree[3] = 0

    if  screen_pic_px[15,408][0]==wood[0]:
        tree[2] = 1
    elif screen_pic_px[115,408][0]==wood[0]:
        tree[2] = 2
    else: tree[2] = 0


    if  screen_pic_px[15,451][0]==wood[0]:
        tree[1] = 1
    elif screen_pic_px[115,451][0]==wood[0]:
        tree[1] = 2
    else: tree[1] = 0

    if  screen_pic_px[15,492][0]==wood[0]:
        tree[0] = 1
    elif screen_pic_px[115,492][0]==wood[0]:
        tree[0] = 2
    else: tree[0] = 0



    for ctrl in tree:
        tmp = ctrl

        if prev == 2:
            tmp = 2
        if tmp == 0:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
        elif tmp == 1:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
        elif tmp == 2:
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        prev = ctrl
        time.sleep(0.015)

   # screen_pic = ImageGrab.grab(bbox=(885, 660, 1035, 695)).load()
  
    #pics.append(cropped_right)
    #pics.append(cropped_left)

    #print(flag)
    
   

    #i = i + 1

#for y in pics:
#    y.show() 



print("Ende")
input("Zum Beenden Enter Taste drücken")    

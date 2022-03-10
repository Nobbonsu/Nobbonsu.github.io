import os
from tkinter.filedialog import asksaveasfilename
import cv2
from tkinter import *
from PIL import Image, ImageTk, ImageEnhance
import tkinter as tk
from gtts import gTTS
from pytesseract import Output
import pytesseract
from pygame import mixer
from queue import Queue
import datetime


mixer.init()


def resize_frame(f, scale=1.40):
    width_3 = int(f.shape[1] * scale)
    height_4 = int(f.shape[0] * scale)
    dimension = (width_3, height_4)

    return cv2.resize(f, dimension, interpolation=cv2.INTER_CUBIC)


def update_image(image_label, cam):
    global frame
    (readSuccessful, f) = cam.read()
    frame = resize_frame(f)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    a = Image.fromarray(cv2image)
    b = ImageTk.PhotoImage(image=a)
    image_label.configure(image=b)
    image_label._image_cache = b  # avoid garbage collection
    root.update()


def ocr():
    mixer.music.load("snake sounds/camera-shutter-click.mp3")
    mixer.music.play()
    # Capturing the frame
    (readSuccessful, f) = cam.read()
    frame = resize_frame(f)

    img_name = "Captured Images/Opencv_frame_1.png".format(1)
    cv2.imwrite(img_name, frame)

    img = cv2.imread("Captured Images/Opencv_frame_1.png")
    img_rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite("Captured Images/Cropped Image.png", img_rotate_90)

    # # crop image
    img = cv2.imread("Captured Images/Cropped Image.png")
    cropped_image = img[30:1640, 0:1007]

    # Save the cropped image
    cv2.imwrite('Captured Images/Cropped Image.png', cropped_image)

    # load the cropped image
    img = Image.open('Captured Images/Cropped Image.png')

    # Enhance the image
    enhancer = ImageEnhance.Sharpness(img)
    enhancer.enhance(2).save('Captured Images/Cropped_Image1.png')

    # Open the image file
    image = cv2.imread("Captured Images/Cropped_Image1.png")

    # Adding custom option
    custom_config = r'--oem 3 --psm 6'

    # get grayscale image
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    bilateral_blur = cv2.bilateralFilter(gray, 10, 15, 20)
    # hImage, w1Image, _ = bilateral_blur.shape

    # Perform ocr on the image
    my_ocr = pytesseract.pytesseract.image_to_data(bilateral_blur, config=custom_config)
    ocr1 = pytesseract.pytesseract.image_to_string(bilateral_blur, config=custom_config, output_type=Output.DICT)
    lines = ocr1['text']

    # use the bounding boxes to extract word by word
    filewrite = open('string.txt', 'w')
    filewrite2 = open('string_audio.txt', 'w')
    for z, a in enumerate(my_ocr.splitlines()):
        if z != 0:
            a = a.split()
            if len(a) == 12:
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                cv2.rectangle(bilateral_blur, (x, y), (x + w, y + h), (255, 0, 0), 1)
                text_1 = a[11]
                print(text_1)
                filewrite2.write(a[11] + " ")
    filewrite2.close()
    filewrite.write(lines + " ")
    filewrite.close()
    fileread = open('string_audio.txt', 'r')
    lang = 'en'
    line = fileread.read()
    if line != " ":
        speech = gTTS(text=line, lang=lang, slow=False)
        speech.save('Temp_Audio/test.mp3')
    # cv2.imshow('image', bilateral_blur)
    # cv2.waitKey(0)


def save_picture():
    mixer.music.load("snake sounds/camera-shutter-click.mp3")
    mixer.music.play()
    # Capture and save the image
    (readSuccessful, f) = cam.read()
    frame = resize_frame(f)
    if readSuccessful:
        now = datetime.datetime.now()
        date = now.strftime('%Y%m%d')
        hour = now.strftime('%H%M%S')
        user_id = '00001'
        filename = 'gallery_Images/frame_{}_{}_{}.png'.format(date, hour, user_id)
        cv2.imwrite(filename, frame)
        image_queue.put_nowait(filename)


def save_text():
    file_name = asksaveasfilename(defaultextension='.txt',
                                  initialdir=r'/Users/mogpatechteam/PycharmProjects/pythonProject2/images',
                                  filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
                                  title='Save file')
    if file_name is None:
        return
    if file_name != "":
        with open("string.txt", "r") as text_file:
            text_reader = text_file.read()
            with open(file_name, "w") as my_file:
                csv_writer = my_file.write(text_reader)


def read_text():
    filename = 'python Capture_display.py'
    os.system(filename)


def toggle_win():
    f1 = Frame(root, width=800, height=100, bg="#12c4c0")
    f1.place(x=480, y=870)

    def bttn(x, y, text, image, cmd):
        global myButton1
        myButton1 = Button(f1, text=text,
                           image=image,
                           compound="top",
                           fg='#262626',
                           font=("Times_New_Roman", 15, "bold"),
                           command=cmd)
        myButton1.place(x=x, y=y)

    global ocr_img
    image4 = Image.open("icon/old-camera.jpg")
    image4 = image4.resize((120, 65), Image.ANTIALIAS)
    ocr_img = ImageTk.PhotoImage(image4)

    global save_img
    image = Image.open("icon/save.jpg")
    image = image.resize((120, 65), Image.ANTIALIAS)
    save_img = ImageTk.PhotoImage(image)

    global capture_img
    image = Image.open("icon/capture.jpg")
    image = image.resize((120, 65), Image.ANTIALIAS)
    capture_img = ImageTk.PhotoImage(image)

    global play_img
    image = Image.open("icon/play.jpg")
    image = image.resize((120, 65), Image.ANTIALIAS)
    play_img = ImageTk.PhotoImage(image)

    bttn(30, 5, 'OCR', ocr_img, ocr)
    bttn(200, 5, "SAVE", save_img, save_text)
    bttn(470, 5, 'CAPTURE', capture_img, save_picture)
    bttn(650, 5, 'PLAY OCR', play_img, read_text)

    def dele():
        f1.destroy()

    global img2
    image3 = Image.open("icon/close.jpg")
    image3 = image3.resize((50, 30), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(image3)

    Button(f1, image=img2, text="close", border=0, activebackground="#12c4c0", bg="#12c4c0", command=dele).place(x=370, y=0)


def update_all(root, image_label, cam):
    update_image(image_label, cam)
    root.after(20, func=lambda: update_all(root, image_label, cam))


def mouse_callback(self, event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        ocr()
    elif event == cv2.EVENT_RBUTTONDOWN:
        read_text()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("OPTOSOL OCR")
    root.geometry("1795x980")
    image_label = tk.Label(master=root)  # label for the video frame
    image_label.pack()
    cam = cv2.VideoCapture(2)

    image_queue = Queue()
    # root.bind("<space>", ocr)
    # root.bind("c", save_picture)
    # root.bind("s", save_text)
    # root.bind("r", read_text)

    image1 = Image.open("icon/open.png")
    image1 = image1.resize((50, 30), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(image1)
    Button(root, command=toggle_win, image=img1, text="open").place(x=850, y=935)

    # setup the update callback
    root.after(0, func=lambda: update_all(root, image_label, cam))
    root.mainloop()

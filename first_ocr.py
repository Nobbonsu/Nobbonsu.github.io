import cv2
import time
import os
from threading import Thread
from gtts import gTTS
from pytesseract import Output
import pytesseract
from pygame import mixer
from queue import Queue
import datetime
from PIL import Image, ImageEnhance
import tkinter.filedialog


def resize_frame(frame, scale=1.5):
    width_3 = int(frame.shape[1] * scale + 100)
    height_4 = int(frame.shape[0] * scale)
    dimension = (width_3, height_4)

    return cv2.resize(frame, dimension, interpolation=cv2.INTER_CUBIC)


def save_text():
    file_name = tkinter.filedialog.asksaveasfilename(defaultextension='.txt',
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


class Camera:
    def __init__(self):
        self.data = None
        self.cam = cv2.VideoCapture(2)

        self.WIDTH = 1980
        self.HEIGHT = 1080

        self.center_x = self.WIDTH / 2
        self.center_y = self.HEIGHT / 2
        self.touched_zoom = False

        self.image_queue = Queue()
        self.video_queue = Queue()

        self.scale = 1
        self.color = 1
        self.__setup()

        self.recording = False

    def __setup(self):
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, self.WIDTH)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.HEIGHT)
        time.sleep(2)

    def get_location(self, x, y):
        self.center_x = x
        self.center_y = y
        self.touched_zoom = True

    def stream(self):
        # streaming thread
        def streaming():
            #
            self.ret = True
            while self.ret:
                self.ret, np_image = self.cam.read()
                if np_image is None:
                    continue
                if self.touched_zoom:
                    np_image = self.__zoom(np_image, (self.center_x, self.center_y))
                else:
                    if not self.scale == 1:
                        np_image = self.__zoom(np_image)
                self.data = np_image
                k = cv2.waitKey(1)
                if k == ord('q'):
                    self.release()
                    break

        Thread(target=streaming).start()

    def ocr(self):
        mixer.init()
        mixer.music.load("snake sounds/camera-shutter-click.mp3")
        mixer.music.play()
        # Capturing the frame
        frame = self.data
        frame = resize_frame(frame)

        img_name = "Captured Images/Opencv_frame_1.png".format(1)
        cv2.imwrite(img_name, frame)

        img = cv2.imread("Captured Images/Opencv_frame_1.png")
        img_rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite("Captured Images/Cropped Image.png", img_rotate_90)

        # # crop image
        img = cv2.imread("Captured Images/Cropped Image.png")
        cropped_image = img[30:1700, 0:1080]

        # Save the cropped image
        cv2.imwrite('Captured Images/Cropped Image.png', cropped_image)

        # load the cropped image
        img = Image.open(r'Captured Images/Cropped Image.png')

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

    def readText(self):
        filename = 'python Capture_display.py'
        os.system(filename)

    def save_picture(self):
        mixer.init()
        mixer.music.load("snake sounds/camera-shutter-click.mp3")
        mixer.music.play()
        # Capture and save the image
        frame = self.data
        frame = resize_frame(frame)
        if frame is not None:
            now = datetime.datetime.now()
            date = now.strftime('%Y%m%d')
            hour = now.strftime('%H%M%S')
            user_id = '00001'
            filename = 'gallery_Images/frame_{}_{}_{}.png'.format(date, hour, user_id)
            cv2.imwrite(filename, frame)
            self.image_queue.put_nowait(filename)

    def __zoom(self, img, center=None):
        # zoom
        height, width = img.shape[:2]
        if center is None:
            #
            center_x = int(width / 2)
            center_y = int(height / 2)
            radius_x, radius_y = int(width / 2), int(height / 2)
        else:
            #
            rate = height / width
            center_x, center_y = center

            #
            if center_x < width * (1 - rate):
                center_x = width * (1 - rate)
            elif center_x > width * rate:
                center_x = width * rate
            if center_y < height * (1 - rate):
                center_y = height * (1 - rate)
            elif center_y > height * rate:
                center_y = height * rate

            center_x, center_y = int(center_x), int(center_y)
            left_x, right_x = center_x, int(width - center_x)
            up_y, down_y = int(height - center_y), center_y
            radius_x = min(left_x, right_x)
            radius_y = min(up_y, down_y)

        #  zoom
        radius_x, radius_y = int(self.scale * radius_x), int(self.scale * radius_y)

        # size
        min_x, max_x = center_x - radius_x, center_x + radius_x
        min_y, max_y = center_y - radius_y, center_y + radius_y

        # size
        cropped = img[min_y:max_y, min_x:max_x]
        #
        new_cropped = cv2.resize(cropped, (width, height))

        return new_cropped

    def touch_init(self):
        self.center_x = self.WIDTH / 2
        self.center_y = self.HEIGHT / 2
        self.touched_zoom = False
        self.scale = 1

    def zoom_out(self):
        # scale to zoom-out
        if self.scale < 1:
            self.scale += 0.1
        if self.scale == 1:
            self.center_x = self.WIDTH
            self.center_y = self.HEIGHT
            self.touched_zoom = False

    def zoom_in(self):
        # scale to zoom-in
        if self.scale > 0.2:
            self.scale -= 0.1

    def zoom(self, num):
        if num == 0:
            self.zoom_in()
        elif num == 1:
            self.zoom_out()
        elif num == 2:
            self.touch_init()

    def change(self):
        if self.color == 1 or self.color > 1:
            self.color += 1
        if self.color == 5:
            self.color = 1

    def change_back(self):
        if self.color > 1:
            self.color -= 1

    def show(self):
        while True:
            frame = self.data
            if frame is not None:
                frame_1 = resize_frame(frame)
                cv2.imshow('OPTOSOL OPTICAL CHARACTER RECOGNITION (OCR)', frame_1)
                cv2.setMouseCallback('OPTOSOL OPTICAL CHARACTER RECOGNITION (OCR)', self.mouse_callback)
            key = cv2.waitKey(1)
            if key % 256 == 27:
                # q : close
                self.release()
                cv2.destroyAllWindows()
                break

            elif key == ord('z') or key == ord('Z'):
                # z : zoom - in
                self.zoom_in()

            elif key == ord('x') or key == ord('X'):
                # x : zoom - out
                self.zoom_out()

            elif key % 256 == 32:
                self.save_picture()

            elif key == ord('b') or key == ord('B'):
                save_text()

            elif key == ord('v') or key == ord('V'):
                # v : zoom original frame
                self.touch_init()

    def release(self):
        self.cam.release()
        cv2.destroyAllWindows()

    def mouse_callback(self, event, flag, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.ocr()
            # print("performing ocr")
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.readText()
            # print("showing text")


if __name__ == '__main__':
    cam = Camera()
    cam.stream()
    cam.show()

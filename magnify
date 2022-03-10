import cv2
import time
from threading import Thread
from queue import Queue
from numpy import uint8
from numpy import array


def resize_frame(frame, scale=1.5):
    width_3 = int(frame.shape[1] * scale + 100)
    height_4 = int(frame.shape[0] * scale)
    dimension = (width_3, height_4)

    return cv2.resize(frame, dimension, interpolation=cv2.INTER_CUBIC)


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
            if center_x < width * (1-rate):
                center_x = width * (1-rate)
            elif center_x > width * rate:
                center_x = width * rate
            if center_y < height * (1-rate):
                center_y = height * (1-rate)
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
        # kernel = np.array([[0, -1, 0],
        #                    [-1, 5, -1],
        #                    [0, -1, 0]])
        # cropped = cv2.filter2D(src=my_cropped, ddepth=-1, kernel=kernel)
        # new_cropped = cv2.bilateralFilter(cropped, 10, 15, 20)
        # new_cropped = ImageEnhance.Sharpness(new_cropped)
        # new_cropped = new_cropped.enhance(2)

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

    def color_inversion(self, frame):
        if self.color == 1:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if self.color == 2:
            thresh, threading = cv2.threshold(frame, 150, 255, cv2.THRESH_BINARY)
            image = cv2.cvtColor(threading, cv2.COLOR_RGB2GRAY)
            maxIntensity = 255.0  # depends on dtype of image data
            # Parameters for manipulating image data
            phi = 1
            theta = 1
            newImage1 = (maxIntensity / phi) * (image / (maxIntensity / theta)) ** 1

            image = array(newImage1, dtype=uint8)
            cv2image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
        if self.color == 3:
            thresh, threading = cv2.threshold(frame, 150, 255, cv2.THRESH_BINARY)
            image = cv2.cvtColor(threading, cv2.COLOR_RGB2GRAY)
            maxIntensity = 255.0  # depends on dtype of image data
            # Parameters for manipulating image data
            phi = 1
            theta = 1
            newImage1 = (maxIntensity / phi) * (image / (maxIntensity / theta)) ** 1

            image = array(newImage1, dtype=uint8)
            run = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
            cv2image = cv2.bitwise_not(run)
        if self.color == 4:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
            maxIntensity = 255.0  # depends on dtype of image data
            # Parameters for manipulating image data
            phi = 1
            theta = 1
            newImage1 = (maxIntensity / phi) * (image / (maxIntensity / theta)) ** 1
            hsv_image = array(newImage1, dtype=uint8)
            thresh, cv2image = cv2.threshold(hsv_image, 200, 255, cv2.THRESH_BINARY)
        if self.color == 5:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2YCR_CB)
            thresh, c = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
            cv2image = cv2.bitwise_not(c)
        return cv2image

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
                img = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
                # kernel = np.array([[0, -1, 0],
                #                    [-1, 5, -1],
                #                    [0, -1, 0]])
                # image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
                cv2.imshow('OPTOSOL MAGNIFIER', self.color_inversion(img))
                cv2.setMouseCallback('OPTOSOL MAGNIFIER', self.mouse_callback)
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
                self.change()

            elif key == ord('n') or key == ord('N'):
                self.change_back()

            elif key == ord('v') or key == ord('V'):
                # v : zoom original frame
                self.touch_init()

    def release(self):
        self.cam.release()
        cv2.destroyAllWindows()

    def mouse_callback(self, event, x, y, flag, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            # self.get_location(x, y)
            self.zoom_in()
            # print("zoom in")
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.zoom_out()
            # print("zoom out")


if __name__ == '__main__':
    cam = Camera()
    cam.stream()
    cam.show()

import cv2


class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename, 'r')

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()


class CustomWrite(object):
    def __init__(self, filename):
        self.filewrite = open(filename, 'w')

    def __enter__(self):
        return self.filewrite

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.filewrite.close()


def resize_frame(frame, scale=1.5):
    width_3 = int(frame.shape[1] * scale + 200)
    height_4 = int(frame.shape[0] * scale)
    dimension = (width_3, height_4)

    return cv2.resize(frame, dimension, interpolation=cv2.INTER_CUBIC)



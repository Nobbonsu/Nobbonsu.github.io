from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import os
import sys
import pyttsx3
import pdfplumber
import PyPDF2
from pygame import mixer
from PIL import Image, ImageTk


mixer.init()


def sayOCR(event):
    mixer.music.load("snake sounds/OCR.mp3")
    mixer.music.play()


def sayMagnify(event):
    mixer.music.load("snake sounds/magnify.mp3")
    mixer.music.play()


def sayAudio(event):
    mixer.music.load("snake sounds/audio.mp3")
    mixer.music.play()


def sayAudioBook(event):
    mixer.music.load("snake sounds/audioBook.mp3")
    mixer.music.play()


def sayGallery(event):
    mixer.music.load("snake sounds/gallery.mp3")
    mixer.music.play()


def sayLoad(event):
    mixer.music.load("snake sounds/load.mp3")
    mixer.music.play()


def saySave(event):
    mixer.music.load("snake sounds/save.mp3")
    mixer.music.play()


def saySettings(event):
    mixer.music.load("snake sounds/settings.mp3")
    mixer.music.play()


def start_camera():
    filename = 'python Optosol_ocr.py'
    os.system(filename)


def start_magnifier():
    filename = 'python Optosol_magnifier.py'
    os.system(filename)


def load_text():
    text_file = filedialog.askopenfilename(initialdir='/Users/mogpatechteam/PycharmProjects/pythonProject2/images',
                                           title='Select a text file')
    if text_file is None:
        return
    if text_file != '':
        with open(text_file, 'r') as f:
            lines = f.read()
            original_stdout = sys.stdout
            with open('load_text', 'w') as file:
                for key, val in enumerate(lines.split(), start=1):
                    sys.stdout = file
                    if key % 4 == 0:
                        print(val, end='\n\n')
                    else:
                        print(val, end=' ')
                    sys.stdout = original_stdout
            original_stdout = sys.stdout
            with open('load_text_1', 'w') as file:
                for key, val in enumerate(lines.split(), start=1):
                    sys.stdout = file
                    if key % 3 == 0:
                        print(val, end='\n\n')
                    else:
                        print(val, end=' ')
                    sys.stdout = original_stdout
            original_stdout = sys.stdout
            with open('load_text_2', 'w') as file:
                for key, val in enumerate(lines.split(), start=1):
                    sys.stdout = file
                    if key % 2 == 0:
                        print(val, end='\n\n')
                    else:
                        print(val, end=' ')
                    sys.stdout = original_stdout
        filename = 'python Load_display.py'
        os.system(filename)


# save text to file
def save_text():
    # open a file
    file_name = asksaveasfilename(defaultextension='.txt',
                                  initialdir=r'/Users/mogpatechteam/PycharmProjects/pythonProject2/images',
                                  filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
                                  title='Save file')
    # check if file exist
    if file_name is None:
        return
    if file_name != "":
        # open the file from dir
        with open("string.txt", "r") as text_file:
            # read the content
            text_reader = text_file.read()
            # write the content to the opened file
            with open(file_name, "w") as my_file:
                csv_writer = my_file.write(text_reader)


# def open_gallery():
def openGallery():
    filename = 'python gallery.py'
    os.system(filename)


# load pdf file and convert to audio
def audioBook():
    file = filedialog.askopenfilename(initialdir='/Users/mogpatechteam/PycharmProjects/pythonProject2',
                                      title='Select a pdf file')
    # check if file exist
    if file is None:
        return
    if file != '':
        # Create a Pdf file object
        pdfFileObj = open(file, 'rb')

        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        pages = pdfReader.numPages

        speaker = pyttsx3.init()

        # Create a pdfPlumber object and loop through the number of pages in PDF file
        with pdfplumber.open(file) as pdf:
            for i in range(0, pages):
                page = pdf.pages[i]
                text = page.extract_text()
                print(text)
                speaker.say(text)
                speaker.save_to_file(text, 'text.mp3')


def widget():
    # create a photo image for the buttons
    # camera button photo image
    global camera
    image = Image.open("icon/old-camera.jpg")
    image = image.resize((400, 350), Image.ANTIALIAS)
    camera = ImageTk.PhotoImage(image)

    # magnify button photo image
    global magnify
    image = Image.open("icon/magnifier.png")
    image = image.resize((400, 350), Image.ANTIALIAS)
    magnify = ImageTk.PhotoImage(image)

    # audio button photo image
    global audio
    image = Image.open("icon/audio.jpg")
    image = image.resize((400, 350), Image.ANTIALIAS)
    audio = ImageTk.PhotoImage(image)

    # audioBook button photo image
    global book
    image = Image.open("icon/book.jpg")
    image = image.resize((400, 350), Image.ANTIALIAS)
    book = ImageTk.PhotoImage(image)

    # save button photo image
    global save
    image = Image.open("icon/save.jpg")
    image = image.resize((400, 350), Image.ANTIALIAS)
    save = ImageTk.PhotoImage(image)

    # setting button photo image
    global setting
    image = Image.open("icon/settings.jpg")
    image = image.resize((400, 350), Image.ANTIALIAS)
    setting = ImageTk.PhotoImage(image)

    # gallery button photo image
    global gallery
    image = Image.open("icon/gallery.jpg")
    image = image.resize((400, 350), Image.ANTIALIAS)
    gallery = ImageTk.PhotoImage(image)

    # load button photo image
    global load
    image = Image.open("icon/load.jpg")
    image = image.resize((400, 350), Image.ANTIALIAS)
    load = ImageTk.PhotoImage(image)

    # create a label for the title
    label = Label(window, text="OPTOSOL iDIGITAL", font=("Times_New_Roman", 30, "bold"), fg="black")
    label.grid(row=0, column=1, columnspan=4)

    #
    button_camera = Button(window, text="OCR", bg="yellow", font=("Times_New_Roman", 30, "bold"), image=camera,
                           compound="top",
                           command=start_camera)
    button_camera.bind("<Enter>", sayOCR)
    button_camera.grid(row=1, column=1, padx=20, pady=20)

    button_magnify = Button(window, text="MAGNIFY", bg="yellow", font=("Times_New_Roman", 30, "bold"),
                            image=magnify,
                            compound="top",
                            command=start_magnifier)
    button_magnify.bind("<Enter>", sayMagnify)
    button_magnify.grid(row=1, column=2, padx=20, pady=20)

    button_audio = Button(window, text="AUDIO", bg="yellow", font=("Times_New_Roman", 30, "bold"), image=audio,
                          compound="top")
    button_audio.bind("<Enter>", sayAudio)
    button_audio.grid(row=1, column=3, padx=20, pady=20)

    button_book = Button(window, text="BOOKS", bg="yellow", font=("Times_New_Roman", 30, "bold"), image=book,
                         compound="top", command=audioBook)
    button_book.bind("<Enter>", sayAudioBook)
    button_book.grid(row=1, column=4, padx=20, pady=20)

    button_load = Button(window, text="LOAD", bg="yellow", font=("Times_New_Roman", 30, "bold"), image=load,
                         compound="top",
                         command=load_text)
    button_load.bind("<Enter>", sayLoad)
    button_load.grid(row=2, column=1, padx=20, pady=20)

    button_save = Button(window, text="SAVE", bg="yellow", font=("Times_New_Roman", 30, "bold"), image=save,
                         compound="top",
                         command=save_text)
    button_save.bind("<Enter>", saySave)
    button_save.grid(row=2, column=2, padx=20, pady=20)

    button_gallery = Button(window, text="GALLERY", bg="yellow", font=("Times_New_Roman", 30, "bold"),
                            image=gallery,
                            compound="top",
                            command=openGallery)
    button_gallery.bind("<Enter>", sayGallery)
    button_gallery.grid(row=2, column=3, padx=20, pady=20)

    button_setting = Button(window, text="SETTINGS", bg="yellow", font=("Times_New_Roman", 30, "bold"),
                            image=setting,
                            compound="top")
    button_setting.bind("<Enter>", saySettings)
    button_setting.grid(row=2, column=4, padx=20, pady=20)


if __name__ == "__main__":
    # create a window
    window = Tk()
    window.geometry("1795x980")
    window.title("OPTOSOL")

    # load the widget into the mainLoop
    widget()

    window.mainloop()

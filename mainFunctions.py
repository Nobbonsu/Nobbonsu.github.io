import TextLoad
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer
import pdfplumber
import sys
import os
from gtts import gTTS
from tkinter.filedialog import asksaveasfilename


def load_text():
    text_file = filedialog.askopenfilename(
        initialdir='../saved text',
        title='Select a text file')
    if text_file is None:
        return
    if text_file != '':
        with TextLoad.CustomOpen(text_file) as f:
            lines = f.read()
            original_stdout = sys.stdout
            with TextLoad.CustomWrite('load_text') as file:
                for key, val in enumerate(lines.split(), start=1):
                    sys.stdout = file
                    if key % 4 == 0:
                        print(val, end='\n\n')
                    else:
                        print(val, end=' ')
                    sys.stdout = original_stdout
            original_stdout = sys.stdout
            with TextLoad.CustomWrite('load_text_1') as file:
                for key, val in enumerate(lines.split(), start=1):
                    sys.stdout = file
                    if key % 3 == 0:
                        print(val, end='\n\n')
                    else:
                        print(val, end=' ')
                    sys.stdout = original_stdout
            original_stdout = sys.stdout
            with TextLoad.CustomWrite('load_text_2') as file:
                for key, val in enumerate(lines.split(), start=1):
                    sys.stdout = file
                    if key % 2 == 0:
                        print(val, end='\n\n')
                    else:
                        print(val, end=' ')
                    sys.stdout = original_stdout
            try:
                with TextLoad.CustomOpen(text_file) as play:
                    text_play = play.read().replace("\n", " ")
                    lang = 'en'
                    speech = gTTS(text=text_play, lang=lang, slow=False)
                    speech.save('Temp_Audio/load_text.mp3')
            except:
                messagebox.showinfo('Return', 'Connect to Internet to play audio', icon='warning')
        filename = 'python Load_display.py'
        os.system(filename)


# save text to file
def save_text():
    # open a file
    file_name = asksaveasfilename(defaultextension='.txt',
                                  initialdir='../saved text',
                                  filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
                                  title='DO YOU WANT TO SAVE THE TEXT')
    # check if file exist
    if file_name is None:
        return
    if file_name != "":
        # open the file from dir
        with TextLoad.CustomOpen("string.txt") as text_file:
            # read the content
            text_reader = text_file.read()
            # write the content to the opened file
            with TextLoad.CustomWrite(file_name) as my_file:
                csv_writer = my_file.write(text_reader)
                print(csv_writer)


# load pdf file and convert to audio
def audioBook():
    text_file = filedialog.askopenfilename(
        initialdir='../saved text',
        title='Select a pdf file')
    if text_file is None:
        return
    if text_file != '':
        with pdfplumber.open(text_file) as pdf:
            pages = pdf.pages
            for i, pg in enumerate(pages):
                page = pages[i].extract_text()
                lang = 'en'
                speech = gTTS(text=page, lang=lang, slow=False)
    file_name = asksaveasfilename(defaultextension='.mp3',
                                  initialdir='../AudioBooks',
                                  filetypes=(("Text files", "*.mp3"), ("All files", "*.*")),
                                  title='SAVE AUDIO')
    # check if file exist
    if file_name is None:
        return
    if file_name != "":
        speech.save(file_name)


def openGallery():
    filename = 'python gallery.py'
    os.system(filename)


# def open_gallery():
def myAudio():
    # import audioLoad
    # audioLoad.main()
    filename = 'python audioLoad.py'
    os.system(filename)


def start_camera():
    import Optosol_ocr
    Optosol_ocr.main()
    # filename = 'python Optosol_ocr.py'
    # os.system(filename)


def start_magnifier():
    import Optosol_magnifier
    Optosol_magnifier.main()
    # filename = 'python Optosol_magnifier.py'
    # os.system(filename)


def sayOCR(evnet):
    mixer.init()
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


def playsound():
    mixer.init()
    mixer.music.load("snake sounds/saving text.mp3")
    mixer.music.play()


def readText():
    filename = 'python Capture_display.py'
    os.system(filename)

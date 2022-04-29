import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
from pygame import mixer
from PIL import Image, ImageTk

import TextLoad
import mainFunctions

mixer.init()


# def voice_assistance():
#
#     while 1:
#         # get the voice input
#         voice_data = Constants.record_audio()
#         # response
#         Constants.response(voice_data)


try:
    def askYesNo():
        MsgBox = messagebox.askquestion('SAVE TEXT', 'DO YOU WANT TO SAVE THE TEXT')
        if MsgBox == 'yes':
            with TextLoad.CustomOpen("string.txt") as text_file:
                text_reader = text_file.read()
                now = datetime.datetime.now()
                date = now.strftime('%Y%m%d')
                hour = now.strftime('%H%M%S')
                user_id = '00001'
                filename = 'save text/TEXT_{}_{}_{}.txt'.format(date, hour, user_id)
                with TextLoad.CustomWrite(filename) as my_file:
                    csv_writer = my_file.write(text_reader)
                    print(csv_writer)
            mixer.init()
            mixer.music.load("snake sounds/text saved.mp3")
            mixer.music.play()
        else:
            messagebox.showinfo('Return', 'Your text will not be saved', icon='warning')

except NameError as e:
    print("error code")


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.speak = None
        self.win3 = None
        self.win2 = None
        self.gallery = None
        self.save = None
        self.load = None
        self.book = None
        self.audio = None
        self.setting = None
        self.button_frame0 = None
        self.button_gallery = None
        self.button_save = None
        self.button_load = None
        self.button_audioBook = None
        self.button_settings = None
        self.button_audio = None
        self.magnify = None
        self.button_magnify = None
        self.camera = None
        self.button_camera = None
        self.win2_status = 0  # to open the new window once
        self.setup_frames()
        self.setup_button()

    def setup_frames(self):
        # frame for button --------------- frame 0 / button
        self.button_frame0 = ttk.LabelFrame(self, text="OPTOSOL SOLUTIONS")
        self.button_frame0.grid(
            row=0, column=0, padx=(5, 10), pady=(5, 10), sticky="nsew")

    def setup_button(self):
        image = Image.open("icon/camera1.png")
        image = image.resize((400, 350), Image.ANTIALIAS)
        self.camera = ImageTk.PhotoImage(image)
        self.button_camera = ttk.Button(
            self.button_frame0, image=self.camera,
            text="OCR",
            style="Accent.TButton",
            compound="top",
            command=mainFunctions.start_camera)
        self.button_camera.bind("<Enter>", mainFunctions.sayOCR)
        self.button_camera.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

        image = Image.open("icon/Look-icon.png")
        image = image.resize((400, 350), Image.ANTIALIAS)
        self.magnify = ImageTk.PhotoImage(image)
        self.button_magnify = ttk.Button(
            self.button_frame0, image=self.magnify,
            text="MAGNIFY",
            style="Accent.TButton",
            compound="top",
            command=mainFunctions.start_magnifier)
        self.button_magnify.bind("<Enter>", mainFunctions.sayMagnify)
        self.button_magnify.grid(row=2, column=2, padx=20, pady=20, sticky="nsew")

        image = Image.open("icon/audio.png")
        image = image.resize((400, 350), Image.ANTIALIAS)
        self.audio = ImageTk.PhotoImage(image)
        self.button_audio = ttk.Button(
            self.button_frame0, image=self.audio,
            text="AUDIO",
            style="Accent.TButton",
            compound="top",
            command=mainFunctions.myAudio)
        self.button_audio.bind("<Enter>", mainFunctions.sayAudio)
        self.button_audio.grid(row=2, column=3, padx=20, pady=20, sticky="nsew")

        image = Image.open("icon/book-icon.png")
        image = image.resize((400, 350), Image.ANTIALIAS)
        self.book = ImageTk.PhotoImage(image)
        self.button_audioBook = ttk.Button(
            self.button_frame0, image=self.book,
            text="AUDIOBOOK",
            style="Accent.TButton",
            compound="top",
            command=mainFunctions.audioBook)
        self.button_audioBook.bind("<Enter>", mainFunctions.sayAudioBook)
        self.button_audioBook.grid(row=2, column=4, padx=20, pady=20, sticky="nsew")

        image = Image.open("icon/file load.png")
        image = image.resize((400, 350), Image.ANTIALIAS)
        self.load = ImageTk.PhotoImage(image)
        self.button_load = ttk.Button(
            self.button_frame0, image=self.load,
            text="LOAD",
            style="Accent.TButton",
            compound="top",
            command=mainFunctions.load_text)
        self.button_load.bind("<Enter>", mainFunctions.sayLoad)
        self.button_load.grid(row=3, column=1, padx=20, pady=10, sticky="nsew")

        image = Image.open("icon/save1.png")
        image = image.resize((400, 350), Image.ANTIALIAS)
        self.save = ImageTk.PhotoImage(image)
        self.button_save = ttk.Button(
            self.button_frame0, image=self.save,
            text="SAVE",
            style="Accent.TButton",
            compound="top",
            command=mainFunctions.save_text)
        self.button_save.bind("<Enter>", mainFunctions.saySave)
        self.button_save.grid(row=3, column=2, padx=20, pady=10, sticky="nsew")

        image = Image.open("icon/gallery2.png")
        image = image.resize((400, 350), Image.ANTIALIAS)
        self.gallery = ImageTk.PhotoImage(image)
        self.button_gallery = ttk.Button(
            self.button_frame0, image=self.gallery,
            text="GALLERY",
            style="Accent.TButton",
            compound="top",
            command=mainFunctions.openGallery)
        self.button_gallery.grid(row=3, column=3, padx=20, pady=10, sticky="nsew")
        self.button_gallery.bind("<Enter>", mainFunctions.sayGallery)

        image = Image.open("icon/setting.png")
        image = image.resize((400, 350), Image.ANTIALIAS)
        self.setting = ImageTk.PhotoImage(image)
        self.button_settings = ttk.Button(
            self.button_frame0, image=self.setting,
            text="SETTINGS",
            style="Accent.TButton",
            compound="top")
        self.button_settings.grid(row=3, column=4, padx=20, pady=10, sticky="nsew")
        self.button_settings.bind("<Enter>", mainFunctions.saySettings)

        # image = Image.open("icon/conductor-icon.png")
        # image = image.resize((100, 100), Image.ANTIALIAS)
        # self.speak = ImageTk.PhotoImage(image)
        # self.button_settings = ttk.Button(
        #     self.button_frame0, image=self.speak,
        #     command=voice_assistance,
        #     style="Accent.TButton", )
        # self.button_settings.grid(row=4, column=2, columnspan=2, padx=20, pip install requests
        # pady=0, sticky="nsew")
        # self.button_settings.bind("<Enter>", saySettings)


def main():
    root = tk.Tk()
    root.title("OPTOSOL iDIGITAL")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    root.mainloop()


if __name__ == "__main__":
    main()

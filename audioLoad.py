import os
from tkinter import *
from tkinter.filedialog import askdirectory
import pygame
from pygame import mixer
from PIL import Image, ImageTk

mixer.init()


class MusicPlayer:
    def __init__(self, window):
        self.playlist = None
        window.geometry('1480x740')
        window.title('Optosol Player')

        image = Image.open("icon/play.png")
        image = image.resize((150, 120), Image.ANTIALIAS)
        self.play_image = ImageTk.PhotoImage(image)
        image = Image.open("icon/load.jpg")
        image = image.resize((180, 120), Image.ANTIALIAS)
        self.load_image = ImageTk.PhotoImage(image)
        image = Image.open("icon/pause.png")
        image = image.resize((150, 120), Image.ANTIALIAS)
        self.pause_image = ImageTk.PhotoImage(image)
        image = Image.open("icon/stop.png")
        image = image.resize((150, 120), Image.ANTIALIAS)
        self.stop_image = ImageTk.PhotoImage(image)
        image = Image.open("icon/next.png")
        image = image.resize((150, 120), Image.ANTIALIAS)
        self.next_image = ImageTk.PhotoImage(image)
        image = Image.open("icon/previous.png")
        image = image.resize((150, 120), Image.ANTIALIAS)
        self.prev_image = ImageTk.PhotoImage(image)
        Load = Button(window, text='Load', font=('Times', 25, "bold"), command=self.load, compound="top", image=self.load_image)
        Play = Button(window, text='Play', font=('Times', 25, "bold"), command=self.play, compound="top", image=self.play_image)
        Pause = Button(window, text='Pause', font=('Times', 25, "bold"), command=self.pause, compound="top", image=self.pause_image)
        Stop = Button(window, text='Stop', font=('Times', 25, "bold"), command=self.stop, compound="top", image=self.stop_image)

        Load.grid(row=0, column=1, columnspan=3, pady=10)
        Play.grid(row=1, column=1, padx=10, pady=10)
        Pause.grid(row=1, column=2, padx=10, pady=10)
        Stop.grid(row=1, column=3, padx=10, pady=10)
        self.music_file = False
        self.playing_state = False

        songsFrame = LabelFrame(window, text="PlayList", font=("times new roman", 20, "bold"))
        songsFrame.grid(row=2, column=1, columnspan=3)

        self.scrol_y = Scrollbar(songsFrame, orient=VERTICAL)
        self.play_list = Listbox(songsFrame, yscrollcommand=self.scrol_y.set, width=86, font=("Helvetica", 30, "bold"), bg="yellow", selectmode=SINGLE)
        self.var = StringVar()

        self.scrol_y.pack(side=RIGHT, fill=Y)
        self.scrol_y.config(command=self.play_list.yview)
        self.song_title = Label(window, font=("Helvetica", 50, "bold"), textvariable=self.var)
        self.play_list.pack(fill=BOTH)

    def load(self):
        self.music_file = askdirectory(initialdir=r'/Users/mogpatechteam/PycharmProjects/pythonProject2/AudioBooks')
        if self.music_file is None:
            return
        if self.music_file != "":
            os.chdir(self.music_file)
            song_list = os.listdir()

            for item in song_list:
                pos = 0
                self.play_list.insert(pos, item)
                pos += 1

    def play(self):
        pygame.mixer.music.load(self.play_list.get(ACTIVE))
        self.var.set(self.play_list.get(ACTIVE))
        pygame.mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()


def main():
    root = Tk()
    app = MusicPlayer(root)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))
    root.mainloop()


if __name__ == "__main__":
    main()

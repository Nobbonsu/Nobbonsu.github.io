from tkinter import *
import os
from PIL import Image, ImageTk

root = Tk()
root.title("Gallery")
root.configure(background='black')

size = (1674, 931)

defaultFolder = "gallery_Images"
path = defaultFolder

imageExtension = ('png', 'jpg', 'jpeg', 'gif')
imageList = [file for file in os.listdir(path) if file.endswith(imageExtension)]

img = Image.open(path + '/' + imageList[0])

labelImage = ImageTk.PhotoImage(img)
rootLabel = Label(image=labelImage)
rootLabel.grid(row=0, column=0, columnspan=3)

cnt = 0


def prevBn():
    global cnt
    global img
    global rootLabel

    rootLabel.grid_forget()
    prevButton.grid_forget()
    nextButton.grid_forget()

    cnt -= 1

    if cnt < 0:
        cnt = len(imageList) - 1

    img = Image.open(path + '/' + imageList[cnt])
    img.thumbnail(size)

    labelImage = ImageTk.PhotoImage(img)
    rootLabel = Label(image=labelImage)

    rootLabel.img = labelImage

    rootLabel.grid(row=0, column=0, columnspan=3)
    prevButton.grid(row=1, column=0, pady=0)
    nextButton.grid(row=1, column=2, pady=0)


def nextBn():
    global cnt
    global img
    global rootLabel

    rootLabel.grid_forget()
    prevButton.grid_forget()
    nextButton.grid_forget()

    cnt += 1

    if cnt == len(imageList):
        cnt = 0

    img = Image.open(path + '/' + imageList[cnt])
    img.thumbnail(size)

    labelImage = ImageTk.PhotoImage(img)
    rootLabel = Label(image=labelImage)

    rootLabel.img = labelImage

    rootLabel.grid(row=0, column=0, columnspan=3)
    prevButton.grid(row=1, column=0, pady=0)
    nextButton.grid(row=1, column=2, pady=0)


# Buttons
prevButton = Button(root, text='<<<<<<<<<<', width=40, height=2, command=prevBn)
nextButton = Button(root, text='>>>>>>>>>>', width=40, height=2, command=nextBn)

# Button grid
prevButton.grid(row=1, column=0, pady=0)
nextButton.grid(row=1, column=2, pady=0)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

root.mainloop()

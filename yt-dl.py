from tkinter import *
from tkinter import filedialog

from pytube import YouTube


def getFolder():
    global folderDir
    filename = filedialog.askdirectory()
    folderDir.set(filename)
    print(filename)


def popupmsg(msg):
    popup = Tk()
    popup.title("Download status")
    Label(popup, text=msg).pack()
    Button(popup, text="okay", command=popup.destroy).pack()
    popup.mainloop()


def downloadVideo():
    yt = YouTube(url.get())
    ss = yt.streams.get_highest_resolution().download(folderDir.get())
    popupmsg("your video downloaded to this folder : " + str(ss))


root = Tk()
root.title("downloader")


folderDir = StringVar()

videoUrl = StringVar()

Label(root, text="enter the url the video to be downloaded: ").grid(row=0, column=1)
url = Entry(root).grid(row=0, column=3)
Label(root, text="save  to : ").grid(row=1)
Label(root, textvariable=folderDir).grid(row=1, column=2)
Button(root, text="Browse", command=getFolder).grid(row=1, column=3)
Button(root, text="Download", command=downloadVideo).grid(row=2, column=3)

mainloop()

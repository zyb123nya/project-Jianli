from tkinter import *

root = Tk()

def show():
    print(GIRLS[v.get()-1][0])

GIRLS = [
    ("西施", 1),
    ("王昭君", 2),
    ("貂蝉", 3),
    ("杨玉环", 4)]

v = IntVar()

for girl, num in GIRLS:
    b = Radiobutton(root, text=girl, variable=v, value=num,command=show)
    b.pack(anchor=W)

mainloop()
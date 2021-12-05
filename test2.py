
import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(root,width=500,height=600)
canvas.pack()

labelList = []
for i in range(3):
    for j in range(3):
        num = 3 * i + j + 1
        var = 'L' + str(num)
        var = tkinter.Label(canvas, width=20, height=20,bg='green')
        var.place(x=10*num,y=10*num)
        labelList.append(var)
        print(labelList)

def delete(event):
    labelList[0].place_forget()
but = tkinter.Button(width=10,height=2,bg='yellow')
but.bind('<Button-1>',delete)
but.pack(side='bottom')

root.mainloop()

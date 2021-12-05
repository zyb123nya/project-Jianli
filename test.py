import tkinter as tk
from tkinter import ttk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.pack()
        self.v1 = tk.StringVar(value='10')
        self.v2 = tk.StringVar(value='20')
        self.v3 = tk.StringVar()
        self.changeValue()
        self.v1.trace('w', self.changeValue)
        self.v2.trace('w', self.changeValue)
        self.createUI()
   

    # 响应v1和v2数值变化的回调函数    
    def changeValue(self, *ignoredArgs):
        if self.v1.get():    #当v1值为空时，表示0
            v1 = int(self.v1.get())
        else:
            v1 = 0
        if self.v2.get():
            v2 = int(self.v2.get())
        else:
            v2 = 0
        self.v3.set(v1+v2)
    

    # 绘制控件，分别绑定三个Entry控件与类属性v1、v2和v3
    def createUI(self):
        frame1 = ttk.Frame(self)
        frame1.pack()

        ttk.Label(frame1, text="v1:").grid(column=0, row=0, sticky='W')
 
        v1Entered = ttk.Entry(frame1, width=12, textvariable=self.v1 )
        v1Entered.grid(column=1, row=0, sticky='W')


        ttk.Label(frame1, text="v2:").grid(column=0, row=1, sticky='W')

        v2Entered = ttk.Entry(frame1, width=12, textvariable=self.v2 )
        v2Entered.grid(column=1, row=1, sticky='W')

        ttk.Label(frame1, text="v1+ v2 = ").grid(column=0, row=2, sticky='W')

        v3Entered = ttk.Entry(frame1, width=12, textvariable=self.v3, state='readonly')  # 设为只读
        v3Entered.grid(column=1, row=2, sticky='W')

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()

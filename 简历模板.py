from tkinter  import *
from tkinter import ttk
import numpy as np
import tkinter as tk
from numpy.lib.shape_base import column_stack
import pandas as pd
from tkinter.messagebox import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.filedialog
from PIL import Image
from PIL import ImageTk
from ttkbootstrap import Style
import tkinter.font as tkFont

import webbrowser
GEN_HTML = "profile.html" 
# from ttkbootstrap import Style
# style = Style()
# style = Style(theme='sandstone')
#想要切换主题，修改theme值即可，有以下这么多的主题，自己尝试吧：['vista', 'classic', 'cyborg', 'journal', 'darkly', 'flatly', 'clam', 'alt', 'solar', 'minty', 'litera', 'united', 'xpnative', 'pulse', 'cosmo', 'lumen', 'yeti', 'superhero', 'winnative', 'sandstone', 'default']
# TOP6 = style.master
#一些函数要用到的
yy = []
for i in range(1970,2050):
    yy.append(i)

mm = []
for i in range(1,13):
    mm.append(i)
#数据初始化

path = 'place.csv'
data = pd.read_csv(path,index_col=None)
data_array = np.array(data)
data_list =data_array.tolist()
print(type(data_list))
city=[x[0] for x in data_list]
# city = data_list
# print(city)

list_National=('蒙古族','回族','藏族','维吾尔族','苗族','彝族','壮族','布依族','朝鲜族'
,'满族','侗族','瑶族','白族','土家族','哈尼族','哈萨克族','傣族','黎族','傈僳族','佤族','畲族','高山族'
,'拉祜族','水族','东乡族','纳西族','景颇族','柯尔克孜族','土族','达斡尔族','仫佬族','羌族','布朗族'
,'撒拉族','毛南族','仡佬族','锡伯族','阿昌族','普米族','塔吉克族'
,'怒族','乌孜别克族','俄罗斯族','鄂温克族','德昂族','保安族','裕固族','京族',
'塔塔尔族','独龙族','鄂伦春族','赫哲族','门巴族','珞巴族','基诺族','汉族'
)
# list_Adress=("北京市","天津市","广东省","重庆市")
list_Degree=("中专","初中","高中","专科","本科","硕士","博士")
#构建GUI框架容器、标题、初始分辨率
window = tk.Tk()



window.title("个人简历模板基本信息部分")
window.geometry("1000x1000")
style = Style(theme = "sandstone") # 使用的主题名称
window = style.master
ft = tkFont.Font(family='Fixdsys', size=30, weight=tkFont.BOLD)

tk.Label(window,text="个人简历模板填写",font=ft).grid(columnspan=5,sticky=N+S)



Address = tk.StringVar()
National = tk.StringVar()
Birth_year = tk.StringVar()
Birth_month = tk.StringVar()
Time_year = tk.StringVar()
Time_year_second = tk.StringVar()
Degree = tk.StringVar()
school = tk.StringVar()
Name = tk.StringVar()
want = tk.StringVar()
Professal = tk.StringVar()


#RadioButton part & 初始化默认选择
def read_text():
    global textbox_sex_get
    if v.get() == 1:
        textbox_sex_get = '男'
    if v.get() == 2:
        textbox_sex_get = '女'
v= IntVar()
# v.set(1)
button_sex_male = tk.Radiobutton(window,text="男",variable=v,value=1,command=read_text)
button_sex_female = tk.Radiobutton(window,text="女",variable=v,value=2,command=read_text)

# if v.get() == 1:
#     textbox_sex_get = '男'
# if v.get() == 2:
#     textbox_sex_get = '女'

def read_Pol_text():
    global textbox_Politic_get
    if p.get() == 0:
        textbox_Politic_get = '群众'
    if p.get() == 1:
        textbox_Politic_get = '共青团员'
    if p.get() == 2:
        textbox_Politic_get = '中共党员'
p = IntVar()
p.set(" ")
button_Politic_People = tk.Radiobutton(window,text='群众',variable=p,value=0,command=read_Pol_text)
button_Politic_Komsomolets = tk.Radiobutton(window,text='共青团员',variable=p,value=1,command=read_Pol_text)
button_Politic_Communist = tk.Radiobutton(window,text='中共党员',variable=p,value=2,command=read_Pol_text) 

#textbox part
textbox_Name = tk.Entry(window,width=15,textvariable=Name)
textbox_Age = tk.Text(window,height=1,width=15)
textbox_Phonenum = tk.Text(window,height=1,width=15)
# textbox_Phonenum_get = textbox_Phonenum("1.0","end")
textbox_School = tk.Entry(window,width=15,textvariable=school)
textbox_Professal = tk.Entry(window,width=15,textvariable=Professal)
textbox_want = tk.Entry(window,width=15,textvariable=want)
textbox_School_2 = tk.Entry(window,width=15,textvariable=school,state='readonly')
textbox_Education = tk.Text(window,height=3,width=15)
textbox_Honor = tk.Entry(window,width=15) 
textbox_Selfass = tk.Text(window,height=3,width=50)
#label part
label_Name = tk.Label(window,text="姓名")
label_Age = tk.Label(window,text="年龄")
label_Sex = tk.Label(window,text="性别")
label_Address = tk.Label(window,text="籍贯")
label_National = tk.Label(window,text="民族")
label_Phonenum = tk.Label(window,text="联系电话")
label_Politic = tk.Label(window,text="政治面貌")
label_Birth = tk.Label(window,text="出生年月")
#label_Professal缺数据，改为手动填写
label_Professal = tk.Label(window,text="专业")
#label_School缺数据,改为手动填写
label_School = tk.Label(window,text="毕业学校")
label_Time = tk.Label(window,text="就读时间")
# label_pass = tk.Label(window,text='至')#这个没啥用，占位而已
label_Degree = tk.Label(window,text="学历")
label_Education = tk.Label(window,text="教育背景")
label_Honor = tk.Label(window,text="校内荣誉")
label_Selfass = tk.Label(window,text="自我评价")
label_want = tk.Label(window,text='求职岗位') 
label_degree = tk.Label(window,textvariable=Degree)
label_tip1 = tk.Label(window,text='已获得的荣誉')
# xVariable = tk.StringVar()
#Combobox Part

Combobox_Address = ttk.Combobox(window,width=12,height=10,textvariable=Address)
Combobox_National = ttk.Combobox(window,width=12,height=10,textvariable=National)
Combobox_Birth_year = ttk.Combobox(window,width=12,height=10,textvariable=Birth_year) 
Combobox_Birth_month = ttk.Combobox(window,width=12,height=10,textvariable=Birth_month) 
Combobox_Degree = ttk.Combobox(window,width=12,height=10,textvariable=Degree)

Combobox_Time_year = ttk.Combobox(window,width=12,height=10,textvariable=Time_year)
Combobox_Time_year_2 = ttk.Combobox(window,width=12,height=10)

#Combox data,可以进阶挂sql
#各个combobox的数据
Combobox_Address["value"] = city
Combobox_National["value"] = list_National
Combobox_Birth_year['value'] = yy
Combobox_Birth_month['value'] = mm
Combobox_Degree['value'] = list_Degree
Combobox_Time_year['value'] = yy
Combobox_Time_year_2['value']=yy
def showing():
    global window
    global e
    global selectFileName
    global img
    e = tkinter.StringVar()
    selectFileName = tkinter.filedialog.askopenfilename(title='选择文件')  # 选择文件
    e.set(selectFileName)

    load = Image.open(e.get())  # open image from path
    load = load.resize((150,225))
    img = ImageTk.PhotoImage(load)           # read opened image
 
    label1=tk.Label(window,image=img)      # create a label to insert this image
    label1.grid(row=1,column=5,rowspan=4)  
    window.mainloop()
submit_button = tk.Button(window, text ="显示图片", command = showing)


def add_label():
    global textbox_Honor
    result=textbox_Honor.get()+Time_year.get()
    label_temp=tk.Label(window,text=result)
    label_temp.grid()
    

plus = Image.open('plus.png')
  
# 调整图片尺寸适应按钮大小
plus = plus.resize((30,30))
plus = ImageTk.PhotoImage(plus)  
button_addlabel = tk.Button(window,image=plus,command=add_label)


def add():
    global window
    # 通过get()函数获得Text（input_txt）的输入内容
    textbox_Name_get = textbox_Name.get()
    # textbox_Age_get = textbox_Age.get("1.0","end")
    textbox_Phonenum_get = textbox_Phonenum.get("1.0","end")
    textbox_School_get = textbox_School.get()
    textbox_Professal_get = textbox_Professal.get()
    textbox_Honor_get = textbox_Honor.get()+Time_year.get()
    textbox_Selfass_get = textbox_Selfass.get("1.0","end")
    Combobox_Address_get = Address.get()
    Combobox_National_get = National.get()
    Combobox_Birth_year_get = Birth_year.get()
    Combobox_Birth_month_get = Birth_month.get()
    Combobox_Degree_get = Degree.get()
    textbox_want_get = textbox_want.get()
   # button_Politic_People_get = button_Politic_People.get("1.0","end")
    DataFrame = pd.DataFrame({
    label_Name.cget("text"):textbox_Name_get,
    label_Sex.cget("text"):textbox_sex_get, 
    label_School.cget("text"):textbox_School_get,
    label_Professal.cget("text"):textbox_Professal_get,
    label_Address.cget("text"):Combobox_Address_get,
    label_National.cget("text"):Combobox_National_get,
    label_Degree.cget("text"):Combobox_Degree_get, 
    label_want.cget('text'):textbox_want_get},index=[0])
    
    DataFrame.to_csv('t.csv',mode='a',index=False,sep=',',encoding='utf-8')
    #收集的数据为“姓名”，“年龄”，“籍贯”，“学历”，“岗位期待”
    #分析所得出的结果为：

    
    f = open(GEN_HTML,'w',encoding='utf-8')
    message = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>我的简历</title>
        <style>
            table{
                border-collapse: collapse;
            }
            table,td.th{
                border: 1px solid blue;
            }
            
                a:link {text-decoration:none};
                a:hover {color:#FF00FF;}
        </style>
<body>
    <table width="700" height="500" border="1" background="img/bacg.jpg" align="center">
                    
    <caption><h3>个人简历</h3></caption>
    <tr>
        <td width="90">姓名</td>
        <td width="100">%s</td>
        <td width="89">出生日期</td>
        <td width="113">%s.%s</td>
        <td width="91">性别</td>
        <td width="48">%s</td>
        <td width="121" rowspan="4" 
        ><img src="%s" width="150px"/></td>
    </tr>
    <tr>
        <td>学历</td>
        <td>%s</td>
        <td>专业</td>
        <td>%s</td>
        <td>民族</td>
        <td>%s</td>
    </tr>
    <tr>
        <td>学校</td>
        <td>%s</td>
        <td>政治面貌</td>
        <td>%s</td>
        <td>联系方式</td>
        <td>%s</td>
    </tr>
    <tr>
        <td>籍贯</td>
        <td>%s</td>
        <td>求职意向</td>
        <td>%s</td>
    </tr>
    <tr height="100">
        <td>教育背景</td>
       <td colspan="6">
           %s
       </td>
    </tr>
    <tr>
        <td>校内荣誉</td>
        <td colspan="6">
            <ul>
                <li>%s</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td colspan="7" align="center"><b>自我评价</b></td>
    </tr>
    <tr>
        <td colspan="7" height="200">
            %s
        </td>
    </tr>
</table>
</body>
</head>
</html>
    """%(textbox_Name_get,Combobox_Birth_year_get,Combobox_Birth_month_get,textbox_sex_get,
        selectFileName,Combobox_Degree_get,textbox_Professal_get,Combobox_National_get,
        textbox_School_get,textbox_Politic_get,textbox_Phonenum_get,Combobox_Address_get,
        textbox_want_get,textbox_School_get,textbox_Honor_get,textbox_Selfass_get
        )
    f.write(message)

    webbrowser.open(GEN_HTML,new = 1) 

    result = showinfo('提示', '所填写内容已经保存至profile.html文件内。')
    print(f'提示: {result}')
    window.destroy()

button_next = tk.Button(text="生成",command=add)

# button_next =filedialog.askopenfilename()

#grid 布局

label_Name.grid(row=1,column=0)
textbox_Name.grid(row=1,column=1)
label_Age.grid(row=1,column=2)
textbox_Age.grid(row=1,column=3)
submit_button.grid(row=1,column=4)

label_Birth.grid(row=2,column=0)
Combobox_Birth_year.grid(row=2,column=1)
Combobox_Birth_month.grid(row=2,column=2)
label_National.grid(row=2,column=3)
Combobox_National.grid(row=2,column=4)

label_Sex.grid(row=3,column=0)
button_sex_male.grid(row=3,column=1)
button_sex_female.grid(row=3,column=2)


label_Address.grid(row=4,column=0)
Combobox_Address.grid(row=4,column=1)
label_want.grid(row=4,column=2)
textbox_want.grid(row=4,column=3)

label_School.grid(row=5,column=0)
textbox_School.grid(row=5,column=1)
label_Degree.grid(row=5,column=2)
Combobox_Degree.grid(row=5,column=3)


label_Phonenum.grid(row=6,column=0)
textbox_Phonenum.grid(row=6,column=1)
label_Professal.grid(row=6,column=2)
textbox_Professal.grid(row=6,column=3)

label_Politic.grid(row=7,column=0)
button_Politic_People.grid(row=7,column=1)
button_Politic_Komsomolets.grid(row=7,column=2)
button_Politic_Communist.grid(row=7,column=3)

label_Education.grid(row=8,column=0)
Combobox_Time_year_2.grid(row=8,column=1)
textbox_School_2.grid(row=8,column=2)
label_degree.grid(row=8,column=3)

label_Honor.grid(row=9,column=0)
Combobox_Time_year.grid(row=9,column=1)
textbox_Honor.grid(row=9,column=2)
button_addlabel.grid(row=9,column=3)

label_Selfass.grid(row=11,column=0)
textbox_Selfass.grid(row=11,column=1,columnspan=3)

button_next.grid(row=12,column=5)#按钮,等待hmtl
label_tip1.grid(row=12,column=0)
window.mainloop()




#垃圾场，也许以后有用 :（
# textbox_Name_get = textbox_Name.get("1.0","end")
# # textbox_Age_get = textbox_Age.get("1.0","end")
# # textbox_Phonenum_get = textbox_Phonenum.get("1.0","end")
# textbox_School_get = textbox_School.get()
# textbox_Professal_get = textbox_Professal.get("1.0","end")
# Combobox_Address_get = Address.get()
# Combobox_National_get = National.get()
# # Combobox_Birth_year_get = Birth_year.get()
# # Combobox_Birth_month_get = Birth_month.get()
# Combobox_Degree_get = Degree.get()
# textbox_want_get = textbox_want.get("1.0","end")
# # button_Politic_People_get = button_Politic_People.get("1.0","end")


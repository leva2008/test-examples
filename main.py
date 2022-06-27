
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Пiцерiя")
window.geometry('650x300')
lbl=Label(text="Найменування")
lbl.place(x=20,y=20,width=100,height=20)
lbl=Label(text="Цiна,грн.")
lbl.place(x=150,y=20,width=60,height=20)
lbl=Label(text="Кiлькiсть")
lbl.place(x=230,y=20,width=60,height=20)
lbl=Label(text="Вартiсть,в грн")
lbl.place(x=310,y=20,width=80,height=20)
lbl=Label(text="Пiца")
lbl.place(x=20,y=60,width=60,height=20)
lbl=Label(text="Морозиво")
lbl.place(x=20,y=100,width=60,height=20)
lbl=Label(text="Тiстечко")
lbl.place(x=20,y=140,width=60,height=20)
lbl=Label(text="Ciк")
lbl.place(x=20,y=180,width=60,height=20)
lbl=Label(text="Вартiсть замовлення")
lbl.place(x=20,y=220,width=120,height=20)
p1=Entry(font="Ariel 12",bg="Sky blue",justify="center")
p1.insert(END,"75")
p1.place(x=150,y=60,width=60,height=30)
p2=Entry(font="Ariel 12",bg="Sky blue",justify="center")
p2.insert(END,"12")
p2.place(x=150,y=100,width=60,height=30)
p3=Entry(font="Ariel 12",bg="Sky blue",justify="center")
p3.insert(END,"16")
p3.place(x=150,y=140,width=60,height=30)
p4=Entry(font="Ariel 12",bg="Sky blue",justify="center")
p4.insert(END,"8")
p4.place(x=150,y=180,width=60,height=30)
y1=0
y2=0
y3=0
y4=0
def rez(y):
    if y==int(y):
        return(int(y))
    else:
        return(y)
def s1_click(val):
    global y1
    k1=int(val)
    x1=float(p1.get())
    y1=x1*k1
    var1.set(rez(y1))
s1=Scale(orient=HORIZONTAL,length=50,from_=0,to=10,command=s1_click)
s1.place(x=230,y=50)
var1=StringVar()
c1=Label(text=0,font="Arial 12",bg="#61a1ff",textvariable=var1)
c1.place(x=310,y=60,width=60,height=30)
def s2_click(val):
    global y2
    k2=int(val)
    x2=float(p2.get())
    y2=x2*k2
    var2.set(rez(y2))
s2=Scale(orient=HORIZONTAL,length=50,from_=0,to=10,command=s2_click)
s2.place(x=230,y=90)
var2=StringVar()
c2=Label(text=0,font="Arial 12",bg="#61a1ff",textvariable=var2)
c2.place(x=310,y=100,width=60,height=30)
def s3_click(val):
    global y3
    k3=int(val)
    x3=float(p3.get())
    y3=x3*k3
    var3.set(rez(y3))
s3=Scale(orient=HORIZONTAL,length=50,from_=0,to=10,command=s3_click)
s3.place(x=230,y=130)
var3=StringVar()
c3=Label(text=0,font="Arial 12",bg="#61a1ff",textvariable=var3)
c3.place(x=310,y=140,width=60,height=30)
def s4_click(val):
    global y4
    k4 = int(val)
    x4 = float(p4.get())
    y4 = x4 * k4
    var4.set(rez(y4))
s4=Scale(orient=HORIZONTAL,length=50,from_=0,to=10,command=s4_click)
s4.place(x=230,y=170)
var4=StringVar()
c4=Label(text=0,font="Arial 12",bg="#61a1ff",textvariable=var4)
c4.place(x=310,y=180,width=60,height=30)
lbl=Label(text="грн")
lbl.place(x=260,y=220,width=60,height=20)
lbl=Label(text="Добавки до пiци,3 грн")
lbl.place(x=440,y=20,width=120,height=20)
var_ch1=IntVar()
ch1=Checkbutton(text="Майонез",font="Arial 12",variable=var_ch1)
ch1.place(x=440,y=60)
var_ch2=IntVar()
ch2=Checkbutton(text="Кетчуп",font="Arial 12",variable=var_ch2)
ch2.place(x=440,y=100)
var_ch3=IntVar()
ch3=Checkbutton(text="Соус",font="Arial 12",variable=var_ch3)
ch3.place(x=440,y=140)
var_ch4=IntVar()
ch4=Checkbutton(text="Ананаси",font="Arial 12",variable=var_ch4)
ch4.place(x=440,y=180)
def btn_click():
    global y1,y2,y3,y4,var_ch1,var_ch2,var_ch3,var_ch4
    k = 0
    if var_ch1.get() == 1:
        k = k + 1
    if var_ch2.get() == 1:
        k = k + 1
    if var_ch3.get() == 1:
        k = k + 1
    if var_ch3.get() == 1:
        k = k + 1
    y=y1+y2+y3+y4+k*3
    var5.set(rez(y))
btn = Button(window,text='Розрахувати', command=btn_click)
btn.place(x=310,y=220,width=100,height=40)
var5=StringVar()
c5=Label(text=0,font="Arial 12",bg="deep sky blue",textvariable=var5)
c5.place(x=200,y=220,width=60,height=30)


window.mainloop()
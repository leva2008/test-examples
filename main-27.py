
from tkinter import *

from tkinter import messagebox

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('440x300')
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
s1=Scale(orient=HORIZONTAL,length=50,from_=0,to=10)
s1.place(x=230,y=50)
s2=Scale(orient=HORIZONTAL,length=50,from_=0,to=10)
s2.place(x=230,y=90)
s3=Scale(orient=HORIZONTAL,length=50,from_=0,to=10)
s3.place(x=230,y=130)
s4=Scale(orient=HORIZONTAL,length=50,from_=0,to=10)
s4.place(x=230,y=170)
c1=Label(text=0,font="Arial 12",bg="deep sky blue")
c1.place(x=310,y=60,width=60,height=30)
c2=Label(text=0,font="Arial 12",bg="deep sky blue")
c2.place(x=310,y=100,width=60,height=30)
c3=Label(text=0,font="Arial 12",bg="deep sky blue")
c3.place(x=310,y=140,width=60,height=30)
c4=Label(text=0,font="Arial 12",bg="deep sky blue")
c4.place(x=310,y=180,width=60,height=30)
c5=Label(text=0,font="Arial 12",bg="deep sky blue")
c5.place(x=200,y=220,width=60,height=30)
lbl=Label(text="грн")
lbl.place(x=290,y=220,width=60,height=20)
def clicked():
    messagebox.showinfo('Message titlze', 'Тестовое сообщение')
btn = Button(window,text='Розрахувати', command=clicked)
btn.place(x=310,y=270,width=100,height=20)
def s1_click(val):
    k1=int(val)
    x1=float(p1.get())
    y1=x1*k1
    var1.set(y1)
s1=Scale(orient=HORIZONTAL,length=50,from_=0,to=10,command=s1_click)
var1=tringVar()
c1=Label(text=0,font="Arial 12",bg="#61a1ff",textvariable=var1)


#def clicked():
#    messagebox.showinfo('Message titlze', 'Тестовое сообщение')

#btn = Button(window,text='Розрахувати', command=clicked)

#btn.grid(column=0,row=0)


window.mainloop()
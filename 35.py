import time
from tkinter import *
import random
window = Tk()
window.title("Морський бiй")
canvas= Canvas(window, width=500, height=500)
canvas.pack()
canvas.create_rectangle(190,480,310,500,fill='black')
canvas.create_rectangle(240,460,260,480,fill='black')
canvas.create_oval(240,460,260,480,fill='gray')
shots=0
canvas.create_text(420,100,text='Кiльксть пострiлiв  '+str(shots))
b=0
yb=460
def ball(event):
    global b,shots,yb
    if shots < 10:
        canvas.delete(b)
        b=canvas.create_oval(240,460,260,480,fill='gray')
        canvas.create_text(420,100, text='Кiльксть пострiлiв  ' + str(shots), fill='#F0F0ED')
        shots=shots+1
        canvas.create_text(420,100, text='Кiльксть пострiлiв  ' + str(shots))
    else:
        canvas.create_text(50,100, text='    Ядра закiньчилися!')
canvas.bind_all('<space>',ball)
ship_image=PhotoImage(file="ship.gif")
k=0
canvas.create_text(420, 140, text='Кiльксть влучень  ' + str(k))
yb=0
xs=500
for z in range(10):
    global s
    s=canvas.create_image(500,0,anchor=NW,image=ship_image)
    v=random.randint(2,5)
    canvas.create_text(420, 120, text='Кiльксть кораблiв  ' + str(z), fill='#F0F0ED')
    canvas.create_text(420, 120, text='Кiльксть кораблiв  ' + str(z+1))
    for y in range(300):
        canvas.move(s, -v, 0)
        canvas.move(b,0,-5)
        window.update()
        time.sleep(0.02)
        if len(canvas.coords(s)) > 1:
          xs = canvas.coords(s)[0]
        if len(canvas.coords(b)) > 1:
          yb = canvas.coords(b)[1]
        if 140<xs<260 and 0<yb<30:
            pow_image=PhotoImage(file='pow.gif')
            p=canvas.create_image(230,10,anchor=NW,image=pow_image)
            window.update()
            time.sleep(2)
            canvas.delete(b)
            canvas.delete(p)
            k=k+1
            canvas.create_text(420, 140, text='Кiльксть влучень  ' + str(k-1),fill='#F0F0ED')
            canvas.create_text(420, 140, text='Кiльксть влучень  ' + str(k))
            break
            #b = canvas.create_oval(240, 460, 260, 480, fill='gray')
window.mainloop()

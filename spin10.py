import turtle
from tkinter import *
import random

#Title of the turtle window.
turtle.title('Spin it!')

#Define the turtles.
t=turtle.Pen()
d=turtle.Pen()
arrow=turtle.Pen()
output=turtle.Pen()

#Define the tkinter.
root=Tk()

#Title of the tkinter window.
root.title('Come and try!')

#Define and grid up the labels.
label1=Label(root,text='Have trouble on choosing something?',bg='light yellow')
label2=Label(root,text='Think of every colour representing an option.',bg='light yellow')
label3=Label(root,text='Now, Spin It to see what you get!!',bg='light yellow')
label1.grid(row=0,column=0,columnspan=2)
label2.grid(row=1,column=0,columnspan=2)
label3.grid(row=2,column=0,columnspan=2)

#Define the turtle's screen.
screen=turtle.Screen()

#Setup the screen's width and height.
screen.setup(600,600)

#Change the colour od the background.
turtle.bgcolor('#b25a38')

#Make the turtle invisible.
t.up()
d.up()
output.up()
t.ht()
d.ht()
output.ht()

#Place output pen on top
output.sety(230)

#Make the turtle fast.
t.speed(0)
d.speed(0)

#The color in the pie of the wheel.
color=['red','pink','blue','gold','green','orange','cyan','purple','yellow','light blue']

#Every piece of the wheel.
def pie(color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(200)
    t.right(90)
    t.circle(-200,36)
    t.right(90)
    t.forward(200)
    t.end_fill()
    t.right(180)

#Setup the animation.
screen.tracer(0)

# Setup the arrow on the top.
arrow.shape('triangle')
arrow.turtlesize(1)
arrow.color('brown')
arrow.fillcolor('brown')
arrow.setheading(-90)
arrow.up()
arrow.goto(0,200)

#The black border outside of the wheel.
d.dot(420)

#Draw the wheel.
def wheel():
    #Draw all the pie into the circle.
    for i in range(10):
        pie(color[i])

wheel()

#Spin the wheel!
def spin(times):
    #The larger speed is, the faster it will start and will make it spin longer.
    speed=15
    limit=random.randint(10,15)/2000
    while speed>limit:
        t.clear()
        wheel()
        screen.update()
        t.right(speed)
        #Slow down the speed.
        speed-=speed*times
    output.clear()
    if 18<=t.heading()<54:
        output.write('yellow',font=('Bahnschrift Condensed',30),align='center')
    elif 54<=t.heading()<90:
        output.write('light blue',font=('Bahnschrift Condensed',30),align='center')
    elif 90<=t.heading()<126:
        output.write('red',font=('Bahnschrift Condensed',30),align='center')
    elif 126<=t.heading()<162:
        output.write('pink',font=('Bahnschrift Condensed',30),align='center')
    elif 162<=t.heading()<198:
        output.write('blue',font=('Bahnschrift Condensed',30),align='center')
    elif 198<=t.heading()<234:
        output.write('gold',font=('Bahnschrift Condensed',30),align='center')
    elif 234<=t.heading()<270:
        output.write('green',font=('Bahnschrift Condensed',30),align='center')
    elif 270<=t.heading()<306:
        output.write('orange',font=('Bahnschrift Condensed',30),align='center')
    elif 306<=t.heading()<342:
        output.write('cyan',font=('Bahnschrift Condensed',30),align='center')
    else:
        output.write('purple',font=('Bahnschrift Condensed',30),align='center')
        

#When the tkinter's button is press.
def click():
    spin(random.randint(30,50)/20000)

#Tkinter's button.
button=Button(root,text='Press me to spin!',padx=100,pady=100,bg='#b25a38',command=click)
button.grid(row=3,column=0,columnspan=2)

#Other labels.
label4=Label(root,text='In case you don\'t know the colours,',bg='light yellow')
label5=Label(root,text='you can see below and note your option here.',bg='light yellow')
#label4.grid(row=4,column=0,columnspan=2)
#label5.grid(row=5,column=0,columnspan=2)

#Define colour labels
colour1=Label(root,text='1) Red: ')
colour2=Label(root,text='2) Pink: ')
colour3=Label(root,text='3) Blue: ')
colour4=Label(root,text='4) Gold: ')
colour5=Label(root,text='5) Green: ')
colour6=Label(root,text='6) Orange: ')
colour7=Label(root,text='7) Cyan: ')
colour8=Label(root,text='8) Purple: ')
colour9=Label(root,text='9) Yellow: ')
colour10=Label(root,text='10) Light Blue: ')

#Define entries.
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e5=Entry(root)
e6=Entry(root)
e7=Entry(root)
e8=Entry(root)
e9=Entry(root)
e10=Entry(root)


#Grid up colour labels.

colour1.grid(row=6,column=0)
colour2.grid(row=7,column=0)
colour3.grid(row=8,column=0)
colour4.grid(row=9,column=0)
colour5.grid(row=10,column=0)
colour6.grid(row=11,column=0)
colour7.grid(row=12,column=0)
colour8.grid(row=13,column=0)
colour9.grid(row=14,column=0)
colour10.grid(row=15,column=0)


#Grid up entries.

e1.grid(row=6,column=1)
e2.grid(row=7,column=1)
e3.grid(row=8,column=1)
e4.grid(row=9,column=1)
e5.grid(row=10,column=1)
e6.grid(row=11,column=1)
e7.grid(row=12,column=1)
e8.grid(row=13,column=1)
e9.grid(row=14,column=1)
e10.grid(row=15,column=1)


#Ending!
root.mainloop()
turtle.done()

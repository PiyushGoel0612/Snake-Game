from tkinter import *
import random
pt = 0
done = 0
direction = 'Down'
sx = 400
sy = 60
fx = 100
fy = 100
tx = 400
ty = 40
x = 0
y = 20
cor_x = [x for x in range(0,481,20)]
cor_y = [y for y in range(0,481,20)]
r = Tk()
f = Frame(r)
f.pack()
c = Canvas(r,height='500',width='500',bg='#008000')

l1 = Label(f,height=1,width=12,text='Points : 00',font=("Comic Sans MS", 20, "bold"))
l1.pack(side='left')
c.pack()

class Head:
    def __init__(self):
        global size,sx,sy
        self.cord = [sx,sy]
        self.sq = c.create_rectangle(sx,sy,sx+20,sy+20,fill='red',width='2')

class Tail:
    def __init__(self):
        global tx,ty
        self.coordinates = []
        self.squares = []
        self.coordinates.append([tx,ty])
        for i in self.coordinates:
            sq = c.create_rectangle(i[0],i[1],i[0]+20,i[1]+20,fill='red',width='2')
            self.squares.append(sq)

class Food:
    def __init__(self):
        global fx,fy
        self.cord = [fx,fy]
        self.fd = c.create_oval(110,110,130,130,fill='white',width='2')
    def place(self,a,b):
        global fx,fy
        c.delete(self.fd)
        self.fd = c.create_oval(a,b,a+20,b+20,fill='white',width='2',activefill='black')
        fx = a
        fy = b
        self.cord = [fx,fy]

def c_dir(event):
    global direction
    new_direction = str(event.keysym)
    if new_direction == 'Right':
        if direction != 'Left':
            direction = new_direction
    elif new_direction == 'Left':
        if direction != 'Right':
            direction = new_direction
    elif new_direction == 'Up':
        if direction != 'Down':
            direction = new_direction
    elif new_direction == 'Down':
        if direction != 'Up':
            direction = new_direction

def Move(way):
    global direction,sx,sy,pt,tx,ty,x,y
    tx = sx
    ty = sy
    x0 = x
    y0 = y
    if direction == 'Up':
        x = 0
        y = -20
        sy -= 20
    elif direction == 'Down':
        x = 0
        y = 20
        sy += 20
    elif direction == 'Right':
        x = 20
        y = 0
        sx += 20
    elif direction == 'Left':
        x = -20
        y = 0
        sx -= 20
    if x0 == 0 and y0 == 0:
        x0 = 0
        y0 = 20

    h.cord = [sx,sy]
    t_cord = [tx,ty]
    if h.cord != f.cord:
        c.delete(t.squares[-1])
        t.squares.pop()
        t.coordinates.pop()
        t.coordinates.insert(0,t_cord)
        sq = c.create_rectangle(t_cord[0],t_cord[1],t_cord[0]+20,t_cord[1]+20,fill='red',width='2')
        t.squares.insert(0,sq)
    else:
        t.coordinates.insert(0,t_cord)
        sq = c.create_rectangle(t_cord[0],t_cord[1],t_cord[0]+20,t_cord[1]+20,fill='red',width='2')
        t.squares.insert(0,sq)

    c.move(h.sq,x,y)
    
    if h.cord == f.cord:
        pt += 1
        if pt > 9:
            txt = str(pt)
        else:
            txt = '0'+str(pt)
        l1.config(text = 'Points : '+str(txt))
        f_place()
    
    check()
    if done:
        del t.coordinates
        del t.squares
        del h.cord
        del f.cord
        del f.fd
        return

    r.after(200,Move,direction)

def f_place():
    global sx,sy,fx,fy,cor_x,cor_y
    while True:
        a = random.choice(cor_x)
        b = random.choice(cor_y)
        if a!=sx and a!=fx:
            if b!=sy and b!=fy:
                if [a,b] not in t.coordinates:
                    break
    f.place(a,b)

def check():
    global done,pt
    if h.cord[0] == -20 or h.cord[0] == 500:
        c.delete('all')
        del h.sq
        l1.config(text='GAME OVER !!')
        done = 1
        if pt > 9:
            txt = str(pt)
        else:
            txt = '0'+str(pt)
        c.create_text(250,250,text='Your score : '+txt,font=("Comic Sans MS", 25, "bold"))
    elif h.cord[1] ==-20 or h.cord[1] == 500:
        c.delete('all')
        del h.sq
        l1.config(text='GAME OVER !!')
        done = 1
        if pt > 9:
            txt = str(pt)
        else:
            txt = '0'+str(pt)
        c.create_text(250,250,text='Your score : '+txt,font=("Comic Sans MS", 25, "bold"))
    elif h.cord in t.coordinates:
        c.delete('all')
        del h.sq
        l1.config(text='GAME OVER !!')
        done = 1
        if pt > 9:
            txt = str(pt)
        else:
            txt = '0'+str(pt)
        c.create_text(250,250,text='Your score : '+txt,font=("Comic Sans MS", 25, "bold"))

h = Head()
f = Food()
t = Tail()

Move(direction)
r.bind('<Key>',c_dir)
r.mainloop()
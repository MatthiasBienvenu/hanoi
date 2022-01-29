from tkinter import *

time = 500

window = Tk()

frame = Frame(window, bg="#ffffe0", bd=0)
frame.pack(expand = YES)

frame2 = Frame(frame, bg="#ffffe0", bd=0)
frame2.pack()

canvas = Canvas(frame2, width = 1800, heigh = 800, bg = "#ffffe0", bd = 0, highlightthickness = 0)
canvas.pack(expand = YES, pady = (25, 25))

n = StringVar()
n.set("3")


def restore():
    global A, B, C, Ldisques, canvas
    A = [-k + int(n.get()) for k in range(int(n.get()))]
    B = [0 for k in range(int(n.get()))]
    C = [0 for k in range(int(n.get()))]
    
    canvas.destroy()
    
    canvas = Canvas(frame2, width = 1800, heigh = 800, bg = "#ffffe0", bd = 0, highlightthickness = 0)
    canvas.pack(expand = YES, pady = (25, 25))
    
    canvas.create_rectangle(285, 100, 315, 800, fill = "#ddd29a", width = 0)
    canvas.create_rectangle(885, 100, 915, 800, fill = "#ddd29a", width = 0)
    canvas.create_rectangle(1485, 100, 1515, 800, fill = "#ddd29a", width = 0)
    
    Ldisques = [canvas.create_rectangle(300-280*((int(n.get()))-k)/int(n.get()), (15-k)*50, 300+280*((int(n.get()))-k)/int(n.get()), (16-k)*50, fill="#d4423e", outline="") for k in range(int(n.get()))]
    
    print(A, B, C)


spinbox = Spinbox(frame, from_=0, to=14, textvar=n, command=restore)
spinbox.pack(pady = (25, 25))
spinbox.selection("from", "3")

window.minsize(1280, 720)
window.geometry('1920x1080')
window.title("Tours d'Hanoi")
window.configure(bg = "#ffffe0")
window.attributes("-fullscreen", True)

restore()


def deplacement(col1, col2):
    for i in range(int(n.get())):
        if col1[-i-1] != 0:
            ele = col1[-i - 1]
            col1[-i-1] = 0
            break
    for k in range(int(n.get())):
        if col2[k] == 0:
            col2[k] = ele
            break
    return col1, col2


def AB():
    global A, B
    for i in range(int(n.get())):
        if A[-i - 1] != 0:
            eleA = A[-i - 1]
            break
        else:
            eleA = int(n.get())+1
    for i in range(int(n.get())):
        if B[-i - 1] != 0:
            eleB = B[-i - 1]
            break
        else:
            eleB = int(n.get())+1
    if eleA < eleB:
        iEleInA = A.index(eleA)
        
        canvas.move(int(n.get())+4-eleA, 600, (iEleInA - deplacement(A, B)[1].index(eleA))*50)
    else:
        iEleInB = B.index(eleB)
        
        canvas.move(int(n.get())+4-eleB, -600, (iEleInB - deplacement(B, A)[1].index(eleB))*50)


def BC():
    global B, C
    for i in range(int(n.get())):
        if B[-i - 1] != 0:
            eleB = B[-i - 1]
            break
        else:
            eleB = int(n.get())+1
    for i in range(int(n.get())):
        if C[-i - 1] != 0:
            eleC = C[-i - 1]
            break
        else:
            eleC = int(n.get())+1
    if eleB < eleC:
        iEleInB = B.index(eleB)
        
        canvas.move(int(n.get())+4-eleB, 600, (iEleInB - deplacement(B, C)[1].index(eleB))*50)

    else:
        iEleInC = C.index(eleC)
        
        canvas.move(int(n.get())+4-eleC, -600, (iEleInC - deplacement(C, B)[1].index(eleC))*50)


def CA():
    global C, A
    for i in range(int(n.get())):
        if C[-i - 1] != 0:
            eleC = C[-i - 1]
            break
        else:
            eleC = int(n.get())+1
    for i in range(int(n.get())):
        if A[-i - 1] != 0:
            eleA = A[-i - 1]
            break
        else:
            eleA = int(n.get())+1
    if eleC < eleA:
        iEleInC = C.index(eleC)
        
        canvas.move(int(n.get())+4-eleC, -1200, (iEleInC - deplacement(C, A)[1].index(eleC))*50)

    else:
        iEleInA = A.index(eleA)
        
        canvas.move(int(n.get())+4-eleA, 1200, (iEleInA - deplacement(A, C)[1].index(eleA))*50)


def win():
    messagebox.showinfo(title="", message=f"Les {n.get()} disques ont été déplacés de la tour A à la tour C")


compteur = 0
def pair():
    global compteur
    
    if compteur == 2**int(n.get())-1:
        win()
        compteur = 0
        
    elif (compteur)%3==0:
        AB()
        window.after(time, pair)
        compteur += 1
        
    elif (compteur-1)%3==0:
        CA()
        window.after(time, pair)
        compteur += 1
        
    elif (compteur-2)%3==0:
        BC()
        window.after(time, pair)
        compteur += 1


def impair():
    global compteur
    
    if compteur == 2**int(n.get())-2:
        CA()
        win()
        compteur = 0
        
    elif compteur%3==0:
        CA()
        window.after(time, impair)
        compteur += 1
        
    elif (compteur-1)%3==0:
        AB()
        window.after(time, impair)
        compteur += 1
        
    elif (compteur-2)%3==0:
        BC()
        window.after(time, impair)
        compteur += 1


def hanoi():
    restore()
    if int(n.get())%2 == 0:
        pair()
    else:
        impair()

button = Button(frame, text = "COMMENCER", command = hanoi)
button.pack(pady = (25, 25))


window.mainloop()
from tkinter import *
import os
root=Tk()
root.attributes("-fullscreen",True)
root.config(bg="black")
root.title("PHYSICS PROJECT BY DURKESH KUMAR ")
lbl=Label(root,text="ENTER PHYSICS LICENCE CODE :")
lbl.config(font=("callibir",24,"italic bold"),fg="white",bg="black")
lbl.pack(side=TOP,padx=10,pady=20)
btn=Button(root,text="EXIT",command=root.destroy)
btn.config(font=("callibri",24,"bold italic"),fg="black",bg="red")
btn.pack(side=RIGHT)
img=PhotoImage(file="in.png")

lbl=Label(root,image=img)
lbl.config(width=700, height=500)

lbl.pack(padx=200)
entry=Entry(root)
entry.config(font=("callibri",20,"bold italic"),fg="black",bg="white")
entry.pack(padx=10,pady=20)

#new code
def sample():
    os.system("python main.py")

def waste():
    os.system("python wrong.py")
def new():
    x=entry.get()
    if x=="phy":
        sample()
    else:
        waste()


btn=Button(root,text="REQUEST",command=new)
btn.config(font=("callibri",20,"bold italic"),fg="black",bg="green")
btn.pack(padx=10,pady=20)
root.mainloop()

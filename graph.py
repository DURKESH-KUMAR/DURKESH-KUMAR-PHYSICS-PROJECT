from tkinter import *
import matplotlib.pyplot as a

root=Tk()
root.attributes("-fullscreen",True)
root.config(bg="black")
lbl=Label(root,text="DURKATHON PHYSICS GRAPH")
lbl.config(font=("callibri",24,"bold italic"),bg="black",fg="white")
lbl.pack(side=TOP,padx=10,pady=20)
btn=Button(root,text="EXIT",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT)

#start
lbl=Label(root,text="ENERGY LEVEL 1 :")
lbl.config(font=("callibri",24,"bold italic"),bg="black",fg="yellow")
lbl.pack(side=TOP,padx=10,pady=20)

entry=Entry(root)
entry.config(font=("callibri",24,"bold italic"))
entry.pack(padx=20,pady=20)
def sample1():
    x=list(entry.get())
    a.plot(x)
    a.show()
btn1=Button(root,text="PLOT",command=sample1)
btn1.config(font=("callibri",20,"bold italic"),fg="black",bg="green")
btn1.pack()

#2
#start
lbl=Label(root,text="ENERGY LEVEL 2 :")
lbl.config(font=("callibri",24,"bold italic"),bg="black",fg="yellow")
lbl.pack(side=TOP,padx=10,pady=20)

entry2=Entry(root)
entry2.config(font=("callibri",24,"bold italic"))
entry2.pack(padx=20,pady=20)
def sample2():
    x=list(entry2.get())
    a.plot(x)
    a.show()
btn2=Button(root,text="PLOT",command=sample2)
btn2.config(font=("callibri",20,"bold italic"),fg="black",bg="green")
btn2.pack()

#3
#start
lbl=Label(root,text="ENERGY LEVEL 3 :")
lbl.config(font=("callibri",24,"bold italic"),bg="black",fg="yellow")
lbl.pack(side=TOP,padx=10,pady=20)

entry3=Entry(root)
entry3.config(font=("callibri",24,"bold italic"))
entry3.pack(padx=20,pady=20)
def sample3():
    x=list(entry3.get())
    a.plot(x)
    a.show()
btn3=Button(root,text="PLOT",command=sample3)
btn3.config(font=("callibri",20,"bold italic"),fg="black",bg="green")
btn3.pack()


root.mainloop()
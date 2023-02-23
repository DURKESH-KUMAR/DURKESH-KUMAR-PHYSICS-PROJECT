from tkinter import *
import pywhatkit
import os
import matplotlib.pyplot as a

root=Tk()
root.attributes("-fullscreen",True)
root.config(bg="black")
lbl=Label(root,text="DURKATHON PHYSICS PROJECT")
lbl.config(font=("callibri",24,"bold italic"),bg="black",fg="white")
lbl.pack(side=TOP,padx=10,pady=20)
btn=Button(root,text="EXIT",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT)
img=PhotoImage(file="1.png")
lbl=Label(root,image=img)
lbl.config(width=1000, height=600)
lbl.pack()

def search():
    os.system("python search.py")
def video():
    os.system("python video.py")
def graph():
    os.system("python graph.py")
def new():
    os.system("python prototype.py")
    
#google
btn=Button(root,text="SEARCH",command=search)
btn.config(font=("callibri",24,"bold italic"),fg="black",bg="green")
btn.pack(side=LEFT,padx=100,pady=20)
#video
btn=Button(root,text="VIDEO",command=video)
btn.config(font=("callibri",24,"bold italic"),fg="black",bg="green")
btn.pack(side=LEFT,padx=100,pady=20)
#graph
btn=Button(root,text="GRAPH",command=graph)
btn.config(font=("callibri",24,"bold italic"),fg="black",bg="green")
btn.pack(side=LEFT,padx=100,pady=20)
#prototype
btn=Button(root,text="PROTOTYPE",command=new)
btn.config(font=("callibri",24,"bold italic"),fg="black",bg="green")
btn.pack(side=LEFT,padx=100,pady=20)

root.mainloop()

    



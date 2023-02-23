from tkinter import *
import pywhatkit
root=Tk()
root.attributes("-fullscreen",True)
root.config(bg="black")
lbl=Label(root,text="DURKATHON PHYSICS SEARCH ENGINE")
lbl.config(font=("callibri",24,"bold italic"),bg="black",fg="white")
lbl.pack(side=TOP,padx=10,pady=20)
btn=Button(root,text="EXIT",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT)
entry=Entry(root)
entry.config(font=("callibri",24,"bold italic"),bg="white",fg="black")
entry.pack(side=TOP,padx=10,pady=20) 
def simple():
    x=entry.get()
    pywhatkit.search(x)
btn=Button(root,text="SEARCH",command=simple)
btn.config(font=("callibri",20,"bold italic"),fg="black",bg="green")
btn.pack(padx=20,pady=20)
img=PhotoImage(file="1.png")
lbl=Label(root,image=img)
lbl.config(width=1000, height=600)
lbl.pack()
root.mainloop()
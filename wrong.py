from tkinter import *
root=Tk()
root.attributes("-fullscreen",True)
root.config(bg="black")
root.title("PHYSICS PROJECT BY DURKESH KUMAR ")
lbl=Label(root,text="PHYSICS LICENCE CODE : WRONG")
lbl.config(font=("callibir",24,"italic bold"),fg="white",bg="black")
lbl.pack(side=TOP,padx=10,pady=20)
btn=Button(root,text="EXIT",command=root.destroy)
btn.config(font=("callibri",24,"bold italic"),fg="black",bg="red")
btn.pack(side=RIGHT)

img=PhotoImage(file="in.png")

lbl=Label(root,image=img)
lbl.config(width=700, height=500)

lbl.pack(padx=200)


lbl=Label(root,text="PLEASE PURCHASE THE PHYSICS LICENCE CODE ")
lbl.config(font=("callibir",24,"italic bold"),fg="white",bg="black")
lbl.pack(side=TOP,padx=10,pady=20)
root.mainloop()
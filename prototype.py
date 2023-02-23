from tkinter import *


root=Tk()
root.attributes("-fullscreen",True)
root.config(bg="black")
lbl=Label(root,text="DURKATHON PHYSICS PROJECT")
lbl.config(font=("callibri",24,"bold italic"),bg="black",fg="white")
lbl.pack(side=TOP,padx=10,pady=20)
btn=Button(root,text="EXIT",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT)

lbl=Label(root,text="ENTER THE ENEGY LEVEL TO GENERATE THE EIGEN VALUE OF ELECTRON:")
lbl.config(font=("callibri",24,"bold italic"),bg="black",fg="yellow")
lbl.pack(side=TOP,padx=20,pady=20)

entry=Entry(root)
entry.config(font=("callibri",24,"bold italic"),fg="black",bg="white")
entry.pack(side=TOP,padx=20,pady=20)

def sample():
    n=(entry.get())
    a=int(n)
    
    e1=((a)**2)*(37.68)
    z="""THE ENERGY LEVEL {} OF AN ELECTRON :{}eV""".format(a,e1)
    lbl=Label(root,text=z)
    lbl.config(font=("callibri",24,"bold italic"),bg="black",fg="yellow")
    lbl.pack(side=TOP,padx=20,pady=20)

    #2
    
    
    e2=((a+1)**2)*(37.68)
    z="""THE ENERGY LEVEL {} OF AN ELECTRON :{}eV""".format(a+1,e2)
    lbl=Label(root,text=z)
    lbl.config(font=("callibri",24,"bold italic"),bg="black",fg="yellow")
    lbl.pack(side=TOP,padx=20,pady=20)

    #3
  
    
    e3=((a+2)**2)*(37.68)
    z="""THE ENERGY LEVEL {} OF AN ELECTRON :{}eV""".format(a+2,e3)
    lbl=Label(root,text=z)
    lbl.config(font=("callibri",24,"bold italic"),bg="black",fg="yellow")
    lbl.pack(side=TOP,padx=20,pady=20)

    def graph():
        import matplotlib.pyplot as plt
        plt.plot([e1,e2,e3])
        plt.title("ENERY LEVEL OF EIGEN VALUE")
        plt.show()
    btn=Button(root,text="GRAPH",command=graph)
    btn.config(font=("callibri",20,"italic bold"),bg="green",fg="black")
    btn.pack(padx=20,pady=20)



btn=Button(root,text="ANSWER",command=sample)
btn.config(font=("callibri",20,"bold italic"),bg="green",fg="black")
btn.pack(side=TOP,padx=20,pady=20)
root.mainloop()
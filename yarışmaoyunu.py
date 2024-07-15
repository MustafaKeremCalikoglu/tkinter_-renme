import tkinter  as  tk 
from PIL import Image,ImageTk

class Yarısma(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("varmısın yokmusun")
        self.resim=ImageTk.PhotoImage(Image.open("var.png"))
        self.arkaplan=tk.Label(image=self.resim)
        self.arkaplan.pack()
        self.resizable(width=tk.FALSE,height=tk.FALSE)

        ################  mavi kutular 1 den 10 a kadar ###########################################
        self.kutu1=tk.Label(bg="blue",fg="white",font="italic 15 bold")
        self.kutu1.place(x=5,y=70)
        
        self.kutu2=tk.Label(bg="blue",fg="white",font="italic 15 bold")
        self.kutu2.place(x=5,y=110)
        
        self.kutu3=tk.Label(bg="blue",fg="white",font="italic 15 bold")
        self.kutu3.place(x=5,y=150)
        
        self.kutu4=tk.Label(bg="blue",fg="white",font="italic 15 bold")
        self.kutu4.place(x=5,y=190)      

        self.kutu5=tk.Label(bg="blue",fg="white",font="italic 15 bold")
        self.kutu5.place(x=5,y=230)
        
        self.kutu6=tk.Label(bg="blue",fg="white",font="italic 15 bold")
        self.kutu6.place(x=5,y=270)

        self.kutu7=tk.Label(bg="blue",fg="white",font="italic 15 bold")
        self.kutu7.place(x=5,y=310)
        
        self.kutu8=tk.Label(bg="blue",fg="white",font="italic 15 bold")
        self.kutu8.place(x=5,y=350)

        self.kutu9=tk.Label(bg="blue",fg="white",font="italic 15 bold")
        self.kutu9.place(x=5,y=390)
        
        self.kutu10=tk.Label(bg="blue",fg="white",font="italic 15 bold")
        self.kutu10.place(x=5,y=430)

        ############################## kırmızı kutular 11 den 20 ye kadar ###################################

        self.kutu11=tk.Label(bg="yellow",fg="white",font="italic 15 bold")
        self.kutu11.place(x=1020,y=70)
        
        self.kutu12=tk.Label(bg="yellow",fg="white",font="italic 15 bold")
        self.kutu12.place(x=1020,y=110)
        
        self.kutu13=tk.Label(bg="yellow",fg="white",font="italic 15 bold")
        self.kutu13.place(x=1020,y=150)
        
        self.kutu14=tk.Label(bg="yellow",fg="white",font="italic 15 bold")
        self.kutu14.place(x=1020,y=190)      

        self.kutu15=tk.Label(bg="red",fg="white",font="italic 15 bold")
        self.kutu15.place(x=1020,y=230)
        
        self.kutu16=tk.Label(bg="red",fg="white",font="italic 15 bold")
        self.kutu16.place(x=1020,y=270)

        self.kutu17=tk.Label(bg="red",fg="white",font="italic 15 bold")
        self.kutu17.place(x=1020,y=310)
        
        self.kutu18=tk.Label(bg="red",fg="white",font="italic 15 bold")
        self.kutu18.place(x=1020,y=350)

        self.kutu19=tk.Label(bg="red",fg="white",font="italic 15 bold")
        self.kutu19.place(x=1020,y=390)
        
        self.kutu20=tk.Label(bg="red",fg="white",font="italic 15 bold")
        self.kutu20.place(x=1020,y=430)

        



pencere=Yarısma()
pencere.mainloop()            



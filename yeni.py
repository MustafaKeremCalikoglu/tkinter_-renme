import time 
from tkinter import*

class Pencere(Tk):
    def __init__(self):
        super().__init__()
        self.title("sayaç")
        self.i=60
        self.y=1
        self.saniye=Label(text="{} : {}".format(str(self.y),str(self.i)),font="verdana 16 bold")
        self.saniye.pack()    
        self.sonuç=StringVar()
        self.sonuç.set(0)
        self.seçenek=Radiobutton(text="durdur",activebackground="green",value="durdur",variable=self.sonuç)
        self.seçenek.pack()
        self.seçenek2=Radiobutton(text="başlat",activebackground="green",value="başlat",variable=self.sonuç)
        self.seçenek2.pack()
        self.düğme=Button(text="başlat",command=self.durdur_başlat)
        self.düğme.pack()
   
   
    def durdur_başlat(self):
        if self.sonuç.get()=="durdur":
            self.after(1000,self.durdur_başlat)
        elif self.sonuç.get()=="başlat":
            self.say()


    def say(self):    
        self.i=self.i-1
        if self.i<=60 and self.i>0 :
            self.saniye["text"]="{} : {}".format(str(self.y),str(self.i))
            self.after(1000,self.durdur_başlat)

        elif self.i==0 and self.y!=0:
            self.i=60
            self.y=self.y-1
            self.saniye["text"]="{} : {}".format(str(self.y),str(self.i))
            self.after(1000,self.durdur_başlat)

        elif self.i==0 and self.y==0:

            self.saniye["text"]="bitmiştir"
    

pencere=Pencere()
pencere.mainloop()
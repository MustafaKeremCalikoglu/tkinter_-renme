import tkinter as tk
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
import random
class Pencere(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("720x425")
        self.resim=ImageTk.PhotoImage(Image.open("tahmin.png"))
        self.resizable(height=tk.FALSE,width=tk.FALSE)
        self.arkaplan=tk.Label(image=self.resim)
        self.arkaplan.pack()
        self.başlık=tk.Label(text="TAHMİN OYUNUNA HOŞGELDİNİZ",bg="purple",fg="white",font="italic 25 bold")
        self.başlık.place(x=100,y=20)
        self.renk_listesi=["sarı","mavi","yeşil","kırmızı","turuncu"]
        self.x=tk.StringVar()

        self.açılan_kutu=Combobox(values=self.renk_listesi,textvariable=self.x,height=20,width=40)
        self.açılan_kutu.place(x=230,y=80)

        self.düğme=tk.Button(text="çevir",command=self.çevir)
        self.düğme.place(x=320,y=200)
        
        
        self.çevirme_sonucu=tk.Label()
        self.çevirme_sonucu.place(x=250,y=130)

        self.genel_sonuç=tk.Label()
        self.genel_sonuç.place(x=250,y=300)
    def çevir(self):
        self.rastgele=random.randint(0,4)
        self.çevirme_sonucu["text"]=self.renk_listesi[self.rastgele]
        self.çevirme_sonucu["bg"]="purple"

        if self.renk_listesi[self.rastgele]==self.x.get():
            self.genel_sonuç["text"]="BİLDİNİZ"
            self.genel_sonuç["bg"]="green"
            self.genel_sonuç["fg"]="white"
        else:
            self.genel_sonuç["text"]="BİLEMEDİNİZ"
            self.genel_sonuç["bg"]="red"
            self.genel_sonuç["fg"]="white"        
        
pencere=Pencere()
pencere.mainloop()
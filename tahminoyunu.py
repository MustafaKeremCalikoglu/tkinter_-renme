from tkinter import *
from tkinter.ttk import Combobox
import random
pencere=Tk()
pencere.title("renk tutturma")
pencere.config(bg="purple")
pencere.geometry("300x230")
pencere.resizable(width=FALSE,height=FALSE)

liste=["kırmızı","pembe","turuncu","yeşil","lila","mavi","sarı","gri","mor"]


x=StringVar()

label_baslık=Label(text="RENK TUTTURMA OYUNU",bg="yellow",fg="purple",font="calibri 15 bold").place(x=60,y=0)

def cevir():
    a=random.randint(0,8)
    label_cevirilen=Label(text=liste[a],bg="yellow",fg="purple",font="calibri 15 bold").place(x=130,y=100)
    if liste[a]==x.get():
        label_bulunan=Label(text="TEBRİKLER BULDUNUZ",bg="red",fg="white",font="calibri 20 italic").place(x=20,y=140)
    else:
        label_bulunmayan=Label(text="MALESEF BULAMADINIZ",bg="red",fg="white",font="calibri 20 italic").place(x=20,y=140)


acılan_kutu=Combobox(pencere,values=liste,textvariable=x,height=10,width=20).place(x=90,y=30)
buton_dondur=Button(text="çevir",bg="yellow",fg="purple",font="calibri 13 bold",command=cevir).place(x=130,y=55)


a=random.randint(0,8)




mainloop()


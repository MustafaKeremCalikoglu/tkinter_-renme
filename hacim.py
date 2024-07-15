from tkinter import *
from PIL import ImageTk,Image

pencere=Tk()
pencere.title("hacim hesaplama uygulaması")
pencere.geometry("1000x629")
pencere.resizable(width=FALSE,height=FALSE)
resim=ImageTk.PhotoImage(Image.open("projekapağı.png"))
arkaplan=Label(pencere,image=resim)
arkaplan.pack()

resim_kare=ImageTk.PhotoImage(Image.open("kare.png"))
resim_küre=ImageTk.PhotoImage(Image.open("küre.png"))
resim_koni=ImageTk.PhotoImage(Image.open("koni.png"))
resim_prizma=ImageTk.PhotoImage(Image.open("prizma.png"))
resim_silindir=ImageTk.PhotoImage(Image.open("silindir.png"))


def kare():
    global karepencere
    global girişa
    global girişb
    global girişc
    global sonuç_etiket_kare

    karepencere=Toplevel()
    karepencere.geometry("1000x604")
    arkaplan_kare=Label(karepencere,image=resim_kare)
    arkaplan_kare.pack()

    girişa=Entry(karepencere)
    girişa.place(x=40,y=120)

    girişb=Entry(karepencere)
    girişb.place(x=40,y=280)

    girişc=Entry(karepencere)
    girişc.place(x=40,y=460)

    son_buton=Button(karepencere,text="HESAPLA",bg="orange",fg="white",font="italic 15 bold",command=kare_hesapla)
    son_buton.place(x=40,y=500)
   
    sonuç_etiket_kare=Label(karepencere,font="italic 30 bold")
    sonuç_etiket_kare.place(x=420,y=250)    

def kare_hesapla():
    hacim_etiket=Label(karepencere,text="HACİM DEĞERİ",fg="orange",font="italic 25 bold")
    hacim_etiket.place(x=390,y=150)
    karesonuç=float(girişa.get()) * float(girişb.get()) * float(girişc.get())
    sonuç_etiket_kare["fg"]="blue"
    sonuç_etiket_kare["bg"]="white"
    sonuç_etiket_kare["text"]=""
    sonuç_etiket_kare["text"]=karesonuç
    girişa.delete(0,END)
    girişb.delete(0,END)
    girişc.delete(0,END)

def küre():
    global kürepencere
    global girişr
    global sonuç_etiket_küre


    kürepencere=Toplevel()
    kürepencere.geometry("1000x598")
    kürepencere.resizable(width=FALSE,height=FALSE)
    
    arkaplan_küre=Label(kürepencere,image=resim_küre)
    arkaplan_küre.pack()
    girişr=Entry(kürepencere)
    girişr.place(x=50,y=200)

    son_buton=Button(kürepencere,text="HESAPLA",bg="orange",fg="white",font="italic 15 bold",command=küre_hesapla)
    son_buton.place(x=60,y=230)

    sonuç_etiket_küre=Label(kürepencere,font="italic 30 bold")
    sonuç_etiket_küre.place(x=420,y=250)

def küre_hesapla():
    hacim_etiket=Label(kürepencere,text="HACİM DEĞERİ",fg="blue",font="italic 25 bold")
    hacim_etiket.place(x=390,y=150)
   
    küresonuç=3.14  * (float(girişr.get()) ** 3  )  *  4 / 3
    sonuç_etiket_küre["fg"]="blue"
    sonuç_etiket_küre["bg"]="white"
    sonuç_etiket_küre["text"]=""
    sonuç_etiket_küre["text"]=küresonuç

    girişr.delete(0,END)

def koni():
    global konipencere
    global girişkonir
    global sonuç_etiket_koni
    global girişkonih

    konipencere=Toplevel()
    konipencere.geometry("1000x598")
    konipencere.resizable(width=FALSE,height=FALSE)
    
    arkaplan_koni=Label(konipencere,image=resim_koni)
    arkaplan_koni.pack()


    girişkonir=Entry(konipencere)
    girişkonir.place(x=50,y=330)

    girişkonih=Entry(konipencere)
    girişkonih.place(x=50,y=160)

    son_buton=Button(konipencere,text="HESAPLA",bg="orange",fg="white",font="italic 15 bold",command=koni_hesapla)
    son_buton.place(x=60,y=400)

    sonuç_etiket_koni=Label(konipencere,font="italic 30 bold")
    sonuç_etiket_koni.place(x=420,y=250)

def koni_hesapla():
    hacim_etiket=Label(konipencere,text="HACİM DEĞERİ",fg="blue",font="italic 25 bold")
    hacim_etiket.place(x=390,y=150)
   
    konisonuç=3.14  * (float(girişkonir.get()) ** 2  ) * float(girişkonih.get())  / 3
    sonuç_etiket_koni["fg"]="blue"
    sonuç_etiket_koni["bg"]="white"
    sonuç_etiket_koni["text"]=""
    sonuç_etiket_koni["text"]=konisonuç

    girişkonir.delete(0,END)
    girişkonih.delete(0,END)


def prizma():
    global prizmapencere
    global girişA
    global girişB
    global girişH
    global sonuç_etiket_prizma

    prizmapencere=Toplevel()
    prizmapencere.geometry("1000x604")
    arkaplan_prizma=Label(prizmapencere,image=resim_prizma)
    arkaplan_prizma.pack()

    girişA=Entry(prizmapencere)
    girişA.place(x=50,y=150)

    girişB=Entry(prizmapencere)
    girişB.place(x=50,y=270)

    girişH=Entry(prizmapencere)
    girişH.place(x=50,y=400)

    son_buton=Button(prizmapencere,text="HESAPLA",bg="orange",fg="white",font="italic 15 bold",command=prizma_hesapla)
    son_buton.place(x=50,y=480)
   
    sonuç_etiket_prizma=Label(prizmapencere,font="italic 30 bold")
    sonuç_etiket_prizma.place(x=420,y=250)    


def prizma_hesapla():
    hacim_etiket=Label(prizmapencere,text="HACİM DEĞERİ",fg="orange",font="italic 25 bold")
    hacim_etiket.place(x=390,y=150)
    sonuçprizma=float(girişA.get()) * float(girişB.get()) * float(girişH.get())  / 3
    sonuç_etiket_prizma["fg"]="blue"
    sonuç_etiket_prizma["bg"]="white"
    sonuç_etiket_prizma["text"]=""
    sonuç_etiket_prizma["text"]=sonuçprizma
    girişA.delete(0,END)
    girişB.delete(0,END)
    girişH.delete(0,END)


def silindir():
    global silindirpencere
    global girişsilindirr
    global sonuç_etiket_silindir
    global girişsilindirh

    silindirpencere=Toplevel()
    silindirpencere.geometry("1000x598")
    silindirpencere.resizable(width=FALSE,height=FALSE)
    
    arkaplan_silindir=Label(silindirpencere,image=resim_silindir)
    arkaplan_silindir.pack()


    girişsilindirr=Entry(silindirpencere)
    girişsilindirr.place(x=50,y=160)

    girişsilindirh=Entry(silindirpencere)
    girişsilindirh.place(x=50,y=330)

    son_buton=Button(silindirpencere,text="HESAPLA",bg="orange",fg="white",font="italic 15 bold",command=silindir_hesapla)
    son_buton.place(x=60,y=400)

    sonuç_etiket_silindir=Label(silindirpencere,font="italic 30 bold")
    sonuç_etiket_silindir.place(x=420,y=250)


def silindir_hesapla():
    hacim_etiket=Label(silindirpencere,text="HACİM DEĞERİ",fg="blue",font="italic 25 bold")
    hacim_etiket.place(x=390,y=150)
   
    silindirsonuç=3.14  * (float(girişsilindirr.get()) ** 2  ) * float(girişsilindirh.get())  
    sonuç_etiket_silindir["fg"]="blue"
    sonuç_etiket_silindir["bg"]="white"
    sonuç_etiket_silindir["text"]=""
    sonuç_etiket_silindir["text"]=silindirsonuç

    girişsilindirr.delete(0,END)
    girişsilindirh.delete(0,END)













seç1=Button(text="seç",bg="black",fg="red",font="italic 12 bold",command=kare)
seç1.place(x=80,y=430)

seç2=Button(text="seç",bg="black",fg="red",font="italic 12 bold",command=küre)
seç2.place(x=295,y=430)

seç3=Button(text="seç",bg="black",fg="red",font="italic 12 bold",command=koni)
seç3.place(x=490,y=430)

seç4=Button(text="seç",bg="black",fg="red",font="italic 12 bold",command=prizma)
seç4.place(x=680,y=430)

seç5=Button(text="seç",bg="black",fg="red",font="italic 12 bold",command=silindir)
seç5.place(x=870,y=430)


mainloop()
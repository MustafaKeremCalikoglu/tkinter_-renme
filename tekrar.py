from tkinter import *
import random
from random import choice

pencere=Tk()
pencere.title("ingilizce kelime ezberleme uygulması")
pencere.geometry("350x350")
pencere.config(bg="blue")


sözlük={"postpone":"ertelem","prefer":"tercih etmek","produce":"üretmek","promise":"söz vermek","propose":"teklif vermek",
        "protect":"korumak","prove":"ispatlamak","provide":"sağlamak","punish":"cezalandırmak","rain":"yağmur",
        "raise":"artırmak","realize":"gerçekleştirmek","receive":"teslim almak","recognize":"tanımak,fark etmek","recommend":"tavsiyede bulunmak",
        "record":"kaydetmek","reduce":"azaltmak","reject":"itiraz etmek","relax":"rahatlamak","release":"serbest bırakmak"


        }

ingilizce=list(sözlük.keys())
türkçe=list(sözlük.values())
a=random.randint(0,len(türkçe)-1)
def onayla():
    global a    
    global lbl_soru    
    global etiket
    global cevap
    if ingilizce[a]==y.get():
            
        etiket=Label(text="bildiniz",bg="green",fg="white",font="times 20 bold").place(x=130,y=160)
        a=random.randint(0,len(türkçe)-1)
        lbl_soru["text"]=türkçe[a]
        lbl_soru.place(x=120,y=30)
        gir_cevap.delete(0,END)


    else:
        
        etiket=Label(text="!!!bilemediniz!!!",bg="red",fg="black",font="times 20 bold")
        etiket.place(x=105,y=160)
        cevap=Label(text=ingilizce[a]+"=="+türkçe[a],bg="blue",fg="black",font="times 16 bold")
        cevap.place(x=50,y=220)
        cevap["text"]=ingilizce[a]+"=="+türkçe[a]
        a=random.randint(0,len(türkçe)-1)
        lbl_soru["text"]=türkçe[a]
        lbl_soru.place(x=120,y=30)                
        gir_cevap.delete(0,END)


a=random.randint(0,len(türkçe)-1)
    
y=StringVar()

lbl_soru=Label(text=türkçe[a],bg="blue",fg="red",font="calibri 20 bold")
lbl_soru.place(x=120,y=30)
gir_cevap=Entry(font="calibri 15 bold",textvariable=y)
gir_cevap.place(x=85,y=80,width=200,height=35)
okey_but=Button(text="onayla",command=onayla).place(x=160,y=120)






















mainloop()


















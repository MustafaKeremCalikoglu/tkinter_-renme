from tkinter import *
import random
from random import choice

pencere=Tk()
pencere.title("ingilizce kelime ezberleme uygulması")
pencere.geometry("350x350")
pencere.config(bg="blue")


sözlük={"postpone":"ertelemek","prefer":"tercih etmek","produce":"üretmek","promise":"söz vermek","propose":"teklif vermek",
        "protect":"korumak","prove":"ispatlamak","provide":"sağlamak","punish":"cezalandırmak","rain":"yağmur",
        "raise":"artırmak","realize":"gerçekleştirmek","receive":"teslim almak","recognize":"tanımak,fark etmek","recommend":"tavsiyede bulunmak",
        "record":"kaydetmek","reduce":"azaltmak","reject":"itiraz etmek","relax":"rahatlamak","release":"serbest bırakmak"


        }

ingilizce=list(sözlük.keys())
türkçe=list(sözlük.values())
a=random.randint(0,len(türkçe)-1)


etiket=Label(bg="blue",fg="white",font="times 20 bold")
etiket.pack(side=BOTTOM)

b=0
puan=Label(text=b,bg="black",fg="white",font="times 14 italic")
puan.place(x=300,y=0)

def onayla():
    global a    
    global etiket
    global b 
    if ingilizce[a]==gir_cevap.get():
        etiket["bg"]="green"    
        etiket["text"]="BİLDİNİZ"
        a=random.randint(0,len(türkçe)-1)
        lbl_soru["text"]=türkçe[a]
        lbl_soru.pack(side=TOP,pady=5)
        gir_cevap.delete(0,END)
        dogrusu["text"]=""
        dogrusu["bg"]="blue"
        b=b+1 
        puan["text"]=b   

    else:
        etiket["bg"]="red"
        etiket["text"]="bilemediniz"
        dogrusu["bg"]="white"
        dogrusu["text"]=ingilizce[a]+"=="+türkçe[a]
        a=random.randint(0,len(türkçe)-1)
        lbl_soru["text"]=türkçe[a]
        lbl_soru.pack(side=TOP,pady=5)
        gir_cevap.delete(0,END)
        b=b-1 
        puan["text"]=b  



lbl_soru=Label(text=türkçe[a],bg="blue",fg="red",font="calibri 20 bold")
lbl_soru.pack(side=TOP,pady=5)
gir_cevap=Entry(font="calibri 15 bold")
gir_cevap.pack(pady=5)
okey_but=Button(text="onayla",command=onayla)
okey_but.pack(pady=8)


dogrusu=Label(bg="blue",fg="black",font="times 16 bold")
dogrusu.pack(pady=8)







mainloop()
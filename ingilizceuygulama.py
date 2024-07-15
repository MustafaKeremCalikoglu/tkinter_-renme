from tkinter import *
import random
from PIL import Image,ImageTk

pencere=Tk()
pencere.title("ingilizce kelime ezberleme uygulması")
pencere.geometry("589x521")
pencere.resizable(width=FALSE,height=FALSE)
resim=ImageTk.PhotoImage(Image.open("images.png"))
arkaplan=Label(pencere,image=resim)
arkaplan.pack()

pencere.config(bg="blue")


sözlük={"postpone":"ertelemek","prefer":"tercih etmek","produce":"üretmek","promise":"söz vermek","propose":"teklif vermek",
      


        }

ingilizce=list(sözlük.keys())
türkçe=list(sözlük.values())
a=random.randint(0,len(türkçe)-1)


etiket=Label(bg="blue",fg="white",font="times 20 bold")
etiket.place(relx=0.7,rely=0.9)

b=0
puan=Label(text=b,bg="black",fg="white",font="times 35 italic")
puan.place(x=500,y=20)



bos=[]
t=0

def onayla():
    global a    
    global etiket
    global b
    global bos
    global türkçe
    global ingilizce
    if ingilizce[a]==gir_cevap.get():
        etiket["bg"]="green"    
        etiket["text"]="BİLDİNİZ"
        türkçe.pop(a)
        ingilizce.pop(a)
        dogrusu["text"]=""
        dogrusu["bg"]="blue"
        b=b+1 
        puan["text"]=b   
        if len(türkçe)==0 :
            label_kazandın=Label(text="KAZANDIN",bg="green",fg="white",font="times 50 italic")
            label_kazandın.place(relx=0.2,rely=0.4)
            
        a=random.randint(0,len(türkçe)-1)
        lbl_soru["text"]=türkçe[a]
        gir_cevap.delete(0,END)
                      
    else:
        etiket["bg"]="red"
        etiket["text"]="bilemediniz"
        dogrusu["bg"]="orange"
        dogrusu["text"]=ingilizce[a]+"=="+türkçe[a]
        a=random.randint(0,len(türkçe)-1,0)
        lbl_soru["text"]=türkçe[a]
        gir_cevap.delete(0,END)
        b=b-1 
        puan["text"]=b  
    


lbl_soru=Label(text=türkçe[a],bg="blue",fg="red",font="calibri 20 bold")
lbl_soru.place(relx=0.30,rely=0.1)
gir_cevap=Entry(font="calibri 15 bold")
gir_cevap.place(relx=0.30,rely=0.2)
okey_but=Button(text="onayla",command=onayla)
okey_but.place(relx=0.3,rely=0.3)


dogrusu=Label(bg="blue",fg="black",font="times 16 bold")
dogrusu.place(relx=0.35,rely=0.45)







mainloop()
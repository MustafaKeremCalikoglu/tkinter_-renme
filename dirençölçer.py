from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter.ttk import Combobox

pencere=Tk()

pencere.title("direnç ölçer")
pencere.geometry("500x500")

resim=ImageTk.PhotoImage(Image.open("C:/Users/malik&mustafa/Desktop/dirençölçer.png"))
resim_label=Label(pencere,image=resim)
resim_label.pack()

#dört bantlı direnç başlangıç
z=IntVar()
z.set(0)

buton1=Radiobutton(text="1",variable=z,value="1")
buton1.place(x=20,y=5)

buton2=Radiobutton(text="2",variable=z,value="2")
buton2.place(x=60,y=5)







def bas():
    global buton1
    
    if z.get()==1 :
        label_4=Label(pencere,text="4 bantlı dirençler için renk kodu okuma",bg="black",fg="white",font="verdana 10 bold")
        label_4.place(x=10,y=50)

        liste1=["kahverengi","kirmizi","turuncu","sarı","yeşil","mavi","mor","gri","beyaz"]
        kutu1=Combobox(pencere,values=liste1)
        kutu1.place(x=10,y=90,width=80)

        liste2=["siyah","kahverengi","kirmizi","turuncu","sarı","yeşil","mavi","mor","gri","beyaz"]
        kutu2=Combobox(pencere,values=liste2)
        kutu2.place(x=100,y=90,width=80)

        liste3=["siyah","kahverengi","kirmizi","turuncu","sarı","yeşil","mavi","altın","gümüş"]

        kutu3=Combobox(pencere,values=liste3)
        kutu3.place(x=190,y=90,width=80)

        liste4=["kahverengi","kırmızı","altın","gümüş"]
        kutu4=Combobox(pencere,values=liste4)
        kutu4.place(x=280,y=90,width=80)

        def hesap():
            if len(kutu1.get())==0 or len(kutu2.get())==0  or len(kutu3.get())==0 or len(kutu4.get())==0 :
                messagebox.showinfo("lütfen boş bırakma",message="boş alanları doldur")
            else:
                sözlük1={"siyah":0,"kahverengi":1,"kirmizi":2,"turuncu":3,"sarı":4,"yeşil":5,"mavi":6,"mor":7,"gri":8,"beyaz":9}
                sözlük2={"siyah":1,"kahverengi":10,"kirmizi":100,"turuncu":1000,"sarı":10000,"yeşil":100000,"mavi":1000000,"altın":0.1,"gümüş":0.01}
                sözlük3={"kahverengi":1,"kırmızı":2,"altın":5,"gümüş":10}
                değer1=kutu1.get()
                değer2=kutu2.get()
                değer3=kutu3.get()
                değer4=kutu4.get()
                #ohm ve toleransın string değerleri
                ohm=str(sözlük1[değer1])+str(sözlük1[değer2])+"x"+str(sözlük2[değer3])
                tolerans="%"+str(sözlük3[değer4])

                label_ohm=Label(pencere,text=ohm,bg="red",fg="black",font="italic 12 bold")
                label_ohm.place(x=10,y=120,width=150)

                label_tolerans=Label(pencere,text=tolerans,bg="red",fg="black",font="italic 12 bold")
                label_tolerans.place(x=10,y=150,width=150)

                #ohm ve toleransın integer değerleri
                
                ohm_sayi=  ( sözlük1[değer1]*10  +sözlük1[değer2]  )  * sözlük2[değer3]
                tolerans_sayi=(ohm_sayi * sözlük3[değer4] ) /100

                label_ohmsayi=Label(pencere,text=ohm_sayi,bg="red",fg="black",font="italic 12 bold")
                label_ohmsayi.place(x=170,y=120,width=150)
                
                labeltolerans_sayi=Label(pencere,text=tolerans_sayi,bg="red",fg="black",font="italic 12 bold")
                labeltolerans_sayi.place(x=170,y=150,width=150)

                
                
        buton1=Button(pencere,text="HESAPLA",command=hesap)
        buton1.place(x=370,y=87)


bas=Button(text="bas",command=bas)
bas.place(x=120,y=5)


mainloop()
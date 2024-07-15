from tkinter import *
from PIL import Image,ImageTk

pencere=Tk()
pencere.config(bg="yellow")
pencere.resizable(width=FALSE,height=FALSE)

pencere.title("HACI CELAL APARTMANI su parası hesaplama")
pencere.geometry("850x510")
resim=ImageTk.PhotoImage(Image.open("dedem.jpg"))
arkaplan=Label(pencere,image=resim)
arkaplan.pack()



label_baslık1=Label(pencere,text="eski su saati",font="italic 15 bold")
label_baslık1.place(x=80,y=10)

label_baslık2=Label(pencere,text="yeni su saati",font="italic 15 bold")
label_baslık2.place(x=240,y=10)

label_baslık3=Label(pencere,text="fark",font="italic 15 bold")
label_baslık3.place(x=400,y=10)

label_tutar=Label(text="tutar",font="italic 15 bold")
label_tutar.place(x=500,y=10)

label_başlık4=Label(text="HACI CELAL APARTMANI",bg="black",fg="white",font="italic 30 bold")
label_başlık4.place(x=150,y=420)

##########################################################3
d1=Label(pencere,text="daire 1:",font="italic 12 bold")
d1.place(x=10,y=45)

d2=Label(pencere,text="daire 2:",font="italic 12 bold")
d2.place(x=10,y=75)

d3=Label(pencere,text="daire 3:",font="italic 12 bold")
d3.place(x=10,y=105)

d4=Label(pencere,text="daire 4:",font="italic 12 bold")
d4.place(x=10,y=135)

d5=Label(pencere,text="daire 5:",font="italic 12 bold")
d5.place(x=10,y=165)

d6=Label(pencere,text="daire 6:",font="italic 12 bold")
d6.place(x=10,y=195)

d7=Label(pencere,text="daire 7:",font="italic 12 bold")
d7.place(x=10,y=225)

##############################################3


d1_giris=Entry(pencere)
d1_giris.place(x=80,y=45)

d2_giris=Entry(pencere)
d2_giris.place(x=80,y=75)

d3_giris=Entry(pencere)
d3_giris.place(x=80,y=105)

d4_giris=Entry(pencere)
d4_giris.place(x=80,y=135)

d5_giris=Entry(pencere)
d5_giris.place(x=80,y=165)

d6_giris=Entry(pencere)
d6_giris.place(x=80,y=195)

d7_giris=Entry(pencere)
d7_giris.place(x=80,y=225)

#####################################################333

d1_giris2=Entry(pencere)
d1_giris2.place(x=240,y=45)

d2_giris2=Entry(pencere)
d2_giris2.place(x=240,y=75)

d3_giris2=Entry(pencere)
d3_giris2.place(x=240,y=105)

d4_giris2=Entry(pencere)
d4_giris2.place(x=240,y=135)

d5_giris2=Entry(pencere)
d5_giris2.place(x=240,y=165)

d6_giris2=Entry(pencere)
d6_giris2.place(x=240,y=195)

d7_giris2=Entry(pencere)
d7_giris2.place(x=240,y=225)






def hesaplafark():
    fark1=int(d1_giris2.get())-int(d1_giris.get())
    fark2=int(d2_giris2.get())-int(d2_giris.get())
    fark3=int(d3_giris2.get())-int(d3_giris.get())
    fark4=int(d4_giris2.get())-int(d4_giris.get())
    fark5=int(d5_giris2.get())-int(d5_giris.get())
    fark6=int(d6_giris2.get())-int(d6_giris.get())
    fark7=int(d7_giris2.get())-int(d7_giris.get())
    toplam=fark1+fark2+fark3+fark4+fark5+fark6+fark7


    label_fark1=Label(text=fark1,fg="black",bg="white",font="italic 10 bold")
    label_fark1.place(x=405,y=45)
    label_fark2=Label(text=fark2,fg="black",bg="white",font="italic 10 bold")
    label_fark2.place(x=405,y=75)
    label_fark3=Label(text=fark3,fg="black",bg="white",font="italic 10 bold")
    label_fark3.place(x=405,y=105)
    label_fark4=Label(text=fark4,fg="black",bg="white",font="italic 10 bold")
    label_fark4.place(x=405,y=135)
    label_fark5=Label(text=fark5,fg="black",bg="white",font="italic 10 bold")
    label_fark5.place(x=405,y=165)
    label_fark6=Label(text=fark6,fg="black",bg="white",font="italic 10 bold")
    label_fark6.place(x=405,y=195)
    label_fark7=Label(text=fark7,fg="black",bg="white",font="italic 10 bold")
    label_fark7.place(x=405,y=225)
   
   
   
    label_toplam=Label(fg="blue",bg="yellow",font="italic 15 bold")
    label_toplam.place(x=405,y=255)
    label_toplam["text"]=toplam

    birimfiyat=float(giris_toplamsuparası.get())  /  float(toplam)
    birim_fiyat["text"]=birimfiyat,"₺"
    #####################   tutar

    tutar1=Label(text=birimfiyat*fark1,bg="red",font="italic 13 bold")
    tutar1.place(x=510,y=45)
    tutar2=Label(text=birimfiyat*fark2,bg="red",font="italic 13 bold")
    tutar2.place(x=510,y=75)
    tutar3=Label(text=birimfiyat*fark3,bg="red",font="italic 13 bold")
    tutar3.place(x=510,y=105)
    tutar4=Label(text=birimfiyat*fark4,bg="red",font="italic 13 bold")
    tutar4.place(x=510,y=135)    
    tutar5=Label(text=birimfiyat*fark5,bg="red",font="italic 13 bold")
    tutar5.place(x=510,y=165)
    tutar6=Label(text=birimfiyat*fark6,bg="red",font="italic 13 bold")
    tutar6.place(x=510,y=195)
    tutar7=Label(text=birimfiyat*fark7,bg="red",font="italic 13 bold")
    tutar7.place(x=510,y=225)

    label_tutartoplam=Label(fg="blue",bg="yellow",font="italic 15 bold")
    label_tutartoplam.place(x=510,y=255)
    
    
    totaltoplam=birimfiyat*toplam
    label_tutartoplam["text"]=totaltoplam,"₺"












label_toplamsuparası=Label(text="su faturası tutarı",bg="yellow",font="italic 15 bold")
label_toplamsuparası.place(x=140,y=330)
giris_toplamsuparası=Entry(pencere)
giris_toplamsuparası.place(x=150,y=370)

etiket_birimfiyat=Label(text="birim fiyat",bg="red",font="italic 13 bold")
etiket_birimfiyat.place(x=380,y=300)

birim_fiyat=Label(bg="yellow",font="italic 13 bold")
birim_fiyat.place(x=400,y=350)



hesaplama_dugme=Button(pencere,text="hesapla",command=hesaplafark)
hesaplama_dugme.place(x=180,y=300)














mainloop()
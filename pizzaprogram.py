from tkinter import *
from tkinter import messagebox

pencere=Tk()
pencere.geometry("500x500")
pencere.title("pizza sipariş programı")


baslık=Label(text="pizza sipariş programına hoşgeldiniz",fg="black",bg="green",font="times 17 bold")
baslık.pack()

Label_ad=Label(text="ad,soyad    :",bg="pink",font="calibri 12 italic").place(x=10,y=40)
Label_boyut=Label(text="boyut         :",bg="pink",font="calibri 12 italic").place(x=10,y=70)
Label_icindekiler=Label(text="içindekiler :",bg="pink",font="calibri 12 italic").place(x=10,y=100)
Label_adres=Label(text="adres         :",bg="pink",font="calibri 12 italic").place(x=10,y=130)

deger4=StringVar()
deger5=StringVar()

giris_ad=Entry(textvariable=deger4).place(x=100,y=40,width=250)
giris_adres=Entry(textvariable=deger5).place(x=100,y=130,width=250)



boyut=StringVar()

rdio_kucuk=Radiobutton(text="küçük",activebackground="green",value="küçük boy",variable=boyut).place(x=100,y=70)
rdio_orta=Radiobutton(text="orta",activebackground="green",value="orta boy",variable=boyut).place(x=180,y=70)
rdio_kucuk=Radiobutton(text="büyük",activebackground="green",value="büyük boy",variable=boyut).place(x=250,y=70)


x=IntVar()
deger1=StringVar()
deger1.set(0)
y=IntVar(0)
deger2=StringVar()
deger2.set(0)

z=IntVar()
deger3=StringVar()
deger3.set(0)

cek_sucuk=Checkbutton(text="sucuk",variable=deger1,onvalue="sucuk").place(x=100,y=100)
cek_mısır=Checkbutton(text="mısır",variable=deger2,onvalue="mısır").place(x=180,y=100)
cek_acılısos=Checkbutton(text="acılı sos",variable=deger3,onvalue="acılı sos").place(x=250,y=100)

def siparişver():
    Label_bilgi=Label(text="sipariş bilgileri",bg="green",font="times 15 bold").place(x=150,y=220)
    Label_adı=Label(text="ad,soyad    :",bg="pink",font="calibri 12 italic").place(x=10,y=250)
    Label_boyutu=Label(text="boyut         :",bg="pink",font="calibri 12 italic").place(x=10,y=280)
    Label_icindekileri=Label(text="içindekiler :",bg="pink",font="calibri 12 italic").place(x=10,y=310)
    Label_adresi=Label(text="adres         :",bg="pink",font="calibri 12 italic").place(x=10,y=340)


    siparis_adi=Label(text=deger4.get(),fg="black",font="times 12 bold").place(x=100,y=250)
    siparis_adres=Label(text=deger5.get(),fg="black",font="times 12 bold").place(x=100,y=340)
    
    

    siparis_icindekiler=Label(text=deger1.get()+'  '+deger2.get()+"  "+deger3.get(),fg="black",font="times 12 bold").place(x=100,y=310)
    siparis_boyut=Label(text=boyut.get(),fg="black",font="times 12 bold").place(x=100,y=280)
def iptal():
    pencere.quit()



siparis=Button(text="sipariş ver",activebackground="green",command=siparişver).place(x=150,y=170)
iptal=Button(text="iptal",activebackground="green",command=iptal).place(x=230,y=170)



#sipariş bilgileri






















mainloop()


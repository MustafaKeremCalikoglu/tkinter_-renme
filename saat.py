from tkinter import*
import time


pencere=Tk()
pencere.title("saat")
pencere.geometry("250x200+500+250")
pencere.config(bg="yellow")


def zaman():
    zaman_formatı=time.strftime("%H:%M:%S")
    zaman_label["text"]=zaman_formatı
    zaman_label.after(200,zaman)

zaman_label=Label(bg="white",font="times 35 bold")
zaman_label.place(relx=0.15,rely=0.40)
zaman()


label_baslık=Label(text="dijital saat uygulaması",bg="yellow",font="times 15 bold").pack()


mainloop()
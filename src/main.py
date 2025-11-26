import tkinter as tk #GUI oluşturmak için gerekli kütüphane 
import time # Geri sayım için saniye bekleme


#Konsol için geri sayım fonksiyonu 

def geri_sayim(saniye):
    while saniye>0:
        print(f"Kalan süre:{saniye} saniye",end="\r") #end="\r" aynı satırda güncelleme yapar
        time.sleep(1) # 1 saniye bekler
        saniye-=1
    print("\n Süre doldu!")

#Kullanıcıdan süre al 
sure = int(input("kaç saniye geri sayim:"))
geri_sayim(sure)

#Konsol Menusu

def zamanlayici_menusu():
    print("Basit Zamanlayici")
    saniye = int(input("Kaç saniye geri sayim:"))
    geri_sayim(saniye)

if __name__ =="__main__":
    zamanlayici_menusu()


import tkinter as tk
import time

def baslat_gui():
    try:
        saniye = int(entry.get())
        while saniye > 0:
            label.config(text=f"Kalan süre: {saniye} saniye")
            root.update()
            time.sleep(1)
            saniye -= 1
        label.config(text="⏰ Süre doldu!")
    except ValueError:
        label.config(text="Lütfen geçerli bir sayı girin!")

root = tk.Tk()
root.title("Basit Zamanlayıcı")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Başlat", command=baslat_gui)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()

# timer
Simple Python countdown timer with console and Tkinter GUI support.
Tamam Serhat! 😎 İşte **tek bir README.md** dosyası, tüm projeyi kapsıyor: **Konsol ve GUI kullanım rehberi dahil**, GitHub’a direkt koyabilirsin.

````markdown
# Basit Zamanlayıcı ⏱️

Basit bir Python zamanlayıcı uygulaması.  
Hem **Konsol** hem de **GUI (Tkinter)** versiyonu vardır.

## Özellikler
- Konsol üzerinde geri sayım
- GUI ile kullanıcı dostu arayüz
- Hatalı giriş kontrolü
- Süre dolduğunda ekrana mesaj gösterir

## Kullanım

### Konsol versiyonu
1. `src/main.py` dosyasını çalıştırın:
```bash
python src/main.py
````

2. Konsol menüsünde süre girin → geri sayım başlasın

### GUI versiyonu

1. Konsol menüsü kodunu kapatın veya yorumlayın:

```python
# zamanlayici_menusu()  # Konsol menüsünü devre dışı bırakın
```

2. Tkinter GUI kodu aktif olmalı (`root.mainloop()` dahil)
3. Python ile çalıştırın:

```bash
python src/main.py
```

4. Küçük bir pencere açılacak → Entry’ye süre girin → Başlat butonuna basın → Label’da geri sayım görünecek
5. Süre bittiğinde Label “⏰ Süre doldu!” mesajını gösterecek

## Gereksinimler

* Python 3.x
* Tkinter (GUI için)

## İleri Geliştirme Önerileri

* Dakika:saniye formatı ekleyin
* Sesli alarm ekleyin (`winsound` veya `playsound`)
* Arka plan renk veya tema ekleyin
* Birden fazla alarm ekleyin
* Süreleri JSON’a kaydedin

```


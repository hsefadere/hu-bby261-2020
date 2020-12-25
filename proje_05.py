from tkinter import *
import time
import datetime
import sqlite3
from tkinter import ttk

penvcer= Tk()
baslik = penvcer.title("Sosyal Medya Tablosu")

def websitem():
    pencere2 = Toplevel()
    butoncv.destroy()
    butoncd.destroy()
    def dosya():

        veritabani = sqlite3.connect('veritabani.db')


        komut = veritabani.cursor()

        komut.execute('''
                         CREATE TABLE IF NOT EXISTS mesajlar 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        ad text NOT NULL, 
                        sosyal text NOT NULL, 
                        eposta text NOT NULL,
                         fiyat INT NOT NULL,
                          tarih text NOT NULL)
                        ''')


        veritabani.commit()

        veritabani.close()

    def bilgiler():

        veritabani = sqlite3.connect('veritabani.db')

        komut = veritabani.cursor()
        saat = time.time()
        zaman = str(datetime.datetime.fromtimestamp(saat).strftime("%y.%m.%d - %H.%M"))


        komut.execute("INSERT INTO mesajlar ('ad','sosyal','eposta', 'fiyat', 'tarih') VALUES (?,?,?,?,?)"
                      , (ad1.get(), sosyall.get(), epostaa.get(), fiyatt.get(), zaman))

        veritabani.commit()
        veritabani.close()

    def sonuc():

        veritabani = sqlite3.connect('veritabani.db')


        komut = veritabani.cursor()

        sonuc1.delete(*sonuc1.get_children())
        for kayitlar in komut.execute('SELECT * from mesajlar'):
            sonuc1.insert("","end",text="kayıtlar",values=kayitlar)

    def silme():
        veritabani = sqlite3.connect('veritabani.db')


        komut = veritabani.cursor()
        sonuc1.delete(*sonuc1.get_children())
        komut.execute("DELETE FROM mesajlar WHERE id = ?", (id2.get()))
        veritabani.commit()

    def güncelleme():
        veritabani = sqlite3.connect('veritabani.db')


        komut = veritabani.cursor()
        sonuc1.delete(*sonuc1.get_children())
        yenieposta = yeni.get()
        komut.execute("UPDATE mesajlar SET ad = ?, sosyal = ?, eposta = ?, fiyat = ? WHERE id = ?", (yeniad.get(), yenisosyal.get(), yenieposta, yenifiyat.get(), epostaE.get()))




        veritabani.commit()

    def arama():
        veritabani = sqlite3.connect('veritabani.db')
        komut = veritabani.cursor()

        komut.execute("SELECT * FROM mesajlar WHERE ad = ?", (ara.get(),))
        sonuc1.delete(*sonuc1.get_children())
        for kayitlar in komut.fetchall():
            sonuc1.insert("", "end", text="kayıtlar", values=kayitlar)
        veritabani.commit()

    def topla():
        veritabani = sqlite3.connect('veritabani.db')
        komut = veritabani.cursor()
        komut.execute("SELECT * FROM mesajlar")
        toplamalar = 0
        toplama.delete(0,END)
        for z in komut.fetchall():
            ab = z[4]
            toplamalar += ab
        toplama.insert(0,toplamalar)
        veritabani.commit()




    baslikk = Label(text="Sosyal Medya Tablosu",fg="black",bg="yellow",width="20", font=("Monotype Corsiva", 25))
    baslikk.grid(row=0, column=1)

    #-----------------------------------------------------------------------------

    etiket1 = Label(text="Dosya Oluşturma",fg="white",bg="#0f14dd",font=("Monotype Corsiva", 14))
    etiket1.grid(row=1, column=1)

    buton1 = Button(text="Dosya Oluştur",font=("cabria", 11), fg="red",command=dosya)
    buton1.grid(row=2, column=1)


    #-----------------------------------------------------------------------------

    etiket2 = Label(text="Bilgi Girişi",fg="white",bg="#0f14dd",font=("Monotype Corsiva", 14))
    etiket2.grid(row=5, column=0)

    isim = Label(text="Müşteri",font=("cabria", 10))
    isim.grid(row=6, column=0)

    ad1 = Entry(width=40)
    ad1.grid(row=7, column=0)

    sosmed = Label(text="Sosyal Medya",font=("cabria", 10))
    sosmed.grid(row=8, column=0)

    sosyall =Entry(width=40)
    sosyall.grid(row=9, column=0)

    mail = Label(text="E-posta",font=("cabria", 10))
    mail.grid(row=10, column=0)

    epostaa = Entry(width=40)
    epostaa.grid(row=11, column=0)

    mesajbilgisi = Label(text="Fiyat Bilgisi",font=("cabria", 10))
    mesajbilgisi.grid(row=12, column=0)

    fiyatt = Entry(width=40)
    fiyatt.grid(row=13, column=0)

    buton2 = Button(text="Kaydet",font=("cabria", 11), fg="red",command=bilgiler)
    buton2.grid(row=14, column=0)

    #-----------------------------------------------------------------------------


    etiket4 = Label(text="Sonuç",fg="white",bg="#0f14dd",font=("Monotype Corsiva", 14))
    etiket4.grid(row=19, column=1)

    sonuc1 = ttk.Treeview(pencere2)
    sonuc1.grid(row=20, column=1)
    sonuc1['columns'] = ('yeni','isim', 'sosyal medya', 'e-posta','fiyat','son')

    sonuc1.heading('yeni', text='Kayıt')
    sonuc1.column('yeni',anchor='center', width=20)

    sonuc1.heading('#1', text='ID')
    sonuc1.column('#1',anchor='center', width=60)

    sonuc1.heading('isim',text="Müsteri Adı")
    sonuc1.column('isim',anchor='center', width=180)

    sonuc1.heading('sosyal medya',text="Sosyal Medya")
    sonuc1.column('sosyal medya',anchor='center', width=180)

    sonuc1.heading('e-posta',text="E-posta")
    sonuc1.column('e-posta',anchor='center', width=180)

    sonuc1.heading('fiyat',text="Fiyat")
    sonuc1.column('fiyat',anchor='center', width=80)

    sonuc1.heading('son',text="Tarih")
    sonuc1.column('son',anchor='center', width=180)

    sonucb= Button(text="Sonuç",font=("cabria", 11), fg="red",command=sonuc)
    sonucb.grid(row=21, column=1)

    #-----------------------------------------------------------------------------
    baslik2 = Label(text="Silme Alanı",fg="white",bg="#0f14dd",font=("Monotype Corsiva", 14))
    baslik2.grid(row=6, column=1)

    id2 = Entry(width=40)
    id2.grid(row=7, column=1)

    buton3 = Button(text="ID numarası ile sil", font=("cabria", 11), fg="red", command=silme)
    buton3.grid(row=8, column=1)



    #-----------------------------------------------------------------------------

    baslik2 = Label(text="Arama Alanı",fg="white",bg="#0f14dd",font=("Monotype Corsiva", 14))
    baslik2.grid(row=10, column=1)

    ara = Entry(width=40)
    ara.grid(row=11, column=1)

    butonAra = Button(text="Ara", font=("cabria", 11), fg="red", command=arama)
    butonAra.grid(row=12, column=1)

    baslik4 =Label(text="Toplama İşlemi",fg="white",bg="#0f14dd",font=("Monotype Corsiva", 14))
    baslik4.grid(row=14, column=1)

    toplama = Entry(width=40)
    toplama.grid(row=15, column=1)

    toplamak = Button(text="Toplama", font=("cabria", 11), fg="red", command=topla)
    toplamak.grid(row=16, column=1)

    #-----------------------------------------------------------------------------

    baslik3 = Label(text="Güncelleme Alanı",fg="white",bg="#0f14dd",font=("Monotype Corsiva", 14))
    baslik3.grid(row=5, column=3)


    yeniadbaslık = Label(text="Yeni Müşteri adını yazınız",font=("cabria", 10))
    yeniadbaslık.grid(row=6, column=3)

    yeniad = Entry(width=40)
    yeniad.grid(row=7, column=3)

    sosyalbaslık = Label(text="Yeni Sosyal medyayı yazınız",font=("cabria", 10))
    sosyalbaslık.grid(row=8, column=3)

    yenisosyal = Entry(width=40)
    yenisosyal.grid(row=9, column=3)

    yenibaslik = Label(text="Yeni E-postayı yazınız",font=("cabria", 10))
    yenibaslik.grid(row=10, column=3)

    yeni = Entry(width=40)
    yeni.grid(row=11, column=3)

    fiyatbaslık = Label(text="Yeni fiyatı yazınız",font=("cabria", 10))
    fiyatbaslık.grid(row=12, column=3)

    yenifiyat = Entry(width=40)
    yenifiyat.grid(row=13, column=3)

    guncelleisim = Label(text="ID numarasını yazınız",font=("cabria", 10))
    guncelleisim.grid(row=14, column=3)

    epostaE = Entry(width=40)
    epostaE.grid(row=15, column=3)

    buton3 = Button(text="Güncelleme", font=("cabria", 11), fg="red", command=güncelleme)
    buton3.grid(row=16, column=3)

butoncd=Button(text="Sosyal Medya",command=websitem, font=("cabria", 11), fg="red")
butoncd.grid()
butoncv= Button(text="Web Sitesi", font=("cabria", 11), fg="red")
butoncv.grid()
mainloop()

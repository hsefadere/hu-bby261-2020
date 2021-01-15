from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import datetime
import locale
import webbrowser

pencer = Tk()
pencer.title("Burç")
pencer.geometry("1500x650")

locale.setlocale(locale.LC_ALL, '')
def gunlukburc():
    an = datetime.datetime.now()
    gun = str(datetime.datetime.now().day)
    ay = datetime.datetime.strftime(an, '%B').lower()
    tarihh = str(an.day) + "-" + ay + "-" + str(an.year)

    url= "https://www.elle.com.tr/astroloji/astroloji-haberleri/"+tarihh+"-gunluk-burc-yorumlari"
    conncet = requests.get(url)
    soep = BeautifulSoup(conncet.content,features = "html.parser" )

    listetext = []
    soup = soep.find_all("p",{"class":""})
    for y in range(len(soup)):

        if gun in soup[y].text:
            listetext.append(soup[y].text)
            listetext.append(soup[y+1].text)

    return listetext

def burcbulma(giris,giris2):
    dgun = int(giris.get())
    dAy = giris2.get().capitalize()
    yorum = gunlukburc()
    burc = ""

    if (dAy == "Ocak") :

        if(dgun > 20):

            burc += yorum[22] +"\n"+ yorum[23]
            
        else:
            burc += yorum[20] + yorum[21]
            

    elif (dAy == "Şubat"):
        if (dgun > 19):
            burc += yorum[24]+"\n"+ yorum[25]
            

        else:
            burc += yorum[22] +"\n"+ yorum[23]
            

    elif (dAy == "Mart"):
        if (dgun > 20):
            burc += yorum[2] +"\n"+ yorum[3]
            

        else:
            burc += yorum[24]+"\n"+ yorum[25]


    elif (dAy == "Nisan"):
        if (dgun > 20):
            burc += yorum[4]+"\n"+ yorum[5]


        else:
            burc += yorum[2] +"\n"+ yorum[3]


    elif (dAy == "Mayıs"):
        if (dgun > 21):
            burc += yorum[6] +"\n"+ yorum[7]


        else:
            burc += yorum[4] +"\n"+ yorum[5]


    elif (dAy == "Haziran"):
        if (dgun > 21):
            burc += yorum[8] +"\n"+ yorum[9]


        else:
            burc += yorum[6] +"\n"+ yorum[7]


    elif (dAy == "Temmuz"):
        if (dgun > 23):
            burc += yorum[10] +"\n"+ yorum[11]


        else:
            burc += yorum[8] + "\n" + yorum[9]


    elif(dAy == "Ağustos"):
        if (dgun > 23):
            burc += yorum[12] + "\n" + yorum[13]


        else:
            burc += yorum[10] +"\n"+ yorum[11]


    elif (dAy == "Eylül"):
        if (dgun > 23):
            burc += yorum[14] + "\n" + yorum[15]


        else:
            burc += yorum[12] + "\n" + yorum[13]


    elif (dAy == "Ekim"):
        if (dgun > 22):
            burc += yorum[16] + "\n" + yorum[17]


        else:
            burc += yorum[14] + "\n" + yorum[15]


    elif (dAy == "Kasım"):
        if (dgun > 22):
            burc += yorum[18] + "\n" + yorum[19]

        else:
            burc += yorum[16] + "\n" + yorum[17]


    elif (dAy == "Aralık"):
        if (dgun > 22):
            burc += yorum[20] + "\n" + yorum[21]


        else:
            burc += yorum[18] + "\n" + yorum[19]


    else:
        burc = "Yeniden Yazınız"

    mesaj = messagebox.showinfo("Burç Penceresi", burc)
    liste.delete(0,END)
    liste.insert(0,burc)


def Yorumlar(burcadi):

    liink = "https://www.elle.com.tr/astroloji/"+ burcadi.get().capitalize()+"/ozellik"
    conncet = requests.get(liink)
    soep = BeautifulSoup(conncet.content, features="html.parser")


    soup = soep.find_all("p", {"class": ""})

    del soup[14:27]
    liste.delete(0, END)
    for b in range(len(soup)):

        liste.insert(0,soup[b].text)
def uyum():
    url ="https://www.milliyet.com.tr/pembenar/ask-uyumu/"
    webbrowser.get().open(url)

def sayfa3():

    pencere3 = Toplevel()
    pencere3.geometry("250x150")

    etiket1 = Label(pencere3, text="Doğum Günü")
    giri1 = Entry(pencere3, width=20)
    etiket2 = Label(pencere3, text="Doğum Ayı")
    giri2 = Entry(pencere3, width=20)
    buton1 = Button(pencere3, text="Yorumla",command=lambda : burcbulma(giri1,giri2))
    etiket1.place(x=10, y=10)
    etiket2.place(x=10, y=50)
    giri1.place(x=100, y=10)
    giri2.place(x=100, y=50)
    buton1.place(x=50, y=90)

def sayfa2():

    pencere2 = Toplevel()
    pencere2.geometry("250x150")

    etiket1 = Label(pencere2, text="Burç")
    gir1 = Entry(pencere2, width=20)



    etiket1.place(x=10, y=10)
    gir1.place(x=100, y=10)
    etiket2 = Label(pencere2, text="Türkçe karakter girmeyiniz")
    etiket2.place(x=55, y=40)

    buton1 = Button(pencere2, text="Sonuç", command=lambda: Yorumlar(gir1))
    buton1.place(x=50, y=90)


baslık =Label(text="Burçlar ve Özellikleri",font="Verdana 20")
baslık.place(x=600, y=20)


but1 = Button(text="Burç Bulma ve Günlük Yorum",width=30,height=3,font="Verdana 10", command=sayfa3)
but1.place(x=50, y=60)


buuut= Button(text="Burç Bilgi",width=30,height=3,font="Verdana 10",command=sayfa2)
buuut.place(x=320,y=60)

but2 = Button(text="Uyumluluk Testi",width=30,height=3,font="Verdana 10", command=uyum)
but2.place(x=600, y=60)




kay =Scrollbar(pencer,orient= HORIZONTAL )
kay.pack(side=BOTTOM,fill=Y)


liste = Listbox(pencer,width=230,height=23,yscrollcommand=kay.get())
liste.place(x=50,y=150)
kay.config(command=liste.yview())





mainloop()

import requests
from bs4 import BeautifulSoup
import time,re


class Hisse:
    def __init__(self):
        self.dongu=True

    def program(self):
        secim=self.menu()
        if secim=="1":
            print("Güncel Fiyatlar Alınıyor..\n")
            time.sleep(2)
            self.guncelfiyat()
        if secim=="2":
            print("Künye Bilgileri Alınıyor..\n")
            time.sleep(2)
            self.kunye()
        if secim=="3":
            print("Cari Degerler Alınıyor..\n")
            time.sleep(2)
            self.carideger()
        if secim=="4":
            print("Şirket Getiri Bilgileri Alınıyor..\n")
            time.sleep(2)
            self.getiriler()
        if secim=="5":
            print("Şirketin Dahil Olduğu Endex Bilgileri Alınıyor..\n")
            time.sleep(2)
            self.dahilolunanendex()
        if secim=="6":
            print("Otomasyondan Cıkıs Yapılıyor..\n")
            time.sleep(2)
            self.cıkıs()


    def menu(self):
        def control(secim):
            if re.search("[^1-6]",secim):
                raise Exception ("lutfen 1 ve 6 arasında gecerlı bır secım yapınız")
            elif len(secim)!=1: #girilen degerın uzunlugunu burda 1 diye belırtmezsek 14 veya 41 gibi girilen degerlerde sistem icinde 1 ve 4 oldugu ıcın hata vermez
                raise Exception ("lutfen 1 ve 6 arasında gecerlı bır secım yapınız")
        while True:
            try:
                secim=input("Merhabalar Hisse Senetleri Bilgi Sistemine Hosgeldiniz.\n\nLutfen yapmak ıstedıgınız ıslemı secınız..\n\n1-Güncel Fiyatlar\n2-Künye Bilgileri\n3-Cari Degerler\n4-Şirket Getiri Bilgileri\n5-Şirketin Dahil Olduğu Endex Bilgileri\n6-Cıkıs Yap\n\n")
                control(secim)
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return secim 


    def guncelfiyat(self):
        while True: #donguye sokma nedenımız kısıden sırket kodu isteyecegiz, o kod yoksa tekrar sorması icin
            try:
                sirket=input("Lütfen Şirket Adı Giriniz: ")
                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/default.aspx"
                parser=BeautifulSoup(requests.get(url).content,"html.parser")
                #hisselerin oldugu kodları parser'a atadık.parser üzerindende hrefi kisinin girdigi alana yönlendirdik
                fiyat=parser.find("a",{"href":"/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket.upper())})\
                .parent.parent.find_all("td")
                bilgi_1=fiyat[1].string #sonfiyat
                bilgi_2=fiyat[2].span.string #degisim %
                bilgi_3=fiyat[3].string #degisim TL
                bilgi_4=fiyat[4].string #hacim TL
                bilgi_5=fiyat[5].string #hacim Adet
                #oncelıkle a etıketı href alanına ulastık. aradıgımız degera etıketı altında olmadıgı ıcın bir oncekı alana gectık oradakı td lerın bi üstü olan tdleri lıste halınde cektık. lıstedende ındexleme yaparak dıger degerlerı aldık
                print(f"Son Fiyat: {bilgi_1}\nDegisim-%: {bilgi_2.lstrip()}\rDegisim-TL: {bilgi_3}\nHacim-TL: {bilgi_4}\nHacim-Adet: {bilgi_5}\n\n")
                break
            except AttributeError: #aradıgımız hisse senedi bulunamayan bir sirket ismi girilirse alınacak hata
                print("HATALI BİR SİRKET ADI GİRDİNİZ..!!")
                time.sleep(2)
        time.sleep(2)
        self.menudon()


    def kunye(self):
        while True:
            try:
                sirket=input("Lütfen Şirket Adı Giriniz: ")
                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)
                parser=BeautifulSoup(requests.get(url).content,"html.parser")

                kunye=parser.find("div",{"id":"ctl00_ctl58_g_6618a196_7edb_4964_a018_a88cc6875488"})\
                .find_all("tr")
                for i in kunye:
                    bilgi_1=i.th.string
                    bilgi_2=i.td.string
                    print(f"{bilgi_1} : {bilgi_2}")
                break
            except AttributeError: #aradıgımız hisse senedi bulunamayan bir sirket ismi girilirse alınacak hata
                print("HATALI BİR SİRKET ADI GİRDİNİZ..!!")
                time.sleep(2)
        time.sleep(2)
        self.menudon()


    def carideger(self):
        while True: 
            try:
                sirket=input("Lütfen Şirket Adı Giriniz: \n")
                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)
                parser=BeautifulSoup(requests.get(url).content,"html.parser")

                carideger=parser.find("div",{"id":"ctl00_ctl58_g_76ae4504_9743_4791_98df_dce2ca95cc0d"})\
                .find_all("tr")
                for i in carideger:
                    bilgi_1=i.th.string
                    bilgi_2=i.td.string
                    print(f"{bilgi_1} : {bilgi_2}\n")
                break
            except AttributeError: #aradıgımız hisse senedi bulunamayan bir sirket ismi girilirse alınacak hata
                print("HATALI BİR SİRKET ADI GİRDİNİZ..!!")
                time.sleep(2)
        time.sleep(2)
        self.menudon()


    def getiriler(self):
        while True: 
            try:
                sirket=input("Lütfen Şirket Adı Giriniz: \n")
                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)
                parser=BeautifulSoup(requests.get(url).content,"html.parser")

                getiri=parser.find("div",{"id":"ctl00_ctl58_g_aa8fd74f_f3b0_41b2_9767_ea6f3a837982"}).find("table")\
                .find("tbody").find_all("tr")

                for i in getiri:
                    bilgi=i.find_all("td")
                    print(f"Birim: {bilgi[0].string} Gün(%): {bilgi[1].string} Hafta(%): {bilgi[2].string} Ay(%): {bilgi[3].string} Yıl(%): {bilgi[4].string}")
                break
            except AttributeError: #aradıgımız hisse senedi bulunamayan bir sirket ismi girilirse alınacak hata
                print("HATALI BİR SİRKET ADI GİRDİNİZ..!!")
                time.sleep(2)
        time.sleep(2)
        self.menudon()


    def dahilolunanendex(self):
        while True: 
            try:
                sirket=input("Lütfen Şirket Adı Giriniz: \n")
                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)
                parser=BeautifulSoup(requests.get(url).content,"html.parser")

                dahiliendex=parser.find("div",{"id":"ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"})\
                .find("table").find("tbody").find("tr").find_all("td")
                dahiliendex_2=parser.find("div",{"id":"ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"})\
                .find("table").find("thead").find("tr").find_all("th")

                for i in range(0,3):
                    print(f"{dahiliendex_2[i].string}:{dahiliendex[i].string}")
                break
            except AttributeError: #aradıgımız hisse senedi bulunamayan bir sirket ismi girilirse alınacak hata
                print("HATALI BİR SİRKET ADI GİRDİNİZ..!!")
                time.sleep(2)
        time.sleep(2)
        self.menudon()


    def menudon(self):
        while True:
            x=input(print("Ana menuye donmek ıcın 7, Cıkmak ıcın lutfen 6'e basınız.\n"))
            if x=="7":
                print("ana menuye dönüyorsunuz..")
                time.sleep(3)
                self.program()
                break
            elif x=="6":
                self.cıkıs()
                break
            else:
                print("gecerli bir deger giriniz.")


    def cıkıs(self):
        print("Hisse Senetleri Bilgi Sisteminden Cıkıs Yapılıyor...")
        time.sleep(3)
        self.dongu=False
        exit()

sistem=Hisse()
while sistem.dongu:
    sistem.program()

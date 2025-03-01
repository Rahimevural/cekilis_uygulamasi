import random
import time


kullanicilar = list()


def kullanici_ekle(x):
    print("-"*30)
    print("kullanıcı ekleme ekranına hoşgeldiniz")
    ekle = input("lütfen eklenecek kullanıcıyı yazınız : ")
    kullanicilar.append(ekle)
    input("Devam etmek için enter tuşuna basınız ")

def kullanici_gor(x):
    say = 1
    print("-"*30)
    for i in x:
        print(str(say) + " Kullanıcı Adı: " + str(i))
        say += 1 
    print("-"*30)
    input("Devam etmek için enter tuşuna basınız ")

def sec(x):
    print("-"*30)
    say = 1
    kisi_sec = int(input("Kaç kişi seçilsin?:")) 
    rastgele_sec = random.sample(x,kisi_sec)   

    for i in rastgele_sec:
        print(str(say) + " Kullanıcı Adı: " + str(i))
        say +=1 
        print("diğer kişi sistemden çekiliyor...")
        time.sleep(2)  
    print("-"*30)
    input("Devam etmek için enter tuşuna basınız ")

def salla(x):
    say = 1
    random.shuffle(x)
    for i in x:
       print(str(say) + " Kullanıcı Adı: " + str(i))
       say +=1 
    input("Devam etmek için enter tuşuna basınız ")

while True:
    print("***** ÇEKİLİŞ UYGULAMASINA HOŞGELDİNİZ *****")
    secim = int(input("1-Kullanıcı ekle\n2-Kullanıcı gör\n3-Kullanıcıları karıştır\n4-Rastgele seçim\n"))

    if secim ==1:
        kullanici_ekle(kullanicilar)
    elif secim ==2:    
        kullanici_gor(kullanicilar)
    elif secim ==3:
        salla(kullanicilar)
    elif secim ==4:
        print("Kişi seçme alanı hesaplanıyor...")
        time.sleep(2)
        sec(kullanicilar)  
    else:
        print("Lütfen uygun bir tercih yapınız!")         
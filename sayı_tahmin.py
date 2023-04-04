import random
import time


print("""
     Sayı tahmin oyunu
     
     
     1 ile 40 arasında sayıyı tahmin edin.

""")

rastegele_sayı = random.randint(1, 40) #randin ve randint fonksiyonlarını kullanarak rastgele sayı üretiyoruz. 1 ve 40 arasında sayı üretiyor.
tahmin_hakkı = 7 #tahmin hakkımız 7
while True:
    
    tahmin = int(input("Tahmininiz: ")) #tahmininizi kullanıcıdan alıyoruz.

    if (tahmin < rastegele_sayı):
        print("bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha büyük bir sayı giriniz.")
        tahmin_hakkı -= 1 #tahmin hakkı 1 azaltıyoruz.

    elif tahmin > rastegele_sayı:
        print("bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha küçük bir sayı giriniz.")
        tahmin_hakkı -= 1 #tahmin hakkı 1 azaltıyoruz.

    else:
        print("Tebrikler bildiniz.")
        break #tahmin doğruysa döngüden çıkıyoruz. 
    if tahmin_hakkı == 0:
        print("tahmin hakkınız bitti...")
        print("Sayı : ",rastegele_sayı)
        break



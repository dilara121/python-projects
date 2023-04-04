from time import time


import time
card_password = 5687
giris_hakki = 2
toplam_bakiye = 1500
# def in_out(a) fonksiyonları verdiğinde bu şekilde denicem

while True:
    sifre = int(input("Kart şifrenizi giriniz : "))
    time.sleep(2)
    if card_password == sifre:
        print("Şifreniz doğru sisteme hoş geldiniz...")
        
        while True:
            print("1)PARA YATIRMA\n"
                  "2)PARA ÇEKME\n"
                  "3)PARA GÖNDERME\n"
                  "4)BAKİYE SORGULAMA\n")
            islem = int(input("Yukarıdaki işlemlerden hangisini yapmak istiyorsanız o işlemin numarasını girin: "))
            time.sleep(3)
            if islem == 1:
                tutar = int(input("Yatırmak istediğiniz tutarı giriniz: "))
                print("Parayı açılan bölmeye yerleştirin.\nParallar sayılıyor...\nYatırılan tutar  {}\n".format(tutar))
                yeni_bakiye = toplam_bakiye + tutar
                print("Yeni bakiye : {} TL".format(yeni_bakiye))
                a = input("ATM den çıkış yapmak için 'Q' tuşuna, işlem menüsüne dönmek için 'X' tuşuna basın: ")
                if a == 'Q':
                    print("ATM den çıkılıyor. İyi günler. Tekrar bekleriz...")
                    break
                elif a == 'X':
                    continue
            if islem == 2:
                cekilen_tutar = int(input("Çekmek istediğiniz tutarı giriniz: "))
                if toplam_bakiye - cekilen_tutar < 0:
                    print("Bu kadar para çekemezsiniz...")
                else:
                    print("İşleminiz gerçekleştiriliyor...\nParanızı bölmeden alın.\nÇekilen tutar {}' TL".format(
                        cekilen_tutar))
                kalan_bakiye = toplam_bakiye - cekilen_tutar
                if kalan_bakiye >= 0:
                    print("Kalan Bakiye : {} TL".format(kalan_bakiye))
                else:
                    print("Toplam bakiyeniz : {} TL".format(toplam_bakiye))
                a = input("ATM den çıkış yapmak için 'Q' tuşuna, işlem menüsüne dönmek için 'X' tuşuna basın: ")
                if a == 'Q':
                    print("ATM den çıkılıyor. İyi günler. Tekrar bekleriz...")
                    break
                elif a == 'X':
                    continue
            if islem == 3:
                i_ban = input("Göndemek istediğiniz hesabın IBAN numarasanı girin: ")
                gonderilen_tutar = int(input("Göndermek istediğiniz tutarı girin: "))
                print("İşleminiz gerçekleştiriliyor...")
                kalan_bakiye = toplam_bakiye - gonderilen_tutar
                print("Kalan Bakiye : {}TL".format(kalan_bakiye))
                a = input("ATM den çıkış yapmak için 'Q' tuşuna, işlem menüsüne dönmek için 'X' tuşuna basın: ")
                if a == 'Q':
                    print("ATM den çıkılıyor. İyi günler. Tekrar bekleriz...")
                    break
                elif a == 'X':
                    continue
            if islem == 4:
                print("Toplam bakiyeniz {}' TL ".format(toplam_bakiye))
        break
    else:
        print("Şifreniz yanlış. {} giriş hakkınız kaldı.".format(giris_hakki))
        giris_hakki -= 1
    if giris_hakki >= 0:
        continue
    print("Tüm giriş haklarınızı kullandınız. Kartınız bloke edilmiştir. En yakın şubeden tekrar kullanıma "
          "açtırabilirsiniz.İYİ GÜNLER DİLERİZ...")
    break

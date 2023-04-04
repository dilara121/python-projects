print("""********************
Kulllanıcı Girişi
********************
""")

kullanici_adi = "dilara"
parola = "634722v65476"
# döngüyle kullanıcı bilgilerini doğru girene kadar veya giriş hakkı bitene kadar tekrar tekrar girdi isteyebiliriz.
giris_hakki = 5
while True:
    a = input("Kullanıcı Adınızı Giriniz : ")
    b = input("Parolanızı Giriniz : ")
    if kullanici_adi != a and parola != b:
        print("Gİrdiğiniz bilgiler yanlış."
              "Bilgilerinizi kontrol edip tekrar giriş yapmayı deneyin")
        giris_hakki -=1
    elif kullanici_adi != a:
        print("Kullanıcı adınızı yanlış girdiniz.Tekrar deneyin.")
        giris_hakki -=1
    elif parola != b:
        print("Parolanızı yanlış girdiniz.Tekrar deneyin.")
        giris_hakki -=1
    else:
        print("***Sistemimize Hoşgeldiniz***")
        break
    if ( giris_hakki == 0):
        print("giriş hakkınız doldu")
        break
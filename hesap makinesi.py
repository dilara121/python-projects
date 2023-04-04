print("""************************
Hesap Makinesi Programı 

İşlemler:

1.Toplama İşlemi

2.Çıkarma İşlemi 

3.Çarpma İşlemi

4.Bölme İşlemi
*************************
""")


a = int(input("Birinci sayı : "))
b = int(input("İkinci sayı : "))

işlem = input("İşlem giriniz : ")

if işlem == "1":
    print(f"İşlem sonucunuz : {a+b}\n")
elif işlem == "2":
    print(f"İşlem sonucunuz : {a-b}\n")
elif işlem == "3":
    print(f"İşlem sonucunuz : {a*b}\n")
elif işlem == "4":
    print(f"İşlem sonucunuz : {a/b}\n")
else:
    print("Girdiğiniz işlem bulunamadı. ")

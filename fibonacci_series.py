"""

Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur.
1,1,2,3,5,8,13,21,34...............

"""
son_sayi = int(input("Seriyi sonlandırmak istediğiniz sayıyı giriniz : "))
ilk_sayi = 1

ikinci_sayi = 1

fibonacci = [ilk_sayi,ikinci_sayi]
for i in range(son_sayi):
     ilk_sayi,ikinci_sayi = ikinci_sayi,ilk_sayi + ikinci_sayi

     fibonacci.append(ikinci_sayi)

print(fibonacci)
import math

print("Kök bulma programımıza hoşgeldiniz")
print("Formatı ax^2+ bx + c gibi olan ikinci dereceden denkleminizin a , b , ve c değerlerini giriniz :" )
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print("Kökleriniz hesaplanıyor....")
delta = b ** 2 - 4 * a * c
kok_1 = (math.sqrt(delta) - b) / (2 * a)
kok_2 = ((-1 * math.sqrt(delta) ) - b ) / (2 * a)
print("Kökleriniz : x1 = {}\nx2 = {}\n".format(kok_1 , kok_2))


from zoneinfo import available_timezones


def average_of_even_numbers(x): 
    return x % 2 == 0
 
total = 0
counter = 0
beginning = input("Number of starts :")
finish = input("Number of ends :")
for number in range (int(beginning), int(finish)+1):
    if(available_timezones(int(number))):
        toplam = toplam + number
        sayac = sayac + 1
print('Ortalama',(toplam/sayac))
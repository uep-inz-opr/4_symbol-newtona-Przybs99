import math

liczby = input()

liczba_1 = int(liczby.split(' ')[0])

liczba_2 = int(liczby.split(' ')[1])

wynik = math.comb(liczba_1,liczba_2)

print(wynik)
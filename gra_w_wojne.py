# # Iwona Kosz - GRA W WOJNE
#
import random

#zmienne
gracz1 = 'gracz1: '
gracz2 = 'gracz2: '

talia1 = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Walet': 11, 'Dama': 12, 'Krol': 13,
          'As': 14}
talia2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

punkty_gracza1 = []
punkty_gracza2 = []

karty_odrzucone = []

#gra
for x in range(1, 12):
    print('Rozgrywka nr ', x)
    while True:
        try:

            print('Oto Twoja talia: ', talia1)

            karta1 = input('Podaj karte z talii: ')

            if karta1 in list(karty_odrzucone):
                print('Karta juz byla.')
                continue
            elif karta1 not in talia1:
                print('Podales karte ktorej nie ma.')
                continue
            else:
                break

        except ValueError:
            print('Podales bledna wartosc.')
    #opcja1
    # if karta1 == 'Walet':
    #     karta1 = 11
    # elif karta1 == 'Dama':
    #     karta1 = 12
    # elif karta1 == 'Krol':
    #     karta1 = 13
    # elif karta1 == 'As':
    #     karta1 = 14

    #opcja2

    #funkcja
    slownik = {'Walet': 11, 'Dama': 12, 'Krol': 13, 'As': 14}
    def zamien_na_liczby(tekst):
        if tekst in slownik:
            tekst = int(slownik[tekst])
        else:
            tekst = int(tekst)
        return tekst

    karta1 = zamien_na_liczby(karta1)


    #karta1 = int(karta1)

    karta2 = int(random.choice(talia2))

    print(gracz1, karta1)
    print(gracz2, karta2)

    if karta1 > karta2:
        print('gracz1 wygral runde')
        punkty_gracza1.append(1)
    elif karta1 == karta2:
        print('Remis w rundzie')
        punkty_gracza1.append(1)
        punkty_gracza2.append(1)
    else:
        print('gracz2 wygral runde')
        punkty_gracza2.append(1)

    #opcja1
    if karta1 == 11:
        karta1 = 'Walet'
    elif karta1 == 12:
        karta1 = 'Dama'
    elif karta1 == 13:
        karta1 = 'Krol'
    elif karta1 == 14:
        karta1 = 'As'
    karta1 = str(karta1)

    #opcja2
    # slownik1 = {11: 'Walet', 12: 'Dama', 13: 'Krol', 14: 'As'}
    # def zamien_na_tekst(liczba):
    #     if liczba in slownik1:
    #         liczba = str(slownik1[liczba])
    #     else:
    #         liczba = str(liczba)
    #     return liczba
    #
    # karta1 = zamien_na_tekst(karta1)

    karty_odrzucone.append(karta1)

    talia1.pop(karta1)
    talia2.remove(karta2)

    #opcjonalnie_opis
    # print('Zostalo ', len(talia1), ' kart w talii1')
    # print('Zostalo ', len(talia2), ' kart w talii2')
    # print('Punkty gracza1: ', punkty_gracza1)
    # print('Punkty gracza2: ', punkty_gracza2)
    print()

#opis_minimum
if len(punkty_gracza1) > len(punkty_gracza2):
    print('gracz1 wygral gre')
elif len(punkty_gracza1) == len(punkty_gracza2):
    print('REMIS, nikt nie wygral gry')
else:
    print('gracz2 wygral gre')

# założenia
# 1 pobieranie hasła od użytkownika
# 2 sprawdzenie długoścci hasła, czy ma minimalnie 8
# 3 Sprwadzenie dużych i małych liter - czy użyto różnego rozmaru
# 4 Krok 4: Sprawdzenie cyfr i znaków specjalnych – Sprawdzamy obecność liczb oraz znaków typu @, #, $, %.
# Krok 5: Ocena i wynik – Podliczamy punkty i wypisujemy na ekranie, czy hasło jest
# "Słabe", "Średnie" czy "Silne".
#
from operator import truediv

# pobieranie hasła od użytkownika
print("Podaj proszę swoje hasło a ja określę czy jest wystarczająco silne")
while True:
 hasło_uzytkownika = str(input("Twoje hasło: "))

 punkty_mocy = 0
 # klasyfikacja punków
 # 1 - słabe
 # 2 - słabe
 # 3 - średnie
 # 4 - mocne

 def naliczanie_punktów_mocy(czy_długie_min_8znakow, czy_wielkie, czy_są_znaki_sppecjalne, czy_są_liczby):
      punkty = 0
      if czy_długie_min_8znakow:
          punkty += 1
      if czy_wielkie:
          punkty += 1
      if czy_są_znaki_sppecjalne:
          punkty += 1
      if czy_są_liczby:
          punkty += 1
      return punkty


 # 2 sprawdzenie długości hasla
 def sprdlugoscihasla():
    dlugosc_hasla = len(hasło_uzytkownika)
    if dlugosc_hasla < 8:
        print("twoje hasło jest zbyt krótkie, musi się składać z minimalnie 8 znaków")
    return dlugosc_hasla

 if sprdlugoscihasla() < 8:
   continue

 #jeżeli warunek jest spełniony to dodaj moc 1 haśle
 #punkty_mocy += 1
 długie = True



 def sprznaki():
    wynik_duzych_liter = 0
    # pętla sprawdzająca wiekosc liter
    for literka in hasło_uzytkownika:
        if literka == literka.upper():
            wynik_duzych_liter += 1
    if wynik_duzych_liter < 2:
        return print("wprowadź minimalnie 2 duży litery w haśle!")


 #sprawdzenie wielości liter

 def wielosc_liter():
    ma_małą = 0
    ma_dużą = 0

    #pętla sprawdzająca wiekosc liter
    for literka in hasło_uzytkownika:
        if literka.isupper():
           ma_dużą += 1

        if literka.islower():
            ma_małą += 1
    if ma_dużą < 2:
        print("wprowadź minimalnie 2 duży litery w haśle!")
        return False
        #print("musisz wpisać poprawne hasło")
    if ma_małą < 2:
        print("użyj przynajmnie 2 małych literek")
        return False
        sprdlugoscihasla()
        return False
    return True
 if wielosc_liter():
    znaki = True
 else:
    continue

 # Sprawdzenie ilości cyfr i znaków specjalnych
 def ilosccyfr_i_znakow(hasło_uzytkownika):

  ilość_cyfr = 0
  ilość_znaków = 0
  ilość_znakow_specjalnych = { "!" : 0, "@" : 0, "#" : 0, "$" : 0,"%" : 0, "^" : 0, "&" : 0, "*" : 0,"(" : 0, ")" : 0, "_" : 0, "~" : 0 }
  ilosccyfr = { "1" : 0, "2" : 0, "3" : 0, "4" : 0,"5" : 0, "6" : 0, "7" : 0, "8" : 0,"9" : 0, "0" : 0 }

  for znak in hasło_uzytkownika:
       if znak in ilość_znakow_specjalnych:
           ilość_znakow_specjalnych[znak] += 1
       if znak in ilosccyfr:
           ilosccyfr[znak] += 1

  for k,v in ilość_znakow_specjalnych.items():
     ilość_znaków += v

  for k,v in ilosccyfr.items():
      ilość_cyfr += v
  #if ilość_cyfr == 0 and ilość_znaków == 0:
    # print(f"Siła twojego hasła wynosi {punkty_mocy}/4 nie użyłeś żadnego znaku specjalnego bądź cyfry!")
  ma_cyfry = ilość_cyfr > 0
  ma_znaki = ilość_znaków > 0

  if ilość_cyfr == 0 and ilość_znaków == 0:
      print("nie użyłeś żadnego znaku specjalnego bądź cyfry")
      return False, False, False

  return True, ma_znaki, ma_cyfry


 if not ilosccyfr_i_znakow(hasło_uzytkownika)[0]:
   continue

 sprdlugoscihasla()

 # 5
 ostateczne_punkty = naliczanie_punktów_mocy(długie, znaki, ilosccyfr_i_znakow(hasło_uzytkownika)[1],
                                            ilosccyfr_i_znakow(hasło_uzytkownika)[2])
 print(f"Twoje punkty: {ostateczne_punkty}/4")

 break






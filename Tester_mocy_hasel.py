# założenia
# 1 pobieranie hasła od użytkownika
# 2 sprawdzenie długoścci hasła, czy ma minimalnie 8
# 3 Sprwadzenie dużych i małych liter - czy użyto różnego rozmaru
# 4 Krok 4: Sprawdzenie cyfr i znaków specjalnych – Sprawdzamy obecność liczb oraz znaków typu @, #, $, %.
# Krok 5: Ocena i wynik – Podliczamy punkty i wypisujemy na ekranie, czy hasło jest
# "Słabe", "Średnie" czy "Silne".
#

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

 # 2 sprawdzenie długości hasla
 def sprdlugoscihasla():
    dlugosc_hasla = len(hasło_uzytkownika)
    if dlugosc_hasla < 8:
        print("twoje hasło jest zbyt krótkie, musi się składać z minimalnie 8 znaków")
    return dlugosc_hasla

 if sprdlugoscihasla() < 8:
   continue

 #jeżeli warunek jest spełniony to dodaj moc 1 haśle
 punkty_mocy += 1


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
        print("musisz wpisać poprawne hasło")
        sprdlugoscihasla()
        return False
    return True
 if wielosc_liter():
    punkty_mocy += 1
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
  if ilość_cyfr == 0 and ilość_znaków == 0:
     print(f"Siła twojego hasła wynosi {punkty_mocy}/4 nie użyłeś żadnego znaku specjalnego bądź cyfry!")
     return False
  return True

 if not ilosccyfr_i_znakow(hasło_uzytkownika):
     continue

 sprdlugoscihasla()
 break






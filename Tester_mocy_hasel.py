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
hasło_uzytkownika = str(input("Twoje hasło: "))

# 2 sprawdzenie długości hasla
def sprdlugoscihasla():
    dlugosc_hasla = len(hasło_uzytkownika)
    if dlugosc_hasla < 8:
        print("twoje hasło jest zbyt krótkie, musi się składać z minimalnie 8 znaków")
    return dlugosc_hasla


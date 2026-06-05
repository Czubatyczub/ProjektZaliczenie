"""Założenia:
1 - pobieranie hasła od użytkownika.
2 - sprawdzenie długości hasła, czy ma minimalnie 8 znaków.
3 - sprawdzenie dużych i małych liter - czy użyto różnej wielkości znaków.
4 - sprawdzenie cyfr i znaków specjalnych – sprawdzamy obecność liczb oraz znaków typu @, #, $, %.
5 - ocena i wynik – podliczamy punkty i wypisujemy na ekranie, czy hasło jest
"Słabe", "Średnie" czy "Silne"."""


def main():
    """Tester mocy haseł"""

    def pobieranie_hasla():
        """pobieranie hasła od użytkownika"""
        print("Podaj proszę swoje hasło a ja określę czy jest wystarczająco silne")
        haslo_uzytkownika = str(input("Twoje hasło: "))
        spr_dlugosc_hasla(haslo_uzytkownika)

    # Klasyfikacja punktów:
    # 1 - słabe
    # 2 - słabe
    # 3 - średnie
    # 4 - mocne

    def spr_dlugosc_hasla(haslo_uzytkownika):
        """sprawdzenie długości hasla"""
        dlugosc_hasla = len(haslo_uzytkownika)
        if dlugosc_hasla < 8:
            print(
                "twoje hasło jest zbyt krótkie, musi się składać z minimalnie 8 znaków"
            )
            pobieranie_hasla()
        else:
            punkty_mocy = 0
            punkty_mocy += 1  # jeżeli warunek jest spełniony to dodaj moc 1 haśle
            wielkosc_liter(haslo_uzytkownika, punkty_mocy)

    def wielkosc_liter(haslo_uzytkownika, punkty_mocy):
        "sprawdzenie wielkości liter"
        male = 0
        duze = 0

        # pętla sprawdzająca wielkość liter
        for literka in haslo_uzytkownika:
            if literka.isupper():
                duze += 1
            if literka.islower():
                male += 1

        if duze < 2:
            print("wprowadź minimalnie 2. duże litery w haśle!")
            print("musisz wpisać poprawne hasło")
            pobieranie_hasla()
        if duze >= 2 and male >= 2:
            punkty_mocy += 1
            ilosc_cyfr_i_znakow_specjalnych(haslo_uzytkownika, punkty_mocy)

    def ilosc_cyfr_i_znakow_specjalnych(haslo_uzytkownika, punkty_mocy):
        "Sprawdzenie ilości cyfr i znaków specjalnych"
        ilosc_cyfr = 0
        ilosc_znakow_specjalnych = 0
        znaki_specjalne = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "~"}

        for znak in haslo_uzytkownika:
            if znak in znaki_specjalne:
                ilosc_znakow_specjalnych += 1
            if znak.isdigit() is True:
                ilosc_cyfr += 1

        if ilosc_cyfr == 0 and ilosc_znakow_specjalnych == 0:
            print(
                f"""Siła twojego hasła wynosi {punkty_mocy}
                nie użyłeś żadnego znaku specjalnego bądź cyfry!"""
            )
        else:
            punkty_mocy += 1
            print(f"Siła twojego hasła wynosi {punkty_mocy}.")
            raise SystemExit

    pobieranie_hasla()


if __name__ == "__main__":
    main()

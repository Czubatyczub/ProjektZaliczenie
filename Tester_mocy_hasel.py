def main():
    print("Podaj hasło, a sprawdzę jego siłę:")

    haslo = input("Twoje hasło: ")

    punkty = 0
    bledy = []

    # 1. długość hasła
    if len(haslo) >= 8:
        punkty += 1
    else:
        bledy.append("Hasło musi mieć minimum 8 znaków")

    # 2. duże i małe litery
    duze = 0
    male = 0

    for c in haslo:
        if c.isupper():
            duze += 1
        if c.islower():
            male += 1

    if duze >= 2:
        punkty += 1
    else:
        bledy.append("Brakuje min. 2 dużych liter")

    if male >= 2:
        punkty += 1
    else:
        bledy.append("Brakuje min. 2 małych liter")

    # 3. cyfry i znaki specjalne
    cyfry = 0
    znaki_specjalne = 0

    znaki = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "~"}

    for c in haslo:
        if c.isdigit():
            cyfry += 1
        if c in znaki:
            znaki_specjalne += 1

    if cyfry > 0:
        punkty += 1
    else:
        bledy.append("Brakuje cyfr")

    if znaki_specjalne > 0:
        punkty += 1
    else:
        bledy.append("Brakuje znaków specjalnych")

    # 4. wynik (5 poziomów)
    print("\n--- WYNIK ---")
    print(f"Punkty: {punkty}/5")

    if punkty <= 1:
        print("Siła hasła: BARDZO SŁABE")
    elif punkty == 2:
        print("Siła hasła: SŁABE")
    elif punkty == 3:
        print("Siła hasła: ŚREDNIE")
    elif punkty == 4:
        print("Siła hasła: DOBRE")
    else:
        print("Siła hasła: BARDZO SILNE")

    # błędy
    if bledy:
        print("\nCo poprawić:")
        for b in bledy:
            print("-", b)


if __name__ == "__main__":
    main()
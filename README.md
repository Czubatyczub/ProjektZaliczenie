# Projekt zaliczeniowy – Tester siły hasła

## Autor
- **Imię i nazwisko:** Adrian Wnorowski

## Opis projektu
Program w języku Python analizuje siłę hasła podanego przez użytkownika.

Program sprawdza:
- długość hasła,
- obecność dużych liter,
- obecność małych liter,
- obecność cyfr,
- obecność znaków specjalnych.

Na podstawie spełnionych kryteriów przyznawane są punkty oraz wyświetlana jest ocena siły hasła.

## Zawartość repozytorium
- `main.py` — kod aplikacji (uruchamia program i wykonuje sprawdzanie siły hasła)

## Wymagania
- Python 3.x
- Git (oraz dostęp do GitHub)

Program nie wymaga instalacji dodatkowych bibliotek.

## Uruchomienie programu

### 1) Pobranie repozytorium
```bash
git clone https://github.com/Czubatyczub/ProjektZaliczenie.git
cd ProjektZaliczenie


2) Uruchomienie
bash

Jak działa program
Program prosi użytkownika o podanie hasła.

Następnie oblicza liczbę punktów od 0 do 5 zgodnie z regułami:

Długość hasła: +1 jeśli len(haslo) >= 8, w przeciwnym razie dodaje błąd.
Duże litery: +1 jeśli występuje co najmniej 2 duże litery, w przeciwnym razie dodaje błąd.
Małe litery: +1 jeśli występuje co najmniej 2 małe litery, w przeciwnym razie dodaje błąd.
Cyfry: +1 jeśli występuje co najmniej 1 cyfra, w przeciwnym razie dodaje błąd.
Znaki specjalne: +1 jeśli występuje co najmniej 1 znak specjalny z listy: ! @ # $ % ^ & * ( ) _ ~
Na końcu program wyświetla:

Punkty: X/5
poziom siły hasła:
<= 1 → BARDZO SŁABE
2 → SŁABE
3 → ŚREDNIE
4 → DOBRE
5 → BARDZO SILNE
listę błędów, jeśli jakieś kryteria nie zostały spełnione
Przykład działania

python main.py


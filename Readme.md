# Nazwa programu: Ocena bezpieczeństwa hasła

## Opis: Ten program umożliwia użytkownikowi wprowadzenie hasła i ocenia jego bezpieczeństwo zgodnie z określonymi regułami. Program sprawdza, czy hasło spełnia wymagania, takie jak zawieranie małych i wielkich liter, znaków specjalnych, braku spacji i minimalnej długości. Program informuje użytkownika, czy hasło jest bezpieczne, a jeśli nie, podaje konkretne reguły, które nie zostały spełnione.

### Instrukcje użytkowania:

Uruchom program.
Program poprosi użytkownika o wprowadzenie hasła. Wprowadź hasło i naciśnij Enter.
Program przetworzy wprowadzone hasło i oceni jego bezpieczeństwo zgodnie z regułami.
Wynik zostanie wyświetlony na ekranie w formie komunikatu.

#### Działanie programu:

Program wczytuje hasło od użytkownika za pomocą funkcji input i zapisuje je w zmiennej password.
Następnie program sprawdza hasło pod kątem kilku warunków:
Czy hasło zawiera małą literę (zmienna has_lowercase).
Czy hasło zawiera wielką literę (zmienna has_uppercase).
Czy hasło zawiera znak specjalny (zmienna has_special_char).
Czy hasło nie zawiera spacji (zmienna has_space).
Czy hasło ma co najmniej 8 znaków (zmienna long_enough).
Program tworzy zmienną is_correct, która jest prawdziwa tylko wtedy, gdy wszystkie te warunki są spełnione.
Na podstawie wartości zmiennej is_correct, program wyświetla odpowiedni komunikat użytkownikowi. Jeśli hasło jest bezpieczne, program wyświetla "Twoje hasło jest bezpieczne". W przeciwnym razie, program informuje użytkownika, które konkretne reguły nie zostały spełnione.
Ten program może być używany do oceny bezpieczeństwa haseł wprowadzanych przez użytkowników i zachęcania do stosowania silnych haseł.

##### przypadki testowe:

1. Silne hasło z małą i wielką literą, znakiem specjalnym, brakiem spacji i długością >= 8 znaków
Dane wejściowe: "Haslo123!"
oczekiwany wynik: Twoje hasło jest bezpieczne 

2. Hasło bez małej litery
Dane wejściowe: "HASLO123!"
oczekiwany wynik: "Twoje hasło nie jest bezpieczne. Dostosuj się do poniższych reguł: Twoje hasło musi zawierać małą literę"

3. Hasło bez wielkiej litery
Dane wejściowe: "haslo123!"
oczekiwany wynik: "Twoje hasło nie jest bezpieczne. Dostosuj się do poniższych reguł: Twoje hasło musi zawierać wielką literę"

4. Hasło bez znaku specjalnego
Dane wejściowe: "Haslo123"
Oczekiwany wynik: "Twoje hasło nie jest bezpieczne. Dostosuj się do poniższych reguł: Twoje hasło musi zawierać znak specjalny"

5. Hasło ze spacją

Dane wejściowe: "Haslo 123!"
Oczekiwany wynik: "Twoje hasło nie jest bezpieczne. Dostosuj się do poniższych reguł: Twoje hasło nie może zawierać spacji"

6. Krótkie hasło (< 8 znaków) z małą i wielką literą oraz znakiem specjalnym

Dane wejściowe: "Kr0t$"
Oczekiwany wynik: "Twoje hasło nie jest bezpieczne. Dostosuj się do poniższych reguł: Twoje hasło musi zawierać minimum 8 znaków"

7. Hasło złożone tylko z małych liter i spacji

Dane wejściowe: "to jest testowe haslo"
Oczekiwany wynik: "Twoje hasło nie jest bezpieczne. Dostosuj się do poniższych reguł: Twoje hasło musi zawierać wielką literę, znak specjalny i nie może zawierać spacji"

8. Puste hasło

Dane wejściowe: ""
Oczekiwany wynik: "Twoje hasło nie jest bezpieczne. Dostosuj się do poniższych reguł: Twoje hasło musi zawierać małą literę, wielką literę, znak specjalny i nie może zawierać spacji oraz musi zawierać minimum 8 znaków"

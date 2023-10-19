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
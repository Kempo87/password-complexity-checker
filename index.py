password = input("Wpisz swoje hasło: ")
has_lowercase = False
has_uppercase = False
has_space = False
has_special_char = False
for char in password:
    if char.islower():
        has_lowercase = True
    elif char.isupper():
        has_uppercase = True 
    elif char.isspace():
        has_space = True
    else:
        has_special_char = True
long_enough = len(password) >= 8

is_correct = (
    has_lowercase and
    has_uppercase and
    has_special_char and
    not has_space and
    long_enough
)

if is_correct:
    print("Twoje hasło jest bezpieczne")
else:
    print("Twoje hasło nie jest bezpieczne. Dostosuj się do poniższych reguł: ")
    if not has_lowercase:
        print("Twoje hasło musi zawierać małą literę")
    if not has_uppercase:
        print("Twoje hasło musi zawierać wielką literę")
    if not has_special_char:
        print("Twoje hasło musi zawierać znak specjalny")
    if has_space:
        print("Twoje hasło nie może zawierać spacji")
    if not long_enough:
        print("Twoje hasło musi zawierać minimum 8 znaków")
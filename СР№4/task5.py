from random import sample
import string
def get_random_password(n=8) -> str:
    # TODO написать функцию генерации случайных паролей
    data=sample(list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits),k=n)
    password_str=''
    for el in data:
        password_str+=el
    return password_str

print(get_random_password())

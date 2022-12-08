import random
import string
def get_random_password() -> str:
    ...  # TODO написать функцию генерации случайных паролей
    list = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = random.sample(list, 8)
    str_password = "".join(password)
    return str_password

print(get_random_password())

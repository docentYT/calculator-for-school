# Napisz funkcję która przepisze listę  moja lista na krotkę.
from random import randint
moja_lista = [randint(1,20) for i in range(20)]
print(moja_lista)

def list_to_tuple(l: list) -> tuple:
    return tuple(l)

print(list_to_tuple(moja_lista))
# Napisz funkcję zwracającą krotki/tuples(10/20 elementów) o losowych wartościach z przedziału 1,10. 
# Następnie napisz 2 funkcję która przyjmie naszą krotkę jako argument, 
# pozbędzie się duplikatów, posortuje (od największej wartości do najmniejszej!) i zwraca krotkę 

from random import randint

def generate_tuples() -> tuple:
    return tuple(randint(1, 10) for i in range(randint(10, 20)))

def sort_and_remove_duplicates(t: tuple) -> tuple:
    l = list(set(t))
    l.sort(reverse=True)
    return l

print(sort_and_remove_duplicates(generate_tuples()))
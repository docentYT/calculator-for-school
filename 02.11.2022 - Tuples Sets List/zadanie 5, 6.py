# Napisz funkcję która sprawdza czy zapytany element jest w set.
# Napisz funkcję która przyjmie nieskończenie wiele elementów i wyświetli które z nich występują w set klasa_1c . 

klasa_1c = {"Ala", "Maciek", "Kasia", "olek", "Basia", "Wojtek"}

# def is_in_set(s:set, what: str) -> bool:
#     return what in s

def is_in_set(s: set, *what: str):
    for i in what: print(i, "jest") if i in s else print(i, "nie ma")

is_in_set(klasa_1c, "Ala", "Basia", "Kuba" , "daniel", "olek")
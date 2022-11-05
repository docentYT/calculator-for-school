# Napisz “Timer” przyjmuje od użytkownika liczbę minut. Liczymy za ile skończy się czas. (program na rozgrzewkę)
from time import sleep

time = float(input("Podaj liczbę minut do odmierzania: ")) * 60

while time > 0:
    print("Pozostało", time, "sekund.")
    sleep(1)
    time -= 1

print("Koniec czasu")
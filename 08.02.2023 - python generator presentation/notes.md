# Generatory w Pythonie

# Co to jest generator?
* Generator jest specjalnym rodzajem funkcji, która zwraca sekwencję wartości.
* Generatory są używane do tworzenia iteratorów, czyli obiektów, które można przeglądać jedna po drugiej.
# Jak tworzyć generatory?
* Aby utworzyć generator, należy użyć słowa kluczowego yield.
* Funkcja zawierająca słowo yield jest nazywana funkcją generatora.
# Jak korzystać z generatorów?
* Aby korzystać z generatora, należy go najpierw wywołać jak zwykłą funkcję.
* Następnie można użyć funkcji `next()` lub `for`, aby przeglądać kolejne wartości.
# Przykład
* Poniżej znajduje się przykład generatora, który zwraca kolejne liczby parzyste.
  ```python
  def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
  ```

* Potem można użyć funkcji next() lub pętli for, aby przeglądać kolejne wartości.
  ```python
    evens = even_numbers(10)
    print(next(evens)) # 0
    print(next(evens)) # 2

    for num in even_numbers(10):
        print(num) # 0, 2, 4, 6, 8
  ```

# Zalety generatorów
* Generator jest bardziej efektywny niż lista, ponieważ generuje wartości tylko wtedy, gdy są one potrzebne.
* Dzięki temu generatory są szczególnie użyteczne do przetwarzania dużych plików lub danych, których nie można zapisać w pamięci.
# Podsumowanie
* Generatory są użytecznymi narzędziami w Pythonie, które pozwalają na tworzenie iteratorów i efektywne przetwarzanie dużych danych.
* Łatwo jest je tworzyć i korzystać z nich, a ich użycie może znacznie poprawić wydajność i efektywność kodu.
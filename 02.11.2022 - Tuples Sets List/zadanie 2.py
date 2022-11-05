# Stwórz krotkę/tuples zawierającą 6 elementów. Zmień ją na listę, usuń 2 ostatnie elementy i zmień z powrotem na krotkę.

t = tuple([1, 2, 3, 4, 5, 6])   # (1, 2, 3, 4, 5, 6)
l = list(t)                     # [1, 2, 3, 4, 5, 6]
l.pop()                         # [1, 2, 3, 4, 5]
l.pop()                         # [1, 2, 3, 4]
t = tuple(l)                    # (1, 2, 3, 4)

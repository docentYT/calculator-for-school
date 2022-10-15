import inspect
from kalkulator import *

DASH_LINE = "-" * 50

def get_input(anonymous):
    args = {}
    for i in inspect.signature(anonymous).parameters: args.update({i: (float(input(f"{i} = "))) })
    return args

while True:
    print(DASH_LINE)
    for key in kalkulator: print('|', list(kalkulator).index(key)+1, "-", key)
    try:
        inp = int(input("| Wpisz numer opcji lub \'0\' aby wyjsc: "))
        if inp == 0: break
        inpp = get_input(kalkulator[list(kalkulator)[inp-1]])
        print("Wynik:", kalkulator[list(kalkulator)[inp-1]](**inpp))
    except: print(DASH_LINE, '\n', "ERROR: Niepoprawne parametry badz numer opcji!")
    

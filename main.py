from ast import Lambda
import inspect
from calculator import *

DASH_LINE = "-" * 50
LIST_CALC = list(calculator)

def print_options(options: dict):
    for key in options: print('|', LIST_CALC.index(key)+1, "-", key)

def get_args_input(anonymous: Lambda) -> list:
    args = {}
    for i in inspect.signature(anonymous).parameters: args.update({i: (float(input(f"{i} = "))) })
    return args

def get_option_input()                  -> int:     return int(input("| Wpisz numer opcji lub \'0\' aby wyjsc: "))
def get_function(option_number: int)    -> Lambda:  return calculator[LIST_CALC[option_number-1]]
def calculate(option_number: int)       -> float:   return get_function(option_number)( **get_args_input(get_function(option_number)) )

while True:
    print(DASH_LINE)
    print_options(calculator)
    try:
        inp = get_option_input()
        if inp == 0: break
        print("Wynik:", calculate(inp))
    except: print(DASH_LINE, '\n', "ERROR: Niepoprawne parametry badz numer opcji!")

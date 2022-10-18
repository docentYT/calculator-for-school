from math import pi, sqrt

calculator = {
    "pole powierzchni prostokata": lambda a, b : a*b ,
    "pole powierzchni prostopadloscianu": lambda a, b, c : 2*a*b + 2*a*c + 2*b*c ,
    "objetosc prostopadloscianu": lambda a, b, h : a*b * h ,
    "objetosc ostroslupa": lambda a, b, h : a*b * h/3 ,
    "pole powierzchni walca": lambda r, h : 2*pi*(r**2) + 2*pi*h ,
    "objetosc walca": lambda r, h : pi*(r**2)*h ,
    "wysokosc trojkata rownobocznego": lambda a : (a*sqrt(3) ) /2 ,
}

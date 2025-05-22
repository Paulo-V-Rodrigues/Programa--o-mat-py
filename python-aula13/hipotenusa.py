import math
def hipotenusa(catO, catA):
    return math.sqrt(catO**2 + catA**2)

def seno(catO, catA):
    return catA/hipotenusa(catO, catA)

def cosseno(catO, catA):
    return catO/hipotenusa(catO, catA)

def tangente(catO, catA):
    return catA/catO

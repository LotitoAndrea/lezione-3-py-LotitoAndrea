import math
areaQuadrato = float(input("Inserisci l'area del quadrato: "))
lato = math.sqrt(areaQuadrato)
latoArrotondato = round(lato, 1)
print("Il lato del quadrato arrotondato è:", latoArrotondato)
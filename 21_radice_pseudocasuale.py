import random
import math
numeroCasuale = random.randint(10, 1000)
radiceQuadrataNumero = math.sqrt(numeroCasuale)
NumeroArrotondato = round(radiceQuadrataNumero, 3)
print("il numero arrotondato e:", NumeroArrotondato)
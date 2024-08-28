import random

N = int(input("Kuinka monta pistettä arvotaan:"))
n = 0
pisteet_arvottu = 0

while pisteet_arvottu < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n += 1

    pisteet_arvottu += 1

pii = 4 * (n / N)

print("Piin likiarvo on noin", pii)
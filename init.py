import math
import random
import first_module

cars = ["Kia", "Chevrolet", "Nissan", "Toyota"]
for i in cars:
    print(i)

for x in range(10):
    random_entero = random.randint(1, 12)
    print(random_entero)

print(first_module.valor_pi)

valor_float = random.uniform(1, 11)
valor_entero = math.trunc(valor_float)

if valor_entero == 1:
    print("Heads")
elif valor_entero == 10:
    print("Tails")

random_entero = random.randint(0, 1)
if random_entero == 0:
    print("Heads randint")
elif random_entero == 1:
    print("Tails randint")
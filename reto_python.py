def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Encontrar primos del 1 al 250
print("Buscando números primos del 1 al 250...")
primos = []

for i in range(1, 251):
    if es_primo(i):
        primos.append(i)

# Guardar en results.txt
with open('results.txt', 'w') as archivo:
    for primo in primos:
        archivo.write(str(primo) + '\n')

print(f"¡Listo! Se encontraron {len(primos)} números primos")
print("Resultados guardados en: results.txt")
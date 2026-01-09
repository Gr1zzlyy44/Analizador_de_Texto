texto = input("Ingrese su texto: ")

palabras = []

texto = texto.lower()

palabras.append(input("Ingrese su primera palabra: ").lower())
palabras.append(input("Ingrese su segunda palabra: ").lower())

print('\n')
print("CANTIDAD DE PALABRAS")
cantidad_palabras = texto.count(palabras[0])
cantidad_palabras1 = texto.count(palabras[1])

print(f"Hemos encontrado la palabra '{palabras[0]}' repetida {cantidad_palabras} veces")
print(f"Hemos encontrado la palabra '{palabras[1]}' repetida {cantidad_palabras1} veces")

print('\n')
print("CANTIDAD DE PALABRAS TOTALES")

texto = texto.split()
print(f"Hemos encontrado {len (texto)} palabras en tu texto")

print('\n')
print("PALABRA INICIO Y PALABRA FINAL")

print(f"La primera palabra de tu texto es: '{texto[0]}'")
print(f"La ultima palabra de tu texto es: '{texto[-1]}'")

print('\n')
print("TEXTO INVERTIDO")

texto.reverse()
texto_final = " ".join(texto)
print("Tu texto invertido quedaria tal que asi: " + texto_final)

print('\n')
print("IDENTIFICAR PALABRA 'PROGRAMACION'")


prog = ("programacion" in texto)
print("Es verdadero o falso que la palabra 'programacion' aparece en el codigo? " "\n" +  str(prog))


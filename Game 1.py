import random

# Palabras para el juego
palabras = ['dados', 'naipes', 'dominós', 'dardos', 'risk']

# Seleccionar una palabra aleatoria
palabra = random.choice(palabras)

# Inicializar variables
intentos = 6
palabra_oculta = ['_'] * len(palabra)
letras_descartadas = []

def mostrar_estado():
    print(' '.join(palabra_oculta))
    print(f'Letras descartadas: {", ".join(letras_descartadas)}')
    print(f'Intentos restantes: {intentos}')

def letra_valida(letra):
    return len(letra) == 1 and letra.isalpha() and letra not in letras_descartadas

def gestion_letra(letra):
    for i, l in enumerate(palabra):
        if l == letra:
            palabra_oculta[i] = letra

print('BIENVENIDO AL JUEGO DEL AHORCADO 🗣️ EDICIÓN Juegos de Mesa 🎲\n')
print('Reglas del juego: Introduce letras para adivinar la palabra oculta.')
print(f'Tienes {intentos} intentos. ¡Buena suerte!\n')

while intentos > 0 and '_' in palabra_oculta:
    mostrar_estado()
    print('-' * 50)
    letra = input('INTRODUCE LETRA: ').lower()

    while not letra_valida(letra):
        letra = input('INTRODUCE OTRA LETRA: ').lower()

    if letra in palabra:
        gestion_letra(letra)
        print('-' * 50)
        print('¡Has acertado la letra! Sigue así.')
    else:
        print('-' * 50)
        print('¡Has fallado la letra!')
        letras_descartadas.append(letra)
        intentos -= 1

if '_' not in palabra_oculta:
    print('\n\n🏆¡Felicidades! ¡HAS GANADO EL JUEGO!🏆')
else:
    print(f'\nOh!💁 Lo siento, ¡has perdido!'
        '''\n
       +---+
       |   |
      💀   |
      /|\\  |
      / \\  |
           |
    =========
    ''')
    print(f'La palabra era: {palabra}')
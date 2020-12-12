nombre_1 = input('¿Cuál es tu nombre?: ')
edad_1 = int(input((f'{nombre_1} ¿Cuál es tu edad?: ')))
nombre_2 = input('¿Cómo se llama la persona que está más cerca de ti?: ')
edad_2 = int(input((f'¿Cuál es la edad de {nombre_2}?: ')))

if edad_1 > edad_2:
    print(f'{nombre_1} eres mayor que {nombre_2}.')
elif edad_1 < edad_2:
    print(f'{nombre_1} eres menor que {nombre_2}.')
else:
    print(f'{nombre_1} tienes la misma edad que {nombre_2}.')

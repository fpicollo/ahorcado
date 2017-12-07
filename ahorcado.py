#!/usr/bin/env python3

palabraAdivinar = ""
listaPalabraAdiv = []
listaPalabraMost = []
intentos = 5
letra = ""
run = True

print ("AHORCADO")
palabraAdivinar = input("Dime una palabra: ")

listaPalabraAdiv = list(palabraAdivinar)

for item in listaPalabraAdiv:
  listaPalabraMost.append('_')
    
while run:
    print(' '.join(listaPalabraMost))
    letra = input("Dame una letra: ")
    for num in range(100):
        print()
    fallo = False
    if letra not in listaPalabraAdiv:
        fallo = True
        intentos = intentos - 1
        print("Has fallado!!!! Te quedan {intentos} intentos".format(intentos=intentos))
    else:
        for key, value in enumerate(listaPalabraAdiv):
         if value == letra:
            listaPalabraMost[key] = value
    if intentos <= 0:
        run = False
        print("Has perdido, la palabra era {palabra}".format(palabra=''.join(listaPalabraAdiv)))
    elif listaPalabraAdiv == listaPalabraMost:
        run = False
        print("Has ganado, la palabra era {palabra}".format(palabra=''.join(listaPalabraAdiv)))

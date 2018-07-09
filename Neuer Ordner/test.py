enemigos = [1, 20, 1]
huecos = [1, 20, 1]
baterias = [1, 20, 1]

facil = []
facil.append(enemigos)
facil.append(huecos)
facil.append(baterias)
facil.append(10)

intermedio = []
intermedio.append(enemigos)
intermedio.append(huecos)
intermedio.append(baterias)
intermedio.append(35)    

dificil = []
dificil.append(enemigos)
dificil.append(huecos)
dificil.append(baterias)
dificil.append(99999999)

configurador = {}
configurador['facil'] = facil
configurador['intermedio'] = intermedio
configurador['dificil'] = dificil

##print(configurador['facil'])
##print(configurador['intermedio'])
##print(configurador['dificil'])
print(configurador)


for key, value in configurador.items():
    count = 0
    print("Dificultad: " + key)
    for val in value:
        if isinstance(val,(list,)):
            if count == 0:
                print("ENEMIGO")
            elif count == 1:
                print("HUECO")
            elif count == 2:
                print("PILAS")
            print("Cantidad: " + str(val[0]))
            print("Velocidad: " + str(val[1]))
            print("Tamanho: " + str(val[2]))
            count += 1
        else:
            print("Limite de puntaje: " + str(val))
            count += 1
    print("--------------------")

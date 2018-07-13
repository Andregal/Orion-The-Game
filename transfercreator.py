def transferirParams(lista, diccionario, dif):
    count = 0
    for key, value in diccionario.items():
        if key == dif:
            for val in value:
                if isinstance(val,(list,)):
                    while count <= 2:
                        val[count] = lista[count]
                        count = count +1
                    count = 0
                else:
                    val = lista[9]

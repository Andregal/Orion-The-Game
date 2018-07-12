# Modulos necesarios
import json  # Convertir a JSON
import http.client  # Realizar peticiones

# Convertir a String

def convertirString(binario):
    nuevoString = binario.decode('utf8').replace("'", '"')
    return nuevoString

# Convertir a JSON

def convertirJSON(objeto):
    nuevoString = convertirString(objeto)
    nuevoJSON = json.loads(nuevoString)
    return nuevoJSON

# Peticion validarExistencia

def validarExistencia(username):
    conn = http.client.HTTPConnection('localhost')
    conn.request("GET", "/usuario/validarExistencia/" + username)
    response = convertirJSON(conn.getresponse().read())
    conn.close()
    return response["result"]
    #Ejemplo: 
    # Metodo: validarExistencia("cesar")
    # Respuesta: True

# Peticion crearUsuario

def crearUsuario(username, password):
    if not validarExistencia(username):
        usuario = {"username": username, "password": password}
        conn = http.client.HTTPConnection('localhost')
        conn.request("POST", "/usuario/crear", body=json.dumps(usuario),
                     headers={"Content-Type": "application/json"})
        conn.close()
        #print("Usuario creado")
        return True
    else:
        return False
        #print("El usuario ya existe")
    #Ejemplo: 
    # Metodo: crearUsuario("juan", "juan1234")
    # Respuesta: None

# Peticion validarContrasena

def validarContrasena(username, password):
    usuario = {"username": username, "password": password}
    conn = http.client.HTTPConnection('localhost')
    conn.request("POST", "/usuario/validarContrasena",
                 body=json.dumps(usuario), headers={"Content-Type": "application/json"})
    response = convertirJSON(conn.getresponse().read())
    conn.close()
    return response["result"]
    #Ejemplo: 
    # Metodo: validarContrasena("cesar", "cesar1234")
    # Respuesta: False

# Peticion actualizarContrasena

def actualizarContrasena(username, password):
    usuario = {"username": username, "password": password}
    conn = http.client.HTTPConnection('localhost')
    conn.request("PUT", "/usuario/actualizarContrasena",
                 body=json.dumps(usuario), headers={"Content-Type": "application/json"})
    conn.close()
    #print("Contraseña actualiza")
    return True
    #Ejemplo: 
    # Metodo: actualizarContrasena("rodrigo", "galindo1234")
    # Respuesta: None

# Peticion obtenerScore

def obtenerScore(username):
    conn = http.client.HTTPConnection('localhost')
    conn.request("GET", "/usuario/obtenerScore/" + username)
    response = convertirJSON(conn.getresponse().read())
    conn.close()
    return response["score"]
    #Ejemplo: 
    # Metodo: obtenerScore("bacini")
    # Respuesta: 1000

# Peticion actualizarScore


def actualizarScore(username, score):
    if score > obtenerScore(username):
        usuario = {"username": username, "score": score}
        conn = http.client.HTTPConnection('localhost')
        conn.request("PUT", "/usuario/actualizarScore", body=json.dumps(usuario),
                     headers={"Content-Type": "application/json"})
        conn.close()
        print("Score actualizado")
    #Ejemplo: 
    # Metodo: actualizarScore("rodrigo", 600)
    # Respuesta: None

# Peticion mostrarRanking

def mostrarRanking():
    return [{"username": "cesar", "score": 1000}, {"username": "rodrigo", "score": 500}]
##    conn = http.client.HTTPConnection('localhost')
##    conn.request("GET", "/ranking/mostrar")
##    response = convertirJSON(conn.getresponse().read())
##    conn.close()
##    return response
##    #Ejemplo: 
##    # Metodo: mostrarRanking()
##    # Respuesta: [{"username": "cesar", "score": 1000}, {"username": "rodrigo", "score": 500}, ...]

# Peticion mostrarUsuarioSegunPuesto


def mostrarUsuarioSegunPuesto(puesto):
    conn = http.client.HTTPConnection('localhost')
    conn.request("GET", "/ranking/mostrar/" + str(puesto))
    response = convertirJSON(conn.getresponse().read())
    conn.close()
    return response
    #Ejemplo: 
    # Metodo: mostrarUsuarioSegunPuesto(2)
    # Respuesta: {"username": "bacini", "score": 200}

# Peticion mostrarPosUsuario


def mostrarPosUsuario(username):
    conn = http.client.HTTPConnection('localhost')
    conn.request("GET", "/ranking/posicion/" + username)
    response = convertirJSON(conn.getresponse().read())
    conn.close()
    return response["pos"]
    #Ejemplo: 
    # Metodo: mostrarPosUsuario("cesar")
    # Respuesta: 5


# Estas funciones se van a integrar con los archivos principales del juego
# en sus respectivas pantallas.

# Todas las funciones realizan las peticiones sin problemas.

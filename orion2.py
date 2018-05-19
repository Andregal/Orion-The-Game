import sqlite3

def crearUsuario(username):
    #Conecta y crear un curso con sqlite3
    sqliteDriver = sqlite3.connect('orion.db')
    c = sqliteDriver.cursor()
    #Crear un nuevo usuario con score 0 por defecto
    c.execute('INSERT INTO users (username) VALUES (?)', (username,))
    #Guardar y cierra conexion
    sqliteDriver.commit()
    sqliteDriver.close()

def usuarioExiste(username):
    #Conecta y crear un curso con sqlite3
    sqliteDriver = sqlite3.connect('orion.db')
    c = sqliteDriver.cursor()
    #Seleccionar el primer usuario
    c.execute('SELECT username FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    #Verifica si existe
    if user != None:
        return True
    else:
        return False
    #Guardar y cierra conexion
    sqliteDriver.commit()
    sqliteDriver.close()

def datosUsuario(username):
    #Conecta y crear un curso con sqlite3
    sqliteDriver = sqlite3.connect('orion.db')
    c = sqliteDriver.cursor()
    #Seleccionar el usuario
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    score = c.fetchone()[1]
    return username, score
    #Guardar y cierra conexion
    sqliteDriver.commit()
    sqliteDriver.close()

def actualizarScore(username, score):
    #Conecta y crear un curso con sqlite3
    sqliteDriver = sqlite3.connect('orion.db')
    c = sqliteDriver.cursor()
    #Actualizar el score de un usuario, verificando si es mayor al score antiguo
    c.execute('SELECT score FROM users WHERE username = ?', (username,))
    scoreAntiguo = c.fetchone()[0]
    if score > scoreAntiguo:
        c.execute('UPDATE users SET score = ? WHERE username = ?', (score,username))
    #Guardar y cierra conexion
    sqliteDriver.commit()
    sqliteDriver.close()

def mostrarRanking():
    #Conecta y crear un curso con sqlite3
    sqliteDriver = sqlite3.connect('orion.db')
    c = sqliteDriver.cursor()
    #Selecciona a todos los usuarios con su respectivo nombre y puntaje
    c.execute('SELECT * FROM users')
    #Muestra a todos los usuarios
    users = c.fetchall()
    for user in users:
        print(user)
    #Guardar y cierra conexion
    sqliteDriver.commit()
    sqliteDriver.close()

def main():
    mostrarRanking()

main() 
    


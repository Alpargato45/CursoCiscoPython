#20)Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y
#te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado
#hacer login y si no se ha podido hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades

def Login(nombre,apellido):
    nombreCorrecto = "usuario1"
    contraseñaCorrecta = "asdasd"
    return nombre == nombreCorrecto, contraseña == contraseñaCorrecta

login = 3
acertado = False
while(acertado == False and login >= 0):
    nombre = input("Nombre del usuario: ")
    contraseña = input("Contraseña del usuario: ")
    nombreAcertado,ContraseñaAcertada = Login(nombre,contraseña)
    if(nombreAcertado and ContraseñaAcertada == True):
        print("Enhorabuena, has acertado!")
        acertado = True
    else:
        print("Lo siento, has fallado, te quedan", login, "intentos.")
        login = login-1
if(login <= 0):
    print("Te has quedado sin intentos")

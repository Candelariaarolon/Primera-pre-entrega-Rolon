import json

def registro():
    usuario = input("Ingrese el nombre de su nuevo usuario: ")
    contrasena = input("Ingrese la contraseña de su nuevo usuario: ")
    
    cuentas = {
        'usuario': usuario,
        'contrasena': contrasena
    }
    
    with open('cuentas.json', 'w') as archivo:
        json.dump(cuentas, archivo, indent=4)
        archivo.write('\n')
    
    print(f"Bienvenido, {usuario}. Te has registrado como usuario exitosamente.") 
          
def iniciosesion(usuario, contrasena): 
    with open('cuentas.json', 'r') as archivo:
        cuentas = json.load(archivo)
        if cuentas['usuario'] == usuario and cuentas['contrasena'] == contrasena:
            print("Inicio exitoso") 
        else:
            print("Usuario o contraseña incorrectos")

def ver_datos():
    with open('cuentas.json', 'r') as archivo:
        cuentas = json.load(archivo)
        print("Usuarios y contraseñas guardadas:")
        for cuenta in cuentas:
            print(f"Usuario: {cuenta['usuario']}, Contraseña: {cuenta['contrasena']}")        
        
repetirmenu = True
while repetirmenu:
    print('''
_________________________________________
                 MENU
__________________________________________
1. Registrarme 
2. Iniciar sesión
3. Ver usuarios y contraseñas guardadas
4. Salir del programa
        
''')

    eleccion = input("Ingrese el número de la acción que desea realizar: ")
    
    if eleccion == "1":
        registro()
        
    elif eleccion == "2":
        usuario = input("Ingrese su nombre de usuario:")
        contrasena = input("Ingrese su contraseña: ")
        iniciosesion(usuario, contrasena)
            
    elif eleccion == "3":
        ver_datos()
        
    elif eleccion == "4":
        print("Adiós")
        repetirmenu = False
        
    else:
        print("Elección incorrecta. Seleccione una opción del menú.")

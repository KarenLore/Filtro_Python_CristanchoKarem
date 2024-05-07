import json

def abrirArchivo():
    with open("info.json", encoding="utf-8") as file:
        return json.load(file)

def guardarArchivo(file):
    with open("./info.json", "w") as file:
        return json.dump(file)

usuarios=abrirArchivo()
def crearUsuario(usuarios):
        print(usuarios)
        id = int(input("Ingresa el ID: "))
        Nombre = input("Nombre: ")
        Apellido = input("Apellido: ")
        Celular = int(input("Celular: "))

        usuarios[0].append(
            {
                "id": id,
                "Nombre": Nombre,
                "Apellido": Apellido,
                "Celular": Celular,
            }
        )
        guardarArchivo(usuarios)

def leerUsuario(usuarios):
    for usua in usuarios[0]["nuevo"]:
        print(f"ID, {usua["id"]}")
        print(f"Nombre, {usua["Nombre"]}")
        print(f"Apellido, {usua["Apellido"]}")
        print(f"Celular, {usua["Celular"]}")
    guardarArchivo(usuarios)

def modificarUsuario(usuarios):
    Nuevo=usuarios
    usuarios= int(input("Ingrese el ID del usuario que deseas modificar: "))
    print("Selecciona el dato que deseas modificar del usuario: ")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Num.Celular")
    opcion = "Seleccione una opción: "
    if opcion == "1":
        print("Ingrese el nuevo nombre para el usuario: ", Nuevo)
    elif opcion == "2":
        print("Ingrese el nuevo apellido para el usuario: ", Nuevo)
    elif opcion == "3":
        print("Ingrese el nuevo Numero celular del usuario: ", Nuevo)
    else:
        print("Opción invalida")
    usuarios.append(usuarios)
    guardarArchivo(usuarios)

def eliminarUsuario(usuarios):
        abrirArchivo()
        print("Ingrese el ID del usuario que deseas eliminar: ")
        for usuario in usuarios[0]["usuarios"]:
            usuarios.remove(usuario)
        guardarArchivo(usuarios)

print("=======Menú=======")
opcion = input("\n1.Crear un nuevo usuario\n2.Ver usuarios\n3.Actualizar usuario\n4.Eliminar usuario ")
def menu():
    if opcion == "1":
         crearUsuario(usuarios)
    elif opcion == "2":
        leerUsuario(usuarios)
    elif opcion == "3":
        modificarUsuario(usuarios)
    elif opcion == "4":
        eliminarUsuario(usuarios)
        
menu()

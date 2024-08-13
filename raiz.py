from Usuarios import Usuario

"""
    Seccionar todo el código (Diferentes Clases)
"""
# Sección de Variables 
list_usuarios = []
objeto_usuario = Usuario()

while True:
    print(" Plataforma de Usuarios ")
    print(" 1.- Agrega Usuarios ")
    print(" 2.- Eliminar Usuarios ")
    print(" 3.- Actualizar Usuarios ")
    print(" 4.- Salida ")

    opciones_menu = input(" Introduce una opción")


    if int(opciones_menu) == 1:
        print(" Agregar Usuarios")
        in_usuario = input("Introduce el nombre")
        list_usuarios.append(objeto_usuario.mostrar_nombre(in_nombre=in_usuario))
        print(list_usuarios)
    elif int(opciones_menu) == 2: 
        print("Eliminar Usuarios")

    elif int(opciones_menu) == 3:
        print("Actualizar Usuarios")

    else:
        print("Gracias")


"""inp = '1'
match inp:
    case '1':
        print('Elegiste la opción 1')
    case '2':
        print('Elegiste la opción 2')"""
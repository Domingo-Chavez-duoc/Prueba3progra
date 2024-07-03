flag  = True
libros = []
#Chequear si es la primera sesión

print("¿Es la primera vez que usa la aplicación? y/n")
check = input()

if check.lower() == "y":
    libros = []
elif check.lower() == "n":
    with open("libreria.txt", "r") as archivo:
        linea = archivo.read().split("\n")
        for dato in linea[:-1]:
            libro = dato.split(",")
            libro = tuple(libro)
            print(libro)
            libros.append(libro)
            print(libros)


#Definir funciones
def reg(nombre, autor, genero):
    libros.append((nombre, autor, genero))
    return None

def search(autor):
    busqueda = []
    for datos in libros:
        if datos[1] == autor:
            busqueda.append(datos[0])
    return busqueda

#Bloque menú
while flag:
    #Bloque prints
    print("Bienvenido a la biblioteca, ingrese el numero correspondiente a la opción deseada")
    print("1.- Registrar libro")
    print("2.- Buscar libro por autor")
    print("3.- Mostrar lista de libros")
    print("4.- Salir \n")

    #Bloque desarrollo
    usuario = input("Ingrese número: ")
    if usuario == "1":
        nombre = input("Ingrese nombre del libro: ")
        autor = input("Ingrese autor del libro: ")
        genero = input("Ingrese género del libro: ")
        reg(nombre, autor, genero)
        print("¡Libro guardado!")

    elif usuario == "2":
        buscar = input("Ingrese nombre del autor: ")
        print("los libros del autor que ingresó son: ", search(buscar))

    elif usuario == "3":
        for datos in libros:
            print(datos)      

    elif usuario == "4":
        with open("libreria.txt", "w") as archivo:
            for datos in libros:
                string = datos[0] + "," + datos[1] + "," + datos[2] + "\n"
                print(string)
                archivo.write(string)
        flag = False
    
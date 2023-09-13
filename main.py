class Agenda:
    def __init__(self):
        self.contenido = []
    
    def menu(self):
        print("""
                1.- Crear una agenda nueva/sobreescribir agenda \n 
                2.- Añadir conctactos \n 
                3.- Buscar un contacto \n 
                4.- Eliminar un contacto \n
                5.- Ver todos los contactos \n 
                6.- Cerrar agenda \n 
                """)

    def cargar(self):
        try:
            file = open("listin.txt", "x")
            file.close()
            print("-------Se ha creado una nueva agenda vacia-------")
        except FileExistsError:
            respuesta = input("El archivo 'listin.txt' ya existe. ¿Deseas sobreescribirlo? (s/n): ")
            if respuesta.lower() == "s":
                file = open("listin.txt", "w")
                file.close()
                print("-------Se ha sobrescrito el archivo 'listin.txt'-------")
            else:
                print("No se ha sobrescrito el archivo 'listin.txt'.")

    def agregar(self, nombre, telefono):
        file = open("listin.txt", "a")
        try: 
            file.write(nombre)
            file.write(', ')
            file.write(telefono)
            file.write('\n')
        finally:
            file.close()
        print("Contacto guardado ")

    def buscar(self, busqueda):
        file = open("listin.txt", "r")
        for i in file.readlines():
            if busqueda in i:
                print(i)
                break
            file.close()
        else:
            print("El contacto no existe")    
  
    def eliminar(self, nombre):
        with open("listin.txt", "r") as file:
            for i in file:
                datos2 = i.split(",")
                if datos2[0] != nombre:
                    self.contenido.append(i)
            # else:
            #     print("el contacto no existe")
        with open("listin.txt", "w") as file:
            file.writelines(self.contenido) #almacena lista de strings    
        print("Contacto borrado ") 
        file.close()

    def eliminar(self, nombre):
        self.contenido = []
        contacto_encontrado = False

        with open("listin.txt", "r") as file:
            for i in file:
                datos2 = i.strip().split(",")
                if datos2[0] != nombre:
                    self.contenido.append(i)
                else:
                    contacto_encontrado = True

        if not contacto_encontrado:
            print("El contacto no existe")
        else:
            with open("listin.txt", "w") as file:
                file.writelines(self.contenido)
            print("Contacto borrado")
            

    def todos(self):
        with open("listin.txt", "r") as file:
            content = file.read()
            if not content:
                print("la agenda esta vacía")
            else:
                print(content)

agenda = Agenda()

while True:
    agenda.menu()
    seleccion = input("Introduce una de las opciones del menú: ")
    match seleccion:
        case "1":
            agenda.cargar()
        case "2":
            print("--------Añadir un contacto nuevo-------")
            mayus = input("Ingresa un nombre: ")
            nombre = mayus.capitalize()
            telefono = input("Ingresa un telefono: ")
            agenda.agregar(nombre, telefono)
        case "3":
            print("----------Buscar un contacto-----------")
            mayus = input("¿Que contacto deseas buscar?: ")
            busqueda = mayus.capitalize()
            agenda.buscar(busqueda)
        case "4":
            print("----------Eliminar un contacto-----------")
            mayus = input("¿Que contacto deseas eliminar?: ")
            nombre = mayus.capitalize()
            agenda.eliminar(nombre)
        case "5":
            print("--------Todos los contactos---------")
            agenda.todos()
        case "6":
            print("Agenda cerrada")
            break
        case _:
            print("Opcion no disponible")
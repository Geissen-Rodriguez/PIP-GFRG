# Importamos modulos necesarios
import json # Para guardar y cargar el estado de la mascota en formato JSON
import os # Para verificar si el archivo de estado existe en el sistema
import re  # Para validar el formato de fecha


# Clase padre Mascota con atributos comunes y metodos generales
class Mascota:
    def __init__(self, nombre, tipo, fecha_nacimiento):
        self.nombre = nombre
        self.tipo = tipo
        self.fecha_nacimiento = fecha_nacimiento
        self.status_hungry = 100
        self.status_sleep = 100
        self.status_dirty = 100
        self.status_happiness = 100
        self.viva = True

# Metodo comun para todas las mascotas
    def saltar(self):
        print(f"{self.nombre} está saltando.")

# Metodos para los estados

    def alimentar(self):
            self.status_hungry = min(100, self.status_hungry + 20)

    def dormir(self):
            self.status_sleep = min(100, self.status_sleep + 20)

    def limpiar(self):
            self.status_dirty = min(100, self.status_dirty + 20)


    # Metodo que actualiza el estado general y verifica si la mascota muere
    def actualizar_estado(self):
            if self.status_hungry < 30:
                self.status_happiness -= 10
            if self.status_hungry <= 0 or self.status_sleep <= 0 or self.status_dirty <= 0:
                self.viva = False
                print(f"{self.nombre} ha muerto.")

    # Metodo para guardar el estado actual en un archivo
    def guardar_estado(self):
            filename = f"{self.nombre}.status.x"
            with open(filename, "w") as f:
                json.dump(self.__dict__, f)

# Clases hijas por tipo de mascota con metodos unicos

class Ave(Mascota):
    def volar(self):
        print(f"{self.nombre} esta volando.")

class Reptil(Mascota):
    def arrastrarse(self):
        print(f"{self.nombre} se esta arrastrando.")

class Pez(Mascota):
    def nadar(self):
        print(f"{self.nombre} esta nadando.")

class Anfibio(Mascota):
    def nadar(self):
        print(f"{self.nombre} esta nadando.")

class Mamifero(Mascota):
    def correr(self):
        print(f"{self.nombre} esta corriendo.")

# Función para cargar el estado desde un archivo existente
def cargar_estado(nombre_archivo):
  try:  # Manejo de errores al cargar archivo
        with open(nombre_archivo, "r") as f:
            datos = json.load(f)

        tipo = datos['tipo']
        clases = {'Ave': Ave, 'Reptil': Reptil, 'Pez': Pez, 'Anfibio': Anfibio, 'Mamifero': Mamifero}
        mascota = clases[tipo](datos['nombre'], tipo, datos['fecha_nacimiento'])
        mascota.__dict__.update(datos)
        return mascota
  except FileNotFoundError:
        print(f" No se encontro el archivo '{nombre_archivo}'.")
        return None
  except KeyError:
        print("El archivo tiene un tipo de mascota no valido.")
        return None

# Funcion principal del juego
def jugar():
    clases = {'Ave': Ave, 'Reptil': Reptil, 'Pez': Pez, 'Anfibio': Anfibio, 'Mamifero': Mamifero}
    nombre_archivo = input("¿Nombre del archivo de estado? (ej: Firulais.status.x): ").strip()

    if nombre_archivo and os.path.exists(nombre_archivo):  # Validacion si el archivo existe y no esta vacio
        mascota = cargar_estado(nombre_archivo)
        if mascota is None:  # Si hubo error al cargar se termina el juego
            return
        print(f"Archivo cargado. Bienvenido de nuevo, {mascota.nombre}!")
    else:
        nombre = input("Nombre de la mascota: ").strip()
        tipo = input("Tipo de mascota (Ave, Reptil, Pez, Anfibio, Mamifero): ").strip()

        while tipo not in clases:  # Validacion del tipo de mascota
            print("Tipo invalido. Intenta nuevamente.")
            tipo = input("Tipo de mascota (Ave, Reptil, Pez, Anfibio, Mamifero): ").strip()

        fecha = input("Fecha de nacimiento (dd-mm-yyyy): ").strip()

        while not re.match(r"\d{2}-\d{2}-\d{4}", fecha):  # Validacion del formato de fecha
            print("Formato invalido. Usa dd-mm-yyyy.")
            fecha = input("Fecha de nacimiento (dd-mm-yyyy): ").strip()

        mascota = clases[tipo](nombre, tipo, fecha)
        
    # Bucle principal del juego
    while mascota.viva:
        # Mostramos el estado actual
        print(f"\nEstado de {mascota.nombre}:")
        print(f"Hambre: {mascota.status_hungry}")
        print(f"Sueño: {mascota.status_sleep}")
        print(f"Suciedad: {mascota.status_dirty}")
        print(f"Felicidad: {mascota.status_happiness}")

        # Preguntamos que acción desea realizar el usuario
        accion = input("¿Qué quieres hacer? (alimentar, dormir, limpiar, saltar, guardar, salir): ")

        # Ejecutamos la accion correspondiente
        if accion == "alimentar":
            mascota.alimentar()
        elif accion == "dormir":
            mascota.dormir()
        elif accion == "limpiar":
            mascota.limpiar()
        elif accion == "saltar":
            mascota.saltar()
        elif accion == "guardar":
            mascota.guardar_estado()
            print("Estado guardado.")
        elif accion == "salir":
            break
        else:
            print("Accion no reconocida. Intenta nuevamente.")  # Validacion de accion

        # Actualizamos el estado despues de cada accion
        mascota.actualizar_estado()

    # Mensaje final cuando termina el juego
    print("Fin del juego.")

# Ejecutamos la funcion principal
jugar()
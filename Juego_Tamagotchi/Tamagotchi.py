# Importamos modulos necesarios
import json # Para guardar y cargar el estado de la mascota en formato JSON
import os # Para verificar si el archivo de estado existe en el sistema
import re  # Para validar el formato de fecha
import random

# Clase padre Mascota con atributos comunes y metodos generales
class Mascota:
    def __init__(self, nombre, tipo, fecha_nacimiento):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__fecha_nacimiento = fecha_nacimiento
        self.__status_hungry = 100
        self.__status_sleep = 100
        self.__status_dirty = 100
        self.__status_happiness = 100
        self.__viva = True

# Metodo comun para todas las mascotas
    def saltar(self):
        print(f"{self.__nombre} está saltando.")
        self.afectar_estado_por_accion()

    def afectar_estado_por_accion(self):
        self.__status_hungry = max(0, self.__status_hungry - 10)
        self.__status_happiness = min(100, self.__status_happiness + 5)

    def alimentar(self):
        self.__status_hungry = min(100, self.__status_hungry + 20)

    def dormir(self):
        self.__status_sleep = min(100, self.__status_sleep + 20)

    def limpiar(self):
        self.__status_dirty = min(100, self.__status_dirty + 20)


    # Metodo que actualiza el estado general y verifica si la mascota muere
    def actualizar_estado(self):
        if self.__status_hungry == 3:
            self.__viva = False
            print(f"{self.__nombre} ha muerto por hambre critica.")
            return

        if self.__status_hungry < 30:
            self.__status_happiness = max(0, self.__status_happiness - 10)

        estados_críticos = sum([
            self.__status_hungry <= 0,
            self.__status_sleep <= 0,
            self.__status_dirty <= 0
        ])

        if estados_críticos >= 2:
            self.__viva = False
            print(f"{self.__nombre} ha muerto por multiples estados criticos.")

    # Metodo para guardar el estado actual en un archivo
    def guardar_estado(self):
        filename = f"{self.__nombre}.status.x"
        estado = {
            "nombre": self.__nombre,
            "tipo": self.__tipo,
            "fecha_nacimiento": self.__fecha_nacimiento,
            "status_hungry": self.__status_hungry,
            "status_sleep": self.__status_sleep,
            "status_dirty": self.__status_dirty,
            "status_happiness": self.__status_happiness,
            "viva": self.__viva
        }
        with open(filename, "w") as f:
            json.dump(estado, f)
        
    def mostrar_estado(self):
        print(f"\nEstado de {self.__nombre}:")
        print(f"Hambre: {self.__status_hungry}")
        print(f"Sueño: {self.__status_sleep}")
        print(f"Suciedad: {self.__status_dirty}")
        print(f"Felicidad: {self.__status_happiness}")

    def esta_viva(self):
        return self.__viva

    def obtener_nombre(self):
        return self.__nombre   
            

# Clases hijas por tipo de mascota con metodos unicos y accion especial por tipo de mascota que heredan y modifican estado

class Ave(Mascota):
    def volar(self):
        print(f"{self.obtener_nombre()} esta volando.")
        super().afectar_estado_por_accion()

class Reptil(Mascota):
    def arrastrarse(self):
        print(f"{self.obtener_nombre()} se esta arrastrando.")
        super().afectar_estado_por_accion()

class Pez(Mascota):
    def nadar(self):
        print(f"{self.obtener_nombre()} esta nadando.")
        super().afectar_estado_por_accion()

class Anfibio(Mascota):
    def nadar(self):
        print(f"{self.obtener_nombre()} esta nadando.")
        super().afectar_estado_por_accion()

class Mamifero(Mascota):
    def correr(self):
        print(f"{self.obtener_nombre()} esta corriendo.")
        super().afectar_estado_por_accion()

# Función para cargar el estado desde un archivo existente
def cargar_estado(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as f:
            datos = json.load(f)

        clases = {
            "Ave": Ave,
            "Reptil": Reptil,
            "Pez": Pez,
            "Anfibio": Anfibio,
            "Mamifero": Mamifero
        }

        tipo = datos["tipo"]
        mascota = clases[tipo](datos["nombre"], tipo, datos["fecha_nacimiento"])
        mascota._Mascota__status_hungry = datos["status_hungry"]
        mascota._Mascota__status_sleep = datos["status_sleep"]
        mascota._Mascota__status_dirty = datos["status_dirty"]
        mascota._Mascota__status_happiness = datos["status_happiness"]
        mascota._Mascota__viva = datos["viva"]
        return mascota

    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

# Funcion principal del juego
def jugar():
    clases = {'Ave': Ave, 'Reptil': Reptil, 'Pez': Pez, 'Anfibio': Anfibio, 'Mamifero': Mamifero}
    nombre_archivo = input("¿Nombre del archivo de estado? (ej: Firulais.status.x): ").strip()

    if nombre_archivo and os.path.exists(nombre_archivo):
        mascota = cargar_estado(nombre_archivo)
        if mascota is None:
            return
        print(f"Archivo cargado. Bienvenido de nuevo, {mascota.obtener_nombre()}!")
    else:
        nombre = input("Nombre de la mascota: ").strip()
        tipo = random.choice(list(clases.keys()))
        print(f"Tipo de mascota asignado aleatoriamente: {tipo}")

        fecha = input("Fecha de nacimiento (dd-mm-yyyy): ").strip()
        while not re.match(r"\d{2}-\d{2}-\d{4}", fecha):
            print("Formato inválido. Usa dd-mm-yyyy.")
            fecha = input("Fecha de nacimiento (dd-mm-yyyy): ").strip()

        mascota = clases[tipo](nombre, tipo, fecha)
        
    # Bucle principal del juego
    while mascota.esta_viva():
        mascota.mostrar_estado()
        accion = input("¿Qué quieres hacer? (alimentar, dormir, limpiar, saltar, moverse, guardar, salir): ").strip().lower()

        # Ejecutamos la accion correspondiente
        if accion == "alimentar":
            mascota.alimentar()
        elif accion == "dormir":
            mascota.dormir()
        elif accion == "limpiar":
            mascota.limpiar()
        elif accion == "saltar":
            mascota.saltar()
        elif accion == "moverse":
            if isinstance(mascota, Ave):
                mascota.volar()
            elif isinstance(mascota, Reptil):
                mascota.arrastrarse()
            elif isinstance(mascota, Pez):
                mascota.nadar()
            elif isinstance(mascota, Anfibio):
                mascota.nadar()
            elif isinstance(mascota, Mamifero):
                mascota.correr()
        elif accion == "guardar":
            mascota.guardar_estado()
            print("Estado guardado.")
        elif accion == "salir":
            break
        else:
            print("Accion no reconocida. Intenta nuevamente.")  # Validacion de accion
            
        #Degradacion pasiva de estados
        mascota._Mascota__status_sleep = max(0, mascota._Mascota__status_sleep - 5)
        mascota._Mascota__status_dirty = max(0, mascota._Mascota__status_dirty - 3)
        mascota._Mascota__status_happiness = max(0, mascota._Mascota__status_happiness - 2)

        # Actualizamos el estado despues de cada accion
        mascota.actualizar_estado()

    # Mensaje final cuando termina el juego
    print("Fin del juego.")

# Ejecutamos la funcion principal
jugar()
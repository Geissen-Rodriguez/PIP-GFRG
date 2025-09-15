import json

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


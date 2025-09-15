import json

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

def saltar(self):
        print(f"{self.nombre} está saltando.")

def alimentar(self):
        self.status_hungry = min(100, self.status_hungry + 20)

def dormir(self):
        self.status_sleep = min(100, self.status_sleep + 20)

def limpiar(self):
        self.status_dirty = min(100, self.status_dirty + 20)

def actualizar_estado(self):
        if self.status_hungry < 30:
            self.status_happiness -= 10
        if self.status_hungry <= 0 or self.status_sleep <= 0 or self.status_dirty <= 0:
            self.viva = False
            print(f"{self.nombre} ha muerto.")

def guardar_estado(self):
        filename = f"{self.nombre}.status.x"
        with open(filename, "w") as f:
            json.dump(self.__dict__, f)
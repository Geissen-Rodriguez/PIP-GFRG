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

class Botella:
    def __init__(self, marca, capacidad):
        self.marca = marca
        self.capacidad = capacidad

    def informacion(self):
        return f"Botella de {self.marca} con capacidad de {self.capacidad} ml"
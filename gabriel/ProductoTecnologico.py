class ProductoTecnologico:
    def __init__(self, marca, voltaje, precio, eficiencia):
        self.marca = marca
        self.voltaje = voltaje
        self.precio = precio
        self.eficiencia = eficiencia





    def calcular_descuento(self):
        if self.__eficiencia in ['A', 'B']:
            return 0.5
        elif self.__eficiencia in ['C', 'D']:
            return 0.3
        elif self.__eficiencia in ['E', 'F']:
            return 0.1
        else:
            return 0.0

 

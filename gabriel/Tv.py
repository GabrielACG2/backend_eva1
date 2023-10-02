from ProductoTecnologico import ProductoTecnologico

class Tv(ProductoTecnologico):
    def __init__(self, voltaje, precio, eficiencia, marca, tamano):
        super().__init__(voltaje, precio, eficiencia, marca)

        self.__tamano = tamano




    def get_tamano(self):
        return self.__tamano
    def set_tamano(self, tamano):
        self.__tamano = tamano





    def calcular_descuento(self):
            if self.__eficiencia in ['A', 'B']:
                return 0.5
            elif self.__eficiencia in ['C', 'D']:
                return 0.3
            elif self.__eficiencia in ['E', 'F']:
                return 0.1
            else:
                return 0.0



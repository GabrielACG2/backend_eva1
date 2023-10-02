from ProductoTecnologico import ProductoTecnologico




class Scoter(ProductoTecnologico):
    def __init__(self, voltaje, precio, eficiencia, marca, aro, velocidad, peso):
        super().__init__(voltaje, precio, eficiencia, marca)

        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso




    def get_aro(self):
        return self.__aro
    def get_velocidad(self):
        return self.__velocidad
    def get_peso(self):
        return self.__peso




    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad
    def set_aro(self, aro):
        self.__aro = aro
    def set_peso(self, peso):
        self.__peso = peso

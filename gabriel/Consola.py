from ProductoTecnologico import ProductoTecnologico




class Consola(ProductoTecnologico):
    def __init__(self, voltaje, precio, eficiencia, marca, nombreConsola, version):
        super().__init__(voltaje, precio, eficiencia, marca)

        self.nombreConsola = nombreConsola
        self.version = version





    def get_nombreConsola(self):
        return self.__nombreConsola
    def get_version(self):
        return self.__version
    


    def set_nombreConsola(self, nombreConsola):
        self.__nombreConsola = nombreConsola
    def set_version(self, version):
        self.__version = version

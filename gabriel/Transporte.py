class Transporte:
    COSTO_DESPACHO_BASE = 4000

    def __init__(self, peso: float, aro: float):
        self.__peso = peso
        self.__aro = aro

    def calcular_despacho(self):
        costo_despacho_total = Transporte.COSTO_DESPACHO_BASE + self.__peso * 400
        return costo_despacho_total

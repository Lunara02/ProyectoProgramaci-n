class GenNum:
    def __init__(self, matriz):
        self.matriz = matriz
        self.n = len(matriz)
        self.num_filas = []
        self.num_columnas = []

    def get_num(self, fila_columna):
        numeros = []
        contador = 0
        for numero in fila_columna:
            if numero==1:
                contador += 1
            elif contador > 0:
                numeros.append(contador)
                contador = 0
        if contador > 0:
            numeros.append(contador)
        return numeros
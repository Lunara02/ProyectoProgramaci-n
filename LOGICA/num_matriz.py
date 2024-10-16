class GenNum:
    def __init__(self, matriz):
        self.matriz = matriz
        self.n = len(matriz)
        self.num_filas = []
        self.num_columnas = []

    def get_num(self, fila_columna):
        num = []
        contador = 0
        for valor in fila_columna:
            if valor == 1:
                contador += 1
            elif contador > 0:
                num.append(contador)
                contador = 0
        if contador > 0:
            num.append(contador)

        if len(num) == 0:
            num.append(0)
        return num

    def create_num(self):
        for i in range (len(self.matriz)):
            self.num_filas.append(self.get_num(self.matriz[i]))
        columnas = []
        for j in range(self.n):
            for i in range(self.n):
                columnas.append(self.matriz[i][j])
            self.num_columnas.append(self.get_num(columnas))
            columnas = []


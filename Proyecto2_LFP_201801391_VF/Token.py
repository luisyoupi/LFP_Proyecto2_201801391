class token:
    def __init__(self,tipo,lexema,fila,columna) -> None:  
        self.__tipo = tipo
        self.__lexema = lexema
        self.__fila = fila
        self.__columna = columna
    #Getters and Setters
    def getTipo(self):
        return self.__tipo
    def setTipo(self,tipo):
        self.__tipo = tipo
    def getLexema(self):
        return self.__lexema
    def setLexema(self,lex):
        self.__lexema = lex
    def getFila(self):
        return self.__fila
    def setFila(self,fila):
        self.__fila = fila
    def getColumna(self):
        return self.__columna
    def setTipo(self,columna):
        self.__columna = columna
    def mostrar(self):
        print("["+self.getTipo()+" , "+self.getLexema()+" , "+str(self.getFila())+" , "+str(self.getColumna())+"]")
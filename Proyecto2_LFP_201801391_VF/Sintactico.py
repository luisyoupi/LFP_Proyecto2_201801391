#No terminales son funciones
from Token import token
class Sintactico:
    def __init__(self,tokens) -> None:
        self.reserved = ["Tk_imprimir","Tk_imprimirln","Tk_promedio","Tk_sumar","Tk_max","Tk_min","Tk_exportarreporte"]
        self.errorSintactico = False
        self.error =[]
        self.tokens = tokens
        self.tokens.append(token("Tk_Final","*",0,0))
        self.posicion = 0
        self.actual = self.tokens[self.posicion].getTipo()
        self.inicio()
    def equals(self,tipo):
        if self.actual != tipo:
            self.errorSintactico = True
            er = self.tokens[self.posicion-1]
            a = token(er.getTipo(),er.getLexema(),er.getFila(),er.getColumna())
            a.setLexema("Token esperado: "+str(tipo)+", token recivido: "+self.actual)
            self.error.append(a)
            print("Token esperado: "+str(tipo)+", token recivido: "+self.actual)
        if self.actual == tipo:
            self.posicion+=1
            self.actual = self.tokens[self.posicion].getTipo()

        if self.actual == "Tk_Final":
            print("Análisis Sintáctico Terminado")

    def reservada(self,tipo):
        for a in self.reserved:
            if tipo == a:
                self.posicion+=1
                self.actual = self.tokens[self.posicion].getTipo()
                return True
        return False
    def inicio(self):
        if self.actual == "Tk_ComentarioLinea":
            self.equals("Tk_ComentarioLinea")
            self.inicio()
        elif self.actual == "Tk_ComentarioMultilinea":
            self.equals("Tk_ComentarioMultilinea")
            self.inicio()
        elif self.reservada(self.actual):
            self.instruccion()
            self.inicio()
        elif self.actual == "Tk_datos" or self.actual == "Tk_conteo":
            self.instruccion2()
            self.inicio()
        elif self.actual == "Tk_contarsi":
            self.contar()
            self.inicio()
        elif self.actual == "Tk_claves":
            self.claves()
            self.inicio()
        elif self.actual == "Tk_registros":
            self.registros()
            self.inicio()

    def instruccion(self):
        self.equals("Tk_AbreP")
        self.equals("Tk_Cadena")
        self.equals("Tk_CierraP")
        self.equals("Tk_PuntoyC")
        
    def instruccion2(self):
        self.accion()
        self.equals("Tk_AbreP")
        self.equals("Tk_CierraP")
        self.equals("Tk_PuntoyC")
    def accion(self):
        if self.actual == "Tk_datos":
            self.equals("Tk_datos")
        elif self.actual == "Tk_conteo":
            self.equals("Tk_conteo")

    def contar(self):
        self.equals("Tk_contarsi")
        self.equals("Tk_AbreP")
        self.equals("Tk_Cadena")
        self.equals("Tk_Coma")
        self.equals("Tk_Numero")
        self.equals("Tk_CierraP")
        self.equals("Tk_PuntoyC")
    def claves(self):
        self.equals("Tk_claves")
        self.equals("Tk_igual")
        self.equals("Tk_AbreC")
        self.campos()
        self.equals("Tk_CierraC")
    def campos(self):
        self.equals("Tk_Cadena")
        self.otro()
    def otro(self):
        if self.actual == "Tk_Coma":
            self.equals("Tk_Coma")
            self.campos()
            
    def registros(self):
        self.equals("Tk_registros")
        self.equals("Tk_igual")
        self.equals("Tk_AbreC")
        self.registro()
        self.equals("Tk_CierraC")

    def registro(self):
        self.equals("Tk_AbreL")
        self.reg()
        self.equals("Tk_CierraL")
        self.mas()

    def reg(self):
        if self.actual == "Tk_Cadena":
            self.equals("Tk_Cadena")
            self.otroR()
        elif self.actual == "Tk_Numero":
            self.equals("Tk_Numero")
            self.otroR()

    def mas(self):
        if self.actual == "Tk_AbreL":
            self.registro()

    def otroR(self):
        if self.actual == "Tk_Coma":
            self.equals("Tk_Coma")
            self.reg()



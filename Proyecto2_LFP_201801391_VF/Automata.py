from Token import token

class analizador:
    def __init__(self) -> None:
        self.__lexema=""
        self.__estado =0
        self.__tokens = []
        self.__errores = []
        self.__simbolo = {"=":"Tk_igual",";":"Tk_PuntoyC","{":"Tk_AbreL","[":"Tk_AbreC","]":"Tk_CierraC","}":"Tk_CierraL",",":"Tk_Coma","(":"Tk_AbreP",")":"Tk_CierraP"}
        self.__reservada = ["claves","registros","imprimir","imprimirln","conteo","promedio","contarsi","datos","sumar","max","min","exportarreporte"]
    def getTokens(self):
        return self.__tokens
    def getErrores(self):
        return self.__errores
    
    def palabraReservada(self,palabra):
        for a in self.__reservada:
            if palabra.lower() == a:
                return True
        return False
    def nuevoToken(self,tipo,lexema,fila,columna):
        tok = token(tipo,lexema,fila,columna)
        if tipo!="Error":
            self.__tokens.append(tok)
            self.__lexema = ""
            self.__estado = 0
        else:
            self.__errores.append(tok)
    def mostrarTokens(self):
        print("--Lista Tokens--")
        for tok in self.__tokens:
            tok.mostrar()
    def mostrarErrores(self):
        print("--Lista Errores--")
        for tok in self.__errores:
            tok.mostrar()
    def analizar(self,entrada):
        i=0
        fila =1
        columna =0
        tkSimbolo = ""
        while i < len(entrada):
            actual = entrada[i] #actual ya es un caracter
            if self.__estado == 0:#Estado inicial
                if actual.isalpha():#Enviar a estado para palabras reservadas
                    self.__lexema+=actual
                    self.__estado = 1
                    columna+=1
                    print("Letra")
                    i+=1
                elif actual.isdigit():#Enviar a estado para numeros
                    self.__lexema+=actual
                    self.__estado=2
                    columna+=1
                    i+=1
                elif actual == "\"":#Enviar a estado de Cadena
                    self.__lexema+=actual
                    self.__estado=3
                    columna+=1
                    i+=1
                elif actual == "#":#Enviar a estado para comentario de linea
                    self.__lexema+=actual
                    self.__estado=4
                    columna+=1
                    i+=1
                elif not self.__simbolo.get(actual) == None:#Enviar a estado de símbolos 
                    tkSimbolo = self.__simbolo.get(actual)
                    self.__lexema+=actual
                    self.__estado=5
                    columna+=1
                    #Dudando en quitar i+=1
                elif actual == "\'":#Enviar a estado para comentario multi linea
                    self.__lexema+=actual
                    self.__estado=6
                    columna+=1
                    i+=1
                elif actual == '\n':
                    fila+=1
                    columna = 0
                    i+=1
                elif actual == '\t' or actual == ' ' or actual == '\r'  : #omitir simbolos
                    columna +=1
                    i+=1
                else:
                    print("El símbolo: "+actual+" no pertenece al lenguaje") #aniadir a errores Lexicos
                    self.nuevoToken("Error",actual,fila,columna)
                    columna+=1
                    i+=1
            elif self.__estado == 1:#Estado para palabras reservadas
                if actual.isalpha():
                    self.__lexema+=actual
                    self.__estado = 1
                    columna+=1
                    print("Letra")
                    i+=1
                else:
                    if self.palabraReservada(self.__lexema):
                        self.nuevoToken("Tk_"+self.__lexema.lower(),self.__lexema,fila,columna) #Aceptarmos la letra (Comprobar si es reservada)(estado=0 y lexema ="" añiadir en el método de tokens)
                        print("Aceptamos la palabra")
                    else:
                        self.nuevoToken("Error",self.__lexema,fila,columna)
                        self.__lexema=""
                        self.__estado=0
                        columna+=1
                        i+=1
            elif self.__estado == 2:#Estado para numeros
                if actual.isdigit():
                    self.__lexema+=actual
                    self.__estado=2
                    columna+=1
                    i+=1
                elif actual ==".":#Para aceptar decimales
                    self.__lexema+=actual
                    self.__estado=7
                    columna+=1
                    i+=1
                else:
                    self.nuevoToken("Tk_Numero",self.__lexema,fila,columna)#Acá aceptamos un número entero
                    print("numero entero")
            elif self.__estado == 3:#Estado de cadenas, LNR
                if actual.isalpha() or actual.isdigit():
                    self.__lexema+=actual
                    self.__estado=3
                    columna+=1
                    i+=1
                elif actual == "\"":#Termina la cadena
                    self.__lexema+=actual
                    self.__estado=5
                    columna+=1
                    #Dudando en quitar i+=1
                else:
                    self.__lexema+=actual
                    self.__estado=3
                    columna+=1
                    i+=1
            elif self.__estado == 4: #Estado de comentarios
                if actual.isalpha() or actual.isdigit():
                    self.__lexema+=actual
                    self.__estado=4
                    columna+=1
                    i+=1
                elif actual == "\n":#Aceptamos el comentario, revisar (aniadir token)
                    self.nuevoToken("Tk_ComentarioLinea",self.__lexema,fila,columna)
                    print("aceptarmos el comentario")
                else:
                    self.__lexema+=actual
                    self.__estado=4
                    i+=1
            elif self.__estado == 5:
                if actual == "\"":
                    print("añadir token cadena")
                    self.nuevoToken("Tk_Cadena",self.__lexema,fila,columna)
                    
                elif actual == "\'":
                    print("aniadir token de comentario multilinea")
                    self.nuevoToken("Tk_ComentarioMultilinea",self.__lexema,fila,columna)
                    
                else:
                    print("añadir token de simbolo")
                    self.nuevoToken(tkSimbolo,self.__lexema,fila,columna)
                i+=1
            elif self.__estado == 6:
                if actual=="\'":
                    self.__lexema+=actual
                    self.__estado = 8
                    columna+=1
                    i+=1
                else:
                    print("Caracter desconocido")
                    self.__estado=0
            elif self.__estado == 7:
                if actual.isdigit():
                    self.__lexema+=actual
                    self.__estado=9
                    columna+=1
                    i+=1
                else:
                    self.__estado=0
                    print("no hay numero luego de punto")
            elif self.__estado == 8:
                if actual=="\'":
                    self.__lexema+=actual
                    self.__estado = 10
                    columna+=1
                    i+=1
                else:
                    print("Caracter desconocido")
                    self.__estado=0
            elif self.__estado == 9:
                if actual.isdigit():
                    self.__lexema+=actual
                    self.__estado=9
                    columna+=1
                    i+=1
                else:
                    self.nuevoToken("Tk_Numero",self.__lexema,fila,columna)#aaadir token
                    print("Aceptamos numero decimal")
            elif self.__estado == 10:
                if actual.isalpha() or actual.isdigit():
                    self.__lexema+=actual
                    self.__estado=10
                    columna+=1
                    i+=1
                elif actual=="\'":
                    self.__lexema+=actual
                    self.__estado = 11
                    columna+=1
                    i+=1
                else:
                    self.__lexema+=actual
                    self.__estado=10
                    columna+=1
                    i+=1
            elif self.__estado == 11:
                if actual=="\'":
                    self.__lexema+=actual
                    self.__estado = 12
                    columna+=1
                    i+=1
                else:
                    print("Caracter desconocido")
                    self.__estado=0
            elif self.__estado == 12:
                if actual=="\'":
                    self.__lexema+=actual
                    self.__estado = 5
                    columna+=1
                else:
                    print("Caracter desconocido")
                    self.__estado=0
        self.mostrarTokens()
        self.mostrarErrores()
        

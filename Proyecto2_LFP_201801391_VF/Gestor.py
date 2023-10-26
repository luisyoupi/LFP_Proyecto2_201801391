from tkinter import *
from Reportes import Reporte
from os import PathLike, system, write
import os
import sys
class Gestor:
    def __init__(self,tokens,consola) -> None:
        self.__tokens = tokens
        self.__info = []
        self.__consola = consola
        self.cant = 0
        self.arbol = ""
        self.asintactico = []
    def llenar(self,error):
        if not error:
            i=0
            n = 1
            while i<len(self.__tokens):
                actual = self.__tokens[i]
                if actual.getTipo() == "Tk_claves":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+1].getTipo()+str(n)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+2].getTipo()+str(n)+"\n"
                    campos = []
                    i+=3
                    actual = self.__tokens[i]
                    while actual.getTipo()!="Tk_CierraC":
                        if actual.getTipo() != "Tk_Coma":
                            self.arbol+="Instruccion"+str(n)+"->\""+actual.getTipo()+str(n+i)+"\"->"+actual.getLexema()+str("\".\""*n)+"\n"
                            campos.append(actual.getLexema().replace("\"","").strip())
                        else:
                            self.arbol+="Instruccion"+str(n)+"->\""+actual.getLexema()+str(n+i)+"\"\n"
                        i+=1
                        actual = self.__tokens[i]
                    self.__info.append(campos)
                    self.arbol+="Instruccion"+str(n)+"->\""+actual.getTipo()+str(n)+"\"\n"
                    self.asintactico.append(self.arbol)   
                    n+=1
                elif actual.getTipo() == "Tk_registros":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i].getTipo()+str(n)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+1].getTipo()+str(n)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+2].getTipo()+str(n)+"\n"
                    registro = []
                    i+=4
                    actual = self.__tokens[i]
                    while actual.getTipo()!="Tk_CierraC":
                        if actual.getTipo() != "Tk_Coma" and actual.getTipo() != "Tk_CierraL" and actual.getTipo() != "Tk_AbreL":
                            self.arbol+="Instruccion"+str(n)+"->\""+actual.getTipo()+str(n+i)+"\"->"+actual.getLexema()+str("\".\""*n)+"\n"
                            registro.append(actual.getLexema().replace("\"","").strip())
                        else:
                            self.arbol+="Instruccion"+str(n)+"->\""+actual.getTipo()+str(n+i)+"\"\n"    
                        if actual.getTipo() == "Tk_CierraL":
                            self.arbol+="Instruccion"+str(n)+"->"+actual.getTipo()+str(n+i)+"\n"   
                            self.__info.append(registro)
                            self.cant+=1
                            registro = []
                        i+=1
                        actual = self.__tokens[i]
                    self.arbol+="Instruccion"+str(n)+"->\""+actual.getTipo()+str(n)+"\"\n"  
                    self.asintactico.append(self.arbol)   
                    n+=1
                elif actual.getTipo() == "Tk_imprimir":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.imprimir(self.__tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+2].getTipo()+str(n+i)+"->"+self.__tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)   
                    n+=1
                elif actual.getTipo() == "Tk_imprimirln":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.imprimirln(self.__tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+1].getTipo()+str(n)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+2].getTipo()+str(n+i)+"->"+self.__tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_conteo":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.conteo()
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+2].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_promedio":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.promedio(self.__tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+2].getTipo()+str(n+i)+"->"+self.__tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_contarsi":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.contarsi(self.__tokens[i+2].getLexema().replace("\"",""),float(self.__tokens[i+4].getLexema()))
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+2].getTipo()+str(n+i)+"->"+self.__tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+4].getTipo()+str(n+i)+"->"+self.__tokens[i+4].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+5].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+6].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_datos":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.datos()
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+2].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_sumar":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.suma(self.__tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+2].getTipo()+str(n+i)+"->"+self.__tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_max":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.max(self.__tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+2].getTipo()+str(n+i)+"->"+self.__tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_min":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.min(self.__tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+2].getTipo()+str(n+i)+"->"+self.__tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_exportarreporte":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.reporte(self.__tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+2].getTipo()+str(n+i)+"->"+self.__tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.__tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                
                i+=1
            print(self.__info) 
        else:
            self.__consola.insert(INSERT,"\nSyntaxError: invalid syntax\nRevisar reporte de errores")
    def imprimir(self,cadena):
        self.__consola.insert(INSERT,cadena)
    def imprimirln(self,cadena):
        self.__consola.insert(INSERT,cadena+"\n")
    def conteo(self):
        self.__consola.insert(INSERT,str(self.cant)+"\n")
    def promedio(self,campo):
        i=0
        promedio = 0
        for j in range(len(self.__info[0])):
            if self.__info[0][j] == campo:
                i=j
        for j in range(1,len(self.__info)):
            promedio+= float(self.__info[j][i])
        if i==0:
            i+=1
        promedio = promedio/i
        self.__consola.insert(INSERT,str(promedio)+"\n")  
    def contarsi(self,campo,valor):
        cantidad = 0
        for j in range(len(self.__info[0])):
            if self.__info[0][j] == campo:
                i=j
        for j in range(1,len(self.__info)):
            if valor == float(self.__info[j][i]):
                cantidad+=1 
        self.__consola.insert(INSERT,str(cantidad)+"\n")  
    def datos(self):
        self.__consola.insert(INSERT,">>>")  
        for linea in self.__info[0]:  
            self.__consola.insert(INSERT,str(linea)+"\t\t")
        
        for i in range(1,len(self.__info)):
            self.__consola.insert(INSERT,"\n>>>") 
            for j in range(len(self.__info[i])):  
                self.__consola.insert(INSERT,self.__info[i][j]+"\t\t")   
        self.__consola.insert(INSERT,"\n")  
          
    def suma(self,campo):
        i=0
        suma = 0
        for j in range(len(self.__info[0])):
            if self.__info[0][j] == campo:
                i=j
        for j in range(1,len(self.__info)):
            suma+= float(self.__info[j][i])
        self.__consola.insert(INSERT,str(suma)+"\n") 
    def max(self,campo):
        i=0
        max = 0
        for j in range(len(self.__info[0])):
            if self.__info[0][j] == campo:
                i=j
        for j in range(1,len(self.__info)):
            if max < float(self.__info[j][i]):
                max = float(self.__info[j][i])
        self.__consola.insert(INSERT,str(max)+"\n")  
    def min(self,campo):
        i=0
        for j in range(len(self.__info[0])):
            if self.__info[0][j] == campo:
                i=j
        min = float(self.__info[1][i])
        for j in range(1,len(self.__info)):
            if min > float(self.__info[j][i]):
                min = float(self.__info[j][i])
        self.__consola.insert(INSERT,str(min)+"\n")
    def reporte(self,titulo):
        report = Reporte()
        report.reporteHTML(titulo,self.__info)
    def reporteArbol(self):
        a = "digraph G {Inicio"
        temp = ""
        for i in range(len(self.asintactico)):
            if i == 0:
                a+="->ListaInstrucciones"+str(i)
                a+=self.asintactico[i]
            else:
                a+="ListaInstrucciones"+str(i-1)
                a+="->ListaInstrucciones"+str(i)
                a+=self.asintactico[i]
        a+="}"
        nam = "ArbolSintactico"
        doc = open(nam+".dot","w")
        doc.write(a)
        doc.close()
        os.environ["PATH"] += os.pathsep+"C:/Program Files/Graphviz/bin"
        os.system("dot -Tpng "+nam+".dot -o "+nam+".png")
        os.startfile(nam+".png")

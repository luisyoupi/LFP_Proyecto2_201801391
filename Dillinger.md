
# Nombre del Curso -Lenguajes formales de programacion
## Semestre/Vacaciones: Semestre

**Universidad San Carlos de Guatemala**  
**Programador:** Luis Fernando Gomez Rendon
**Carne:** 201801391 
**Correo:** Luisfer789b@gmail.com

---

# Manual de tecnico

## Introducción

El presente manual tiene como objetivo proporcionar una guía comprensible y accesible sobre el uso de un software diseñado para ejecutar una variedad de instrucciones a partir de la lectura de un archivo de texto plano con extensión ".bizdata" o de instrucciones escritas directamente en un área de texto.

A lo largo de esta guía, dirigida a personas sin experiencia previa en programación, exploraremos detalladamente las funcionalidades de esta herramienta y proporcionaremos instrucciones paso a paso para su correcto uso. Este manual está diseñado para ser una puerta de entrada a la informática y la automatización de tareas, independientemente del nivel de experiencia del usuario.

A medida que avanzamos en el manual, aprenderemos a cargar archivos ".bizdata" de instrucciones, analizar su contenido y ejecutar tareas específicas. Además, se presentarán ejemplos prácticos que ilustrarán cómo este software puede ser una herramienta poderosa en diversos contextos, desde la automatización de tareas cotidianas hasta la gestión de datos complejos.

## Requisitos del Sistema
Antes de utilizar la aplicación, asegúrate de tener instalados los siguientes componentes:

Python: Debe tener una instalación funcional de Python 3.x en su sistema.

Bibliotecas de Python: Deben estar instaladas las bibliotecas tkinter, json, math, y . Puedes instalar estas bibliotecas usando pip:
pip install grahiz
.

## Instalación y Ejecución

1. Descargue el archivo ejecutable o los archivos de código fuente de la aplicación desde [enlace de descarga].
2. Instale la librería Graphviz siguiendo las instrucciones de su sitio web oficial: [enlace de instalación de Graphviz].
3. Ejecute la aplicación utilizando el siguiente comando en la terminal o símbolo del sistema:

       4.pip install grahpiz 

## Interfaz de Usuario (UI)
Interfaz de Usuario
La interfaz de usuario (UI) de la aplicación es sencilla y amigable. Se compone de tres secciones principales:

Barra de Herramientas (ToolBar): Esta sección proporciona acceso rápido a las funciones esenciales de la aplicación. La barra de herramientas contiene una etiqueta que muestra el nombre del proyecto.

Área de Código (CodeFrame): Aquí es donde los usuarios pueden cargar archivos de texto ".bizdata" o ingresar sus propias instrucciones. Un cuadro de texto les permite realizar estas acciones.

Consola (ConsoleFrame): La consola proporciona una ventana de salida para los resultados de análisis y otros mensajes importantes.

```
class App:
    def __init__(self,root:tk.Toplevel) -> None:
        #Variables
        self.entrada= ""
        self.tokens = []
        self.errores = []
        self.erroresSintacticos=[]
        #Ventana
        root.title("Analizador Bizdata")
        root.config(bg="green")
        #Frames
            #ToolBar
        toolBar = tk.Frame(root,width=700,height=50,bg="black").grid(row=0,padx=5,pady=5)
            #Cuadro donde irá el código
        codeFrame = tk.Frame(root,width=700,height=300,bg="black")
        codeFrame.grid(row=1,padx=5,pady=5)
            #Consola
        consoleFrame = tk.Frame(root,width=100,height=100,bg="black")
        consoleFrame.grid(row=2,padx=5,pady=5)
        
        #Menu
        menubar = Menu(root)
            #Carga y Salir
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.carga)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)
            #Analizar
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Analizar", command=self.analizar)
        '''        '''
        menubar.add_cascade(label="Analizar Archivo", menu=editmenu)
            #Reportes
        reportMenu = Menu(menubar, tearoff=0)
        reportMenu.add_command(label="Reporte de Tokens", command=self.reporteTokens)
        reportMenu.add_command(label="Reporte de Errores", command=self.reporteErrores)
        reportMenu.add_command(label="Árbol de Derivación", command=self.arbol)
        menubar.add_cascade(label="Reportes", menu=reportMenu)
        root.config(menu=menubar)

        
        #Botones
        
        buttons = tk.Frame(toolBar,width=700,height=50,bg="black")
        buttons.grid(row=0,padx=5,pady=5)
        self.label = tk.Label(buttons,text="proyecto 2 201801391",relief=RAISED).grid(row=0,column=0,padx=5,pady=5)
        
        # Consola
        self.text = Text(codeFrame,width=86,height=20)
        self.text.grid(row=0,column=0,padx=5,pady=5)
        # Consola
        self.console = Text(consoleFrame,width=86,height=15)#Ver para que sea solo lectura
        self.console.grid(row=0,column=0,padx=5,pady=5)

    def carga(self):
        try:
            path = filedialog.askopenfilename(filetypes=[('Texto plano', '*.bizdata')])
            self.entrada = open(path,"r").read()
            self.text.delete("1.0",END)
            self.text.insert(INSERT,self.entrada)
            messagebox.showinfo("Carga","Carga de archivo exitosa")
        except:
            messagebox.showerror("Error","Error al cargar el archivo")
    def analizar(self):
        text = self.text.get("1.0",END)#Imprime por linneas separado por \n, SUSCEPTIBLE A CAMBIOS POR QUE ES CONSOLA
        # print(text[len(text)-1])#el texto siempre termian con un salto de linea
        # for a in text:
        #     self.console.insert(INSERT,">>>"+a+"\n")
        analizar = analizador()
        analizar.analizar(text)
        self.tokens = analizar.getTokens()
        self.errores = analizar.getErrores()
        sintact = Sintactico(self.tokens)
        self.erroresSintacticos = sintact.error
        self.ges = Gestor(sintact.tokens,self.console)
        self.ges.llenar(sintact.errorSintactico)
        messagebox.showinfo("OJO","Análisis realizado")
    def reporteTokens(self):
        report = Reporte()
        report.reporteTokens("Tokens",self.tokens,None)
    def reporteErrores(self):
        report = Reporte()
        report.reporteTokens("Errores",self.errores,self.erroresSintacticos)
    def arbol(self):
        self.ges.reporteArbol()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop() 
```






...
### Funciones Principales
El programa ofrece una variedad de funciones que facilitan el análisis de texto y la generación de informes. Aquí están las principales funcionalidades destacadas:

Cargar Archivos
Los usuarios pueden cargar archivos de texto ".bizdata" utilizando la opción "Abrir" en el menú "Archivo". El contenido del archivo se mostrará en el área de código, lo que facilita la preparación para el análisis.

Análisis de Texto
La función de análisis permite a los usuarios procesar el contenido del área de código. Después de hacer clic en "Analizar" en el menú "Analizar Archivo", el programa realizará un análisis del texto, identificando tokens y posibles errores. Los resultados se almacenan en variables internas para su posterior uso.

Generación de Reportes
El programa puede generar informes que muestran los resultados del análisis. Ofrece tres tipos de informes:

Reporte de Tokens: Muestra los tokens identificados durante el análisis.
Reporte de Errores: Muestra los errores identificados durante el análisis.
Árbol de Derivación: Representa gráficamente la estructura de las instrucciones.

```
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
```



```



#### Reporte
Generación de Tablas en HTML
printTableToken: Esta función genera una tabla HTML para representar tokens. La tabla incluye columnas para el tipo de token, el lexema, la fila y la columna en la que se encontró. Los datos de tokens se extraen de una lista proporcionada como argumento.

printTableError: Similar a printTableToken, esta función crea una tabla para mostrar errores. Los errores se representan con columnas para el mensaje de error, la fila y la columna donde ocurrieron. Los datos de errores se toman de una lista proporcionada.

Generación de Informes en HTML
reporteTokens: Esta función genera un informe completo en formato HTML para mostrar los tokens analizados. El informe se crea con etiquetas HTML que incluyen un estilo de fondo atractivo y una estructura de tabla organizada. Además, si se proporciona una lista de errores sintácticos, se genera un informe separado para estos errores. Los informes se guardan en archivos HTML y se abren automáticamente en un navegador web para que los usuarios los revisen.

reporteHTML: Esta función se utiliza para generar informes en HTML a partir de un conjunto de datos específico, como registros de una tabla. Los informes se guardan en archivos HTML y se abren automáticamente en un navegador web para su revisión.

```
class Reporte:
    def __init__(self) -> None:
        print("")
    def printTableToken(self,report,lis):
        report.write("""<div class="container"><table class="table">
                                <thead class="letra">
                                    <tr>
                                    <th scope="col">Token</th>
                                    <th scope="col">Lexema</th>
                                    <th scope="col">Fila</th>
                                    <th scope="col">Columna</th>
                                    </tr>
                                </thead>
                                <tbody class="letra">
                                """)
        for tok in lis:
            if tok.getTipo() != "Final":
                report.write("<tr><td>"+tok.getTipo()+"</td><td>"+str(tok.getLexema())+"</td><td>"+str(tok.getFila())+"</td><td>"+str(tok.getColumna())+"</td></tr>")
        report.write(""" </center></tbody>
                                </table></div>""")
    def printTableError(self,report,lis):
        report.write("""<div class="container"><table class="table">
                                <thead class="letra">
                                    <tr>
                                    <th scope="col">Error</th>
                                    <th scope="col">Fila</th>
                                    <th scope="col">Columna</th>
                                    </tr>
                                </thead>
                                <tbody class="letra">
                                """)
        for tok in lis:
             report.write("<tr><td>"+str(tok.getLexema())+"</td><td>"+str(tok.getFila())+"</td><td>"+str(tok.getColumna())+"</td></tr>")
        report.write(""" </center></tbody>
                                </table></div>""")
    def reporteTokens(self,titulo,tokens,sintactico):
        report = open("Reporte"+titulo+".html","w")
        report.write("<html><head><title>Reporte "+titulo+" </title>"+
        """<style>
        body{
        background: #b92b27;  /* fallback for old browsers */
        background: -webkit-linear-gradient(to top, #1565C0, #b92b27);  /* Chrome 10-25, Safari 5.1-6 */
        background: linear-gradient(to top, #1565C0, #b92b27); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        }
        .letra{
            color: White;
        }
        h1, h2{
            color: White;
        }
        </style>
        <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC\" crossorigin=\"anonymous\"><link rel=\"stylesheet\" href=\"style.css\"></link></head>""")
        report.write("<body><center><h1>Reporte de "+titulo+" </h1><br>")
        report.write("<br>")
        self.printTableToken(report,tokens)
        if titulo =="Errores":
            report.write("<h2>Reporte de "+titulo+" Sintácticos</h2><br>")
            self.printTableError(report,sintactico)
        report.write("</body></html>")
        report.close()
        webbrowser.open("Reporte"+titulo+".html")
    def reporteHTML(self,titulo,registros):
        report = open(titulo+".html","w")
        report.write("<html><head><title>Reporte "+titulo+" </title>"+
        """<style>
        body{
        background: #8e9eab;  /* fallback for old browsers */
        background: -webkit-linear-gradient(to top, #eef2f3, #8e9eab);  /* Chrome 10-25, Safari 5.1-6 */
        background: linear-gradient(to top, #eef2f3, #8e9eab); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        }
        .letra{
            color: White;
        }
        h1{
            color: White;
        }
        </style>
        <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC\" crossorigin=\"anonymous\"><link rel=\"stylesheet\" href=\"style.css\"></link></head>""")
        report.write("<body><center><h1>"+titulo+" </h1><br>")
        report.write("<br>")
        self.printTable(titulo,report,registros)
        report.write("</body></html>")
        report.close()
        webbrowser.open(titulo+".html")
    def printTable(self,titulo,report,lis):
        report.write("""<div class="container"><table class="table table-dark table-striped table-hover">
                                <thead class="letra">""")
        report.write("<tr class=\"table-dark\"><th colspan=\""+str(len(lis[0]))+"\">"+titulo+"</th></tr><tr>")
        for campo in lis[0]:
            report.write("<th scope=\"col\">"+campo+"</th>")
        report.write("""                            </tr>
                                </thead>
                                <tbody class="letra">
                                """)
        for i in range(1,len(lis)):
            report.write("<tr>")
            for j in range(len(lis[i])):  
                report.write("<td>"+lis[i][j]+"</td>")
            report.write("</tr>")
        report.write(""" </center></tbody>
                                </table></div>""")
```
  
###  Salir de la Aplicación
Para cerrar la aplicación, simplemente haz clic en la opción "Salir" en el menú "Archivo" o cierra la ventana principal.

```
# Función para salir de la aplicación
def salir():
    ventana.quit()
    
    [Texto alternativo]https://github.com/luisyoupi/LFP_Proyecto2_201801391/blob/main/expresionRegulal.png

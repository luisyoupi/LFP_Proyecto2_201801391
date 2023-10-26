# Nombre del Curso -Lenguajes formales de programacion
## Semestre/Vacaciones: Semestre

**Universidad San Carlos de Guatemala**  
**Programador:** Luis Fernando Gomez Rendon
**Carne:** 201801391 
**Correo:** Luisfer789b@gmail.com

---

# Manual de Usuario

## Introducción

Este manual de usuario proporciona información detallada sobre cómo utilizar la aplicación de análisis de código fuente desarrollada en Python con la librería Tkinter. Esta aplicación tiene como objetivo identificar un lenguaje específico a partir de un archivo JSON, analizar el código, ejecutar las instrucciones y generar informes visuales de la jerarquía de operaciones. Además, se puede registrar y consultar errores en un formato JSON.

## Requisitos del Sistema

- Python 3.x instalado en su sistema.
- La librería Tkinter incluida en su instalación de Python.
- La librería Graphviz para generar diagramas.

## Instalación y Ejecución

1. Descargue el archivo ejecutable o los archivos de código fuente de la aplicación desde [enlace de descarga].
2. Instale la librería Graphviz siguiendo las instrucciones de su sitio web oficial: [enlace de instalación de Graphviz].
3. Ejecute la aplicación utilizando el siguiente comando en la terminal o símbolo del sistema:

       4.pip install graphiz 

## Interfaz de Usuario

Ventana Principal
Título de la Ventana: La ventana principal se titula "Analizador Bizdata" y tiene un fondo verde.
Barra de Herramientas
La barra de herramientas en la parte superior de la ventana proporciona opciones de interacción con la aplicación.

Abrir Archivo: Permite seleccionar y cargar un archivo .bizdata para su análisis.
Área de Edición de Código
Cuadro de Texto de Código: En el área de edición de código, puedes escribir o cargar el código fuente que deseas analizar. Este cuadro es editable y admite la escritura y edición de código.
Área de Consola
Cuadro de Texto de Resultados: En esta área, se muestran los resultados del análisis, incluyendo los tokens generados y los errores encontrados. La consola proporciona información detallada sobre el proceso de análisis.
Menú
El menú en la parte superior izquierda de la ventana ofrece varias opciones:

Archivo: Contiene opciones para cargar archivos y salir de la aplicación.

Abrir: Permite seleccionar un archivo .bizdata para cargar.
Exit: Cierra la aplicación.
Analizar Archivo: Ofrece la opción para iniciar el proceso de análisis del código fuente cargado.

Reportes: Proporciona opciones para generar informes relacionados con el análisis:

Reporte de Tokens: Genera un informe que muestra los tokens encontrados en el código.
Reporte de Errores: Genera un informe que lista los errores léxicos y sintácticos detectados.
Árbol de Derivación: Genera un informe que muestra el árbol de derivación del análisis sintáctico

...

_Puedes continuar con el contenido técnico en Markdown relacionado con el proyecto._



### Cargar y Analizar un Archivo bizdata
Puedes cargar y analizar un archivo .bizdata siguiendo estos pasos:

Abre la aplicación "Analizador Bizdata".
Selecciona "Archivo" > "Abrir" en el menú.
Se abrirá una ventana de diálogo que te permitirá navegar a la ubicación del archivo que deseas cargar.
Selecciona el archivo .bizdata que deseas analizar y haz clic en "Abrir".
El contenido del archivo se cargará en el área de edición de código.
Puedes revisar o editar el código según sea necesario.
Cuando estés listo para realizar el análisis, selecciona "Analizar Archivo" en el menú.
Los resultados del análisis, incluyendo los tokens y errores, se mostrarán en el cuadro de texto de resultados y en la consola.





#### Guardar y Exportar Resultados

Guardar: Puedes guardar los resultados en el archivo JSON cargado utilizando el botón "Guardar". Esto sobrescribirá el archivo existente.

Guardar como: Si deseas guardar los resultados en un nuevo archivo JSON, utiliza el botón "Guardar como". Esto te permitirá elegir una ubicación y un nombre para el nuevo archivo.

 
### Informe de Errores
La aplicación generará un informe de errores en el cuadro de texto de informe. En este informe, se detallarán los errores encontrados durante el análisis del archivo bizdata, incluyendo el tipo de error y una descripción.



#### Reporte
Puedes generar informes detallados sobre el análisis del código:

Reporte de Tokens: Muestra los tokens encontrados en el código fuente.
Reporte de Errores: Muestra los errores léxicos y sintácticos encontrados en el código.
Árbol de Derivación: Proporciona una representación gráfica del árbol de derivación del análisis sintáctico.
Estos informes te ayudarán a entender el resultado del análisis y a identificar posibles problemas en el código.
  
###  Salir de la Aplicación
Para cerrar la aplicación, simplemente haz clic en la opción "Salir" en el menú "Archivo" o cierra la ventana principal.

###  Anexos

![Texto alternativo](https://github.com/luisyoupi/LFP_Proyecto2_201801391/blob/main/ImagenA.png)

![Texto alternativo](https://github.com/luisyoupi/LFP_Proyecto2_201801391/blob/main/ImagenB.png)

![Texto alternativo](https://github.com/luisyoupi/LFP_Proyecto2_201801391/blob/main/ImagenC.png)

![Texto alternativo](https://github.com/luisyoupi/LFP_Proyecto2_201801391/blob/main/ImagenD.png)

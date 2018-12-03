# Decide-Ío-Censo 
## Grupo 2
## ID de Opera: 13

## Miembros del grupo y esfuerzo realizado:

* **Cebrero Rodriguez, Pablo:** Introducir puntuacion
* **Galán Montero, José Juan:**
* **González García, Iván:**
* **Luque Muñoz, Miguel:**


## Enlaces de interés:

* [**repositorio de código**](#codigo)
* [**sistema desplegado**](#bugs)
* [**otros enlaces**](#bugs)
* [**otros enlaces**](#bugs)

### Resumen

### Introducción y contexto

### Descripción del sistema
* Creación de varios censos simultáneamente (la votación se indica una sola vez)
* Agrupación de censos por votación
* Selección de votantes por DNI y nombre al crear
* Reutilización de censo
* Exportación de censo
* Importación de censo desde Excel
* Filtrado por edad/sexo/otros (Coordinación con Autenticación)

### Planificación del proyecto

### Entorno de desarrollo

#### Instalación Python 3.6.4
* Instalar Python (en la carpeta c:\Python36):
  https://www.python.org/download
En Windows, ir a Equipo (botón derecho) > Propiedades > Configuración avanzada del
sistema > Variables de entorno… > En Variables del sistema Editar la variable Path
(añadir : C:\Python36;C:\Python36\Scripts) 

#### Instalación de Django

* Acceder a cmd e introducir: pip install Django 

#### Instalación Eclipse Oxygen http://www.eclipse.org
#### Instalación Pydev en eclipse
**Importante: PyDev requiere Java 8 y Eclipse 4.6 (Neon) o
superior(Oxygen) para soportar Python 2.6 o superior.**
* Otras versiones:
    * Eclipse 4.5, Java 8: PyDev 5.2.0
    * Eclipse 3.8, Java 7: PyDev 4.5.5
    * Eclipse 3.x, Java 6: PyDev 2.8.2
* Seguir las instrucciones recogidas en:
http://www.pydev.org/manual_101_install.html

#### Comprobando la instalación
Ir a 'window > preferences' y comprobar si hay una opción PyDev.
Configurar el intérprete de Python
1. Ir a window > preferences > PyDev > Interpreter - Python
2. Elegir el intérprete que hemos instalado, para ello basta pulsar Auto Config
El Auto Config intentará encontrarlo (python.exe) en PATH, pero puede fallar.
3. El System libs debe contener al menos los directorios Lib y Lib/site-packages.
4. Pulsar Aceptar.

Información obtenida de http://www.lsi.us.es/docencia/get.php?id=9175

#### Instalando decide
En el siguiente enlace tenemos un breve tutorial de como empezar:
https://1984.lsi.us.es/wiki-egc/images/egc/2/22/02-Decide-Install.pdf

## Gestión del cambio, incidencias y depuración

Durante el desarrollo normal del proyecto se comunicará cualquier incidencia interna mediante GitHub, utilizando las etiquetas que más se adecúen al caso. Posteriormente, el desarrollador que haya realizado el último commit sobre la funcionalidad que ha provocado la incidencia deberá encargarse de la misma, bien resolviéndola o delegando su resolución. La persona al cargo de resolver la incidencia, ya sea sobre código o sobre documentación, deberá hacer un branch cuando considere necesario (según prioridad) en el que trabajará. Finalmente, combinará su trabajo con la rama principal.

En cuanto a las incidencias reportadas a otros subsistemas, se seguirá la plantilla encontrada en el repositorio del subsistema en cuestión, de la misma forma que se espera que las incidencias externas se reporten siguiendo la plantilla indicada en el documento "Guía de Incidencias".

### Gestión del código fuente

Se realiza un fork propio del grupo encargado del subsistema, a partir de ahí el grupo trabajará sobre ese fork.
Para la gestión del código se usará github desktop. Antes de comenzar a trabajar se hará un pull del repositorio para disponer de él en local. Cuando algún integrante quiera llevar a cabo algún cambio, primero deberá asegurarse de hacer pull. Si no existe ningún conflicto, podrá hacer commit de los cambios realizados y push. En caso contrario, deberá dirigirse al historial de cambios y buscar al responsable del código que genera el conflicto. A este se le comunicará la naturaleza del conflicto y una propuesta de posible solución ya sea por su parte o de forma conjunta. La resolución del conflicto debe satisfacer a ambas partes pudiendo intervenir el coordinador si fuese necesario.
Ejemplos:
Se ha modificado un archivo mostrando en rojo las lineas antiguas y en verde el resultado tras la modificación.

https://github.com/DECIDEIO-CENSO/decideio-censo/commit/0580fb334d8d7aef44d00e7b449e73e6da3e7e88#diff-c7dc8742947f13f1ddc89ee1ebf164f1

### Gestión de la construcción e integración continua

### Gestión de liberaciones, despliegue y entregas

### Mapa de herramientas

### Ejercicio de propuesta de cambio

### Conclusiones y trabajo futuro

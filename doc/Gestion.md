# Decide-Io-Censo 
## Grupo 2
## ID de Opera: 13

## Miembros del grupo y esfuerzo realizado:

* **Cebrero Rodriguez, Pablo:** Introducir puntuacion
* **Galán Montero, José Juan:**
* **González García, Iván:**
* **Luque Muñoz, Miguel:**

Guia y plantillas necesarias para la creación de incidencias del grupo Decide-Io en el modulo de Censo.

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
* Exportación
* Importación
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

### Gestión del código fuente
Se realiza un fork propio del grupo encargado del subsistema, a partir de ahí el grupo trabajará sobre ese fork
Antes de comenzar a trabajar se hará un pull del repositorio para disponer de él en local. Cuando algún integrante quiera llevar a cabo algún cambio, primero deberá asegurarse de hacer pull. Si no existe ningún conflicto, podrá hacer commit de los cambios realizados y push. En caso contrario, deberá dirigirse al historial de cambios y buscar al responsable del código que genera el conflicto. A este se le comunicará la naturaleza del conflicto y una propuesta de posible solución ya sea por su parte o de forma conjunta. La resolución del conflicto debe satisfacer a ambas partes pudiendo intervenir el coordinador si fuese necesario.

### Gestión de la construcción e integración continua

### Gestión de liberaciones, despliegue y entregas

### Mapa de herramientas

### Ejercicio de propuesta de cambio

### Conclusiones y trabajo futuro

# Decide-Ío-Censo 
## Grupo 2
## ID de Opera: 13

## Miembros del grupo y esfuerzo realizado:

* **Cebrero Rodriguez, Pablo:** 5
* **Galán Montero, José Juan:** 5
* **González García, Iván:** 5
* **Luque Muñoz, Miguel:** 5


## Enlaces de interés:

* [**Repositorio de código**](https://github.com/DECIDEIO-CENSO/decideio-censo/tree/master/decide)
* [**Sistema desplegado**](https://decide-io-censo.herokuapp.com/census/home)
* [**Información del proyecto**](#información-del-proyecto)
  * [**Resumen**](#resumen)
  * [**Introducción y contexto**](#introducción-y-contexto)
  * [**Descripción del sistema**](#descripción-del-sistema)
  * [**Planificación del proyecto**](#planificación-del-proyecto)
  * [**Entorno de desarrollo**](#entorno-de-desarrollo)
  * [**Gestión del cambio, incidencias y depuración**](#gestión-del-cambio-incidencias-y-depuración)
  * [**Gestión del código fuente**](#gestión-del-código-fuente)
  * [**Gestión de la construcción e integración continua**](#gestión-de-la-construcción-e-integración-continua)
  * [**Gestión de liberaciones, despliegue y entregas**](#gestión-de-liberaciones-despliegue-y-entregas)
  * [**Mapa de herramientas**](#mapa-de-herramientas)
  * [**Ejercicio de propuesta de cambio**](#ejercicio-de-propuesta-de-cambio)
  * [**Conclusiones y trabajo futuro**](#conclusiones-y-trabajo-futuro)

### Resumen
El sistema decide es una plataforma de voto electrónico que consta de varios subsistemas, en nuestro caso el subsistema elegido ha sido el de censo, y debido a que vemos importante mejorar varios campos de este subsistema se han propuesto 6 cambios o mejoras en él.

### Introducción y contexto
El proyecto consiste en una plataforma educativa de voto electrónico que, por lo tanto, requiere de simplicidad y debe ofrecer diferentes garantías como voto electrónico seguro, la anonimicidad y el voto seguro. Además, este sistema consta de varios subsistemas como:
 * Autenticación
 * Censo
 * Votaciones
 * Cabina de votación
 * Almacenamiento de votos (cifrados)
 * Recuento / MixNet
 * Post-procesado
 * Visualización de resultados
 
 En nuestro caso, hemos elegido el subsistema **Censo**, que consiste en almacenar y asociar a que votaciones tienen acceso cada uno de los usuarios del sistema, es decir, un votante que se registre no tiene por qué tener acceso a todas las votaciones.
 
### Descripción del sistema

La descripción del sistema se corresponde con la descrita en el proyecto de **decide**, la cual puede consultarse en los siguientes enlaces:
* **Descripción y configuración del sistema** : https://github.com/DecideIO/decide-io/blob/master/README.md
* **Descripción de los diferentes subsistemas** : https://github.com/DecideIO/decide-io/blob/master/doc/subsistemas.md

A continuación se enumeran los cambios propuestos que se llevarán a cabo para estre proyecto:

* Creación de varios censos simultáneamente (la votación se indica una sola vez)
* Agrupación de censos por votación
* Creación de las vistas para facilitar el uso de todas las funcionalidades.
* Reutilización de censo
* Exportación de censo
* Importación de censo desde Excel


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

Durante el desarrollo normal del proyecto se comunicará cualquier incidencia interna mediante GitHub, utilizando las etiquetas que más se adecúen al caso. Posteriormente, el desarrollador que haya realizado el último commit sobre la funcionalidad que ha provocado la incidencia deberá encargarse de la misma, bien resolviéndola o delegando su resolución. Si la incidencia no tiene un error como origen, será el coordinador el encargado de asignar a alguien a la misma. (Ej.: https://github.com/DECIDEIO-CENSO/decideio-censo/issues/8)
La persona al cargo de resolver la incidencia, ya sea sobre código o sobre documentación, deberá hacer un branch cuando considere necesario (según prioridad) en el que trabajará. Finalmente, combinará su trabajo con la rama principal. (Ej.: https://github.com/DECIDEIO-CENSO/decideio-censo/tree/frontend)

En cuanto a las incidencias reportadas a otros subsistemas, se seguirá la plantilla encontrada en el repositorio del subsistema en cuestión, de la misma forma que se espera que las incidencias externas se reporten siguiendo la plantilla indicada en el documento "Guía de Incidencias". (Ej.: https://github.com/DECIDEIO-CENSO/decideio-censo/issues/9)


### Gestión de commit

Debe realizarse commit cada vez que se consiga un pequeño incremento modular de funcionalidad, para tener una mejor traza de los cambios sufridos.

Los commits deberán tener el siguiente formato:
```
(Tipo del commit) Added/Updated/Fixed [nombre del archivo]
(LÍNEA EN BLANCO)
Descripción más detallada de los cambios y modo de visualización, si procede
(LÍNEA EN BLANCO)
#ISSUE1234 (Código de incidencia, si procede)
```

El tipo del commit será uno de entre:
* **Feature**: Corresponde a una nueva feature del sistema.
* **Bug**: Corresponde a un arreglo de algún bug.
* **Docs**: Corresponde a creación y gestión de documentación.
* **Refactor**: Corresponde a cambios en el formato del código.
* **Tests**: Corresponde a nuevos tests o cambios en ellos.
* **Otros**: Corresponde a pequeños arreglos ajenos al código o el propio sistema.

(Ej.: https://github.com/DECIDEIO-CENSO/decideio-censo/commit/f2ff9845708f4afbd30d8cec53ef429c8de4e3cf)


### Gestión del código fuente

Se realiza un fork propio del grupo encargado del subsistema, a partir de ahí el grupo trabajará sobre ese fork.
Para la gestión del código se usará github desktop. Antes de comenzar a trabajar se hará un pull del repositorio para disponer de él en local. Cuando algún integrante quiera llevar a cabo algún cambio, primero deberá asegurarse de hacer pull. Si no existe ningún conflicto, podrá hacer commit de los cambios realizados y push. En caso contrario, deberá dirigirse al historial de cambios y buscar al responsable del código que genera el conflicto. A este se le comunicará la naturaleza del conflicto y una propuesta de posible solución ya sea por su parte o de forma conjunta. La resolución del conflicto debe satisfacer a ambas partes pudiendo intervenir el coordinador si fuese necesario.
Ejemplos:
Se ha modificado un archivo mostrando en rojo las lineas antiguas y en verde el resultado tras la modificación.

https://github.com/DECIDEIO-CENSO/decideio-censo/commit/0580fb334d8d7aef44d00e7b449e73e6da3e7e88#diff-c7dc8742947f13f1ddc89ee1ebf164f1


### Gestión de la construcción e integración continua

Para la integración continua y la realización de los test de forma automática usaremos la herramienta Travis CI que se añadirá al proyecto tal y como se vio durante la sesión de prácticas. 

Cada vez que un usuario realice un commit, Travis comprobara que el funcionamiento del proyecto es el correcto y producirá un log con los posibles errores que hubiese encontrado en la aplicación.

Para acceder a ese log de Travis basta con entrar con nuestra cuenta de GitHub en la página web de [Travis](https://travis-ci.org/) o desde la propia página de GitHub podemos comprobar si los test han sido superados con éxitos o no pulsando en el siguiente [enlace](https://github.com/DECIDEIO-CENSO/decideio-censo/commits/master). Si los test no se hubiesen pasado satisfactoriamente encontraríamos una X roja al lado de nuestro commit.


### Gestión de liberaciones, despliegue y entregas

Para poder desplegar, utilizaremos Heroku, mediante la guía proporcionada por la asignatura de EGC(Evolución y Gestión de la Configuración).

Guía paso a paso: https://1984.lsi.us.es/wiki-egc/index.php/Despliegue_(Heroku).

Una vez integrado Heroku con nuestra rama "master" lo configuramos para que se integre con Travis, de forma que no proceda al despliegue si la rama no pasa los tests automáticos.

Teniendo en cuenta esto, el modo de proceder es trabajar en una rama de desarollo proveniente de master, la cual tiene integrada Travis.
De esta forma tan solo se hace *"Push"* a la rama "master" cuando todo está testeado y en un estado en el que no existan errores manteniendo esta en una versión estable que permita su despliegue en Heroku.


### Mapa de herramientas

IDE: Eclipse Oxygen

Control de versiones: Git

Repositorio: Github

Control de repositorio: Github desktop

Integración continua: Travis CI

Despliegue: Docker

Despliegue: Heroku


### Ejercicio de propuesta de cambio

Para la realización de una propuesta de cambio lo primero es organizar una reunión del grupo en la cual se acordarán qué cambios se van a llevar a cabo. Una vez definidos estos cambios, y quien los va a implementar, el coordinador creará las issues siguiendo la plantilla [Feature](https://github.com/DECIDEIO-CENSO/decideio-censo/issues/new?template=propuesta-de-feature.md)
 y las asignará al miembro del grupo acordado, el cual será ahora responsable de la issue.

Una vez que tenga la issue asignada uno de los miembros, este deberá ir a la [Guía de incidencias](https://github.com/DECIDEIO-CENSO/decideio-censo/blob/master/doc/Guia_incidencias.md) y seguir los pasos allí descritos. Posteriormente deberá, desde la consola de comandos de Git, hacer los siguientes pasos:

-checkout master

-git pull

-git branch nombre_nueva_rama (Si el miembro del grupo considera que no es necesario podrá no hacerlo)

Después de realizar esos comandos, deberá implementar la nueva funcionalidad descrita en la issue y una vez acabada volvera a usar la consola de comandos de Git para realizar los siguientes pasos:

-git status (Para ver los ficheros modificados)

-git add ficheros_modificados

-git commit (Siguiendo las indicaciones [**Gestión de commit**](#gestión-de-commit))

-git pull

-git push

Una vez terminado con la consola deberá hacer merge de su rama con la rama Dev y comprobar que los test que se pasan en [Travis CI](https://travis-ci.org/) se completan correctamente.

Si todo ha ido bien ya solo le quedara cerrar su issue siguiendo una vez más la [Guía de incidencias](https://github.com/DECIDEIO-CENSO/decideio-censo/blob/master/doc/Guia_incidencias.md) y hacer merge de la rama Dev con la rama Master.

Nota: La creación de la rama es opcional y depende del criterio del miembro encargado, si considera que los cambios no son suficientemente grandes como para crear una rama nueva deberá trabajar sobre la rama Dev y nunca sobre Master.



### Conclusiones y trabajo futuro

#### Conclusiones

El objetivo de este proyecto era implementar cambios en Decide y aprender el uso de diversas herramientas que nos permiten trabajar en grupo y realizar una gestión e integración continua del software.

Al comenzar el proyecto no fue fácil habituarnos al uso de estas herramientas, puesto que para todos los miembros del grupo eran algo nuevo. Aunque al final, pudimos establecer un plan de trabajo con el que hemos conseguido implementar los cambios en el proyecto haciendo un uso correcto de todas las herramientas.

#### Trabajo futuro

Las propuestas de trabajo futuro para mejorar el censo son las siguientes:

-Actualmente se pueden crear censos que con id de users que no existen y con id de votings que no existen y lo correcto sería que se comprobase antes de crearse un censo.

-Los censos se crean actualmente con los id de los votings y los id de los voters y es algo lioso para una persona puesto que son solo números, por lo tanto, estaría bien que al crearse se viese el nombre del voting y el nombre o el dni de los voters.

# Informe trabajo parcial

## Descripción y Fundamentación del Problema   

Según Freire & Ocaña (2021), el problema que abordaremos en este proyecto se centra en la creación y optimización de una red social que conecte a usuarios. La necesidad de resolver este problema radica en la creciente importancia de las redes sociales en la sociedad actual. Conectar a usuarios de manera eficiente y ofrecer una experiencia satisfactoria es fundamental para el éxito de una plataforma de este tipo.

La fundamentación de este problema se basa en la relevancia de las redes sociales en la actualidad. Estas plataformas no solo son herramientas de comunicación, sino también espacios de interacción, difusión de información y generación de comunidades en línea. Una red social efectiva puede influir en la opinión pública, facilitar la colaboración y proporcionar oportunidades comerciales.

## Descripción y Visualización de Datos

### Descripción de los datos

Para la realización de este proyecto, se ha desarrollado una base de datos que consta de dos tablas: `users` y `user_followers`.

En la tabla `users`, se almacenan los detalles de los usuarios, que en el contexto de nuestro proyecto, representan los nodos del grafo con el cuál trabajaremos.

Estos datos incluyen aquella información selecciondada para satisfacer las necesidades de nuestra red social. Los campos incluyen:

- `username`: Nombre de usuario
- `email`: Correo electrónico
- `password`: Contraseña
- `first_name`: Nombre
- `last_name`: Apellido
- `date_of_birth`: Fecha de nacimiento
- `country`: País de residencia
- `phone_number`: Número de teléfono
- `joined_date`: Fecha de registro

Por otro lado, la tabla `user_followers` almacena las relaciones entre los usuarios, es decir, a quiénes siguen los usuarios. En el contexto del proyecto, esta tabla almacena las aristas o conexiones entre los nodos.

### Origen de los datos
Para generar estos datos, se han implementado dos scripts en Python que se encuentran en los archivos [user_generation.py](https://github.com/202210494/complejidad-algoritmica-grupo-05/blob/main/Base%20de%20datos/user_generation.py) y [followers_generation.py](https://github.com/202210494/complejidad-algoritmica-grupo-05/blob/main/Base%20de%20datos/followers_generation.py).

`user_generation.py`

> Este archivo emplea la biblioteca [Faker](https://github.com/joke2k/faker) para generar datos ficticios de **1500** posibles usuarios y los incorpora en la base de datos.

`followers_generation.py`

> Este archivo procesa cada usuario en la tabla `users`, utilizando la biblioteca `random` de Python para determinar aleatoriamente a cuántos usuarios seguirá el usuario en cuestión, y luego añade esas relaciones a la base de datos en la tabla correspondiente.
>
> Es importante destacar que resulta complicado determinar la cantidad exacta de aristas que contendrá nuestro conjunto de datos debido a su naturaleza aleatoria. Sin embargo, se estima que habrá aproximadamente alrededor de **37500** aristas o, en el contexto de nuestro proyecto, conexiones entre usuarios.

### Visualización de los datos

Para llevar a cabo la visualización de los datos, se ha desarrollado el script [visualizacion_datos.py](../Base%20de%20datos/visualizacion_datos.py), el cual hace uso de la biblioteca [pyvis](https://github.com/WestHealth/pyvis).<br>
Esta biblioteca nos ha proporcionado las herramientas necesarias para generar una visualización del grafo con el que trabajaremos.

Para realizar esta visualización no se emplearon todos los datos disponibles, sino simplemente una muestra representativa que consta de `200` nodos y `1604` aristas.<br>
La razón detrás de esta decisión radica en la imposibilidad de visualizar la totalidad de los datos debido a su volumen.

A continuación, se muestra la representación gráfica del grafo generado a partir de esta muestra.<br>
En este contexto, cada nodo representa a un usuario, y cada arista simboliza una conexión del tipo "sigue a":


![Grafo 200 nodos, ~1500 aristass](../Base%20de%20datos/Visualizacion/grafo_200_15.png)


## Nuestra propuesta

### Objetivos

Nosotros hemos propuesto nuestros objetivos en base a la metodología de objetivos smart:

Nuestro objetivo principal es crear una red social con funcionalidades básicas (creación de un perfil, seguir perfiles y buscar perfiles) durante las
siguientes 8 semanas con sprints intermedios. Nuestro proyecto debe implementarse en base a algoritmos eficientes capaces de soportar grandes cantidades de datos. 


### Tecnica y Metodología

La metodología utilizada en este proyecto se basa en la metodología ágil. Hemos dividido el proyecto en sprints, lo cuales nos permiten una mejor organización en cuestión a los objetivos.

Las partes que componen cada sprint son:

> Objetivos de sprints (Inicio)<br>
> Seguimiento diario (Desarrollo)<br>
> Revision de cumplimiento (Cierre)

## Fuentes
Freire, T., & Ocaña, P. (2021). Impacto de la gestión de redes sociales en las empresas gastrononómicas.
https://preprints.scielo.org/index.php/scielo/preprint/download/2556/4414/4583


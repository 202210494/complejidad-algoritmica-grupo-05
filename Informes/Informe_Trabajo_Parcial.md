# Informe trabajo parcial

## Descripción y Fundamentación del Problema   

Según Freire & Ocaña (2021), la sobrecarga de algoritmos en las redes sociales, especialmente en las funciones de seguimiento, búsqueda y agregación, plantea un problema sustancial al inundar a los usuarios con recomendaciones y contenido poco relevantes, notificaciones intrusivas y una experiencia general de usuario abrumadora. Esta deficiencia algorítmica impacta negativamente la navegación, la privacidad y la satisfacción de los usuarios, subrayando la necesidad de desarrollar algoritmos más precisos y equilibrados que personalicen la experiencia de manera efectiva mientras se abordan las preocupaciones éticas y de privacidad para mejorar la calidad de las redes sociales en línea. Además, esta sobrecarga algorítmica también puede tener implicaciones más amplias en la sociedad, ya que influye en la forma en que las personas interactúan, consumen información y toman decisiones en un mundo cada vez más digitalizado. La calidad de los algoritmos en las redes sociales no solo afecta la satisfacción individual del usuario, sino que también puede influir en la polarización política, la difusión de información errónea y la formación de burbujas de filtro, lo que subraya aún más la importancia de abordar este problema de manera efectiva para mantener una comunidad en línea saludable y equilibrada.

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

Nuestro objetivo como grupo es aplicar algoritmos de busqueda para la elaboracion de una red social con funcionalidades basicas. Asimismo, buscamos optmizar procesos y algoritmos para una mejor eficienica y experiencia en los usuarios.

### Tecnica y Metodologia

La metologia utilizada en este proyecto se basa en la metologia ágil. Hemos divido el proyecto en sprints, lo cuales nos permiten una mejor organicazion en cuestion a los objetivos.

Las partes que componen cada sprint son:

> Objetivos de sprints (Inicio)<br>
> Seguimiento diario (Desarrollo)<br>
> Revision de cumplimiento (Cierre)

## Fuentes
Freire, T., & Ocaña, P. (2021). Impacto de la gestión de redes sociales en las empresas gastrononómicas.
https://preprints.scielo.org/index.php/scielo/preprint/download/2556/4414/4583


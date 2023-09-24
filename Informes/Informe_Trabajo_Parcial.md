1. Redactar la descripción y fundamentación del problema citando fuentes.
2. Descripción y visualización de datos:
   1. Redactar las caracteristicas y el origen de los datos motivo de análisis.
   2. Mencionar el número de nodos identificados.
   3. Mostrar mediante un grafo los datos recolectados.
3. Propuesta:
   1. Redactar de forma preliminar el objetivo, técnica y metodologia a realizar.

# Informe trabajo parcial

## Descripción y Fundamentación del Problema

## Descripción y Visualización de Datos

### Descripción de los datos

Para la realización de este proyecto, se ha desarrollado una base de datos que consta de dos tablas: `users` y `user_followers`.

En la tabla `users`, se almacenan los detalles de los usuarios, que en el contexto de nuestro proyecto, representan los nodos del grafo con el cuál trabajaremos.

Estos datos incluyen aquella información selecciondada para satisfacer las necesidades de nuestra red social. Los campos incluyen:

- Nombre de usuario (`username`)
- Correo electrónico (`email`)
- Contraseña (`password`)
- Nombre (`first_name`)
- Apellido (`last_name`)
- Fecha de nacimiento (`date_of_birth`)
- País de residencia (`country`)
- Número de teléfono (`phone_number`)
- Fecha de registro (`joined_date`)

Por otro lado, la tabla `user_followers` almacena las relaciones entre los usuarios, es decir, a quiénes siguen los usuarios. En el contexto del proyecto, esta tabla almacena las aristas o conexiones entre los nodos.

### Origen de los datos
Para generar estos datos, se han implementado dos scripts en Python que se encuentran en los archivos [user_generation.py](https://github.com/202210494/complejidad-algoritmica-grupo-05/blob/main/Base%20de%20datos/user_generation.py) y [followers_generation.py](https://github.com/202210494/complejidad-algoritmica-grupo-05/blob/main/Base%20de%20datos/followers_generation.py).

> `user_generation.py`
>
> Este archivo emplea la biblioteca [Faker](https://github.com/joke2k/faker) para generar datos ficticios de **1500** posibles usuarios y los incorpora en la base de datos.

> `followers_generation.py`
>
> Este archivo procesa cada usuario en la tabla `users`, utilizando la biblioteca `random` de Python para determinar aleatoriamente a cuántos usuarios seguirá el usuario en cuestión, y luego añade esas relaciones a la base de datos en la tabla correspondiente.
>
> Es importante destacar que resulta complicado determinar la cantidad exacta de aristas que contendrá nuestro conjunto de datos debido a su naturaleza aleatoria. Sin embargo, se estima que habrá aproximadamente alrededor de **37500** conexiones entre usuarios o, en el contexto de nuestro proyecto, aristas.


## Nuestra propuesta

## Fuentes
# La Bayeta de la Fortuna

La Bayeta de la Fortuna es una aplicación web sencilla desarrollada en Python que, cada vez que se accede a ella, devuelve una o varias frases auspiciosas de manera aleatoria. A lo largo del proyecto se ha evolucionado desde un simple script de consola hasta una aplicación web completa, desplegada en contenedores y con persistencia de datos mediante MongoDB y Docker Compose.

## Descripción del proyecto

El objetivo del proyecto es construir una aplicación reproducible, versionada y desplegable de forma consistente tanto en entorno local como en un entorno similar a producción. Para ello se han utilizado las siguientes tecnologías:

- Python y entorno virtual (venv) para aislar dependencias.
- Flask para exponer una API web.
- MongoDB como base de datos para almacenar las frases.
- Docker para contenerizar la aplicación.
- Docker Compose para orquestar la aplicación y la base de datos.
- Git y GitHub para el control de versiones y publicación de versiones.

## Estructura principal del proyecto

- **app.py**: aplicación Flask que define los endpoints.
- **bayeta.py**: lógica de negocio de la aplicación.
- **mongo_frases.py**: módulo encargado de interactuar con MongoDB.
- **frases.txt**: fichero inicial con frases auspiciosas.
- **Dockerfile**: definición de la imagen de la aplicación.
- **compose.yml**: orquestación de la aplicación y MongoDB.
- **requirements.txt**: dependencias Python necesarias.

## Requisitos

Para ejecutar la aplicación se necesita:

- Docker
- Docker Compose
- Git (si se va a clonar el repositorio)

No es necesario tener MongoDB ni Python instalados en el sistema si se utiliza Docker Compose.

## Clonado del proyecto

Clonar el repositorio desde GitHub:

```bash
git clone git@github.com:RyoCAS44/pps_python_git_docker.git
cd pps_python_git_docker
```

## Ejecución con Docker Compose

Desde la raíz del proyecto, donde se encuentra el fichero `compose.yml`, ejecutar:

```bash
sudo docker-compose up --build
```

Este comando:

- Construye la imagen de la aplicación.
- Descarga la imagen oficial de MongoDB.
- Crea la red interna entre contenedores.
- Crea un volumen para la persistencia de datos de MongoDB.
- Arranca ambos servicios.

La aplicación estará disponible en:

```
http://localhost:5000
```

## Endpoints disponibles

### GET /

Devuelve un mensaje básico de comprobación.

### GET /frotar/<n>

Devuelve `n` frases auspiciosas en formato JSON. Las frases se seleccionan de forma aleatoria desde MongoDB.

**Ejemplo:**
```
http://localhost:5000/frotar/3
```

### POST /frotar/add

Permite añadir nuevas frases auspiciosas a la base de datos.

Recibe un JSON con la siguiente estructura:

```json
{
  "frases": [
    "La suerte favorece a quien se mueve",
    "El conocimiento es poder"
  ]
}
```

**Ejemplo usando curl:**

```bash
curl -X POST http://127.0.0.1:5000/frotar/add \
  -H "Content-Type: application/json" \
  -d '{"frases":["Nueva frase 1","Nueva frase 2"]}'
```

Si la operación es correcta, devuelve código 200 y un mensaje de confirmación.

## Persistencia de datos

MongoDB almacena los datos en la ruta interna `/data/db`. En el fichero `compose.yml` se define un volumen Docker que se monta sobre esa ruta, garantizando que los datos no se pierdan aunque los contenedores se detengan o se eliminen.

Para comprobar los volúmenes creados:

```bash
sudo docker volume ls
```

## Parar la aplicación

Para detener los servicios:

```
Ctrl + C
```

O bien:

```bash
sudo docker-compose down
```

## Ejecución sin Docker (modo desarrollo)

Opcionalmente, se puede ejecutar en local utilizando un entorno virtual de Python:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

En este caso, MongoDB debe estar accesible y configurado correctamente.

## Control de versiones

El proyecto se ha desarrollado utilizando ramas para cada nueva funcionalidad (entorno virtual, integración con MongoDB, Docker, Docker Compose, inserción de frases, etc.), fusionando posteriormente cada rama en `main` y publicando versiones mediante GitHub Releases.

## Conclusión

La Bayeta de la Fortuna ha evolucionado desde un simple script que imprimía "Hola, mundo" hasta una aplicación web completa con arquitectura modular, base de datos persistente y despliegue reproducible mediante contenedores. El uso de Docker y Docker Compose garantiza que el entorno de ejecución sea consistente y estable, independientemente de la máquina donde se despliegue.

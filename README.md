# La Bayeta de la Fortuna 🧽✨

La Bayeta de la Fortuna es una aplicación web sencilla inspirada en las clásicas
galletas de la fortuna y en las frases filosóficas que uno puede encontrar
escritas en una servilleta de bar.

Cada vez que el usuario accede a la aplicación, se mostrará un mensaje
aleatorio de carácter irónico, motivacional o absurdo.

## Objetivo del proyecto

Este proyecto se utiliza como ejercicio práctico para aprender a:

- Controlar versiones del código con Git
- Trabajar de forma colaborativa usando GitHub
- Gestionar dependencias con Python y entornos virtuales (venv)
- Garantizar la portabilidad y reproducibilidad del entorno mediante Docker

## Tecnologías utilizadas

- Python
- Git
- Docker

El proyecto irá evolucionando progresivamente, publicando distintas versiones
conforme se añadan nuevas funcionalidades.

## Ejecución de la aplicación

Para garantizar que la aplicación se ejecuta de forma aislada e independiente del sistema, se utiliza un entorno virtual de Python (`venv`).

### Requisitos
- Python 3 instalado en el sistema
- Git

### Pasos de instalación y ejecución

1. Clonar el repositorio:
	git clone git@github.com:RyoCAS44/pps_python_git_docker.git
	cd pps_python_git_docker

2. Crear el entorno virtual:

	python3 -m venv venv


3. Activar el entorno virtual:

	source venv/bin/activate


4. Instalar las dependencias:

	pip install -r requirements.txt


5. Ejecutar la aplicación:

	python app.py

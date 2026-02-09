# La Bayeta de la Fortuna 🧽✨

La Bayeta de la Fortuna es una aplicación web sencilla inspirada en las clásicas
galletas de la fortuna y en las frases que uno podría encontrar escritas en una
servilleta de bar.

El objetivo del proyecto es simular un desarrollo colaborativo moderno,
utilizando Python, Git y Docker, garantizando un entorno de ejecución
reproducible y consistente entre desarrollo y producción.

---

## Funcionalidad

La aplicación permite:

- Acceder a una página principal que muestra el mensaje **“Hola, mundo”**
- Obtener frases auspiciosas mediante el endpoint `/frotar/<n_frases>`
- Devolver las frases en formato JSON
- Ejecutarse tanto en local como en un contenedor Docker

Las frases se seleccionan de forma aleatoria desde un fichero de texto.

---

## Ejecución en entorno local (Python + venv)

### Requisitos
- Python 3
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

##La aplicación estará disponible en:

	http://127.0.0.1:5000

	http://127.0.0.1:5000/frotar/3

##Ejecución mediante Docker (despliegue seguro)

La aplicación puede ejecutarse dentro de un contenedor Docker, garantizando que
el entorno de ejecución sea idéntico en cualquier sistema.

##Requisitos

Docker

Construcción de la imagen
	docker build -t bayeta-fortuna .

Ejecución del contenedor
	docker run -p 5000:5000 bayeta-fortuna


La aplicación estará disponible en:

	http://127.0.0.1:5000

	http://127.0.0.1:5000/frotar/3

##Estructura del proyecto
.
├── app.py           # Aplicación web Flask
├── bayeta.py        # Lógica de generación de frases
├── frases.txt       # Almacenamiento de frases
├── requirements.txt # Dependencias del proyecto
├── Dockerfile       # Imagen Docker multifase
├── .dockerignore    # Exclusión de ficheros innecesarios
└── README.md

### Crear un entorno virtual con version de python especifico.

    $ pipenv --python=3.10

### Crear o Activar entorno virtual y si no existe el entorno virtual lo crea con la version de python por defecto.

    $ pipenv shell

### Instalar modulos dentro del entorno virtual lo ejecutamos con el comando:  pipenv install modulo

    $ pipenv install flask


### exportar comando flask para poder usar db init, db migrate o db upgrade

- Windows

    $ SET FLASK_APP=src/app.py

- Mac or Linux

    $ export FLASK_APP=src/app.py
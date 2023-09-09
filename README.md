# python-pip
Curso de Python: PIP y Entornos Virtuales

que super tip se aventaron en esta clase:

# Python con Git y GitHub 5/20
https://platzi.com/clases/4261-python-pip/55125-python-con-git-y-github/

de haberlo sabido antes en html y css jajaja todo lo que me hubiera evitado teclear de extansiones de imagenes y video 😂


siempre que haga un cambio en VS Code al final hacer un push


# Flujo de trabajo en Python 6/20
https://platzi.com/clases/4261-python-pip/55126-flujo-de-trabajo-en-python/

# Game Proyect

```sh
cd game
python3(aquí puedes poner tab y se auto completa la version completa) main.py
```

## FOLLOW ME

# https://github.com/iecgerman/

```sh
ESTE TIPO DE TIPS SON LOS QUE SE USAN EN LOS COMENTARIOS DE PLATZI
```

# Usando entornos virtuales en Python 10/20
https://platzi.com/clases/4261-python-pip/55130-usando-entornos-virtuales-en-python/

Para saber donde está instalado Python:

german@iecgerman:~$ which python3
/usr/bin/python3

Para saber donde está instalado Pip:

german@iecgerman:~$ which pip3
/home/german/.local/bin/pip3


Si estás usando wsl o Linux (en mi caso Ubuntu) tienes que instalar:

A mi me funcionó con:

german@iecgerman:~$ sudo apt install -y python3.10-venv


Dentro de la carpeta de alguno de nuestros proyectos, en este caso empezaremos con la carpeta app que es la de las graficas de la población de los países, ahi vamos a crear su ambiente virtual aislado de los demás:

german@iecgerman:~/python-pip$ cd app
german@iecgerman:~/python-pip/app$ pwd
/home/german/python-pip/app
german@iecgerman:~/python-pip/app$ python3 -m venv env
german@iecgerman:~/python-pip/app$ ll
total 252
drwxr-xr-x 5 german german   4096 sep  4 18:09 ./
drwxrwxr-x 6 german german   4096 sep  4 02:00 ../
-rw-r--r-- 1 german german    466 sep  4 02:25 charts.py
-rw------- 1 german german  29247 sep  4 02:22 data.csv
drwxrwxr-x 5 german german   4096 sep  4 18:09 env/
drwxrwxr-x 2 german german   4096 sep  4 02:51 imagenes/
-rw-r--r-- 1 german german    800 sep  4 02:51 main.py
-rw-rw-r-- 1 german german 184908 sep  4 02:51 pie.png
drwxrwxr-x 2 german german   4096 sep  4 02:45 __pycache__/
-rw-r--r-- 1 german german    409 sep  4 02:08 read_csv.py
-rw-r--r-- 1 german german   1004 ago  5 03:04 utilidades.py
german@iecgerman:~/python-pip/app$ 

ahora ocupamos activar el ambiente virutal:

german@iecgerman:~/python-pip/app$ source env/bin/activate
(env) german@iecgerman:~/python-pip/app$ 

y para salir es con el comando:

deactivate

si volvemos a darle un which nos dará ahora la ruta del ambiente virtual:

(env) german@iecgerman:~/python-pip/app$ which python3
/home/german/python-pip/app/env/bin/python3
(env) german@iecgerman:~/python-pip/app$ which pip3
/home/german/python-pip/app/env/bin/pip3
(env) german@iecgerman:~/python-pip/app$ 

si le damos un pip3 freeze, no nos saldrá nada porque no hemos instalado nada para este modulo
instalamos por ejemplo matplotlib:

(env) german@iecgerman:~/python-pip/app$ pip3 install matplotlib

(env) german@iecgerman:~/python-pip/app$ pip3 freeze
contourpy==1.1.0
cycler==0.11.0
fonttools==4.42.1
kiwisolver==1.4.5
matplotlib==3.7.2
numpy==1.25.2
packaging==23.1
Pillow==10.0.0
pyparsing==3.0.9
python-dateutil==2.8.2
six==1.16.0
(env) german@iecgerman:~/python-pip/app$ 

si vemos matplotlib instaló otras dependencias porque las ocpupa para poder funcionar correctamente


OTRO EJEMPLO CON EL MODULO GAME

german@iecgerman:~/python-pip$ cd game
german@iecgerman:~/python-pip/game$ 

german@iecgerman:~/python-pip/game$ pwd
/home/german/python-pip/game
german@iecgerman:~/python-pip/game$ python3 -m venv env
german@iecgerman:~/python-pip/game$ source env/bin/activate
(env) german@iecgerman:~/python-pip/game$ pip3 install matplotlib==3.5.0


(env) german@iecgerman:~/python-pip/game$ pip3 freeze
cycler==0.11.0
fonttools==4.42.1
kiwisolver==1.4.5
matplotlib==3.5.0
numpy==1.25.2
packaging==23.1
Pillow==10.0.0
pyparsing==3.1.1
python-dateutil==2.8.2
setuptools-scm==7.1.0
six==1.16.0
tomli==2.0.1
typing_extensions==4.7.1
(env) german@iecgerman:~/python-pip/game$ 


# requirements.txt 11/20
https://platzi.com/clases/4261-python-pip/55131-requirementstxt/

para crear el al archivo requirements.txt
(env) german@iecgerman:~/python-pip/app$ pip3 freeze > requirements.txt


# Instrucciones para APP PROJECT

```sh
git clone
cd app
python3 -m  venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

# Solicitudes HTTP con Requests 12/20
https://platzi.com/clases/4261-python-pip/55132-solicitudes-http-con-requests/ 

cd python-pip/
mkdir web-server

Verificamos cual es el entorno que esta encendido:
```sh
which python3
```
usamos deacivate en caso de estar en otro entorno, por ejemplo app

cd web-server/

Creamos un entorno virtual sólo para el proyecto web-server:
```sh
python3 -m venv env
```

Activamos el entorno virtual:
```sh
source env/bin/activate
```

Volvemos a verificar que apuntemos al ambiente de web-server:
```sh
which python3
```

Instalamos la dependencia que necesitamos que es Requests
```sh
pip3 install requests
```
Verificamos la instalación con un freeze
```sh
pip3 freeze
```
Como es un proyecto nuevo creamos el archivo requeriments.txt por si una persona nueva quiere desplegar este proyecto
```sh
pip freeze > requeriments.txt
```

code .
python3 main.py 

(env) german@iecgerman:~/python-pip/web-server$ python3 main.py 
200
[{"id":1,"name":"Clothes","image":"https://picsum.photos/640/640?r=6397","creationAt":"2023-09-07T03:30:09.000Z","updatedAt":"2023-09-07T03:30:09.000Z"},{"id":2,"name":"Electronics","image":"https://picsum.photos/640/640?r=5186","creationAt":"2023-09-07T03:30:09.000Z","updatedAt":"2023-09-07T03:30:09.000Z"},{"id":3,"name":"Furniture","image":"https://picsum.photos/640/640?r=2966","creationAt":"2023-09-07T03:30:09.000Z","updatedAt":"2023-09-07T03:30:09.000Z"},{"id":4,"name":"Shoes","image":"https://picsum.photos/640/640?r=5871","creationAt":"2023-09-07T03:30:09.000Z","updatedAt":"2023-09-07T03:30:09.000Z"},{"id":5,"name":"Others","image":"https://picsum.photos/640/640?r=5523","creationAt":"2023-09-07T03:30:09.000Z","updatedAt":"2023-09-07T03:30:09.000Z"},{"id":6,"name":"Plants","image":"https://cdn.pixabay.com/photo/2016/11/18/17/20/flowers-1835619_960_720.jpg","creationAt":"2023-09-07T06:42:18.000Z","updatedAt":"2023-09-07T06:42:18.000Z"}]
<class 'str'>

nos da dice que es un string y tenemos que trasformarlo a una lista:

print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category['name'])

(env) german@iecgerman:~/python-pip/web-server$ python3 main.py 
200
[{"id":1,"name":"Clothes","image":"https://picsum.photos/640/640?r=6397","creationAt":"2023-09-07T03:30:09.000Z","updatedAt":"2023-09-07T03:30:09.000Z"},{"id":2,"name":"Electronics","image":"https://picsum.photos/640/640?r=5186","creationAt":"2023-09-07T03:30:09.000Z","updatedAt":"2023-09-07T03:30:09.000Z"},{"id":3,"name":"Furniture","image":"https://picsum.photos/640/640?r=2966","creationAt":"2023-09-07T03:30:09.000Z","updatedAt":"2023-09-07T03:30:09.000Z"},{"id":4,"name":"Shoes","image":"https://picsum.photos/640/640?r=5871","creationAt":"2023-09-07T03:30:09.000Z","updatedAt":"2023-09-07T03:30:09.000Z"},{"id":5,"name":"Others","image":"https://picsum.photos/640/640?r=5523","creationAt":"2023-09-07T03:30:09.000Z","updatedAt":"2023-09-07T03:30:09.000Z"},{"id":6,"name":"Plants","image":"https://cdn.pixabay.com/photo/2016/11/18/17/20/flowers-1835619_960_720.jpg","creationAt":"2023-09-07T06:42:18.000Z","updatedAt":"2023-09-07T06:42:18.000Z"}]
<class 'str'>
Clothes
Electronics
Furniture
Shoes
Others
Plants

ahora si nos a una lista la cual podemos, iterar, transformar, filtrar, etc.


# Pandas 13/20
https://platzi.com/clases/4261-python-pip/55133-pandas/

PANDAS

Es una de las librerias mas utilizadas en python y nos sirven para analizar y manipular datos de archivos duros

  673  cd python-pip/
  674  ll
  675  cd app
  676  ll
  677  source env/bin/activate
  678  which python3
  679  cat requirements.txt 
  680  pip3 install pandas
  681  pip3 freeze
  684  cat requirements.txt
  685  pip3 freeze > requirements.txt 
  686  cat requirements.txt
  687  python3 main.py 
  688  ll
  689  history

# Python para Backend: web server con FastAPI 14/20
https://platzi.com/clases/4261-python-pip/55134-python-para-backend-web-server-con-fastapi/

https://fastapi.tiangolo.com/#installation

https://www.uvicorn.org/ 
https://fastapi.tiangolo.com/advanced/custom-response/?h=response+html 

  695  cd web-server
  696  source env/bin/activate
  697  which python3
  698  pip3 install fastapi
  700  pip3 install "uvicorn[standard]"
  701  pip3 freeze
  702  pip3 freeze > requeriments.txt 
  703  cat requeriments.txt 
       ya no se corre el main como python3 main.py como un script ahora usamos:
  704  uvicorn main:app --reload # este es un flag para que recargue el servidor

# Python en contenedores de Docker

# ¿Qué es Docker? 15/20
https://platzi.com/clases/4261-python-pip/55135-que-es-docker/
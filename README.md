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


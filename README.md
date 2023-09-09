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

https://docs.docker.com/

Docker

Es una herramienta que nos sirve para aislar entornos de ejecucion, eso lo hace con contenedores que tiene docker por detras.

# Instalación de Docker 16/20
https://platzi.com/clases/4261-python-pip/55136-instalacion-de-docker/

Instalación en Ubuntu 🐧

https://docs.docker.com/engine/install/ubuntu/

# german@iecgerman:~$ sudo apt-get update
Obj:1 https://download.docker.com/linux/ubuntu jammy InRelease
Obj:2 http://packages.microsoft.com/repos/code stable InRelease                
Des:3 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]      
Obj:4 http://mx.archive.ubuntu.com/ubuntu jammy InRelease                      
Obj:5 https://dl.google.com/linux/chrome/deb stable InRelease                  
Des:6 http://mx.archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]     
Obj:7 https://ppa.launchpadcontent.net/git-core/ppa/ubuntu jammy InRelease     
Des:8 http://mx.archive.ubuntu.com/ubuntu jammy-backports InRelease [109 kB]   
Descargados 338 kB en 1s (274 kB/s) 
Leyendo lista de paquetes... Hecho

# german@iecgerman:~$ sudo apt-get install ca-certificates curl gnupg lsb-release
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias... Hecho
Leyendo la información de estado... Hecho
lsb-release ya está en su versión más reciente (11.1.0ubuntu4).
ca-certificates ya está en su versión más reciente (20230311ubuntu0.22.04.1).
curl ya está en su versión más reciente (7.81.0-1ubuntu1.13).
gnupg ya está en su versión más reciente (2.2.27-3ubuntu2.1).
0 actualizados, 0 nuevos se instalarán, 0 para eliminar y 0 no actualizados.

# german@iecgerman:~$ sudo mkdir -p /etc/apt/keyrings
german@iecgerman:~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
El fichero '/etc/apt/keyrings/docker.gpg' ya existe. ¿Sobreescribir? (s/N) S

# german@iecgerman:~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
El fichero '/etc/apt/keyrings/docker.gpg' ya existe. ¿Sobreescribir? (s/N) S

# german@iecgerman:~$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
[sudo] contraseña para german: 

# german@iecgerman:~$ sudo apt-get update
Obj:1 http://mx.archive.ubuntu.com/ubuntu jammy InRelease
Obj:2 https://download.docker.com/linux/ubuntu jammy InRelease                 
Obj:3 http://mx.archive.ubuntu.com/ubuntu jammy-updates InRelease              
Obj:4 https://dl.google.com/linux/chrome/deb stable InRelease                  
Obj:5 http://packages.microsoft.com/repos/code stable InRelease                
Obj:6 http://security.ubuntu.com/ubuntu jammy-security InRelease               
Des:7 http://mx.archive.ubuntu.com/ubuntu jammy-backports InRelease [109 kB]   
Obj:8 https://ppa.launchpadcontent.net/git-core/ppa/ubuntu jammy InRelease     
Descargados 109 kB en 1s (141 kB/s)
Leyendo lista de paquetes... Hecho

# german@iecgerman:~$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias... Hecho
Leyendo la información de estado... Hecho
containerd.io ya está en su versión más reciente (1.6.22-1).
docker-ce-cli ya está en su versión más reciente (5:24.0.6-1~ubuntu.22.04~jammy).
docker-ce ya está en su versión más reciente (5:24.0.6-1~ubuntu.22.04~jammy).
docker-compose-plugin ya está en su versión más reciente (2.21.0-1~ubuntu.22.04~jammy).
0 actualizados, 0 nuevos se instalarán, 0 para eliminar y 0 no actualizados.

# german@iecgerman:~$ sudo docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
719385e32844: Pull complete 
Digest: sha256:dcba6daec718f547568c562956fa47e1b03673dd010fe6ee58ca806767031d1c
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

german@iecgerman:~$ 


# Dockerizando scripts de Python 17/20
https://platzi.com/clases/4261-python-pip/55137-dockerizando-scripts-de-python/





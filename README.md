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

USANDO UBUNTU:

german@iecgerman:~/python-pip/app$ docker-compose build <--- NO FUNCIONA CON UBUNTU
No se ha encontrado la orden «docker-compose», pero se puede instalar con:
sudo snap install docker
# german@iecgerman:~/python-pip/app$ sudo docker compose build
[+] Building 23.9s (8/9)                                         docker:default
 => [app-csv internal] load build definition from Dockerfile               0.0s
 => => transferring dockerfile: 236B                                       0.0s
 => [app-csv internal] load .dockerignore                                  0.0s
 => => transferring context: 2B                                            0.0s
 => [app-csv internal] load metadata for docker.io/library/python:3.8      1.1s
 => [app-csv 1/5] FROM docker.io/library/python:3.8@sha256:9c7e79fb6ee13  18.7s
 => => resolve docker.io/library/python:3.8@sha256:9c7e79fb6ee130af5c0be2  0.0s
 => => sha256:9c7e79fb6ee130af5c0be2e3dea04cb6537891e9d39 1.86kB / 1.86kB  0.0s
 => => sha256:18e3604e7dae49be47932b21a261687ef39dc415239 2.01kB / 2.01kB  0.0s
 => => sha256:00046d1e755ea94fa55a700ca9a10597e4fac7c47 24.03MB / 24.03MB  2.5s
 => => sha256:d2a527900b6d84c6360fae82d650180bff11ea92dca 7.56kB / 7.56kB  0.0s
 => => sha256:012c0b3e998c1a0c0bedcf712eaaafb188580529d 49.56MB / 49.56MB  3.1s
 => => sha256:9f13f5a53d118643c1f1ff294867c09f224d00edc 64.11MB / 64.11MB  4.5s
 => => sha256:e13e76ad6279c3d69aa6842a935288c7db6687 210.99MB / 210.99MB  10.7s
 => => extracting sha256:012c0b3e998c1a0c0bedcf712eaaafb188580529dd026a04  1.5s
 => => sha256:ad4c837a72f8d2d63d64bf7f9d7c43fe9e67f3d82af 6.39MB / 6.39MB  3.7s
 => => sha256:9e4f17820ba9758fdce31eaf26badefc8f96822e3 17.28MB / 17.28MB  5.2s
 => => sha256:2db6ac4d34c87613f23af427aa9f00748db1760e4330605 242B / 242B  4.6s
 => => sha256:56b9a6ce12e5399ea92b6a692eafcd51a4db0d6b3ce 2.85MB / 2.85MB  4.9s
 => => extracting sha256:00046d1e755ea94fa55a700ca9a10597e4fac7c47be19d97  0.5s
 => => extracting sha256:9f13f5a53d118643c1f1ff294867c09f224d00edca21f56c  2.1s
 => => extracting sha256:e13e76ad6279c3d69aa6842a935288c7db66878ec3b7815e  6.9s
 => => extracting sha256:ad4c837a72f8d2d63d64bf7f9d7c43fe9e67f3d82af7ac47  0.2s
 => => extracting sha256:9e4f17820ba9758fdce31eaf26badefc8f96822e3408b993  0.5s
 => => extracting sha256:2db6ac4d34c87613f23af427aa9f00748db1760e4330605c  0.0s
 => => extracting sha256:56b9a6ce12e5399ea92b6a692eafcd51a4db0d6b3ce06466  0.2s
 => [app-csv internal] load build context                                  1.0s
 => => transferring context: 231.84MB                                      1.0s
 => [app-csv 2/5] WORKDIR /app                                             1.1s
 => [app-csv 3/5] COPY requirements.txt /app/requirements.txt              0.0s
 => ERROR [app-csv 4/5] RUN pip install --no-cache-dir --upgrade -r /app/  3.0s
------
 > [app-csv 4/5] RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt:
1.351 Collecting contourpy==1.1.0
1.462   Downloading contourpy-1.1.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (300 kB)
1.525      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 300.4/300.4 kB 4.9 MB/s eta 0:00:00
1.552 Collecting cycler==0.11.0
1.574   Downloading cycler-0.11.0-py3-none-any.whl (6.4 kB)
1.676 Collecting fonttools==4.42.1
1.707   Downloading fonttools-4.42.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.6 MB)
1.804      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 47.6 MB/s eta 0:00:00
1.913 Collecting kiwisolver==1.4.5
1.938   Downloading kiwisolver-1.4.5-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.2 MB)
1.951      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 104.0 MB/s eta 0:00:00
2.161 Collecting matplotlib==3.7.2
2.189   Downloading matplotlib-3.7.2-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (9.2 MB)
2.333      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.2/9.2 MB 64.7 MB/s eta 0:00:00
2.670 ERROR: Ignored the following versions that require a different python version: 1.25.0 Requires-Python >=3.9; 1.25.0rc1 Requires-Python >=3.9; 1.25.1 Requires-Python >=3.9; 1.25.2 Requires-Python >=3.9; 1.26.0b1 Requires-Python <3.13,>=3.9; 1.26.0rc1 Requires-Python <3.13,>=3.9; 3.8.0rc1 Requires-Python >=3.9
2.670 ERROR: Could not find a version that satisfies the requirement numpy==1.25.2 (from versions: 1.3.0, 1.4.1, 1.5.0, 1.5.1, 1.6.0, 1.6.1, 1.6.2, 1.7.0, 1.7.1, 1.7.2, 1.8.0, 1.8.1, 1.8.2, 1.9.0, 1.9.1, 1.9.2, 1.9.3, 1.10.0.post2, 1.10.1, 1.10.2, 1.10.4, 1.11.0, 1.11.1, 1.11.2, 1.11.3, 1.12.0, 1.12.1, 1.13.0, 1.13.1, 1.13.3, 1.14.0, 1.14.1, 1.14.2, 1.14.3, 1.14.4, 1.14.5, 1.14.6, 1.15.0, 1.15.1, 1.15.2, 1.15.3, 1.15.4, 1.16.0, 1.16.1, 1.16.2, 1.16.3, 1.16.4, 1.16.5, 1.16.6, 1.17.0, 1.17.1, 1.17.2, 1.17.3, 1.17.4, 1.17.5, 1.18.0, 1.18.1, 1.18.2, 1.18.3, 1.18.4, 1.18.5, 1.19.0, 1.19.1, 1.19.2, 1.19.3, 1.19.4, 1.19.5, 1.20.0, 1.20.1, 1.20.2, 1.20.3, 1.21.0, 1.21.1, 1.21.2, 1.21.3, 1.21.4, 1.21.5, 1.21.6, 1.22.0, 1.22.1, 1.22.2, 1.22.3, 1.22.4, 1.23.0rc1, 1.23.0rc2, 1.23.0rc3, 1.23.0, 1.23.1, 1.23.2, 1.23.3, 1.23.4, 1.23.5, 1.24.0rc1, 1.24.0rc2, 1.24.0, 1.24.1, 1.24.2, 1.24.3, 1.24.4)
2.671 ERROR: No matching distribution found for numpy==1.25.2
2.828 
2.828 [notice] A new release of pip is available: 23.0.1 -> 23.2.1
2.828 [notice] To update, run: pip install --upgrade pip
------
failed to solve: process "/bin/sh -c pip install --no-cache-dir --upgrade -r /app/requirements.txt" did not complete successfully: exit code: 1
german@iecgerman:~/python-pip/app$ 

# german@iecgerman:~/python-pip/app$ sudo docker compose up -d
[+] Building 3.8s (8/9)                                          docker:default
 => [app-csv internal] load .dockerignore                                  0.0s
 => => transferring context: 2B                                            0.0s
 => [app-csv internal] load build definition from Dockerfile               0.0s
 => => transferring dockerfile: 236B                                       0.0s
 => [app-csv internal] load metadata for docker.io/library/python:3.8      0.5s
 => [app-csv 1/5] FROM docker.io/library/python:3.8@sha256:9c7e79fb6ee130  0.0s
 => [app-csv internal] load build context                                  0.2s
 => => transferring context: 912.70kB                                      0.2s
 => CACHED [app-csv 2/5] WORKDIR /app                                      0.0s
 => CACHED [app-csv 3/5] COPY requirements.txt /app/requirements.txt       0.0s
 => ERROR [app-csv 4/5] RUN pip install --no-cache-dir --upgrade -r /app/  3.1s
------                                                                          
 > [app-csv 4/5] RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt:                                                                             
1.359 Collecting contourpy==1.1.0                                               
1.562   Downloading contourpy-1.1.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (300 kB)                                                           
1.615      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 300.4/300.4 kB 5.7 MB/s eta 0:00:00
1.650 Collecting cycler==0.11.0
1.669   Downloading cycler-0.11.0-py3-none-any.whl (6.4 kB)
1.796 Collecting fonttools==4.42.1
1.818   Downloading fonttools-4.42.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.6 MB)
1.906      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 53.6 MB/s eta 0:00:00
2.030 Collecting kiwisolver==1.4.5
2.052   Downloading kiwisolver-1.4.5-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.2 MB)
2.064      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 108.2 MB/s eta 0:00:00
2.301 Collecting matplotlib==3.7.2
2.328   Downloading matplotlib-3.7.2-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (9.2 MB)
2.467      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.2/9.2 MB 67.4 MB/s eta 0:00:00
2.770 ERROR: Ignored the following versions that require a different python version: 1.25.0 Requires-Python >=3.9; 1.25.0rc1 Requires-Python >=3.9; 1.25.1 Requires-Python >=3.9; 1.25.2 Requires-Python >=3.9; 1.26.0b1 Requires-Python <3.13,>=3.9; 1.26.0rc1 Requires-Python <3.13,>=3.9; 3.8.0rc1 Requires-Python >=3.9
2.770 ERROR: Could not find a version that satisfies the requirement numpy==1.25.2 (from versions: 1.3.0, 1.4.1, 1.5.0, 1.5.1, 1.6.0, 1.6.1, 1.6.2, 1.7.0, 1.7.1, 1.7.2, 1.8.0, 1.8.1, 1.8.2, 1.9.0, 1.9.1, 1.9.2, 1.9.3, 1.10.0.post2, 1.10.1, 1.10.2, 1.10.4, 1.11.0, 1.11.1, 1.11.2, 1.11.3, 1.12.0, 1.12.1, 1.13.0, 1.13.1, 1.13.3, 1.14.0, 1.14.1, 1.14.2, 1.14.3, 1.14.4, 1.14.5, 1.14.6, 1.15.0, 1.15.1, 1.15.2, 1.15.3, 1.15.4, 1.16.0, 1.16.1, 1.16.2, 1.16.3, 1.16.4, 1.16.5, 1.16.6, 1.17.0, 1.17.1, 1.17.2, 1.17.3, 1.17.4, 1.17.5, 1.18.0, 1.18.1, 1.18.2, 1.18.3, 1.18.4, 1.18.5, 1.19.0, 1.19.1, 1.19.2, 1.19.3, 1.19.4, 1.19.5, 1.20.0, 1.20.1, 1.20.2, 1.20.3, 1.21.0, 1.21.1, 1.21.2, 1.21.3, 1.21.4, 1.21.5, 1.21.6, 1.22.0, 1.22.1, 1.22.2, 1.22.3, 1.22.4, 1.23.0rc1, 1.23.0rc2, 1.23.0rc3, 1.23.0, 1.23.1, 1.23.2, 1.23.3, 1.23.4, 1.23.5, 1.24.0rc1, 1.24.0rc2, 1.24.0, 1.24.1, 1.24.2, 1.24.3, 1.24.4)
2.770 ERROR: No matching distribution found for numpy==1.25.2
2.953 
2.953 [notice] A new release of pip is available: 23.0.1 -> 23.2.1
2.953 [notice] To update, run: pip install --upgrade pip
------
failed to solve: process "/bin/sh -c pip install --no-cache-dir --upgrade -r /app/requirements.txt" did not complete successfully: exit code: 1
german@iecgerman:~/python-pip/app$ 

# german@iecgerman:~/python-pip/app$ sudo docker compose ps
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS
german@iecgerman:~/python-pip/app$ 

# AQUI ME MARCABA EL SIGUIENTE ERROR:

# german@iecgerman:~/python-pip/app$ sudo docker compose up -d
[+] Building 3.6s (8/9)                                          docker:default
 => [app-csv internal] load .dockerignore                                  0.0s
 => => transferring context: 2B                                            0.0s
 => [app-csv internal] load build definition from Dockerfile               0.0s
 => => transferring dockerfile: 236B                                       0.0s
 => [app-csv internal] load metadata for docker.io/library/python:3.8      0.3s
 => [app-csv 1/5] FROM docker.io/library/python:3.8@sha256:9c7e79fb6ee130  0.0s
 => [app-csv internal] load build context                                  0.2s
 => => transferring context: 912.70kB                                      0.2s
 => CACHED [app-csv 2/5] WORKDIR /app                                      0.0s
 => CACHED [app-csv 3/5] COPY requirements.txt /app/requirements.txt       0.0s
 => ERROR [app-csv 4/5] RUN pip install --no-cache-dir --upgrade -r /app/  3.1s
------                                                                          
 > [app-csv 4/5] RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt:                                                                             
1.369 Collecting contourpy==1.1.0                                               
1.507   Downloading contourpy-1.1.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (300 kB)                                                           
1.572      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 300.4/300.4 kB 4.9 MB/s eta 0:00:00
1.605 Collecting cycler==0.11.0
1.685   Downloading cycler-0.11.0-py3-none-any.whl (6.4 kB)
1.810 Collecting fonttools==4.42.1
1.833   Downloading fonttools-4.42.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.6 MB)
1.936      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 45.7 MB/s eta 0:00:00
2.053 Collecting kiwisolver==1.4.5
2.076   Downloading kiwisolver-1.4.5-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.2 MB)
2.090      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 94.7 MB/s eta 0:00:00
2.292 Collecting matplotlib==3.7.2
2.323   Downloading matplotlib-3.7.2-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (9.2 MB)
2.530      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.2/9.2 MB 45.1 MB/s eta 0:00:00
2.835 ERROR: Ignored the following versions that require a different python version: 1.25.0 
# Cambie a python 3.10 en el archivo Dockerfile y listo
Requires-Python >=3.9; 1.25.0rc1 Requires-Python >=3.9; 1.25.1 Requires-Python >=3.9; 1.25.2 Requires-Python >=3.9; 1.26.0b1 Requires-Python <3.13,>=3.9; 1.26.0rc1 Requires-Python <3.13,>=3.9; 3.8.0rc1 Requires-Python >=3.9 
2.835 ERROR: Could not find a version that satisfies the requirement numpy==1.25.2 (from versions: 1.3.0, 1.4.1, 1.5.0, 1.5.1, 1.6.0, 1.6.1, 1.6.2, 1.7.0, 1.7.1, 1.7.2, 1.8.0, 1.8.1, 1.8.2, 1.9.0, 1.9.1, 1.9.2, 1.9.3, 1.10.0.post2, 1.10.1, 1.10.2, 1.10.4, 1.11.0, 1.11.1, 1.11.2, 1.11.3, 1.12.0, 1.12.1, 1.13.0, 1.13.1, 1.13.3, 1.14.0, 1.14.1, 1.14.2, 1.14.3, 1.14.4, 1.14.5, 1.14.6, 1.15.0, 1.15.1, 1.15.2, 1.15.3, 1.15.4, 1.16.0, 1.16.1, 1.16.2, 1.16.3, 1.16.4, 1.16.5, 1.16.6, 1.17.0, 1.17.1, 1.17.2, 1.17.3, 1.17.4, 1.17.5, 1.18.0, 1.18.1, 1.18.2, 1.18.3, 1.18.4, 1.18.5, 1.19.0, 1.19.1, 1.19.2, 1.19.3, 1.19.4, 1.19.5, 1.20.0, 1.20.1, 1.20.2, 1.20.3, 1.21.0, 1.21.1, 1.21.2, 1.21.3, 1.21.4, 1.21.5, 1.21.6, 1.22.0, 1.22.1, 1.22.2, 1.22.3, 1.22.4, 1.23.0rc1, 1.23.0rc2, 1.23.0rc3, 1.23.0, 1.23.1, 1.23.2, 1.23.3, 1.23.4, 1.23.5, 1.24.0rc1, 1.24.0rc2, 1.24.0, 1.24.1, 1.24.2, 1.24.3, 1.24.4)
2.835 ERROR: No matching distribution found for numpy==1.25.2
3.025 
3.025 [notice] A new release of pip is available: 23.0.1 -> 23.2.1
3.025 [notice] To update, run: pip install --upgrade pip
------
failed to solve: process "/bin/sh -c pip install --no-cache-dir --upgrade -r /app/requirements.txt" did not complete successfully: exit code: 1

# german@iecgerman:~/python-pip/app$ sudo docker compose up -d
[+] Building 14.5s (10/10) FINISHED                              docker:default
 => [app-csv internal] load .dockerignore                                  0.0s
 => => transferring context: 2B                                            0.0s
 => [app-csv internal] load build definition from Dockerfile               0.0s
 => => transferring dockerfile: 237B                                       0.0s
 => [app-csv internal] load metadata for docker.io/library/python:3.10     0.9s
 => [app-csv 1/5] FROM docker.io/library/python:3.10@sha256:1a8dcc0736806  1.5s
 => => resolve docker.io/library/python:3.10@sha256:1a8dcc07368065c2b285b  0.0s
 => => sha256:c6478014f220f7770a05928eb5102c81ebade156edd 3.08MB / 3.08MB  0.2s
 => => sha256:17b967fa748a2929eb2682018a9d0e335aeebff3963 2.01kB / 2.01kB  0.0s
 => => sha256:aa51dc5b3e4b04c28168c424bb88a7329fa5ddea735 7.53kB / 7.53kB  0.0s
 => => sha256:31f059ee2e3049f82504fc8227668a34b17b36f76 17.15MB / 17.15MB  0.6s
 => => sha256:c368f0c33c1e0fd7583a410727c3ee1d2dc73d303f9b5fe 244B / 244B  0.1s
 => => sha256:1a8dcc07368065c2b285b24236a98e80355d6de7f68 1.65kB / 1.65kB  0.0s
 => => extracting sha256:31f059ee2e3049f82504fc8227668a34b17b36f7664a3dbc  0.6s
 => => extracting sha256:c368f0c33c1e0fd7583a410727c3ee1d2dc73d303f9b5feb  0.0s
 => => extracting sha256:c6478014f220f7770a05928eb5102c81ebade156edd564e2  0.2s
 => [app-csv internal] load build context                                  0.2s
 => => transferring context: 912.91kB                                      0.2s
 => [app-csv 2/5] WORKDIR /app                                             0.1s
 => [app-csv 3/5] COPY requirements.txt /app/requirements.txt              0.0s
 => [app-csv 4/5] RUN pip install --no-cache-dir --upgrade -r /app/requi  10.0s
 => [app-csv 5/5] COPY . /app                                              0.9s 
 => [app-csv] exporting to image                                           1.0s
 => => exporting layers                                                    1.0s
 => => writing image sha256:982f48c4f2a620ab419e2e277575047f44c125cf4e2d6  0.0s
 => => naming to docker.io/library/app-app-csv                             0.0s
[+] Running 2/2
 ✔ Network app_default      Created                                        0.1s 
 ✔ Container app-app-csv-1  Started                                        0.0s 
german@iecgerman:~/python-pip/app$ 

# german@iecgerman:~/python-pip/app$ sudo docker compose exec app-csv bash
root@58f845560ada:/app# 

# root@58f845560ada:/app# ls -l
total 176
-rw-rw-r-- 1 root root    198 Sep 12 07:01 Dockerfile
drwxrwxr-x 2 root root   4096 Sep  8 07:29 __pycache__
-rw-r--r-- 1 root root    466 Sep  4 08:25 charts.py
-rw------- 1 root root  29247 Sep  8 07:46 data.csv
-rw-rw-r-- 1 root root     82 Sep 12 06:38 docker-compose.yml
drwxrwxr-x 6 root root   4096 Sep  5 00:17 env
drwxrwxr-x 2 root root   4096 Sep  4 08:51 imagenes
-rw-r--r-- 1 root root   1109 Sep  8 07:50 main.py
-rw-rw-r-- 1 root root 106059 Sep  9 08:41 pie.png
-rw-r--r-- 1 root root    409 Sep  4 08:08 read_csv.py
-rw-rw-r-- 1 root root    231 Sep  9 08:37 requirements.txt
-rw-r--r-- 1 root root   1004 Aug  5 09:04 utilidades.py
root@58f845560ada:/app# 

# root@58f845560ada:/app# python3 main.py
🏴‍☠️  Escribe el pais del cual quieres su poblacion: Colombia
Colombia
{'Rank': '28', 'CCA3': 'COL', 'Country/Territory': 'Colombia', 'Capital': 'Bogota', 'Continent': 'South America', '2022 Population': '51874024', '2020 Population': '50930662', '2015 Population': '47119728', '2010 Population': '44816108', '2000 Population': '39215135', '1990 Population': '32601393', '1980 Population': '26176195', '1970 Population': '20905254', 'Area (km²)': '1141748', 'Density (per km²)': '45.4339', 'Growth Rate': '1.0069', 'World Population Percentage': '0.65'}
root@58f845560ada:/app#

# Si llegamos a salir es con exit


Tambien ya no es necesario poner python3
# root@f6117148fe3b:/app# python main.py 
🏴‍☠️  Escribe el pais del cual quieres su poblacion: Argentina
Argentina
{'Rank': '33', 'CCA3': 'ARG', 'Country/Territory': 'Argentina', 'Capital': 'Buenos Aires', 'Continent': 'South America', '2022 Population': '45510318', '2020 Population': '45036032', '2015 Population': '43257065', '2010 Population': '41100123', '2000 Population': '37070774', '1990 Population': '32637657', '1980 Population': '28024803', '1970 Population': '23842803', 'Area (km²)': '2780400', 'Density (per km²)': '16.3683', 'Growth Rate': '1.0052', 'World Population Percentage': '0.57'}
root@f6117148fe3b:/app# 


CONCLUSION:

Con Docker tu puedes tener diferentes con tenedores y en cada uno podrías tener diferentes lenguajes, por ejemplo en un contenedor podrías correr python, en otro contenedor podrías correr ruby, en otro contenedor podrías correr go, etc. sin tener que instalar todo en tu entorno; posiblemente como python developer usemos mas ambientes virtuales pero es bueno familiarizarnos con contenedores de Docker un poco.


# Docker para el día a día: automatizando la vinculación de archivos 18/20
https://platzi.com/clases/4261-python-pip/55138-docker-para-el-dia-a-dia-automatizando-la-vinculac/

En docker-compose.yml hacemos lso siguientes cambios:

services:
  app-csv:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app

y con esto podemos ahora si hacer en tiempo real cambio por ejemplo en charts.py:

def generate_pie_chart(labels, values):  
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('chart_pie_cambios_finales.png')
  plt.close()

  pero antes ejecutamos los commandos:

```sh
sudo docker compose up -d
sudo docker compose exec app-csv bash
cat charts.py
```

# Dockerizando web services 19/20
https://platzi.com/clases/4261-python-pip/55139-dockerizando-web-services/

Aplicamos la técnica legendaria de copiar y pegar en los archivos:

app/Dockerfile

Aquí todo se queda igual excepto la última línea:

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

app/docker-compose.yml

hacemos estos cambios:

services:
  web-server:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
    ports:
      - '80:80'

y ahora si entramos a la carpeta web-server y vovlemos a construir con:

# german@iecgerman:~/python-pip/web-server$ sudo docker compose build
[+] Building 12.2s (10/10) FINISHED                              docker:default
 => [web-server internal] load build definition from Dockerfile            0.0s
 => => transferring dockerfile: 334B                                       0.0s
 => [web-server internal] load .dockerignore                               0.0s
 => => transferring context: 2B                                            0.0s
 => [web-server internal] load metadata for docker.io/library/python:3.10  0.3s
 => [web-server 1/5] FROM docker.io/library/python:3.10@sha256:1a8dcc0736  0.0s
 => [web-server internal] load build context                               0.0s
 => => transferring context: 256.10kB                                      0.0s
 => CACHED [web-server 2/5] WORKDIR /app                                   0.0s
 => [web-server 3/5] COPY requirements.txt /app/requirements.txt           0.0s
 => [web-server 4/5] RUN pip install --no-cache-dir --upgrade -r /app/re  11.3s
 => [web-server 5/5] COPY . /app                                           0.2s
 => [web-server] exporting to image                                        0.3s 
 => => exporting layers                                                    0.3s 
 => => writing image sha256:f139ab5bc18965f98448d58a809fc1f78fb80024cba3b  0.0s 
 => => naming to docker.io/library/web-server-web-server                   0.0s 
german@iecgerman:~/python-pip/web-server$       


Levantamos con:

# german@iecgerman:~/python-pip/web-server$ sudo docker compose up -d             
[+] Running 2/2
 ✔ Network web-server_default         Crea...                              0.1s 
 ✔ Container web-server-web-server-1  Started                              0.0s 
german@iecgerman:~/python-pip/web-server$ 


Verificamos si levanto con:

# german@iecgerman:~/python-pip/web-server$ sudo docker compose ps
NAME                      IMAGE                   COMMAND                                       SERVICE      CREATED         STATUS         PORTS
web-server-web-server-1   web-server-web-server   "uvicorn main:app --host 0.0.0.0 --port 80"   web-server   2 minutes ago   Up 2 minutes   0.0.0.0:80->80/tcp, :::80->80/tcp
german@iecgerman:~/python-pip/web-server$ 



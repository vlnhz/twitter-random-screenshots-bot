# Twitter Random Screenshots Bot

Bot de twitter que postea frames de series cada x tiempo.
Ejemplo: [botsimuladores](https://www.twitter.com/botsimuladores/)

## Tutorial para configurar y usar el bot en tu cuenta

### Requisitos previos

Cosas que tenés que tener instaladas para poder usar el bot.

```
Python
Tweepy
```

### Instalación

##### 1. Instalar python desde la [web de python](https://www.python.org/downloads/)

##### 2.  Instalar tweepy con el comando:
```
pip install git+https://github.com/tweepy/tweepy.git
```
##### 3. Descargar o clonar el proyecto
Para esto podemos usar la opción 'Download ZIP' que aparece cuando clickeamos el botón verde 'Code' de arriba a la derecha de esta página.

## Configurar el bot
### Paso 1: Credenciales de Twitter
Una vez descargado el repo, abrir el archivo ``config.ini`` con un editor de texto. Este archivo contiene las variables necesarias para que funcione el bot.

Dentro del archivo hay que completar las variables:
```
API_KEY =
API_KEY_SECRET =
ACCESS_TOKEN =
ACCESS_TOKEN_SECRET = 
```
con las credenciales de twitter para desarrolladores.

Si ya sabes como obtener las credenciales para desarrolladores de Twitter podes saltearte este paso y pegar las credenciales directamente en el archivo ```config.ini```.
Si no sabes como hacerlo a continuación un mini tutorial:


### Credenciales de twitter para desarrolladores
Guía corta para generar las credenciales de twitter para desarrolladores.
##### Pasos: 
* Entrar a [Twitter Apps](https://apps.twitter.com/) y en la sección `Standalone Apps` elegir la opción `(+)Create App`.
* Rellenar el nombre y crear la app.
* Se nos mostrarán los tokens ``Api Key`` y ``Api Secret Key``. Estos los pegaremos en los campos ``API_KEY`` y ``API_KEY_SECRET`` del archivo ``config.ini`` que abrimos antes.
* Ahora buscamos nuestra app en el panel de la izquierda, la clickeamos, y bajamos hasta la parte de ```User authentication settings```, le damos al botón ```Set up``` y activamos la opción ```OAuth 1.0a```.
* Rellenamos todos los datos que pide Twitter y en la parte de ```App permissions``` seleccionamos la opción READ AND WRITE (muy importante, si hacemos mal esto el bot no va a tener permisos para twittear).
* Luego volvemos a la pagina anterior y volvemos a clickear en nuestra app, ahora vamos a la parte de ``Keys and tokens`` clickeamos en la opción ``Generate`` de la sección ``Access Token and Secret``.
* Dentro de la ventana que se muestra veremos nuestros ``Access Token`` y ``Access Token Secret``. Estos tokens deben tener permisos de lectura y escritura. Una vez generados los copiamos y los pegamos respectivamente en los campos ```ACCESS_TOKEN``` y ```ACCESS_TOKEN_SECRET``` del ```config.ini```

### Paso 2: Configurar los capítulos (y opcionalmente subtítulos)
Lo único que nos queda por hacer es copiar nuestros capítulos y subtítulos dentro de las carpetas ```capitulos/``` y ```subtitulos/```.

#### Aclaraciones:
* IMPORTANTE: eliminar los archivos ```.gitkeep``` que se encuentran adentro de las carpetas ```capitulos/``` y ```subtitulos/```.
* El formato de los videos de los capitulos recomendado es ```.mp4``` (no está probado con otros formatos pero se puede intentar).

#### Configurar los subtítulos (opcional):
Solo hacer esto si vamos a usar subtítulos en las capturas
* Primero que nada, vamos a cambiar en la config el campo ```withSubtitles = false``` por ```withSubtitles = true```
* El formato de los archivos de los subtítulos tiene que ser ```.srt```
* Si vamos a usar la opción de postear la capturas con subtítulos, los archivos ```.srt``` tienen que tener el mismo nombre que el archivo de video del capítulo al que corresponden, con la diferencia de la extensión.

Ejemplo :

```
📂capitulos/:
    🎞️capitulo1.mp4
    🎞️capitulo2.mp4
```

```
📂subtitulos/:
    📝capitulo1.srt
    📝capitulo2.srt
```

### Paso 3: Configurar el tiempo entre tweets
En este paso vamos a configurar el tiempo que va a pasar entre cada tweet del bot. Lo mínimo seguro para que no nos suspendan la cuenta es de 30 minutos (1800 segundos).
Esto lo vamos a modificar en la variable ```tiempoEspera``` del archivo de configuración.

Si estás en Windows, la variable ```alwaysRunning``` la vamos a dejar en siempre en True.

Si estás en Linux podes setearla en false y usar un programa como ```crontab``` para ejecutar automáticamente el script cada un determinado intervalo de tiempo.

### Paso 4: Ejecutar el bot
Para ejecutar el bot vamos a abrir el archivo bot.py con python. Para esto le hacemos click derecho > abrir con... > Python.


También podemos correrlo desde un cmd con el comando ```python bot.py```, habiéndonos posicionado previamente en el directorio donde se encuentra el script.

Si hicimos todo bien, nos va a aparecer un mensaje que dice ```Twitteando captura...``` y después ```Captura twitteada```. En ese momento tendríamos que ver un nuevo tweet con una captura aleatoria de la cuenta cuyas credenciales escribimos en la configuración.

Después de twittear el bot se va a quedar esperando la cantidad de segundos que le hayamos configurado y pasado ese tiempo va a volver a postear.
Mientras tengamos esta ventana abierta el bot va a seguir twitteando según el tiempo establecido en la configuración.

### Fin


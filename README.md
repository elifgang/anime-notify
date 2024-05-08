[![v1.1.2b](https://img.shields.io/badge/release-v1.2-green)](python)

### Descripción general

Este script permite recibir notificaciones cuando un nuevo episodio de un anime específico esté disponible. El usuario proporciona el nombre del anime, y el script busca el anime en [notify.moe](https://notify.moe/) y comprueba si hay un nuevo episodio disponible. Si lo hay, se envía una notificación. De lo contrario, el script comprueba cuántos días faltan para el siguiente episodio y envía una notificación con esta información.

### Funciones

* `request(url)`:
  * Esta función realiza una solicitud HTTP GET al `url` proporcionado y devuelve una instancia de `BeautifulSoup` con el contenido HTML de la página.
* `complete_link()`:
  * Esta función toma una URL parcial y devuelve la URL completa de `https://notify.moe`.
* `search_Anime()`:
  * Esta función busca en la página de inicio de `https://notify.moe` y devuelve una lista de nombres de anime que contienen la cadena de búsqueda proporcionada por el usuario.
* `get_AnimeLink()`:
  * Esta función toma el nombre del anime como entrada y devuelve la URL de la página del anime en `https://notify.moe`.
* `get_AnimeName()`:
  * Esta función toma la URL de la página del anime y devuelve el nombre del anime.
* `get_AnimeEpisode()`:
  * Esta función toma la URL de la página del anime y devuelve el número de episodios disponibles.
* `get_state_episode()`:
  * Esta función toma la URL de la página del anime y devuelve un valor booleano que indica si el último episodio disponible está disponible o no.
* `get_restTime()`:
  * Esta función toma la URL de la página del anime y el número de episodios y devuelve el número de días restantes hasta que se emita el próximo episodio.
* `send_notification()`:
  * Esta función toma un título y un mensaje y envía una notificación utilizando la biblioteca `notifypy`.
* `main()`:
  * Esta es la función principal del script que llama a las otras funciones y envía las notificaciones.

### Requisitos

* `beautifulsoup4` - Para extraer información de las páginas web.
* `requests` - Para realizar solicitudes HTTP a `https://notify.moe`.
* `datetime` - Para manejar fechas y tiempos.
* `re` - Para trabajar con expresiones regulares.
* `notifypy` - Para enviar notificaciones al escritorio.

Para instalar estos paquetes, se puede usar `pip`.

### Uso

1. Ejecute el script.
2. Ingrese el nombre del anime que desea recibir notificaciones.
3. El script buscará el anime y enviará una notificación si hay un nuevo episodio disponible. De lo contrario, enviará una notificación con la fecha del próximo episodio.

## Funciones Futuras

* Tiene la capacidad de buscar el Anime que este en la base de datos.
* Obtendra una notificacion pop-up en Windows con el nombre y episodio, tambien el tiempo restante si no ha salido.

## Hoja de Ruta

- Mostrar la notificacion vía Web.
- Realizar la busqueda del Anime vía Web.
- Mostrar una parilla con todos los animes disponibles.

## Aclaraciones y Agradecimientos

Por el momento solo se puede visualizar la notificación si se ejecuta el código en su IDLE de preferencia. Pero se está desarrollando para que sea una aplicación para la computadora y a futuro próximo una web.

# **Notas del Desarrollador**

Declaración de responsabilidad, LePravda Group (nosotros en adelante) tenemos conocimiento de los posibles problemas que esto pueda surgir en un futuro al Usuario (usted en adelante) si estos problemas dan como resultado la prohibición temporal o permanente del servicio. Nosotros optaremos a suspender el desarrollo/publicación de este Proyecto. Puesto que el operador de la web la ha diseñado con Usted en mente, su apertura automática mediante un *web scraper*  puede suponer un **incumplimiento de las condiciones de uso**. Estas acciones se vuelven especialmente relevantes cuando se accede a grandes volúmenes de información procedente de varias páginas al mismo tiempo o en sucesión rápida, de un modo en el que una persona nunca sería capaz de interactuar con la página. En ningún momento se está tomando datos sensibles,
sí por algún motivo encontramos una brecha de seguridad o detectanos que se pueda usar datos sensibles se le notificara inmediatamente al operador de la web.

*Este proyecto está bajo desarrollo, cualquier error que se pueda genera puede contactarnos.*

*[Notify.moe](https://notify.moe/)* es una web que nos proporciona un indexado de todos los animes que están en transmisión. Además de indicarnos que episodio ya han sido lanzado. Puede revisar su repositorio en [Github](https://github.com/animenotifier/notify.moe).

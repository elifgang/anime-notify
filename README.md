Changelog v2.0

* Optimización de guardado de animes.

Esto hace referencia al cambio en el guardado de datos, pasando de listas a diccionarios. Además, este cambio fue impulsado por la optimización en el rendimiento y los tiempos de ejecución del código. Con esto, se mantiene un orden, dando como resultado el guardado de anime en el formato anime:link (clave:valor).

* Se eliminó la función get_Posicion, ya que en el actual modelo de uso es irrelevante.

La función *get_Posicion* trabajaba de tal manera que, dependiendo del anime que se quisiera saber, lo buscaría en la lista y daría la posición en la que se encuentra. Como se comentó en el punto anterior, se dejó de utilizar listas, por lo tanto, esta funcionalidad carece de uso.

* Se modificó y simplificó get_AnimeLink y get_Name.

Ahora ~~get_AnimeLink~~ pasa a ser **get_link** y ~~get_Name~~ solo cambia a **get_name**. En funcionalidad, no cambia mucho, solo el proceso, ya que estos solo recibirán el nombre del anime para entregar el nombre o enlace. Estos gestionan la toma de la clave o valor del diccionario. La función **find** es la encargada de recibir el diccionario y el nombre de la búsqueda como tal, y de igual manera verifica que este exista.

* Reestructurada la función get_episode.

Esta función es la encargada de conocer el episodio actual del anime. El cambio significativo fue que ahora, en lugar de hacer un conteo de los episodios, toma directamente el episodio. Anteriormente, lo que hacía era que, en la web (notify.moe), en la sección de episodios, marcaba siempre 12 episodios y a partir de ahí se realizaba el conteo. Sin embargo, debido a que hay animes que tienen dos temporadas (o continuación) incluidas en un solo anime, el conteo siempre era de los 12 últimos episodios, y lo que se devolvía era el conteo. Ahora se mostrará correctamente el episodio actual del anime

* Eliminado search_anime

Esta función ha sido eliminada, ya que no será necesaria. En caso de que se requiera esta funcionalidad, se tendría a la función **find**.

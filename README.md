# Proyecto_Individual1
proyecto individual fase de labs, centrado en generar las transformaciones requeridas desde csv, y disponibilizarlas por medio de fastapi y deta 

                       Descripcion de archivos dentro de repositorio

DF_Servicios.csv: este csv contiene la el dataframe integrando los DF originales y con sus transformaciones disponibles realizada

main.py: este archivo contiene el codigo de que da funcionamiento a a la api y las funciones para la realizacion de las querys, en este archivo tambien esta comentado los pasos que segui para la realizacion de cada query

requirements.txt: este archivo es en el cual estan las librerias que usa la api

transformaciones.py: este archivo contiene todos los pasos que realize para efectuar las transformaciones, cada paso esta descrito con su respectiva anotacion

                       
                              funcionamiento de la api
                          
la api cuenta con 4 funciones que enlisto a continuacion incluyendo descripcion de funcionamiento, link de acceso y un ejemplo de uso 


#Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

https://qchgvu.deta.dev/get_score_count

https://qchgvu.deta.dev/get_score_count/netflix/85/2010


#Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

https://qchgvu.deta.dev/get_word_count

https://qchgvu.deta.dev/get_word_count/netflix/love


#La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

https://qchgvu.deta.dev/get_second_score

https://qchgvu.deta.dev/get_second_score/amazon


#Cantidad de series y películas por rating

https://qchgvu.deta.dev/get_rating_count

https://qchgvu.deta.dev/get_rating_count/18+

en caso de error en la realizacion de la consulta, la api respondera con opciones disponibles para realizar si error



                       pasos que segui para la realizacion de el proyecto

  1 - el primer paso fue el proceso de transformaciones que esta detallado en el archivo transformaciones.py

  2 - para concluir las transformaciones genere llamado DF_Servicios.csv con todas las transformaciones requieridas para poder disponibilizarlo para la api

  3 - el sigiente paso fue generar un ambiente virtual de pyton y la instalacion de las libreria a usar

  4 - en este paso instale y configure fastapi y deta, para esto cree una carpeta llamada fastapideta, en esta esta carpeta se encuentran los archivos requierments.txt en el cua estan las librerias que usa deta y en el archivo main.py  

  5 - en el archivo main-py se encuentran las instrucciones para el deploy y las funciones para realizar las consulta que se me requirieron, tambien estan descritos lo paso que segui dentro de este mismo archivo

  6 - el ultimo paso fue la comprobacion de funcionamiento en este link https://qchgvu.deta.dev 

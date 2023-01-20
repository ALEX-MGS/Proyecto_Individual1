from fastapi import FastAPI
import pandas as pd
import pandasql as ps
app = FastAPI()

#dataframe a utilizar se descarga desde git
df=pd.read_csv("https://raw.githubusercontent.com/ALEX-MGS/Proyecto_Individual1/main/DF_Servicios.csv")

@app.get("/")
def read_root():
    return {"Hello": "Worlds"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

#Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
@app.get("/get_word_count/{plataforma}/{name}")
def get_word_count(plataforma:str,name:str):
    #lista de plataformas disponibles a consulta
    list_serv=["amazon","disney","hulu","netflix"]
    #comprobacion de que se consulto una plataforma disponible 
    if plataforma in list_serv:
        #extraccion de primer letra de plataforma y agregado de simbolo % para su uso en query
        platf_code= plataforma[0]
    else:
        return 'hay un error en la plataforma elegida, prueba con alguna de las siguientes, amazon, disney, hulu, netflix'
    if name == "": 
        return {"No se especifico el keyword a buscar"}
    else:
        respuesta = {"keyword":name,
                    "plataformas":[] 
                    }
        local_data = df[df['id'].str.startswith(platf_code, na=False)]
        local_data = local_data[local_data['title'].str.contains(name, na=False, regex=False)]

        cant = local_data.shape[0]
        if cant > 0:
            return  'en ' + plataforma + ' la palabra ' + name + ' se encuentra en el titulo de ' + str(cant) +' peliculas'

#Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/get_score_count/{platf}/{punt}/{year}")
def get_score_count(platf:str,punt:int,year:int):
    #lista de plataformas disponibles a consulta
    list_serv=["amazon","disney","hulu","netflix"]
    #comprobacion de que se consulto una plataforma disponible 
    if platf in list_serv:
        #extraccion de primer letra de plataforma y agregado de simbolo % para su uso en query
        platf_code= platf[0]+'%'
    else:
        return 'hay un error en la plataforma elegida, prueba con alguna de las siguientes, amazon, disney, hulu, netflix'
    #generacion de query usando sql
    consulta= f"SELECT COUNT(title) FROM df WHERE id LIKE '{platf_code}' AND type == 'movie' AND score > {punt} AND release_year == {year}"
    resultado = ps.sqldf(consulta)
    # if para disernir en caso de haber 0 resultados 
    if not resultado.iloc[0,0]==0:
        return 'En el año ' + str(year) + ' hubieron ' + str(resultado.iloc[0,0]) + ' peliculas en ' + platf + ' con raiting mayor a ' + str(punt)
    else:
        return'no hay peliculas con ese puntaje, en ese año en esa plataforma'

#La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
@app.get("/get_second_score/{platf}")
def get_second_score(platf:str):
    #lista de plataformas disponibles a consulta
    list_serv=["amazon","disney","hulu","netflix"]
    #comprobacion de que se consulto una plataforma disponible 
    if platf in list_serv:
        platf_code= platf[0]
    else:
        return 'hay un error en la plataforma elegida, prueba con alguna de las siguientes, amazon, disney, hulu, netflix'
    #filtrado de pelicula
    filter_peli = df[df['type'].str.startswith('mov', na=False)]
    #filtrado por plataforma usando el codigo 
    filter_platf = filter_peli[filter_peli['id'].str.startswith(platf_code, na=False)]
    #ordenado por titulo
    sort_title=filter_platf.sort_values(by=['title'],ascending=False)
    #ordenado por score
    sort_score=sort_title.sort_values(by=['score'],ascending=False)
    #seleccion de segundo lugar en titulo y score
    a=sort_score['title'].iloc[1]
    b=sort_score['score'].iloc[1]
    return str(a)+' '+str(b)


#Cantidad de series y películas por rating
@app.get("/get_rating_count/{rating}")
def get_rating_count(rating:str):
   #filtrado de serie
   filter_serie = df[df['type'].str.startswith('tv show')]
   #lista de ratings disponibles
   ratings=['g', '13+', 'all', '18+', 'r', 'tv-y', 'tv-y7', 'nr', '16+',
       'tv-pg', '7+', 'tv-14', 'tv-nr', 'tv-g', 'pg-13', 'tv-ma', 'pg',
       'nc-17', 'unrated', '16', 'ages_16_', 'ages_18_', 'all_ages',
       'not_rate', 'tv-y7-fv', 'not rated']

   #comprobacion de que se consulto una raiting valido
   if rating in ratings:
      filter_rating = filter_serie[filter_serie['rating'].str.contains(rating)]
      lista_ratings=filter_rating['rating']
      return str(len(lista_ratings))
   else:
      return 'el rating que se consulto no esta disponible o hay algun error en la escritura, esta es la lista de los ratings validos g, 13+, all, 18+, r, tv-y, tv-y7, nr, 16+,tv-pg, 7+, tv-14, tv-nr, tv-g, pg-13, tv-ma, pg, nc-17, unrated, 16, ages_16_, ages_18_, all_ages, not_rate, tv-y7-fv, not rated'

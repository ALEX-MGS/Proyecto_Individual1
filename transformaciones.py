import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#cree una funcion para generar el id con la clave de servicio
def id_generator(data):
    #extraigo el nombre de el data set como string
    name =[x for x in globals() if globals()[x] is data][0]
    #genere una nueva columna llena con la inicial de el servicio
    data['clas']= name[0]
    #sume la columna con la clave de la plataforma y el id en una nueva columna llamada id
    id=data['clas'] + data['show_id']
    #insertol a nueva columna id en la  primer columna dentro de el dataframe 
    data.insert(0,'id',id)
    #elimino la columna creada para la inicial de el servicio
    data=data.drop(columns=['clas'])

    
    return data
#carge los csv de cada servicio en variables en pandas
amz= pd.read_csv(r"Datasets\amazon_prime_titles-score.csv")
dis= pd.read_csv(r"Datasets\disney_plus_titles-score.csv")
hul= pd.read_csv(r"Datasets\hulu_titles-score (2).csv")
netf= pd.read_csv(r"Datasets\netflix_titles-score.csv")

# lista de data frames
list_serv=[amz,dis,hul,netf]
#iteracion por lista de dataframes para hacer transformaciones
for ite in list_serv:
        #remplazo e valores nan en rating por 'G'
        ite['rating']=ite["rating"].fillna('G')
        #ejecucion de funcion para crear ids
        id_generator(ite)
        #cambio de formato a fechas
        ite['date_added']=pd.to_datetime(ite['date_added'])
        ite = ite.apply(lambda x: x.str.lower() if x.dtype=='object' else x)
#unificar los data frame de las diferentes servicios en un solo df
df_servicios=pd.concat([amz,dis,hul,netf])
#convertir todas las palabras a lowercase
df_servicios['duration'].replace('nan',np.NaN)
df_servicios = df_servicios.apply(lambda x: x.str.lower() if x.dtype=='object' else x)
#resete los index por que estaban repetidos
df_servicios.reset_index(inplace= True)
df_servicios.drop(columns='index',inplace=True)
#remplace los nan por 0 en la columna duration para pooder dar tipo de dato correcto a columna
df_servicios['duration'].fillna(0,inplace=True)
df_servicios['duration'].value_counts(dropna=False)
#generar dos columnas a partir de columna duration
df_servicios[['duration_int', 'duration_type']] = df_servicios["duration"].apply(lambda x: pd.Series(str(x).split(" ")))
#modificasion en tipo de dato a int en columna duration_int
df_servicios['duration_int'] = df_servicios['duration_int'].astype(int)
#exportar el dataframe a un csv
df_servicios.to_csv(r'C:\Users\aleja\Documents\Documentos alx\cursos y educasion, libros escuela\data henry\data 06\PI01-Data-Engineering-main\PI01-Data-Engineering-main\DF_Servicios.csv')

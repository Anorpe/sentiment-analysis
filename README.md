# sentiment-analysis

Prueba de concepto sobre solución end-to-end de un modelo de análisis de comentarios de una aplicación móvil de Play Store.

## Models Dev

Este notebook contiene el proceso de desarrollo de los modelos con sus respectivas fases de Adquisición de datos, Preprocesamiento de datos y Entrenamiento de los modelos utilizando AutoKeras. Los modelos resultantes son:

Clasificador de connotación positiva de comentarios : Este modelo devuelve la probabilidad de que un comentario tenga una connotación positiva.
Predictor de score de comentarios : Este modelo predice la cantidad de estrellas (en un rango de 1-5) de un comentario. 

## models

Esta carpeta contiene los modelos guardados.

## main.py

Este script contiene la publicación como API del modelo.

## Dockerfile

Contiene información sobre el contenedor Docker.

## Requirements

Contiene los paquetes necesarios y sus versiones.


# API

el modelo esta desplegado como API en Heroku con el siguiente endopoint https://anorpe-sentiment-analysis.herokuapp.com/

esta API tiene dos metodos :

- Acceder a los comentarios de la aplicación : Mediante una petición GET y definiendo un parámetro n igual a la cantidad de lo últimos comentarios que retornara la API :

GET : https://anorpe-sentiment-analysis.herokuapp.com/?n=1

RESPONSE : "{\"reviewId\":{\"349\":\"gp:AOqpTOHbA4AN-9lBzFkm4ST6KMplhGRYfLesa6V2uHztTC1fL9gkW90ISWgIGwzFC8Sav3Hry3dGeQqhsOTfqJ8\"},\"userName\":{\"349\":\"Andr\és Bot\ía\"},\"userImage\":{\"349\":\"https:\/\/play-lh.googleusercontent.com\/a-\/AOh14GjCpNwFuXUwBCdz2Zm6KaaSogZfD7GHDdXzEExV\"},\"content\":{\"349\":\"Error de protocolos de comunicacion, no se puede entrar ni por la pagina web.\"},\"score\":{\"349\":1},\"thumbsUpCount\":{\"349\":0},\"reviewCreatedVersion\":{\"349\":\"11.2.0\"},\"at\":{\"349\":1622798018000},\"replyContent\":{\"349\":\"\¡Hola Andr\és! Nos encargamos de solucionar la novedad que presentabas, por favor ingresa nuevamente a la App para que disfrutes de todo lo que tenemos para ti, cualquier duda que tengas escr\íbenos en la opci\ón de \\\"Chatea con nosotros\\\" y con gusto te ayudamos.\"},\"repliedAt\":{\"349\":1623264388000},\"positiveComment\":{\"349\":0}}"


- Acceder a los resultados de los modelos: Mediante una petición POST y definiendo un JSON para el envio vamos a poder clasificar y predecir con los modelos desarrollados.

POST : https://anorpe-sentiment-analysis.herokuapp.com/ , 
BODY JSON : {
    "content" : ["Excelente hasta el momento el servicio","Cuando inicia pide permisos de administrador"]
}


RESPONSE : {
    "content": [
        "Excelente hasta el momento el servicio",
        "Cuando inicia pide permisos de administrador"
    ],
    "positiveComment": [
        0.4534933269023895,
        0.2469242662191391
    ],
    "score": [
        3.519031524658203,
        3.540288209915161
    ]
}

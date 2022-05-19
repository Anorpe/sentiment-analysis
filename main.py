from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import get_file 
from tensorflow.keras.utils import load_img 
from tensorflow.keras.utils import img_to_array
from tensorflow import expand_dims
from tensorflow.nn import softmax
from numpy import argmax
from numpy import max
from numpy import array
from json import dumps
from uvicorn import run
import os

from google_play_scraper import Sort, reviews_all
import pandas as pd
import numpy as np
import autokeras as ak
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)


clf = load_model("models/classifier")
rgs = load_model("models/regressor")




@app.get("/")
async def root(n: int = 1):
    us_reviews = reviews_all(
    'com.clarocolombia.miclaro',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
    )
    df = pd.DataFrame(np.array(us_reviews),columns=['review'])
    df = df.join(pd.DataFrame(df.pop('review').tolist()))
    df = df.sample(n)

    def get_positive_comment(row):
        return 1 if(row>3) else 0
    
    df['positiveComment'] = df['score'].apply(get_positive_comment)

    return df.to_json(orient = 'columns')

class PostRequest(BaseModel):
    content: list


@app.post("/")
async def get_prediction(inputs: PostRequest):#n_gens: int = 1):

    clf_predictions = clf.predict(np.array(inputs.content)).reshape(-1).tolist()
    rgs_predictions = rgs.predict(np.array(inputs.content)).reshape(-1).tolist()


    #return {"respuesta":"correcta"}

    return {
        "content": inputs.content,
        "positiveComment": clf_predictions,
        "score": rgs_predictions
    }


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    run(app, host="0.0.0.0", port=port)
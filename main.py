import pickle
import pandas as pd
from fastapi import FastAPI

# Load saved files
movies = pickle.load(open("movies.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

app = FastAPI(title="🎬 Movie Recommendation API")


@app.get("/")
def home():
    return {"message": "API is running"}


@app.get("/recommend/{movie}")
def recommend(movie: str):

    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        recommendations = []
        for i in movies_list:
            recommendations.append(movies.iloc[i[0]].title)

        return {"recommendations": recommendations}

    except:
        return {"error": "Movie not found"}
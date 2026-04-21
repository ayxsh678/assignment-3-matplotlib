import streamlit as st
import pickle

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

st.title("🎬 Movie Recommender")

selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button("Recommend"):
    results = recommend(selected_movie)
    for movie in results:
        st.write(movie)

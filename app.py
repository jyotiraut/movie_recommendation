import pandas as pd
import streamlit as st
import pickle
import requests

# Fetch movie poster using TMDb API
def fetch_movie_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=4478e512d14f301d8a85be5eead78e53&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Fetch movie details using TMDb API
def fetch_movie_details(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=4478e512d14f301d8a85be5eead78e53&language=en-US".format(movie_id))
    data = response.json()
    details = {
        'title': data['title'],
        'overview': data['overview'],
        'release_date': data['release_date'],
        'runtime': data['runtime'],
        'genres': [genre['name'] for genre in data['genres']],
        'poster_path': "https://image.tmdb.org/t/p/w500/" + data['poster_path'],
        'cast': [],
        'director': ''
    }

    # Fetch cast details
    cast_response = requests.get("https://api.themoviedb.org/3/movie/{}/credits?api_key=4478e512d14f301d8a85be5eead78e53&language=en-US".format(movie_id))
    cast_data = cast_response.json()
    for cast_member in cast_data['cast'][:5]:  # Get top 5 cast members
        details['cast'].append(cast_member['name'])

    for crew_member in cast_data['crew']:
        if crew_member['job'] == 'Director':
            details['director'] = crew_member['name']
            break

    return details

# Define the recommendation function
def recommend(selected_movie):
    movie_index = movies[movies['title'] == selected_movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    recommended_movie_ids = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_movie_poster(movie_id))
        recommended_movie_ids.append(movie_id)

    return recommended_movies, recommended_movies_poster, recommended_movie_ids

# Load the movie dictionary and similarity matrix from pickle files
movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

# Title of the Streamlit app
st.title("Movie Recommender System")

# Create a selectbox with movie titles
selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

# Recommend movies when the button is clicked
if st.button("Recommend"):
    names, posters, movie_ids = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            if st.button(names[i], key=i):
                details = fetch_movie_details(movie_ids[i])
                st.image(details['poster_path'])
                st.subheader(details['title'])
                st.write(f"**Overview:** {details['overview']}")
                st.write(f"**Release Date:** {details['release_date']}")
                st.write(f"**Runtime:** {details['runtime']} minutes")
                st.write(f"**Genres:** {', '.join(details['genres'])}")
                st.write(f"**Director:** {details['director']}")
                st.write(f"**Cast:** {', '.join(details['cast'])}")
            st.image(posters[i], use_column_width=True)

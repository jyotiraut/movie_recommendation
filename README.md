# 🎬 Movie Recommender System

This is a **content-based movie recommender system** built using Python, machine learning (NLP + cosine similarity), and deployed via **Streamlit**. The app suggests movies similar to the one you choose and provides key details like poster, overview, release date, runtime, genres, cast, and director fetched using the TMDb API.

---

## 🚀 Features

- Select any movie from a list and get **5 similar movie recommendations**
- View **posters and detailed info** (overview, cast, director, runtime, etc.) for each recommended movie
- Uses **Natural Language Processing (NLP)** to understand movie content
- Interactive and **user-friendly UI with Streamlit**

---

## 📁 Dataset

Two CSV files from TMDb:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

These are merged and preprocessed to extract:

- Genres  
- Keywords  
- Cast (top 3 actors)  
- Crew (Director)  
- Overview  

---

## 🛠️ How It Works

### Data Preprocessing:

- Extract and clean `genres`, `keywords`, `cast`, `crew`, and `overview`
- Combine all into a single `tags` field
- Apply **Porter stemming** to normalize the text

### Vectorization & Similarity:

- Use `CountVectorizer` with max 5000 features and English stop words
- Compute **cosine similarity** between movie vectors

### Recommendation Logic:

- Based on the selected movie, sort other movies by similarity score
- Return the **top 5 most similar movies**

### Poster & Details Fetching:

- Use **TMDb API** to get posters and movie metadata via REST calls

### Streamlit UI:

- Dropdown to select a movie
- "Recommend" button to fetch similar movies
- Buttons and image cards for each recommendation with full details on click

---

## 🧪 Requirements

Install dependencies using pip:

```bash
pip install pandas numpy scikit-learn nltk streamlit requests

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



### Data Preprocessing:

- Extract and clean `genres`, `keywords`, `cast`, `crew`, and `overview`
- Combine all into a single `tags` field
- Apply **Porter stemming** to normalize the text


## 🧪 Requirements

Install dependencies using pip:

```bash
pip install pandas numpy scikit-learn nltk streamlit requests
```



▶️ Running the App
Step 1: Clone the repository or download the files
```
git clone https://github.com/jyotiraut/movie_recommendation.git
cd recommendation-main
```
Step 2: Add the Dataset
Place `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` in the project folder.  
Download them from [Kaggle - TMDb Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-dataset)


Step 3: Preprocess the Data
Run the preprocessing script to generate movie_dict.pkl and similarity.pkl:

```bash
movie-recommender-system.ipynb
```
This script processes and vectorizes the movie data.

Step 4: Run the App
Launch the Streamlit web app:

```bash

streamlit run app.py
```
Step 5: Use the App
Select a movie

Click Recommend

View recommended movies with posters and details

📸 Results
<img width="592" alt="image" src="https://github.com/user-attachments/assets/9649711c-d4ff-4aed-86bc-3447244939be" />

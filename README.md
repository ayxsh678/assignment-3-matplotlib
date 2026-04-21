# 🎬 Movie Recommender System

A content-based movie recommendation system built using machine learning and natural language processing techniques.
It suggests similar movies based on genres, keywords, cast, and overview using cosine similarity.

---

## 🚀 Live Overview

This project demonstrates how real-world recommendation systems (like Netflix or Amazon) work using content-based filtering.

---

## 🧠 How It Works

1. **Data Collection**
   Uses the TMDB 5000 Movies Dataset.

2. **Data Preprocessing**

   * Extracts important features: genres, keywords, cast, crew, overview
   * Converts JSON-like data into usable format
   * Removes spaces and normalizes text

3. **Feature Engineering**

   * Combines all features into a single "tags" column
   * Applies stemming using NLTK

4. **Vectorization**

   * Converts text into numerical vectors using `CountVectorizer`

5. **Similarity Calculation**

   * Uses **cosine similarity** to measure similarity between movies

6. **Recommendation**

   * Returns top 5 most similar movies

---

## ⚙️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* NLTK
* Streamlit (for UI)

---

## 📊 Example

**Input:**

```id="eg2k3x"
Avatar
```

**Output:**

```id="2hh5u7"
Aliens vs Predator: Requiem
Aliens
Falcon Rising
Independence Day
Titan A.E.
```

---

## 🖥️ Run Locally

### 1. Clone the repository

```bash id="0lm7ey"
git clone https://github.com/ayxsh678/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Install dependencies

```bash id="l3e0k7"
pip install -r requirements.txt
```

### 3. Run the app

```bash id="2f5o3r"
streamlit run app.py
```

---

## 📁 Project Structure

```id="h2s9t8"
movie-recommender-system/
│
├── app.py                # Streamlit UI
├── movie_recommender.ipynb
├── movies.pkl            # processed data
├── similarity.pkl        # similarity matrix
├── requirements.txt
└── README.md
```

---

## ✨ Features

* Recommend movies based on similarity
* Uses cosine similarity for accurate results
* NLP-based text preprocessing
* Clean and modular pipeline
* Simple UI with Streamlit

---

## 🔮 Future Improvements

* Add movie posters using TMDB API
* Improve UI/UX design
* Add search functionality instead of dropdown
* Deploy online for public access

---

## 👨‍💻 Author

**Ayush Verma**

* GitHub: https://github.com/ayxsh678
* LinkedIn: www.linkedin.com/in/ayushverma567



---

## ⭐ If you found this useful

Give this repo a star ⭐ — it helps a lot!

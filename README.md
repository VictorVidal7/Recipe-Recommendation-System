# 🍲 Recipe Recommendation System

Welcome to the Recipe Recommendation System! This project aims to provide users with personalized recipe recommendations based on the ingredients and other details of recipes they like.

## 🌟 Overview

The system uses content-based filtering to suggest recipes similar to those the user has entered. The similarity between recipes is calculated using cosine similarity on the TF-IDF vectors of the recipe ingredients.

## 🛠️ Project Structure

The project is divided into three main scripts:

1. **`load_data.py`**: Loads recipe data from a SQLite database.
2. **`recipe_recommender.py`**: Builds the content-based recommendation model and provides functions to get recommendations.
3. **`app.py`**: Provides a user interface using Streamlit to interact with the recommendation system.

## 🚀 Setup and Installation

Follow these steps to set up your environment and run the project:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/recipe-recommendation-system.git
    cd recipe-recommendation-system
    ```

2. **Create a virtual environment and install dependencies**:
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Create a `requirements.txt` file with the necessary dependencies**:
    ```txt
    pandas
    sqlalchemy
    scikit-learn
    streamlit
    ```

## 📜 Usage
🎉 Running the Project
To run the Streamlit application:
```
streamlit run app.py
```
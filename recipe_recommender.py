import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#import streamlit as st
from load_data import load_recipes

# Load data
df = load_recipes()

# Convert ingredients to a text string
df['ingredients_str'] = df['ingredients'].apply(lambda x: ' '.join(x.split(', ')))

# Vectorization of ingredients
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['ingredients_str'])

# Calculate cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to search for recipes by keyword
def search_recipes(keyword):
    matches = df[df['title'].str.contains(keyword, case=False, na=False)]
    return matches['title'].tolist()


# Function to obtain recommendations
def get_recommendations(title):
    try:
        idx = df[df['title'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        recipe_indices = [i[0] for i in sim_scores]
        return df['title'].iloc[recipe_indices].tolist()
    except IndexError:
        return []

# Example of use
#print(get_recommendations('Red Lentil Soup with Chicken and Turnips'))

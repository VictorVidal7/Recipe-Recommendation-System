import requests
import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import time

# API configuration
API_KEY = '2c57f6ec23fb41fea9402b7e99025545'  # Make sure to replace with your API key.
BASE_URL_SEARCH = 'https://api.spoonacular.com/recipes/complexSearch'
BASE_URL_DETAILS = 'https://api.spoonacular.com/recipes/{id}/information'

# Parameters of the request
search_params = {
    'apiKey': API_KEY,
    'number': 25  # Número de recetas a obtener
}

# Make the request
response = requests.get(BASE_URL_SEARCH, params=search_params)
data = response.json()

# Check the API response
print(f"Total Results: {data.get('totalResults', 'No data')}")
print(f"Results Type: {type(data.get('results', []))}")
print(f"First Result: {data.get('results', [])[0] if data.get('results', []) else 'No results'}")

# Process the search data
recipes = []
recipe_ids = [recipe['id'] for recipe in data.get('results', [])]

# Obtain details of each recipe individually
for recipe_id in recipe_ids:
    details_url = BASE_URL_DETAILS.format(id=recipe_id)
    details_params = {'apiKey': API_KEY}
    details_response = requests.get(details_url, params=details_params)
    recipe_details = details_response.json()
    
    # Verify and process detail data
    if 'extendedIngredients' in recipe_details:
        recipes.append({
            'id': recipe_details.get('id', ''),
            'title': recipe_details.get('title', ''),
            'summary': recipe_details.get('summary', ''),
            'ingredients': ', '.join([ingredient['name'] for ingredient in recipe_details.get('extendedIngredients', [])]),
            'instructions': recipe_details.get('instructions', ''),
            'readyInMinutes': recipe_details.get('readyInMinutes', 0),
            'servings': recipe_details.get('servings', 0)
        })
    
    # Pause to avoid exceeding the API request limit
    time.sleep(1)

# Verify the processed data before converting it to DataFrame
print(f"Recipes Processed: {len(recipes)}")
if recipes:
    print(f"First Processed Recipe: {recipes[0]}")

# Convert the data to a DataFrame of pandas
df = pd.DataFrame(recipes)

# Verify the DataFrame structure
print(df.head())
print(df.dtypes)

# Make sure that the necessary columns are present.
required_columns = ['id', 'title', 'summary', 'ingredients', 'instructions', 'readyInMinutes', 'servings']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print(f"Faltan las siguientes columnas: {missing_columns}")
else:
    # Convert data types if necessary
    df['readyInMinutes'] = df['readyInMinutes'].astype(int)
    df['servings'] = df['servings'].astype(int)

    # Connect to SQLite database
    engine = create_engine('sqlite:///recipes.db')
    df.to_sql('recipes', con=engine, if_exists='replace', index=False)
import pandas as pd
from sqlalchemy import create_engine

def load_recipes():
    # Conectar a la base de datos SQLite
    engine = create_engine('sqlite:///recipes.db')
    # Leer los datos de la base de datos
    df = pd.read_sql('recipes', con=engine)
    return df
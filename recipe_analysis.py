import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sqlalchemy import create_engine
import sqlite3

# Conectar a la base de datos SQLite
engine = create_engine('sqlite:///recipes.db')

# Leer los datos de la base de datos
df = pd.read_sql('recipes', con=engine)

# Distribución de tiempo de preparación
plt.figure(figsize=(10, 6))
sns.histplot(df['readyInMinutes'], bins=20, kde=True)
plt.title('Preparation Time Distribution')
plt.xlabel('Minutes')
plt.ylabel('Number of Recipes')
plt.show()

# Portion distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['servings'], bins=20, kde=True)
plt.title('Portion Distribution')
plt.xlabel('Portions')
plt.ylabel('Number of Recipes')
plt.show()

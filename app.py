import streamlit as st
from recipe_recommender import get_recommendations, search_recipes

# Application title
st.title('Recipe Recommendation System')

# Status of the application to manage the selection of suggested recipes
if 'selected_recipe' not in st.session_state:
    st.session_state['selected_recipe'] = None

# User login
recipe_name = st.text_input('Enter the name of a recipe:', value=st.session_state['selected_recipe'] or "")

# Show recommendations
if recipe_name and not st.session_state['selected_recipe']:
    recommendations = get_recommendations(recipe_name)
    if recommendations:
        st.write(f'Recommendations for **{recipe_name}**:')
        for rec in recommendations:
            st.write(f'- {rec}')
    else:
        st.write("The recipe was not found. Here are some suggestions that might match:")
        suggestions = search_recipes(recipe_name)
        for suggestion in suggestions:
            if st.button(suggestion):
                st.session_state['selected_recipe'] = suggestion
                st.experimental_rerun()
elif st.session_state['selected_recipe']:
    recipe_name = st.session_state['selected_recipe']
    recommendations = get_recommendations(recipe_name)
    st.write(f'Recommendations for **{recipe_name}**:')
    for rec in recommendations:
        st.write(f'- {rec}')
    st.session_state['selected_recipe'] = None  # Resetting the selected recipe after displaying the recommendations

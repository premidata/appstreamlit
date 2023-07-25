import streamlit as st



st.title("Application Multi-pages avec Streamlit")
st.sidebar.title("Navigation")
pages = ["Accueil", "Scatter Plot"]
choice = st.sidebar.selectbox("Sélectionnez une page", pages)

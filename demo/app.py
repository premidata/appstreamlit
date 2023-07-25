import streamlit as st
import pandas as pd
import plotly.express as px
import os
import random
from PIL import Image
import numpy as np
from io import BytesIO


liste_films = os.listdir()
l = []
for n in liste_films:
    if n.endswith('.jpg'):
        l.append(n.replace('.jpg',''))



pages = ["Présentation du Projet","Plotly Express","Bande Annonce","Quizz Affiche","Quizz Musical","Les petits prezis de Philou","Maxi Poster","Lilian nous explique le principe des startups"]
choice = st.sidebar.radio("Sélectionnez une page", pages)

if choice == "Présentation du Projet":
    st.title('Projet Cinéma')
    st.markdown("Bienvenue dans notre passionnant projet de données dédié au monde du cinéma ! 🎬")
    st.markdown("Plongez dans l'univers magique du 7ème art à travers notre exploration de données cinématographiques. Notre équipe s'est lancée dans cette aventure afin de vous offrir une expérience immersive au sein de l'industrie cinématographique. Grâce à notre analyse approfondie de vastes bases de données cinématographiques, nous avons rassemblé des informations fascinantes sur des milliers de films, acteurs, réalisateurs, genres et bien plus encore. Découvrez les tendances cinématographiques qui ont marqué différentes époques, explorez les chefs-d'œuvre intemporels et suivez l'évolution du cinéma à travers le temps.")
    st.markdown("Nous avons créé des visualisations interactives et des graphiques éclairants pour rendre les données cinématographiques accessibles à tous. Que vous soyez un cinéphile chevronné ou simplement curieux de découvrir le monde du cinéma, notre projet vous propose une expérience enrichissante.")
    st.markdown("Alors, asseyez-vous confortablement, préparez le pop-corn et embarquez avec nous dans ce voyage fascinant à travers les données cinématographiques ! 🍿🎥")

elif choice == "Plotly Express":
    df = pd.read_csv('projet/test2.csv')
    st.title('Plotly Express')
    st.subheader('Correlation Budget/BoxOffice')
    fig = px.scatter(data_frame=df,x='logBudget',y='logBoxOffice',hover_name='movie_name',color='genre')
    st.plotly_chart(fig)
    movie_weekly_dvd =  pd.read_csv('projet/movie_weekly_dvd.csv')
    movie_weekly_bluray = pd.read_csv('projet/movie_weekly_bluray.csv',sep=';')
    st.subheader('Line Chart DVD')
    fig2 = px.line(data_frame=movie_weekly_dvd,x='chart_date',y='total_units',color='display_name')
    st.plotly_chart(fig2)
    st.subheader('Line Chart bluray')
    fig3 = px.line(data_frame=movie_weekly_bluray,x='chart_date',y='total_units',color='display_name')
    st.plotly_chart(fig3)

elif choice == "Choisis ton poster":
    st.title('Choisis ton poster !')
    img = st.selectbox("Poster", l)
    st.image(f'{img}.jpg')
    st.download_button('Telecharge le !',f'{img}.jpg')
   


elif choice == "Maxi Poster":
    st.title('Commande ton Maxi Poster !')
    st.image('Poster affiches3.jpg')
    quantite = st.number_input('Quantité',1,10)
    Prix = st.metric('Prix',round((quantite*19.99),2))
    promo = st.text_input('Code Promo')
    if promo == 'LPC':
        Prix_Final = st.metric('Prix Final',0)
    else:
        Prix_Final = st.metric('Prix',round((quantite*19.99),2))
    selected = st.checkbox("J'accepte que mes données soient utilisés à des fins malveillantes")
    
    if st.button('commande'):
        if selected:
            st.download_button('Telecharge le !','Poster affiches3.jpg')



elif choice == "Bande Annonce":
    st.title('Les sorties du moment !')
    st.subheader('Barbie')
    st.video('https://www.youtube.com/watch?v=2oOzWcbVf1c')
    st.subheader('Oppenheimer')
    st.video('https://www.youtube.com/watch?v=CoXtvSRpHgM')
    st.subheader('Mission Impossible')
    st.video('https://www.youtube.com/watch?v=AzRdtaXA3VM')
    

elif choice == 'Quizz Affiche':

    st.title('Quizz Affiche')
    if 'stage' not in st.session_state:
        st.session_state.stage = 0


    def get_id():
        return np.random.randint(0,49)
      
    def set_state(i):
        st.session_state.stage = i

# "Jouer"
    if st.session_state.stage == 0:
        st.button('Jouer', on_click=set_state, args=[1])

# Drapeau + "Réponse"
    if st.session_state.stage == 1:
        st.session_state.id = get_id()
        st.image(f'{l[st.session_state.id]}.jpg',width=400)
        st.button('Réponse', on_click=set_state, args=[2])

    # Drapeau + Réponse + "Rejouer"
    if st.session_state.stage == 2:
        st.image(f'{l[st.session_state.id]}.jpg',width=400)
        st.subheader(l[st.session_state.id])
        st.button('Rejouer', on_click=set_state, args=[1])

    ##########################################
elif choice == "Quizz Musical":

    st.title('Quizz Musique')

    if 'stage' not in st.session_state:
        st.session_state.stage = 0


    def get_id():
        return np.random.randint(0,49)
      
    def set_state(i):
        st.session_state.stage = i

# "Jouer"
    if st.session_state.stage == 0:
        st.button('Jouer', on_click=set_state, args=[1])

# Drapeau + "Réponse"
    if st.session_state.stage == 1:
        st.session_state.id = get_id()
        st.audio(f"{l[st.session_state.id]}.mp3")
        st.button('Réponse', on_click=set_state, args=[2])

    # Drapeau + Réponse + "Rejouer"
    if st.session_state.stage == 2:
        st.audio(f"{l[st.session_state.id]}.mp3")
        st.image(f"{l[st.session_state.id]}.jpg",width=400)
        st.header(l[st.session_state.id])
        st.button('Rejouer', on_click=set_state, args=[1])



elif choice == "Les petits prezis de Philou":
    st.title("Prezi presentation")
    st.subheader('Prezi Matrix')
    st.markdown("""<iframe src="https://prezi.com/p/embed/JGCBcZ8glHdl4R9ioAS7/" id="iframe_container" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="" allow="autoplay; fullscreen" height="472" width="840"></iframe>""", unsafe_allow_html=True)
    st.subheader('Prezi Indiana Jones')
    st.markdown("""<iframe src="https://prezi.com/p/embed/1IlD9EmVIkwdfpBUmaO4/" id="iframe_container" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="" allow="autoplay; fullscreen" height="472" width="840"></iframe>""",unsafe_allow_html=True)
    st.markdown("Si vous en voulez plus suivez l'ami Philor sur Linkdin  https://www.linkedin.com/in/philippe-loranchet/")


elif choice == "Lilian nous explique le principe des startups":
    st.title("Lilian nous explique le principe des startups")
    st.video('https://www.youtube.com/watch?v=cnNL4blAy6A')
        
        
        
        
        
        
        
        
    
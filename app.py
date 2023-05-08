from pathlib import Path
import streamlit as st
from PIL import Image

# 
# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file_fr = current_dir / "assets" / "CV_fr_mbengue.pdf"
resume_file_eng = current_dir / "assets" / "CV_eng_mbengue.pdf"
profile_pic = current_dir / "assets" / "photo_ous_circle.png"
tristar_vid= current_dir / "assets" / "video_tristar.mp4"
video_tristar_file = open(tristar_vid, 'rb')
video_tristar_bytes = video_tristar_file.read()

ufc_vid= current_dir / "assets" / "video_ufc_comparison.mp4"
video_ufc_file = open(ufc_vid, 'rb')
video_ufc_bytes = video_ufc_file.read()

ballon_or_vid= current_dir / "assets" / "video_ballon_or.mp4"
video_ballon_or_file = open(ballon_or_vid, 'rb')
video_ballon_or_bytes = video_ballon_or_file.read()

e_h_vid= current_dir / "assets" / "endress_hausser.mp4"
video_ballon_or_file = open(ballon_or_vid, 'rb')
video_ballon_or_bytes = video_ballon_or_file.read()

# --- GENERAL SETTINGS ---
st.set_page_config(page_title="Digital CV | Benjamin-Ousmane M'Bengue", page_icon= "📃", layout="centered")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)
 
# download pdf
with open(resume_file_fr, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    
st.download_button(
        label=" 📄 Télécharger le CV",
        data=PDFbyte,
        file_name=resume_file_fr.name,
        mime="application/octet-stream",
    ) 
 
col_name, col_pic = st.columns([5,2], gap="small")
with col_name:
    st.title("Benjamin-Ousmane M'Bengue")
    st.subheader("**Ingénieur Logiciel _(Data Science & IA)_**")

    # --- Médias ---
    # st.subheader("Médias")
    st.write("📫", "benjamin-ousmane.mbengue@hotmail.com")
    st.markdown("""
    <a href="https://github.com/Benjamin-Ousmane" style="padding: 0; display: block;">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" 
            height="20" 
            alt="GitHub"
            style="border-radius: 10px; float: left; margin-right: 10px;">
        <p style="float: left; margin-top: 0;">https://github.com/Benjamin-Ousmane</p>
        <div style="clear: both;"></div>
    </a>

    <a href="https://www.linkedin.com/in/benjamin-ousmane-m-bengue-61a8a8205/" style="padding: 0; display: flex;">
        <img src="https://cdn4.iconfinder.com/data/icons/social-messaging-ui-color-shapes-2-free/128/social-linkedin-square2-512.png" 
            height="20" 
            alt="LinkedIn"
            style="border-radius: 10px; float: left; margin-right: 10px;">
        <p style="float: left; margin-top: 0;">https://www.linkedin.com/in/benjamin-ousmane-m-bengue-61a8a8205</p>
        <div style="clear: both;"></div>
    </a>
    """, unsafe_allow_html=True)
    
with col_pic:
    st.text("")
    st.text("")
    st.image(profile_pic, width=230)

# --- Résumé ---
# st.write("---")
st.subheader("Résumé")
st.markdown("""
            <div style="text-align: justify;">
                Jeune ingénieur logiciel diplômé de Polytechnique Montréal (Québec, Canada), 
                je reviens m'installer en France pour débuter ma carrière professionnelle. 
                De par ma formation, je possède des connaissances approfondies en <b>data science</b> notamment en <b>visualisation de données</b> et <b>machine learning</b>, ainsi qu'en <b>développement d'applications web</b>.
                Discipliné et réfléchi, je suis à la recherche d'une expérience professionnelle en tant que <b>data scientist</b> ou <b>web developer</b>.   
            </div>
            """, unsafe_allow_html=True)

st.write("")
st.write("---")
    
# col1, col2 = st.columns([4,5], gap="large")

# with col2:
# --- HISTORIQUE PROFESSIONNEL ---
st.subheader("Expériences professionnelles")

# --- POSTE 1
st.write(":red[**🚧 Junior Data Scientist | Endress+Hauser, Polytechnique Montréal** _(Septembre 2022 - Décembre 2022)_]")
st.write("Endress+Hauser est une société produisant des instruments de mesure et d'automatisation pour les processus industriels")
st.write("**Conception d'un système d'alerte précoce pour l'IIoT avec IA** (équipe de six, méthode agile)")
st.write("- ► Débruitage du signal de capteurs de température, identification et suppression des valeurs singulières, détection de clusters au sein des données")
st.write("- ► Tests et comparaisons de différents modèles d'apprentissage automatique (RNN, LSTM, N-BEATS) afin de prévoir la durée de vie des capteurs (prévision de séries temporelles)")
st.write("- ► Création d'un tableau de bord avec Streamlit pour visualiser les étapes du prétraitement des données et des prédictions")

st.write('\n')
st.write("🚧", ":red[**Junior Data Scientist | Goldspot Discoveries** _(Septembre 2021 - Décembre 2021)_]")
st.write("Goldspot Discoveries est une startup mêlant intelligence artificielle et géoscience")
st.write("- ► Développement d'outils de visualisation pour des jeux de données provenant de forages (estimation des ressources minérales)")
st.write("- ► Développement d'une application web permettant l'analyse d'images satellites en utilisant des ratios de bandes spectrales (télédétection)")

# --- Projects ---
st.write("---")
st.subheader("Projets")

# --- Projet --- 
st.write(":red[**🏆 Comparateur de combattants à l'UFC** _(Hiver 2023, 15 heures de travail)_]")
st.write("**Description** : _Application web pour comparer les statistiques des combattants à l'UFC_")
st.write("**Outils utilisés** : _Streamlit, Altair_")
st.write("📺 [Démo : https://benjamin-ousmane-ufc-app-app-l8bv5i.streamlit.app/](https://benjamin-ousmane-ufc-app-app-l8bv5i.streamlit.app/)")
st.video(video_ufc_bytes)
# --- Projet --- 


# --- Projet --- 
st.write('\n')
st.write(":red[**🏆 Application Tristar Gym** _(Automne 2022, 30 heures de travail)_]")
st.write("**Description** : _Application web permettant aux membres du Tristar Gym de suivre leur progression et de revoir les techniques montrées durant les cours_")
st.write("**Outils utilisés** : _NextJS, React, Firebase_")
st.write("**Superviseur** : _hamza.lakrati@outlook.com_")
st.write("📺 Démo :")
st.video(video_tristar_bytes)

# --- Projet --- 
st.write('\n')
st.write(":red[**🏆 Qui mérite le Ballon d'Or 2022 ? | Sports AI, Polytechnique Montréal** _(Été 2022, 25 heures de travail)_]")
st.write("**Description** : _Comparaison des performances de joueurs de football (Mbappé, Benzema, Mané)_")
st.write("- ► Conception de maquettes")
st.write("- ► Nettoyage et analyse des données des joueurs")
st.write("- ► Implémentation de graphiques interactifs")
st.write("**Outils utilisés** : _Figma, D3, React_")
st.write("📺 Démo :")
st.video(video_ballon_or_bytes)


# with col1:
# --- Compétences ---
st.write("---")
st.subheader("Compétences")
st.write("💻 **Programmation** ")
st.write("- _Python, Typescript, Javascript, SQL, HTML, CSS_")
st.write("📱 **Développement d'applications** ")
st.write("- _Streamlit, React, Angular, Firebase_")
st.write("🤖 **Science de données et IA** ")
st.write("- _Pandas, Scikit-learn, TensorFlow, Hugging Face_")
st.write("📊 **Visualisation de données** ")
st.write("- _D3, Altair, Matplotlib_")

# --- FORMATION ---
st.write("---")
st.subheader("Formation")
st.write("👨‍🎓", "**Polytechnique Montréal, Canada, QC** _(Janvier 2018 - Mai 2023)_")
st.write("Diplôme en génie logiciel (science des données et intelligence artificielle)")
st.write("- _Traitement automatique de la langue naturelle, visualisation de données, fouille de données, méthodes probabilistiques et statistiques pour IA, machine learning, deep learning_")

st.text("")
st.write("👨‍🎓", "**Lycée Joseph-Marie Carriat, France, 01** _(Septembre 2014 - Juillet 2017)_ ")
st.write("Diplôme du baccalauréat scientifique (sciences de l'ingénieur)")


# --- Expérience sportive ---
st.write("---")
st.subheader("Expériences sportives")
st.write("🥋 Grappling - _Tristar Gym Montréal_")
st.write("⚽ Football - _5 ans au Football Bourg-en-Bresse Péronnas 01_")
st.write("🙋‍♂️ Arbitre de football - _Ligues du Centre d’éducation physique et des sports de l’Université de Montréal_ ")
st.write("📚 Documentation personnelle - _Podcasts, livres et articles scientifiques sur le sport et la préparation physique_") 
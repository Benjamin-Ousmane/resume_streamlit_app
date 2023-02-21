from pathlib import Path
import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file_fr = current_dir / "assets" / "CV_fr_mbengue.pdf"
resume_file_eng = current_dir / "assets" / "CV_eng_mbengue.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
tristar_vid= current_dir / "assets" / "video_tristar.mp4"
video_tristar_file = open(tristar_vid, 'rb')
video_tristar_bytes = video_tristar_file.read()

ufc_vid= current_dir / "assets" / "video_ufc_comparison.webm"
video_ufc_file = open(ufc_vid, 'rb')
video_ufc_bytes = video_ufc_file.read()

ballon_or_vid= current_dir / "assets" / "video_ballon_or.mp4"
video_ballon_or_file = open(ballon_or_vid, 'rb')
video_ballon_or_bytes = video_ballon_or_file.read()

# --- GENERAL SETTINGS ---
st.set_page_config(page_title="Digital CV | Benjamin-Ousmane M'Bengue", page_icon= "📃", layout="centered")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
# with col1:
#     language = st.selectbox('', ['Français', 'English'])
 
language = 'Français'  
### FRANCAIS    
if language == "Français":
    # download pdf
    with open(resume_file_fr, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    with col1:   
        st.download_button(
            label=" 📄 Télécharger le CV",
            data=PDFbyte,
            file_name=resume_file_fr.name,
            mime="application/octet-stream",
        )
        
    st.title("Benjamin-Ousmane M'Bengue")
    st.subheader("**Ingénieur Logiciel _(Science des données & IA)_**")
    # --- Médias ---
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

    <a href="https://www.linkedin.com/in/benjamin-ousmane-m-bengue-61a8a8205/" style="padding: 0; display: block;">
        <img src="https://cdn4.iconfinder.com/data/icons/social-messaging-ui-color-shapes-2-free/128/social-linkedin-square2-512.png" 
            height="20" 
            alt="LinkedIn"
            style="border-radius: 10px; float: left; margin-right: 10px;">
        <p style="float: left; margin-top: 0;">https://www.linkedin.com/in/benjamin-ousmane-m-bengue-61a8a8205</p>
        <div style="clear: both;"></div>
    </a>
    """, unsafe_allow_html=True)

    # --- Résumé ---
    st.write("---")
    st.subheader("Résumé")
    st.write(
        """
    - ✔️ Compétences en développement d'applications et en visualisation de données 
    - ✔️ Connaissances en science de données et inteligence artificielle (fouille de données, traitement automatique des langues, prévision de séries temporelles)
    - ✔️ Grand intérêt pour la recherche et l'analyse de données, en particulier dans le domaine du sport et de la performance athlétique 
    """
    )
    
    # --- Compétences ---
    st.write("---")
    st.subheader("Compétences")
    st.write(
        """
    - 💻 **Programmation** : _Python, Typescript, Javascript, HTML, CSS, SQL_
    - 📱 **Développement d'applications** : _Streamlit, React, Angular, Firebase_
    - 🤖 **Science de données et IA** : _Pandas, Scikit-learn, TensorFlow, Hugging Face_
    - 📊 **Visualisation de données** : _D3, Altair, Matplotlib_
    """
    )
    
    # --- FORMATION ---
    st.write("---")
    st.subheader("Formation")
    st.write("👨‍🎓", "**Polytechnique Montréal, Canada, QC** _(Janvier 2018 - Mai 2023)_")
    st.write("Diplôme en génie logiciel (science des données et intelligence artificielle)")
    st.text("")
    st.write("👨‍🎓", "**Lycée Joseph-Marie Carriat, France, 01** _(Septembre 2014 - Juillet 2017)_ ")
    st.write("Diplôme du baccalauréat scientifique (sciences de l'ingénieur)")

    # --- HISTORIQUE PROFESSIONNEL ---
    st.write("---")
    st.subheader("Historique Professionnel")

    # --- POSTE 1
    st.write("🚧", ":red[**Junior Data Scientist | Goldspot Discoveries** _(Septembre 2021 - Décembre 2021)_]")
    st.write("- ► Développement d'outils de visualisation pour les jeux de données de forage (estimation des ressources minérales)")
    st.write("- ► Développement d'une application web permettant l'analyse d'images satellites en utilisant des ratios de bandes spectrales (télédétection)")

    # --- Projects ---
    st.write("---")
    st.subheader("Projets")

    # --- Projet --- 
    st.write(":red[**🏆 Comparateur de combattants à l'UFC** _(Hiver 2023)_]")
    st.write("**Description** : _application web pour comparer les statistiques des combattants à l'UFC_")
    st.write("**Outils utilisés** : _Streamlit, Altair_")
    st.write("📺 [Démo : https://benjamin-ousmane-ufc-app-app-l8bv5i.streamlit.app/](https://benjamin-ousmane-ufc-app-app-l8bv5i.streamlit.app/)")
    st.video(video_ufc_bytes)
    # --- Projet --- 
    st.write('\n')
    st.write(":red[**🏆 Projet final en intelligence artificielle** _(Automne 2022)_]")
    st.write("**Description** : _prédiction de la durée de vie d'un capteur_")
    st.write("- ► **Prétraitement** : débruitage du signal, suppression des valeurs singulières, détection de clusters")
    st.write("- ► **Modélisation** : test et comparaison de différents modèles d'apprentissage automatique pour la prévision de séries temporelles (RNN, LSTM, N-BEATS)")
    st.write("- ► **Visualisation** : création d'un tableau de bord afin de visualiser les étapes du projet")
    st.write("**Outils utilisés** : _Tensorflow, Scikit-learn, Ruptures, Streamlit, Altair_")

    # --- Projet --- 
    st.write('\n')
    st.write(":red[**🏆 Application Tristar Gym** _(Automne 2022)_]")
    st.write("**Description** : _application web permettant aux membres du Tristar Gym de suivre leur progression et de revoir les techniques montrées durant les classes_")
    st.write("**Outils utilisés** : _NextJS, React, Firebase_")
    st.write("**Superviseur** : _hamza.lakrati@outlook.com_")
    st.write("📺 Démo :")
    st.video(video_tristar_bytes)
    
    # --- Projet --- 
    st.write('\n')
    st.write(":red[**🏆 Qui mérite le Ballon d'Or 2022 ?** _(Été 2022)_]")
    st.write("**Description** : _comparaison des performances de joueurs de football (Mbappé, Benzema, Mané)_")
    st.write("**Outils utilisés** : _D3, React_")
    st.write("📺 Démo :")
    st.video(video_ballon_or_bytes)

    # --- Expérience sportive ---
    st.write("---")
    st.subheader("Expériences Sportives")
    st.write("🥋 Grappling - _Tristar Gym Montréal_")
    st.write("⚽ Football - _5 ans au Football Bourg-en-Bresse Péronnas 01_")
    st.write("🙋‍♂️ Arbitre de football - _Ligues du CEPSUM_ ")
    st.write("📚 Documentation personnelle") 
    st.write("- ► Podcasts _(Peter Attia, Andrew Huberman, Mark Bell)_")
    st.write("- ► Livres _(Michael Gundill, Kelly Starrett, Didier Reiss)_")
    st.write("- ► Études de méthodes _(ATG for Coaches, méthode Weck, méthode Ido Portal, etc.)_")



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# if language == "English":
#     # download pdf
#     with open(resume_file_eng, "rb") as pdf_file:
#         PDFbyte = pdf_file.read()
#     with col2:   
#         st.text("")
#         st.text("")
#         st.download_button(
#             label="📄 Download Resume",
#             data=PDFbyte,
#             file_name=resume_file_eng.name,
#             mime="application/octet-stream",
#         )

#     st.title("Benjamin-Ousmane M'Bengue")
#     st.subheader("**_Software Engineer & Data Scientist_**")
    
#     # --- Medias ---
#     st.write("📫", "benjamin-ousmane.mbengue@hotmail.com")
#     st.markdown("""
#     <a href="https://github.com/Benjamin-Ousmane" style="padding: 0; display: block;">
#         <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" 
#             height="20" 
#             alt="GitHub"
#             style="border-radius: 10px; float: left; margin-right: 7px;">
#         <p style="float: left; margin-top: 0;">https://github.com/Benjamin-Ousmane</p>
#         <div style="clear: both;"></div>
#     </a>

#     <a href="https://www.linkedin.com/in/benjamin-ousmane-m-bengue-61a8a8205/" style="padding: 0; display: block;">
#         <img src="https://cdn4.iconfinder.com/data/icons/social-messaging-ui-color-shapes-2-free/128/social-linkedin-square2-512.png" 
#             height="20" 
#             alt="LinkedIn"
#             style="border-radius: 10px; float: left; margin-right: 7px;">
#         <p style="float: left; margin-top: 0;">https://www.linkedin.com/in/benjamin-ousmane-m-bengue-61a8a8205</p>
#         <div style="clear: both;"></div>
#     </a>
#     """, unsafe_allow_html=True)

#     # --- Summary ---
#     st.write('\n')
#     st.write("---")
#     st.subheader("Summary")
#     st.write(
#         """
#     - ✔️ Skills in application development and data visualization
#     - ✔️ Good understanding of data science principles and machine learning models (NLP, data mining, time series forecasting)
#     - ✔️ Knowledge of the software development process and group management (agile methods, git)
#     - ✔️ Strong interest in research and data analysis, particularly in the field of sport and athletic performance
#     """
#     )

#     # --- SKILLS ---
#     st.write('\n')
#     st.write("---")
#     st.subheader("Skills")
#     st.write(
#         """
#     - 💻 **Programming** : _Python, Typescript, Javascript, Html, Css, SQL_
#     - 📱 **App development** : _Streamlit, React, Angular, Firebase_
#     - 🤖 **AI & data science** : _Pandas, Scikit-learn, TensorFlow, Hugging Face_
#     - 📊 **Data visualization** : _D3, Altair, Matplotlib_
#     """
#     )

#     # --- EDUCATION ---
#     st.write('\n')
#     st.write("---")
#     st.subheader("Education")
#     st.write(
#         """
#     - _January 2018 - May 2023_
#     """
#     )
#     st.write("👨‍🎓", "**Polytechnique Montreal (Canada, QC)**")
#     st.write("Bachelor's Degree in Software Engineering (_data science and artificial intelligence_)")
#     st.text("")
#     st.write(
#         """
#     - _September 2014 - July 2017_
#     """
#     )
#     st.write("👨‍🎓", "**Lycée Joseph-Marie Carriat (France, 01)**")
#     st.write("Diploma of the General Scientific Baccalaureate")

#     # --- WORK HISTORY ---
#     st.write('\n')
#     st.write("---")
#     st.subheader("Work History")

#     # --- JOB 1
#     st.write("- _September 2021 - December 2021_")
#     st.write("🚧", "**Junior data scientist | Goldspot Discoveries**")
#     st.write("► Development of visualization tools for drilling data sets (mineral resource estimation)")
#     st.write("► Development of a web application allowing the analysis of satellite images using spectral band ratios (remote sensing)")


#     # --- Projects ---
#     st.write('\n')
#     st.write("---")
#     st.subheader("Projects")

#     # --- Projet 1 --- 
#     st.write("**🏆 Final project in artificial intelligence**")
#     st.write("_Prediction of the lifetime of a sensor_")
#     st.write("- ► **Preprocessing** : denoise signal, remove singular values, detect clusters")
#     st.write("- ► **Modeling** : test and compare different machine learning models for time series forcasting (RNN, LSTM, N-BEATS)")
#     st.write("- ► **Visualizing** : build a dashboard with Streamlit")

#     # --- Projet 2 --- 
#     st.write('\n')
#     st.write("**:red[🏆 Tristar gym app]**")
#     st.write("_Web application for Tristar Gym members build with NextJs, React and Firebase_")
#     st.write("Supervisor : hamza.lakrati@outlook.com ")
#     st.write("📺 Demo :")
#     st.video(video_bytes)

#     # --- Projet 3 --- 
#     st.write('\n')
#     st.write("**🏆 Who deserves 2022 Ballon d'Or ?**")
#     st.write("_Comparing soccer player performances with d3 charts (app build with react)_")
#     st.write("📺 [Demo : https://benjamin-ousmane.github.io/2022-Ballon-Or-Project](https://benjamin-ousmane.github.io/2022-Ballon-Or-Project/)")

#     # --- Sports Experience ---
#     st.write('\n')
#     st.write("---")
#     st.subheader("Sports Experience")
#     st.write("🥋 Grappling - _Tristar Gym Montreal_")
#     st.write("⚽ Football - _5 years at Football Bourg-en-Bresse Péronnas 01_")
#     st.write("🙋‍♂️ Football referee - _CEPSUM leagues_ ")
#     st.write("📚 Personal documentation - _Podcasts (Peter Attia, Andrew Huberman, Mark Bell, Micheal Gundill), methods (ATG for coaches, Weck method), books, scientific papers, etc._ ")
    
    
    

from pathlib import Path
import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file_fr = current_dir / "assets" / "CV_fr_mbengue.pdf"
resume_file_eng = current_dir / "assets" / "CV_eng_mbengue.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
tristar_vid= current_dir / "assets" / "video_tristar.mp4"
video_file = open(tristar_vid, 'rb')
video_bytes = video_file.read()

def get_pdf():
    html = st.get_html_content()
    pdf = pdfkit.from_string(html, False)
    return pdf

# --- GENERAL SETTINGS ---
st.set_page_config(page_title="Digital CV | Benjamin-Ousmane M'Bengue", page_icon= "📃", layout="centered")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    language = st.selectbox('', ['English', 'Français'])

if language == "English":
    # download pdf
    with open(resume_file_eng, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    with col2:   
        st.text("")
        st.text("")
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file_eng.name,
            mime="application/octet-stream",
        )

    st.title("Benjamin-Ousmane M'Bengue")
    st.subheader("**_Software Engineer & Data Scientist_**")
    
    # --- Medias ---
    st.write("📫", "benjamin-ousmane.mbengue@hotmail.com")
    st.markdown("""
    <a href="https://github.com/Benjamin-Ousmane" style="padding: 0; display: block;">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" 
            height="20" 
            alt="GitHub"
            style="border-radius: 10px; float: left; margin-right: 7px;">
        <p style="float: left; margin-top: 0;">https://github.com/Benjamin-Ousmane</p>
        <div style="clear: both;"></div>
    </a>

    <a href="https://www.linkedin.com/in/benjamin-ousmane-m-bengue-61a8a8205/" style="padding: 0; display: block;">
        <img src="https://cdn4.iconfinder.com/data/icons/social-messaging-ui-color-shapes-2-free/128/social-linkedin-square2-512.png" 
            height="20" 
            alt="LinkedIn"
            style="border-radius: 10px; float: left; margin-right: 7px;">
        <p style="float: left; margin-top: 0;">https://www.linkedin.com/in/benjamin-ousmane-m-bengue-61a8a8205</p>
        <div style="clear: both;"></div>
    </a>
    """, unsafe_allow_html=True)

    # --- Summary ---
    st.write('\n')
    st.write("---")
    st.subheader("Summary")
    st.write(
        """
    - ✔️ Skills in application development (streamlit, react, angular)
    - ✔️ Good understanding of data science principles and machine learning models (NLP, data mining, time series forecasting)
    - ✔️ Knowledge of the software development process and group management (agile methods, git)
    - ✔️ Strong interest in research and data analysis, particularly in the field of sport and athletic performance
    """
    )

    # --- SKILLS ---
    st.write('\n')
    st.write("---")
    st.subheader("Skills")
    st.write(
        """
    - 💻 **Programming** : _Python, Typescript, Javascript, Html, Css, SQL_
    - 📱 **App development** : _Streamlit, React, Angular, Firebase_
    - 🤖 **AI & Data science** : _Pandas, Scikit-learn, TensorFlow, Hugging Face_
    - 📊 **Data visualization** : _D3, Altair, Matplotlib_
    """
    )

    # --- EDUCATION ---
    st.write('\n')
    st.write("---")
    st.subheader("Education")
    st.write(
        """
    - _January 2018 - May 2023_
    """
    )
    st.write("👨‍🎓", "**Polytechnique Montreal (Canada, QC)**")
    st.write("Bachelor's Degree in Software Engineering (_data science and artificial intelligence_)")
    st.text("")
    st.write(
        """
    - _September 2014 - July 2017_
    """
    )
    st.write("👨‍🎓", "**Lycée Joseph-Marie Carriat (France, 01)**")
    st.write("Diploma of the General Scientific Baccalaureate")

    # --- WORK HISTORY ---
    st.write('\n')
    st.write("---")
    st.subheader("Work History")

    # --- JOB 1
    st.write("- _September 2021 - December 2021_")
    st.write("🚧", "**Junior Data Scientist | Goldspot Discoveries**")
    st.write("► Development of visualization tools for drilling data sets (mineral resource estimation)")
    st.write("► Development of a web application allowing the analysis of satellite images using spectral band ratios (remote sensing)")


    # --- Projects ---
    st.write('\n')
    st.write("---")
    st.subheader("Projects")

    # --- Projet 1 --- 
    st.write("**🏆 Final project in artificial intelligence**")
    st.write("_Prediction of the lifetime of a sensor_")
    st.write("- ► **Preprocessing** : denoise signal, remove singular values, detect clusters")
    st.write("- ► **Modeling** : test and compare different machine learning models for time series forcasting (RNN, LSTM, N-BEATS)")
    st.write("- ► **Visualizing** : build a dashboard with Streamlit")

    # --- Projet 2 --- 
    st.write('\n')
    st.write("**🏆 Tristar gym app**")
    st.write("_Web application for Tristar Gym members build with NextJs, React and Firebase_")
    st.write("Supervisor : hamza.lakrati@outlook.com ")
    st.write("📺 Demo :")
    st.video(video_bytes)

    # --- Projet 3 --- 
    st.write('\n')
    st.write("**🏆 Who deserves 2022 Ballon d'Or ?**")
    st.write("_Comparing soccer player performances with d3 charts (app build with react)_")
    st.write("📺 [Demo : https://benjamin-ousmane.github.io/2022-Ballon-Or-Project](https://benjamin-ousmane.github.io/2022-Ballon-Or-Project/)")

    # --- Sports Experience ---
    st.write('\n')
    st.write("---")
    st.subheader("Sports Experience")
    st.write("🥋 Grappling - _Tristar Gym Montreal_")
    st.write("⚽ Football - _5 years at Football Bourg-en-Bresse Péronnas 01_")
    st.write("🙋‍♂️ Football referee - _CEPSUM leagues_ ")
    st.write("📚 Personal documentation - _Podcasts (Peter Attia, Andrew Huberman, Mark Bell, Micheal Gundill), methods (ATG for coaches, Weck method), books, scientific papers, etc._ ")
    
    
    
### FRANCAIS    
if language == "Français":
    # download pdf
    with open(resume_file_fr, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    with col2:   
        st.text("")
        st.text("")
        st.download_button(
            label=" 📄 Télécharger le CV",
            data=PDFbyte,
            file_name=resume_file_fr.name,
            mime="application/octet-stream",
        )
        
        
    st.title("Benjamin-Ousmane M'Bengue")
    st.subheader("**_Ingénieur Logiciel & Data Scientist_**")
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
    st.write('\n')
    st.write("---")
    st.subheader("Résumé")
    st.write(
        """
    - ✔️ Compétences en développement d'application (streamlit, react, angular)
    - ✔️ Compréhension des concepts de science de données et des modèles d'apprentissage automatique (NLP, data mining, prévision de séries temporelles)
    - ✔️ Connaissance du processus de développement logiciel et de la gestion de groupe (méthodes agiles, git)
    - ✔️ Grand intérêt pour la recherche et l'analyse de données, en particulier dans le domaine du sport et de la performance athlétique 
    """
    )
    
    # --- Compétences ---
    st.write('\n')
    st.write("---")
    st.subheader("Compétences")
    st.write(
        """
    - **Programmation** : _Python, Typescript, Html/Css, SQL, Java_
    - **Développement d'applications** : _Streamlit, React, Angular, Firebase_
    - **Science de données** : _Pandas, Scikit-learn, TensorFlow, Hugging Face_
    - **Visualisation de données** : _D3, Altair, Matplotlib_
    """
    )

    # --- FORMATION ---
    st.write('\n')
    st.write("---")
    st.subheader("Formation")
    st.write(
        """
    - _Janvier 2018 - Mai 2023_
    """
    )
    st.write("👨‍🎓", "**Polytechnique Montréal (Canada, QC)**")
    st.write("Diplôme en ingénierie logicielle (_science des données et intelligence artificielle_)")
    st.text("")
    st.write(
        """
    - _Septembre 2014 - Juillet 2017_
    """
    )
    st.write("👨‍🎓", "**Lycée Joseph-Marie Carriat (France, 01)**")
    st.write("Diplôme du Bac scientifique général")

    # --- HISTORIQUE PROFESSIONNEL ---
    st.write('\n')
    st.write("---")
    st.subheader("Historique professionnel")

    # --- POSTE 1
    st.write("- _Septembre 2021 - Décembre 2021_")
    st.write("🚧", "**Junior Data Scientist | Goldspot Discoveries**")
    st.write("► Développement d'outils de visualisation pour les jeux de données de forage (estimation des ressources minérales)")
    st.write("► Développement d'une application web permettant l'analyse d'images satellites en utilisant des ratios de bandes spectrales (télédétection)")

    # --- Projects ---
    st.write('\n')
    st.write("---")
    st.subheader("Projets")

    # --- Projet 1 --- 
    st.write("**🏆 Projet final en intelligence artificielle**")
    st.write("_Prédiction de la durée de vie d'un capteur_")
    st.write("- ► **Prétraitement** : débruitage du signal, suppression des valeurs singulières, détection de clusters")
    st.write("- ► **Modélisation** : test et comparaison de différents modèles d'apprentissage automatique pour la prévision des séries chronologiques (RNN, LSTM, N-BEATS)")
    st.write("- ► **Visualisation** : création d'un tableau de bord avec Streamlit pour afficher nos résultats")

    # --- Projet 2 --- 
    st.write('\n')
    st.write("**🏆 Application Tristar Gym**")
    st.write("_Application web pour les membres du Tristar Gym, construite avec NextJS, React et Firebase_")
    st.write("Superviseur : hamza.lakrati@outlook.com ")
    st.write("📺 Démo :")
    st.video(video_bytes)
    
    # --- Projet 3 --- 
    st.write('\n')
    st.write("**🏆 Qui mérite le Ballon d'Or 2022 ?**")
    st.write("_Comparaison des performances de joueurs de football avec des graphiques d3 (application construite avec React)_")
    st.write("📺 [Démo : https://benjamin-ousmane.github.io/2022-Ballon-Or-Project](https://benjamin-ousmane.github.io/2022-Ballon-Or-Project/)")
    st.write("💻 [Code : https://github.com/Benjamin-Ousmane/2022-Ballon-Or-Project](https://github.com/Benjamin-Ousmane/2022-Ballon-Or-Project)")

    # --- Expérience sportive ---
    st.write('\n')
    st.write("---")
    st.subheader("Expérience sportive")
    st.write("🥋 Grappling - _Tristar Gym Montréal_")
    st.write("⚽ Football - _5 ans au Football Bourg-en-Bresse Péronnas 01_")
    st.write("🙋‍♂️ Arbitre de football - _Ligues du CEPSUM_ ")
    st.write("📚 Documentation personnelle - _Podcasts (Peter Attia, Andrew Huberman, Mark Bell), Livres (Michael Gundill, Kelly Starrett, Didier Reiss), Méthodes (ATG for Coaches, méthode Weck)_")






            
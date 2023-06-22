from pathlib import Path
import streamlit as st
from PIL import Image

# 
# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
# resume_file_fr = current_dir / "assets" / "CV_fr_mbengue.pdf"
# resume_file_eng = current_dir / "assets" / "CV_eng_mbengue.pdf"
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
# with open(resume_file_fr, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
    
# st.download_button(
#         label=" 📄 Télécharger le CV",
#         data=PDFbyte,
#         file_name=resume_file_fr.name,
#         mime="application/octet-stream",
#     ) 
 
st.title("Benjamin-Ousmane M'BENGUE")
st.header("**Software Engineer - Data Science & AI**")
st.subheader("**_Polytechnique Montreal_**")

col_name, col_pic = st.columns([5,2], gap="small")
with col_name:

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
    st.image(profile_pic, width=150)


# --- Projects ---
st.write("---")
st.write('\n')

# --- Projet --- 
st.write(":red[**🏆 UFC Fighter Comparator**  \n _(Winter 2023)_]")
st.write("**Description** : _Web application to compare UFC fighters statistics_")
st.write("- ► Scraping data")
st.write("- ► Preprocessing data")
st.write("- ► Implementing interactive graphic")
st.write("**Tools used** : _Streamlit, Altair_")
st.write("📺 [Demo : https://benjamin-ousmane-ufc-app-app-l8bv5i.streamlit.app/](https://benjamin-ousmane-ufc-app-app-l8bv5i.streamlit.app/)")
st.video(video_ufc_bytes)


# --- Projet --- 
st.write("---")
st.write('\n')
st.write(":red[**🏆 Tristar Gym application**  \n _(Fall 2022)_]")
st.write("**Description** : _Web application that allows Tristar Gym members to track their progress and review the techniques demonstrated in class_")
st.write("- ► Implementing modules allowing teachers to create lessons")
st.write("- ► Handling Firebase database")
st.write("**Tools used** : _NextJS, React, Firebase_")
st.write("**Supervisor** : _hamza.lakrati@outlook.com_")
st.write("📺 Demo :")
st.video(video_tristar_bytes)

st.write("---")
# --- Projet --- 
st.write('\n')
st.write('\n')
st.write(":red[**🏆 Who deserves the Ballon d'Or 2022 ? | Sports AI, Polytechnique Montreal**  \n _(Summer 2022)_]")
st.write("**Description** : _Comparing the performance of soccer players (Mbappe, Benzema, Mane)_")
st.write("- ► Designing mock-ups")
st.write("- ► Cleaning and analyzing player data")
st.write("- ► Implementing interactive graphics")
st.write("**Tools used** : _Figma, D3, React_")
st.write("📺 Demo :")
st.video(video_ballon_or_bytes)
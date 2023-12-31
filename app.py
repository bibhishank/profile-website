from pathlib import Path
from PIL import Image
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
        
 

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
local_css = current_dir / "styles" / "style.css"
resume_file = current_dir / "assets" / "bibhishan_resume.pdf"
profile_pic = current_dir / "assets" / "bibhishan-pic.png"
architecture_image = current_dir / "assets" / "001-validate-generative-ai-outputs-especially-for-higher-stakes-cases.png"



lottie_coder = load_lottieurl("https://lottie.host/def90568-8eae-4ed5-8eb5-3970f81d6894/8jPhbSZYhY.json")   
contact_animation = load_lottieurl("https://lottie.host/4ec7f77f-81e9-43ef-8d4b-3de8180aeb0f/eCexr9sDOl.json")
genAI_image = Image.open(architecture_image)

# --- GENERAL SETTINGS ---
PAGE_TITLE = "About | Bibhishan Karadkar"
PAGE_ICON = ":large_green_circle:"    # :wave:"    #:technologist"
NAME = "Bibhishan Karadkar"
DESCRIPTION = """
Experienced software leader adept at driving business results through collaborative leadership, guiding high-performing global teams in lean Agile, DevOps, and Big Data projects for transformative success over 9 years.
"""
EMAIL = "bibhishan_k@yahoo.com"
SOCIAL_MEDIA = {
    #"YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com/in/bibhishan-karadkar-910ba77",
    "GitHub": "https://github.com",
    "Profile": "https://twitter.com",
}


PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout= "wide")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(local_css) as f1:
    st.markdown("<style>{}</style>".format(f1.read()), unsafe_allow_html=True)


with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)


# --- profile SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(":email:", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('---')


with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About' , 'Generative A.I. and Data Projects', 'Contact me'],
        #add these names from https://icons.getbootstrap.com    
        icons = ['person', 'code-slash', 'chat-left-text-fill'], 
        orientation = 'horizontal'
    )
    
if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am him")
            st.title("Technical project manager")
        with col2:
            st_lottie(lottie_coder)
    
    st.write('---')
    
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
            Education
            - Master of Computer Management (MCM) - Savitribai Phule Pune University
            - Diploma in Computer Management (DCM) - Savitribai Phule Pune University
             
                         """)
        with col4:
            st.subheader("""
            Experience
            - Zoom
            - Zensar/Cisco
                         """)
                         

if selected == "Generative A.I. and Data Projects":
    with st.container():
        st.header("My GenetiveAI and Data Projects")
        st.write("##")
        col5, col6 = st.columns((1,2))
        with col5:
            st.image(genAI_image)
        with col6:
            st.subheader("Generative A.I. projects ")
            #st.write("""
            #         
            #         """)
            st.markdown("[Visit Github page](https://github.com/bibhishank)")
            
if selected == "Contact me":
    st.header("Reach out to me")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/bibhishan_k@yahoo.com" method="POST">
     <input type = "hidden" name = "_captcha" value = "false">
     <input type="text" name="name" placeholder= "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
     <textarea name="message" placeholder = "Your Message" required></textarea>
     <button type="submit">Send</button>
     </form>
    """
            
    left_col, right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html= True )
    with right_col:
        st_lottie(contact_animation, height = 100)
        
        

            
            
            
            
        
        
        

















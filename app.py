from pathlib import Path
from PIL import Image
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import google.generativeai as genai


#Google libraries
import pathlib
import textwrap
import google.generativeai as genai

# Used to securely store your API key
#from google.colab import userdata
from IPython.display import display
from IPython.display import Markdown

import PyPDF2
import pandas as pd
import json
import ast
from MCQGenerator import getMCQData 


number_of_pages = 0
text_length_char = 0
text_length_char_txt = 0
all_page_text = ""


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
        
 
def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            global number_of_pages
            number_of_pages = len(pdf_reader.pages)
            if number_of_pages > 5:
                return "MORE_THAN_FIVE_PAGES"
            for page in pdf_reader.pages:
                text+= page.extract_text()
            global text_length_char
            text_length_char = len(text)
            if text_length_char < 500:
                return "LESS_TEXT_IN_TXT"
            if text_length_char > 8000:
                return "MORE_TEXT_IN_TXT"
            return text
        except Exception as e:
            raise Exception ("error reading the PDF file")

    elif file.name.endswith(".txt"):
        text_file_text = file.read().decode("utf-8")
        global text_length_char_txt
        text_length_char_txt =  len(text_file_text) 
        return text_file_text
    else:
        raise Exception(
            "unsupported file format only pdf and text file suppoted")
    

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
local_css = current_dir / "styles" / "style.css"
resume_file = current_dir / "assets" / "bibhishan_resume.pdf"
profile_pic = current_dir / "assets" / "bibhishan-pic.png"
architecture_image = current_dir / "assets" / "001-validate-generative-ai-outputs-especially-for-higher-stakes-cases.png"
zoom_logo = current_dir / "assets" / "zoom-png.png"
zensar_logo = current_dir / "assets" / "zensar-png.png"
cisco_logo = current_dir / "assets" / "cisco-png.png"
scrum_alliance_logo= current_dir / "assets" / "scrum_alliance_logo.png"
aws_logo= current_dir / "assets" / "aws_logo.png"
google_logo= current_dir / "assets" / "google_logo.png"
pune_university_logo= current_dir / "assets" / "pune_university_logo.png"
github_logo = current_dir / "assets" / "github_logo.png"
linkedin_logo = current_dir / "assets" / "linkedIn_logo.png"


lottie_coder = load_lottieurl("https://lottie.host/def90568-8eae-4ed5-8eb5-3970f81d6894/8jPhbSZYhY.json")   
contact_animation = load_lottieurl("https://lottie.host/4ec7f77f-81e9-43ef-8d4b-3de8180aeb0f/eCexr9sDOl.json")
tpm_lottie_animation = load_lottieurl("https://lottie.host/074d4b22-2c7e-4548-af99-45241313a1a3/5KNHB0m4YM.json")
coder1_lottie_animation = load_lottieurl("https://lottie.host/d58de5a6-fd08-4a93-94bf-67449621cf30/N6TwWjSS4C.json")
db_animation = load_lottieurl("https://lottie.host/25b11da3-9595-4625-90a9-ccf6a9f26002/dkRzaoDXqG.json")
tpm_option_1_animation = load_lottieurl("https://lottie.host/a887c6cf-22a8-42f6-82d8-a0b28dc6fb3b/y1LOKdVe9W.json")
tpm_option_2_animation = load_lottieurl("https://lottie.host/5c6784f5-dd06-4837-b697-98c5679874d0/Z4XZZNBeg8.json")


genAI_image = Image.open(architecture_image)

# --- GENERAL SETTINGS ---
PAGE_TITLE = "About | Bibhishan Karadkar"
PAGE_ICON = ":large_green_circle:"    # :wave:"    #:technologist"
NAME = "Bibhishan Karadkar"
ROLE = "Technical Project Manager"
DESCRIPTION = """
Experienced software leader adept at driving business results through collaborative leadership, guiding high-performing global teams in lean Agile, DevOps, and Big Data projects for transformative success over 9 years.
"""
EMAIL = "bibhishan_k@yahoo.com"
SOCIAL_MEDIA = {
    #"YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com/in/bibhishan-karadkar-910ba77",
    "GitHub": "https://github.com/bibhishank/profile-website/tree/main",
    #"Profile": "https://twitter.com",
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
    st.subheader(ROLE)
    st.write(DESCRIPTION)
    row1, row2 = st.columns(2, gap="small")
    with row1:
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",        
            )
    with row2:    
        st.write(":email:", EMAIL)
    
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        #cols[index].write(social_logo_pic)
        cols[index].write( f"[{platform}]({link})")


#st.write('---')
# --- SOCIAL LINKS ---
# st.write('\n')


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
        col01, col02 = st.columns(2)
        with col01:
            st.subheader("PROFESSIONAL EXPERIENCE")

# --- ZOOM experiwnce            
    with st.container(border=True):
        col1, col2 = st.columns([7,3],gap="small")
        with col1:
            with st.container():
                col001, col1002 = st.columns([1,18])
                with col001:
                    zoom_logo_pic = Image.open(zoom_logo)
                    st.image(zoom_logo_pic,width=60)
                with col1002:
                    st.subheader("Zoom Video communication, CA")
                
            #st.write("##")
            #st.image(zoom_logo)
            st.subheader("Technical project manager")
            st.write("""
                     Led cross-functional e-commerce projects, prioritizing revenue initiatives from concept to launch, and secured a rapid promotion within a year for exceptional performance and impactful contributions. Led diverse product growth strategies, incentivizing free users on both mobile and desktop platforms, and collaborated with the data engineering team to ensure thorough data tracking in Snowplow for analysis.
                     """)
        with col2:
            st_lottie(lottie_coder , height=200)
            #st.markdown("<h1 style='text-align: center'>SSep 2021 – PRESENT</h1>", unsafe_allow_html=True)
            st.write("Sep 2021 – PRESENT")

        
        expander = st.expander(" Project Details ")
        
        with expander:
            st.write(" ### :large_green_circle: Free user monetization projects: ### ")
            st.write("  ####  :arrow_right: Introduce forced break between meetings #### ")
            st.write(" - ► Implemented forced breaks between consecutive Zoom meetings to counter users exploiting the 40-minute limit, creating opportunities for monetization among free users.")
            st.write(" - ► Conducted cross-functional meetings with teams in strategy, finance, revenue, legal, and marketing, addressing the impact of changes and exploring strategies for user upgrades, including coupon incentives.")
            st.write(" - ► Led project kick-off meetings involving mobile, desktop, and web engineering, ensuring seamless collaboration and Agile implementation. Worked with the data team to integrate analytics and enhance visibility through Tableau dashboards.")
            st.write(" - ► Spearheaded a revenue-driving project, resulting in a significant $500k MRR growth.")
            st.write(" #### :arrow_right: Reducing time limit of 1:1 free meetings #### ")
            st.write("""
                     - ► Implemented a uniform 40-minute meeting duration limit for all Basic (free) users, focusing on 1:1 meetings to streamline and enhance user experience.
                     - ► Led cross-functional discussions and project kick-off meetings, involving teams in strategy, finance, revenue, legal, marketing, mobile, desktop, web engineering, and QA. This initiative contributed significantly to a $500,000 increase in Monthly Recurring Revenue (MRR).
                     """
                     )
            
            st.write(" ### :large_green_circle: Audience segmentation, Data science project ### ")
            st.write(" - ► Collaborated with Data Engineering to integrate diverse data sources, ensuring comprehensive demographic, behavioral, psychographic, and usage data in Snowflake, later processing it in Databricks.")
            st.write(" - ► Participated in discussions for Exploratory Data Analysis (EDA) and Feature Engineering, utilizing the k-means algorithm with the Elbow method to identify potential customer segments: Champions, Dormant, and At Risk.")
            st.write(" - ► Socialized segment data with product teams, making predictive data accessible on web and client platforms for targeted customer engagement.")
            
    st.write('\n\n\n\n')              

# --- Cisco Zensar experiwnce    
    with st.container(border=True):
        col1, col2 = st.columns([7,3])
        with col1:
            with st.container():
                col001, col002, col003 = st.columns([1,1,9], gap="small")
                with col001:
                    zensar_logo_pic = Image.open(zensar_logo)
                    st.image(zensar_logo_pic,width=85)
                with col002:
                    cisco_logo_pic = Image.open(cisco_logo)
                    st.image(cisco_logo_pic,width=70)                
                with col003:
                    st.subheader("Zensar Technologies/Cisco Systems, CA")
                
            #st.write("##")
            #st.image(zoom_logo)
            st.subheader("Technical project manager")
            st.write("""
                     As a Technical Project Manager, led the System Recommendation project for Cisco employees, overseeing the implementation of a machine learning engine. Collaborated globally, engaged in strategic planning, and optimized recommendation accuracy through proficiency in Python and Big Data tools, contributing to Learning Management System migrations. Spearheaded. containerization and migration of The Multiplier Effect to AWS, managing cost, budget, AWS setup, configuring components, and implementing CI/CD pipelines for Docker containers, with a focus on containerizing the Drupal Web App on a PHP+Apache image..
                     """)
        with col2:
            st_lottie(tpm_lottie_animation  , height=200)
            #st.markdown("<h1 style='text-align: center'>SSep 2021 – PRESENT</h1>", unsafe_allow_html=True)
            st.write("May 2014 – Sep 2021")

        expander = st.expander(" Project Details ")
        
        
        with expander:
            #st.write(" ### :large_green_circle: Free user monetization projects: ### ")
            st.write("  ####  :arrow_right: The Multiplier Effect (https://www.multiplydiversity.com/)  #### ")
            st.write(" - ► Led a cross-functional team in containerizing and migrating an application to AWS for the Multiplier Effect project, managing cost, budget, and AWS account setup. Configured various AWS components(EC2, VPC, S3, ELB, CloudFront, IAM, RDS, CloudWatch, EKS, ECR) and managed Docker containers, implementing CI/CD pipelines for deploying images and focusing on containerizing the Drupal Web App on a PHP+Apache image.")

            st.write("  ####  :arrow_right: Learning system recommendations for Cisco employees  #### ")
            st.write(" - ► Led the System Recommendation project as a Technical Project Manager, overseeing the implementation of a machine learning engine for personalized learning recommendations based on diverse attributes.")
            st.write(" - ► Collaborated with global teams, engaged in strategic planning, architecture design, and hands-on coding, demonstrating proficiency in Python and Big Data tools, and optimized recommendation accuracy through algorithm adjustments and knowledge of Hadoop, Scoop, Hive, Spark, and Solr.")

            st.write("  ####  :arrow_right: Learning Management System, Content Management System (TeamSIte) migration to new enterprise platform #### ")
            st.write(" - ► Led communication and coordination for integrated application teams at Cisco, developing the next-gen UI for the Enterprise Learning site, configuring the Sales Enablement Reach Media platform, and contributing to a multilingual mobile app for partners. Key involvement in enterprise-level application platform migrations..")

    st.write('\n\n\n\n')              
    
# --- ZOOM experiwnce prioer to 2014
    with st.container(border=True):
        col1, col2 = st.columns([7,3])
        with col1:
            with st.container():
                col001, col002, col003 = st.columns([1,1,9], gap="small")
                with col001:
                    zensar_logo_pic = Image.open(zensar_logo)
                    st.image(zensar_logo_pic,width=85)
                with col002:
                    cisco_logo_pic = Image.open(cisco_logo)
                    st.image(cisco_logo_pic,width=70)                
                with col003:
                    st.subheader("Zensar Technologies/Cisco Systems, CA")
                
            #st.write("##")
            #st.image(zoom_logo)
            st.subheader("Software engineer, Senior Technical Lead")
            st.write("""
                     As a Senior Tech Lead, spearheaded client collaboration, roadmap development, and successful project delivery, with a focus on enhancing Enterprise Learning Services, facilitating ERP integration for cost savings, implementing Mobile Transformation, and actively engaging in agile development and continuous delivery, along with framework enhancements, search engine integrations, and seamless application integrations using Web Service Gateways..
                     """)
        with col2:
            st_lottie(coder1_lottie_animation , height=200)
            #st.markdown("<h1 style='text-align: center'>SSep 2021 – PRESENT</h1>", unsafe_allow_html=True)
            st.write("2004 – April 2014")


# --- ZOOM experiwnce prioer to 2004
    with st.container(border=True):
        col1, col2 = st.columns([7,3])
        with col1:
            with st.container():
                col202, col203 = st.columns([1,9], gap="small")
                with col202:
                    #cisco_logo_pic = Image.open(cisco_logo)
                    #st.image(cisco_logo_pic,width=70)
                    st.write(" :globe_with_meridians: ")
                with col203:
                    st.subheader("ETH/Dishnet DSL, Pune India")
                
            #st.write("##")
            #st.image(zoom_logo)
            st.subheader("Java/ J2EE Sr. Developer")
            st.write("""
                     As a Java Developer, implemented multithreading and Socket programming to craft a chat server with a Visual Basic client-side interface, collaborated with Dr. Vijay Bhatkar, CEO of Dishnet, and presented learning applications to India's President, *Dr. APJ Abdul Kalam*.
                     """)
        with col2:
            st_lottie(db_animation , height=200)
            #st.markdown("<h1 style='text-align: center'>SSep 2021 – PRESENT</h1>", unsafe_allow_html=True)
            st.write("Prier experience and achievements")

# --- Certificatiion
    with st.container():
        cert_col01, cert_col02 = st.columns(2)
        with cert_col01:
            st.subheader("Certification and Learning")
                
    with st.container(border=True):
        cert_col1, cert_col2 = st.columns([1,18])
        with cert_col1:
            aws_logo_pic = Image.open(aws_logo)
            st.image(aws_logo_pic,width=60)
        with cert_col2:
            st.subheader("AWS Certified Solutions Architect – Associate")

        cert_col1, cert_col2 = st.columns([1,18])
        with cert_col1:
            aws_logo_pic = Image.open(aws_logo)
            st.image(aws_logo_pic,width=60)
        with cert_col2:
            st.subheader("AWS Certified Cloud Practitioner")

        cert_col1, cert_col2 = st.columns([1,18])
        with cert_col1:
            google_logo_pic = Image.open(google_logo)
            st.image(google_logo_pic,width=60)
        with cert_col2:
            st.subheader("Introduction to Generative AI")

        cert_col1, cert_col2 = st.columns([1,18])
        with cert_col1:
            scrum_alliance_logo_pic = Image.open(scrum_alliance_logo)
            st.image(scrum_alliance_logo_pic,width=60)
        with cert_col2:
            st.subheader("Certified Scrum Master (SCM)")



#scrum_alliance_logo
#aws_logo
#google_logo
#pune_university_logo

        #st.write("""
        #    - Master of Computer Management (MCM) - Savitribai Phule Pune University
        #    - Diploma in Computer Management (DCM) - Savitribai Phule Pune University
        #    """)

# --- Education
    with st.container():
        edu_col01, edu_col02 = st.columns(2)
        with edu_col01:
            st.subheader("Education")
        
                
    with st.container(border=True):
        edu_col1, edu_col2 = st.columns([1,18])
        with edu_col1:
            pune_university_logo_pic = Image.open(pune_university_logo)
            st.image(pune_university_logo_pic,width=45)
        with edu_col2:
            st.write("Master of Computer Management (MCM) - Savitribai Phule Pune University")
        cert_col1, cert_col2 = st.columns([1,18])
        with edu_col1:
            #aws_logo_pic = Image.open(aws_logo)
            st.image(pune_university_logo_pic,width=45)
        with edu_col2:
            st.write('\n')
            st.write("Diploma in Computer Management (DCM) - Savitribai Phule Pune University")                          
                         

if selected == "Generative A.I. and Data Projects":
    with st.container():
        st.subheader("Projects worked on to learn latest technologies like Generative AI")
        
        #Create a form using st.form 
        form = st.form ("Basic form")
        
        with form:
            col1, col2, col3, col4  =  st.columns([4, 1, 1, 2])
            with col1:
                #uploaded_file = form.file_uploader("upload .txt or .pdf file")
                uploaded_file = st.file_uploader("Upload .pdf or .txt")
            with col2:
                #mcq_count = form.number_input("No, of MCQs", min_value = 1 , max_value = 5)
                #mcq_count = st.number_input("No, of MCQs", min_value = 1 , max_value = 3)
                mcq_count = st.number_input("No, of MCQs", 1 , 3)
            with col3:
                subject = st.text_input("Subject", max_chars =20)
            with col4:
                #tone = st.text_input("Complexity", max_chars=20, placeholder="Simple")
                tone = st.selectbox('Complexity',('Simple', 'Medium', 'Complex'))
            #with col5:
            colbutton1, colbutton2 =  st.columns([1, 1])
            with colbutton1:
                st.write("")
            with colbutton2:
                submitted = st.form_submit_button(label="Generate MCQ's")

        #Validation of all the fields
        if submitted:
            #initiate_vars()
            if uploaded_file is not None and mcq_count and subject and tone:        
                file_text = read_file(uploaded_file)
                if file_text == "MORE_THAN_FIVE_PAGES":
                    st.write("PDF file contains more than 5 pages, please upload file with 5 or less pages")
                elif file_text == "LESS_TEXT_IN_PDF":
                    st.write("File has not enough content to generate MCQ, please reupload file with enough content")
                elif file_text == "LESS_TEXT_IN_TXT":
                    st.write("File has not enough content to generate MCQ, please reupload file with enough content")
                elif file_text == "MORE_TEXT_IN_TXT":
                    st.write("File is too large, please reduce text size and reupload file.") 
                else:
                    #st.write("Conditions are satisfied, calling OpenAI")
                    mcq_output = getMCQData(file_text, mcq_count, subject, tone)
                    st.write("Here is quiz  :point_down: ")
                    #st.write(mcq_output)
                    #print(mcq_output)
                    #st.write(type(mcq_output))
                    #output_json = json.loads(json.dumps(mcq_output))
                    
                    quiz_table_data = []
                    tmp_dump = ast.literal_eval(mcq_output)
                    #st.write(tmp_dump)
                    json_dump = json.dumps(tmp_dump)
                    #st.write(tmp_dump)
                    json_obj = json.loads(json_dump)
                    #st.write(json_obj)
                    for key, value in json_obj.items():
                        mcq = value["mcq"]
                        #st.write(mcq)
                        options = " | ".join(
                        [
                            f"{option}: {option_value}"
                            for option, option_value in value["options"].items()
                        ]
                        )
                        correct = value["correct"]
                        quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
                        
                    
                    st.write(pd.DataFrame(quiz_table_data))
        
        
                    #st.write(number_of_pages , len(file_text), text_length_char, text_length_char_txt)
                    #st.write(file_text , mcq_count , subject, tone)
                #st.write(number_of_pages, len(file_text), text_length_char, text_length_char_txt , file_text)
            else:
                st.write("Please provide all the values")
        
        



        #st.write("##")
        #col5, col6 = st.columns((1,2))
        #with col5:
        #    st.image(genAI_image)
        #with col6:
        #    st.subheader("Generative A.I. projects ")
        #    st.markdown("[Visit Github page](https://github.com/bibhishank)")
            
        #    st.markdown("[![Title](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://github.com/bibhishank)")
    #with st.container():
        # Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
        #GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
        #genai.configure(api_key=GOOGLE_API_KEY)
        
        
    
            
if selected == "Contact me":
    st.subheader("Reach out to me")
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
        

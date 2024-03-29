from pathlib import Path
from PIL import Image
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
#import google.generativeai as genai 

#import pathlib
#import textwrap
#import PyPDF2
#import pandas as pd
#import json
#import ast
#from MCQGenerator import getMCQData 
#from BlogGenerator import getBLOGLLamaresponse
#from GetPexelsImage import getBlogImage

number_of_pages = 0
text_length_char = 0
text_length_char_txt = 0
all_page_text = ""


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
        
#Below block is commented as AI features are disabled from the site 
# def read_file(file):
#     if file.name.endswith(".pdf"):
#         try:
#             pdf_reader = PyPDF2.PdfReader(file)
#             text = ""
#             global number_of_pages
#             number_of_pages = len(pdf_reader.pages)
#             if number_of_pages > 5:
#                 return "MORE_THAN_FIVE_PAGES"
#             for page in pdf_reader.pages:
#                 text+= page.extract_text()
#             global text_length_char
#             text_length_char = len(text)
#             if text_length_char < 500:
#                 return "LESS_TEXT_IN_TXT"
#             if text_length_char > 8000:
#                 return "MORE_TEXT_IN_TXT"
#             return text
#         except Exception as e:
#             raise Exception ("error reading the PDF file")

#     elif file.name.endswith(".txt"):
#         text_file_text = file.read().decode("utf-8")
#         global text_length_char_txt
#         text_length_char_txt =  len(text_file_text) 
#         return text_file_text
#     else:
#         raise Exception(
#             "unsupported file format only pdf and text file suppoted")

#Below function is commented as Generative AI code is removed    
# def getQuize(file_text, mcq_count, subject, tone):
#     mcq_output = getMCQData(file_text, mcq_count, subject, tone)
#     st.write("Here is quiz  :point_down: ")
#     #print(mcq_output)
#     quiz_table_data = []
#     tmp_dump = ast.literal_eval(mcq_output)
#     #st.write(tmp_dump)
#     json_dump = json.dumps(tmp_dump)
#     #st.write(tmp_dump)
#     json_obj = json.loads(json_dump)
#     #st.write(json_obj)
#     for key, value in json_obj.items():
#         mcq = value["mcq"]
#         #st.write(mcq)
#         options = " | ".join(
#         [
#             f"{option}: {option_value}"
#             for option, option_value in value["options"].items()
#         ]
#         )
#         correct = value["correct"]
#         quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
        
#     st.write(pd.DataFrame(quiz_table_data))
    

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
local_css = current_dir / "styles" / "style.css"
resume_file = current_dir / "assets" / "Bibhishan_Karadkar_Resume.pdf"
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
web_logo =  current_dir / "assets" / "web.png"


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
ROLE = "Sr. Technical Project Manager"

#DESCRIPTION = """
#Experienced Sr. technical project manager with a proven track record of delivering business value. Skilled in working collaboratively with multiple teams like  engineering, product, infrastructure, data. Successfully  implemented multiple cross-functional programs over the past 9+ years highlighting a consistent ability to lead and execute initiatives that involve coordination across various departments.
#"""
DESCRIPTION = """
<small>Accomplished Sr. Technical Project Manager with 9+ years experience and additional software engineering expertise, leveraging tools, partnerships and technology to deliver business value. Demonstrates success identifying new technologies and opportunities to develop solutions that drive revenue, efficiency, and productivity. Strong reputation for building collaborative relationships with cross-functional teams (engineering, product, infrastructure, data) across multiple time zones (China, India, U.S.), effectively leading and executing initiatives.</small>
"""

EMAIL = "bibhishan_k@yahoo.com"
SOCIAL_MEDIA = {
    #"YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com/in/bibhishan-karadkar-910ba77",
    "GitHub": "https://github.com/bibhishank/profile-website/tree/main",
    #"Profile": "https://twitter.com",
}

PROJECTS = {
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout= "wide",menu_items=None)
st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}

    /* This code gets the first element on the sidebar,
    and overrides its default styling */
    section[data-testid="stSidebar"] div:first-child {
        top: 0;
        height: 100vh;
    }
</style>
""",unsafe_allow_html=True)


#TODO: Move this Utils.py
st.markdown("""
    <style>
    
           /* Remove blank space at top and bottom */ 
           .block-container {
               padding-top: 0rem;
               padding-bottom: 0rem;
            }
           
           /* Remove blank space at the center canvas */ 
           .st-emotion-cache-z5fcl4 {
               position: relative;
               top: -20px;
               }
           
           /* Make the toolbar transparent and the content below it clickable */ 
           .st-emotion-cache-18ni7ap {
               pointer-events: none;
               background: rgb(255 255 255 / 0%)
               }
           .st-emotion-cache-zq5wmm {
               pointer-events: auto;
               background: rgb(255 255 255);
               border-radius: 5px;
               }
            
    </style>
    """, unsafe_allow_html=True)

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
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(profile_pic, width=230)
    
    #st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.subheader(ROLE)
    #st.write(DESCRIPTION)
    st.markdown(DESCRIPTION, unsafe_allow_html=True)
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
    
    #st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)") 
        
        # if platform == "LinkedIn":
            
        #     cols[index].markdown(  f"   [{platform}]({link})""", unsafe_allow_html=True)
        # else:
        #     cols[index].write( f"[{platform}]({link})")

        #githubImage = f""" <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
        #        <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
        #        </svg>"""

#st.write('---')
# --- SOCIAL LINKS ---
# st.write('\n')


with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About' , 'Generative A.I. Projects', 'Contact me'],
        #add these names from https://icons.getbootstrap.com    
        icons = ['person', 'code-slash', 'chat-left-text-fill'], 
        orientation = 'horizontal',
        styles={
            "container": { "max-width":"100%"},
        #"container": {"padding": "0px", "margin":"0px", "width":"0px"}
        #"container": {"padding": "0px", "overflow": "auto",    "width":"100%", "border": "3px solid green;"}
        #"container": {"width":"100%"}
        }
    )
    
if selected == 'About':
    with st.container():
        col01, col02 = st.columns(2)
        with col01:
            #st.subheader("Professional experience:")
            st.markdown("<h3 style='text-align: left'>Professional experience:</h3>", unsafe_allow_html=True)
            

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
                    #st.subheader("Zoom Video communication, CA")
                    st.markdown("<h4 style='text-align: left'>Zoom Video communication, CA</h4>", unsafe_allow_html=True)
                
            st.markdown("<h5 style='text-align: left'>Sr. Technical project manager</h5>", unsafe_allow_html=True)
            st.markdown("""
                        <ul><li> • <small>Managed several end-to-end cross-functional projects for eCommerce marketing online revenue growth.</small></li><li> • <small>Achieved rapid promotion within 1  year due to exceptional performance and impactful contributions</small></li><li> • <small>Recognized with awards like "Dream Team" and "All In One" Award by the GM during All Hands meetings.</small></li><li> • <small>Led 8-10 projects/Qtr & managed big teams of 10-15 engineers addressing  all blockers & launch. </small></li></ul>""",
                        unsafe_allow_html=True)
                        
        with col2:
            st_lottie(lottie_coder , height=200)
            st.markdown("<h6 style='text-align: center'>Sep 2021 – PRESENT</h6>", unsafe_allow_html=True)
        
        expander = st.expander( " :small_red_triangle_down: **⚙️ Project Details** ")
        
        with expander:
            st.write("")
            st.markdown("<h6 style='text-align: left; color: #00E1FF'> ● Key Initiative 1) Forced Break 40 min for free sequential meeting (Free user monetization) </h6>", unsafe_allow_html=True)
            st.markdown(""" <ul><li> 
                         • <small>Managed global program to  limit users have  1:1 meetings reducing duration & restricted back to back  meetings (Impact : Drove massive revenue growth for Zoom in FY23 ~$2M).</small></li><li>
                         • <small>Collaborated with 7-8 technical teams and non technical (Product,Finance, revenue, sales, legal, marketing) leading to successful implementation.</small></li><li>
                         • <small>Led 10-15 Engineers and QA team in the development and launch.</small></li><li>
                         • <small>Led project planning & execution across infrastructure,  mobile, desktop, and web.</small></li><li>
                         • <small>Conducted A/B testing for 5 min and 10 min break control variant before 5 weeks of the roll out.</small></li><li>
                         • <small>Partnered w/ data team to integrate analytics and measure via Tableau dashboards. </small></li></ul>""",
                        unsafe_allow_html=True)
            
            st.markdown("<h6 style='text-align: left; color: #00E1FF'> ● Key Initiative 2) Data Science & Engineering (Audience segmentation ~$3M expected revenue) </h6>", unsafe_allow_html=True)
            st.markdown(""" <ul><li> 
                         • <small>Collaborated 6 product teams  & data science to enable data tracking in Snowplow telemetry.</small></li><li>
                         • <small>Led projects with Data Engineering to merge diverse data sources for comprehensive demographic, behavioral, psychographic, and usage data in Snowflake, processed in Databricks.</small></li><li>
                         • <small>Engaged in Exploratory Data Analysis (EDA) discussions and Feature Engineering, utilizing the k-means algorithm with the Elbow method identify # of segments: Champions, Dormant and At Risk.</small></li><li>
                         • <small>Collaborated with 5 Product Eng teams to share data that will help in enabling targeted customer engagement through predictive data on web and client platforms. </small></li></ul>""",
                        unsafe_allow_html=True)

            st.markdown("<h5 style='text-align: left; color: #00E1FF'>  ● Responsibilities and tasks </h5> ", unsafe_allow_html=True)
            st.markdown(""" <ul><li>
                        ●  Adopted  Agile, Scrum and Waterfall approaches using tools like JIRA, Asana MS Project, Custom template</li><li>
                        ●  Led  In App Purchase programs  for improving checkout of  Zoom products on Apple and Android devices</li><li>
                        ●  Managed NPI enablement  of Zoom Products for Online customers like Zoom Phone, Home Destination</li><li>
                        ●  Managed project plan for  Zoom AI Companion that uses  natural language processing (NLP), machine learning, and voice recognition technology to understand meetings and convert into meeting summaries</small></li><li>
                        ●  Led project related to cloud recording enforcing limits for online customers (Impact $296K MRR) partnering with infrastructure teams</li><li>
                        ●  Led projects related to in product growth marketing to increase sign up on Client & Web and Free Sign-Up Optimizations (Impact 500K MRR) partnering with Marketing & Retention Product Management </li><li>
                        ●  Managed projects related to Mobile & desktop client for showing pre & post meeting dialogues to Online customers for driving retention promotions for Online marketing increasing free to paid conversions </li></ul>""" ,
                        unsafe_allow_html=True)


    
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
                    #st.subheader("Zensar Technologies/Cisco Systems, CA") 
                    st.markdown("<h4 style='text-align: top'>Zensar Technologies - Client : Cisco Systems</h4>", unsafe_allow_html=True)

                
            #st.write("##")
            #st.image(zoom_logo)
            #st.subheader("Technical project manager")
            st.markdown("<h5 style='text-align: left'>Technical project manager</h5>", unsafe_allow_html=True)
            st.markdown("""
                     <small>As a Technical Project Manager, led the System Recommendation project for Cisco employees, overseeing the implementation of a machine learning engine. Collaborated globally, engaged in strategic planning, and optimized recommendation accuracy through proficiency in Python and Big Data tools, contributing to Learning Management System migrations. Spearheaded. containerization and migration of The Multiplier Effect to AWS, managing cost, budget, AWS setup, configuring components, and implementing CI/CD pipelines for Docker containers, with a focus on containerizing the Drupal Web App on a PHP+Apache image.</small> """,
                     unsafe_allow_html=True)
                     
        with col2:
            st_lottie(tpm_lottie_animation  , height=200)
            #st.markdown("<h1 style='text-align: center'>SSep 2021 – PRESENT</h1>", unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: center'>May 2014 – Sep 2021</h6>", unsafe_allow_html=True)
            #st.write("May 2014 – Sep 2021")

        expander = st.expander("  :small_red_triangle_down: **⚙️ Project Details**  ")
        with expander:
            st.write('\n\n\n\n')    
            zencol01,zencol02 = st.columns([5,5])
            with zencol01:
                st.markdown("<h5 style='text-align: left'> <u>Technical project manager </u></h5>", unsafe_allow_html=True)
            with zencol02:
                st.markdown("<h6 style='text-align: right'>May 2014 – Sep 2021</h6>", unsafe_allow_html=True)
            st.markdown("<small> Key Initiatives : </small>", unsafe_allow_html=True)
            
            st.markdown("<h6 style='text-align: left; color: #00E1FF'>  ● The Multiplier Effect (https://www.multiplydiversity.com/) </h6> ", unsafe_allow_html=True)
            st.markdown(""" <ul><li> 
                        • <small>Led a cross-functional teams to containerizing and migrating inhouse applications to AWS for the Multiplier Effect project, managing cost, budget, and AWS account setup. Configured various AWS components(EC2, VPC, S3, ELB, CloudFront, IAM, RDS, CloudWatch, EKS, ECR) and managed Docker containers, implementing CI/CD pipelines for deploying images and focusing on containerizing the Drupal Web App on a PHP+Apache image.</small></li></ul>
                        """ , unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: left; color: #00E1FF'>  ● Learning system recommendations for Cisco employees </h6> ", unsafe_allow_html=True)
            st.markdown(""" <ul><li> 
                        • <small> Led the System Recommendation project as a Technical Project Manager, overseeing the implementation of a machine learning engine for personalized learning recommendations based on diverse attributes.</small></li><li>
                        • <small> Collaborated with global teams, engaged in strategic planning, architecture design, and hands-on coding, demonstrating proficiency in Python and Big Data tools, and optimized recommendation accuracy through algorithm adjustments and knowledge of Hadoop, Scoop, Hive, Spark, and Solr.</small></li></ul>
                        """ , unsafe_allow_html=True)

            st.markdown("<h6 style='text-align: left; color: #00E1FF'>  ● Learning Management System, Content Management System (TeamSIte) migration to new enterprise platform </h56> ", unsafe_allow_html=True)
            st.markdown(""" <ul><li> 
                        • <small> Led managed communication and coordination for integrated application teams at Cisco, developing the next-gen UI for the Enterprise Learning site, configuring the Sales Enablement Reach Media platform, and contributing to a multilingual mobile app for partners. Key involvement in enterprise-level application platform migrations.</small></li></ul>
                        """ , unsafe_allow_html=True)
            
            st.write('\n\n\n\n')
            zencol03,zencol04 = st.columns([5,5])
            with zencol03:
                st.markdown("<h5 style='text-align: left'> <u>Software engineer, Senior Technical Lead </u></h5>", unsafe_allow_html=True)
            with zencol04:
                st.markdown("<h6 style='text-align: right'> April 2004 – April 2014</h6>", unsafe_allow_html=True)
                
            st.markdown(""" <ul><li> 
                        • <small> Spearheaded client collaboration, roadmap development, and successful project delivery, with a focus on enhancing Enterprise Learning Services, facilitating ERP integration for cost savings, implementing Mobile Transformation, and actively engaging in agile development and continuous delivery, along with framework enhancements, search engine integrations, and seamless application integrations using Web Service Gateways.</small></li></ul>
                        """ , unsafe_allow_html=True)


    st.write('\n\n\n\n')  

    with st.container(border=True):
        col1, col2 = st.columns([7,3],gap="small")
        with col1:
            with st.container():
                col001, col1002 = st.columns([1,18])
                with col001:
                    web_logo_pic = Image.open(web_logo)
                    st.image(web_logo_pic,width=60)
                with col1002:
                    #st.subheader("Zoom Video communication, CA")
                    st.markdown("<h4 style='text-align: left'>Employer: ETH/Dishnet DSL, Pune India</h4>", unsafe_allow_html=True)
                
            st.markdown("<h6 style='text-align: left'>Java/ J2EE Sr. Developer</h6>", unsafe_allow_html=True)
            st.markdown(""" <ul><li> 
                        • <small>As a Java Developer, I utilized multithreading and Socket programming to design a chat server, incorporating Visual Basic for the user interface on the client side and Java for server-side operations. </small></li><li>
                        • <small> I had the privilege of working with Dr. Vijay Bhatkar, the CEO of Dishnet, and showcasing learning applications/projects to </small> <b> India's President, Dr. APJ Abdul Kalam </b>. </li></ul>""",
                        unsafe_allow_html=True)
                        
        with col2:
             st_lottie(coder1_lottie_animation , height=200)
             #st.markdown("<h1 style='text-align: center'>SSep 2021 – PRESENT</h1>", unsafe_allow_html=True)
             st.markdown("<h6 style='text-align: center'>Prier experience and achievements</h6>", unsafe_allow_html=True)
             #st.write("Prier experience and achievements")
            

# --- Certificatiion
    with st.container():
        cert_col01, cert_col02 = st.columns(2)
        with cert_col01:
            st.subheader("Certification and Learning")
                
    with st.container(border=True):
        cert_col1, cert_col2 = st.columns([1,18])
        with cert_col1:
            aws_logo_pic = Image.open(aws_logo)
            st.image(aws_logo_pic,width=40)
        with cert_col2:
            st.markdown("<h6 style='text-align: left'>AWS Certified Solutions Architect – Associate</h6>", unsafe_allow_html=True)
            #st.subheader("AWS Certified Solutions Architect – Associate")

        cert_col1, cert_col2 = st.columns([1,18])
        with cert_col1:
            aws_logo_pic = Image.open(aws_logo)
            st.image(aws_logo_pic,width=40)
        with cert_col2:
            #st.subheader("AWS Certified Cloud Practitioner")
            st.markdown("<h6 style='text-align: left'>AWS Certified Cloud Practitioner</h6>", unsafe_allow_html=True)

        cert_col1, cert_col2 = st.columns([1,18])
        with cert_col1:
            google_logo_pic = Image.open(google_logo)
            st.image(google_logo_pic,width=30)
        with cert_col2:
            #st.subheader("Introduction to Generative AI")
            st.markdown("<h6 style='text-align: left'>Introduction to Generative AI</h6>", unsafe_allow_html=True)

        cert_col1, cert_col2 = st.columns([1,18])
        with cert_col1:
            scrum_alliance_logo_pic = Image.open(scrum_alliance_logo)
            st.image(scrum_alliance_logo_pic,width=30)
        with cert_col2:
            #st.subheader("Certified Scrum Master (SCM)")
            st.markdown("<h6 style='text-align: left'>Certified Scrum Master (SCM)</h6>", unsafe_allow_html=True)


# --- Education
    with st.container():
        edu_col01, edu_col02 = st.columns(2)
        with edu_col01:
            st.subheader("Education")
        
                
    with st.container(border=True):
        edu_col1, edu_col2 = st.columns([1,18])
        with edu_col1:
            pune_university_logo_pic = Image.open(pune_university_logo)
            st.image(pune_university_logo_pic,width=35)
        with edu_col2:
            st.write("Master of Computer Management (MCM) - Savitribai Phule Pune University")
        cert_col1, cert_col2 = st.columns([1,18])
        with edu_col1:
            #aws_logo_pic = Image.open(aws_logo)
            st.image(pune_university_logo_pic,width=35)
        with edu_col2:
            st.write('\n')
            st.write("Diploma in Computer Management (DCM) - Savitribai Phule Pune University")                          
                         

if selected == "Generative A.I. Projects":

    with st.container():
        
        
        genai_col1, genai_col2, genai_col3 = st.columns([1,8,1], gap="small")
        with genai_col2:
            st.subheader("My work in Generative AI")
            st.markdown(""" Constructed website(<a href='https://www.interviewhelperai.com' target='_blank'> https://www.interviewhelperai.com </a>)  to help people who are in process of finding a Job  
                        <p style='font-size:100%;'><b>LLM’s:</b> <small> OpenAI, Gemini Pro, Llama-2 </small> </p>
                        <p style='font-size:100%;'><b>Tools/technics:</b> <small> Langchain, Prompt Engineering, Google OAuth, Firebase </small> </p>
                        """ ,unsafe_allow_html = True)
            st.markdown(f"""<p style='font-size:75%;'>  Mission of the website is to empower users worldwide with personalized and effective interview preparation assistance leveraging cutting-edge AI technology. 
                    We aim to provide a comprehensive platform where users can access tailored resources, including mock interviews, expert feedback, and personalized coaching, to enhance their interview skills and confidence. 
                    Our goal is to democratize access to high-quality interview preparation support, 
                    regardless of background or experience, ultimately helping users secure their dream jobs and advance their careers.</p>""" ,unsafe_allow_html = True)
        
            VIDEO_URL = "https://www.youtube.com/watch?v=dSdOddlGPOA"
            st.video(VIDEO_URL)
#     with st.container():
#         
        
#         st.write("  :blue[ **1) Generate blog and image for given subject or profession** ]  ")  
#         multi = ''' :blue[ **Technologies and Tools:** ] <small>OpenAI LLM, LLAMA, DALL-E-3,LangChain, PromptTemplate, Python, Streamlit, GIT, AWS, EC2, CloudFront.</small>  
#         :blue[ **How it works:** ] <small>Provide blog Topic, lengt of the Blog and for what profession user want to generate a blog and image.</small>
#         '''
#         st.markdown(multi, unsafe_allow_html=True)

#         #Create a form using st.form 
#         form1 = st.form("Blog form")        
        
#         with form1:
#             ## creating to more columns for additonal 2 fields
#             input_text=st.text_input("Enter the Blog Topic")
#             col1,col2=st.columns([5,5])
#             with col1:
#                 no_words=st.text_input('No of Words')
#             with col2:
#                 blog_style=st.selectbox('Writing the blog for',
#                                     ('Researchers','Data Scientist','Common People', 'Teachers', 'Economists'),index=0)
            
#             button_col1, button_col2=st.columns([1,5], gap="small")
#             with button_col1:
#                 form1_submit=st.form_submit_button(" Generate a Blog")
            
#             with button_col2:
#                 message_container = st.container(border=False)
#                 with message_container:
#                     form_text = st.markdown("", unsafe_allow_html=True)
#                 #message_container.write("Init")
                            
#             #form_text.text("Second")
        
#         if form1_submit:
#             if input_text and no_words and blog_style:
#                 #print(input_text,no_words,blog_style)
#                 form_text.markdown("<h6 style='text-align: left; color: #00E1FF'> <b>Generating blog and image, please wait...</b></h6>", unsafe_allow_html=True)
#                 blog_response = getBLOGLLamaresponse(input_text,no_words,blog_style)
#                 blog_image_url = getBlogImage(input_text)

#                 blog_col1,blog_col2=st.columns([5,5])
#                 with blog_col1:
#                     st.write("")
#                     st.write("")
#                     st.subheader(input_text)
#                 with blog_col2:
#                     if blog_image_url:
#                         #blog_image = Image.open(blog_image_url)
#                         st.image(blog_image_url, width=500)
#                     else:
#                         st.write("")
                
#                 st.write(blog_response)
#                 form_text.markdown(" :point_down: Here is blog and related image, generated by OpenAI and DALL-E.", unsafe_allow_html=True)
#                 #form_text.toast("Here is blog and related image, generated by OpenAI and DALL-E.")
                
#             else:
#                 form_text.markdown("<h8 style='text-align: left; color: red'> Please provide all the values </h8>" , unsafe_allow_html=True)
#                 #form_text.toast("Please provide all the values")


# #====Second project of Blog generation        
#     with st.container():
#         st.write("")
#         st.write("")
#         st.write("")
#         st.divider()
        
#         st.write("   :blue[ **2) Generate Multiple choice quiz from given file content or text** ]  ")  
#         multi = ''' :blue[ **Technologies and Tools:** ] <small>OpenAI LLM, LangChain, PromptTemplate, Python, Streamlit, GIT, AWS, EC2, CloudFront.</small>  
#         :blue[ **How it works:** ] <small>Upload a .pdf or .txt file from MCQ quiz is to be generated, provide number of questions, Subject and complexity level like Simple Medium Complex. Download .csv file.</small>
#         '''
#         st.markdown(multi, unsafe_allow_html=True)
        
#         #Create a form using st.form 
#         form = st.form ("Basic form")
        
#         with form:
#             col1, col2, col3, col4  =  st.columns([4, 1, 1, 2])
#             with col1:
#                 #uploaded_file = form.file_uploader("upload .txt or .pdf file")
#                 uploaded_file = st.file_uploader("Upload .pdf or .txt")
#             with col2:
#                 mcq_count = st.number_input("No, of MCQs", 1 , 3)
#             with col3:
#                 subject = st.text_input("Subject", max_chars =20)
                
#             with col4:
#                 #tone = st.text_input("Complexity", max_chars=20, placeholder="Simple")
#                 tone = st.selectbox('Complexity',('Simple', 'Medium', 'Complex'))
#             #with col5:
#             colbutton1, colbutton2 =  st.columns([1, 1])
#             with colbutton1:
#                 #st.write("")
#                 mcq_txt = st.text_area(
#                     label = "If file is not uploaded add text to generate MCQ",
#                     height = 200,
#                     max_chars = 4000 ,
#                     placeholder = "Text to generate MCQ"
#                     )
#             with colbutton2:
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 submitted = st.form_submit_button(label="Generate MCQ's")


#         #Validation of all the fields
#         if submitted:
#             #initiate_vars()
#             if (uploaded_file is not None or mcq_txt) and mcq_count and subject and tone:        
#             #if uploaded_file is not None and mcq_count and subject and tone:
#                 if len(mcq_txt) >= 500:
#                     file_text = mcq_txt
#                     getQuize(file_text, mcq_count, subject, tone)
#                     #st.write("Text size is too short to generate quize, add more content or upload file.")    
#                 elif uploaded_file is None and len(mcq_txt) < 500:
#                     st.write("Text size is too short to generate quize, add more content or upload file.")    
#                 elif uploaded_file is not None and (len(mcq_txt) < 500 or mcq_txt is None):
#                     file_text = read_file(uploaded_file)
#                     if file_text == "MORE_THAN_FIVE_PAGES":
#                         st.write("PDF file contains more than 5 pages, please upload file with 5 or less pages")
#                     elif file_text == "LESS_TEXT_IN_PDF":
#                         st.write("File has not enough content to generate MCQ, please reupload file with enough content")
#                     elif file_text == "LESS_TEXT_IN_TXT":
#                         st.write("File has not enough content to generate MCQ, please reupload file with enough content")
#                     elif file_text == "MORE_TEXT_IN_TXT":
#                         st.write("File is too large, please reduce text size and reupload file.") 
#                     else:
#                         getQuize(file_text, mcq_count, subject, tone)
#                         #st.write("Conditions are satisfied, calling OpenAI")
#                 else:
#                     st.write("Text size is too short to generate quize, add more content or upload file.")

#             else:
#                 st.write("Please provide all the values")
        
            
if selected == "Contact me":
    #contact_me_col1, contact_me_col2, contact_me_col3 = st.columns([1,8,1], gap="small")
    #with contact_me_col2:
    #<input type="email" style="background-color: lightblue; border-radius: 2px;" name="email" placeholder = "Your Email" required>
    contact_form = """
    <form action="https://formsubmit.co/bibhishan_k@yahoo.com" method="POST">
    <input type = "hidden" name = "_captcha" value = "false">
    <input type="text" style="border-radius: 6px; " name="name" placeholder= "Your Name" required>
    <input type="email" style="border-radius: 6px; " name="email" placeholder = "Your Email" required>
    <textarea name="message" style="border-radius: 6px; " placeholder = "Your Message" required></textarea>
    
    <style>
    .contactbutton {
    background-color: #FF8C02; /* #04AA6D Green */
    border: none;
    color: white;
    padding: 15px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 3px 1px;
    cursor: pointer;
    }
    .contactbuttonradius {border-radius: 12px;}
    </style>
    <center><button type="submit" class="contactbutton contactbuttonradius">Send</button></center>
    </form>
    """
            
    left_col, middle_col, right_col = st.columns([1,7,2])
    with middle_col:
        st.subheader("Reach out to me")
        st.markdown(contact_form, unsafe_allow_html= True )
    with right_col:
        st_lottie(contact_animation, height = 100)
        
    #<button type="submit">Send</button>

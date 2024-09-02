import streamlit as st
from PIL import Image

def show_about_me():
    st.header("About Me")
    st.write("""
        I am a 4th-year IT student with a strong grasp of programming languages and software development. 
        My journey in technology has been driven by curiosity and a desire to innovate. 
        Quick learner and adaptable team player with a keen interest in staying updated on industry trends.
        Dedicated to applying technical skills in the real world and eager to continue learning and growing in the tech industry.
        """)

def show_experience():
    st.header("Experience")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(":sparkles: Social Media Marketing Intern:")
    st.write("""
    - *EFAM Training Consultancy Services, Feb 2021 - Mar 2021* 
    - Designed marketing content selected by the United Nations World Peace Association.
    """)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(":sparkles: Mobile App Development Intern:")
    st.write("""
    - *CREOTEC Philippines Inc., Feb 2021 - Mar 2021*
    - Worked on both front-end and back-end development for mobile apps.
    """)

def show_education():
    st.header("Education")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(":mortar_board: Bachelor of Science in Information Technology:")
    st.write("*Cebu Institute of Technology - University, 2021 - Present*")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(":mortar_board: Senior High School:")
    st.write("*University of San Jose - Recoletos, 2019 - 2021*")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(":mortar_board: Junior High School:")
    st.write("*Cebu Institute of Technology - University, 2015 - 2019*")

def show_projects():
    st.header("Projects")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(":art: Cranvas")
    st.write("""
    - It is a multivendor e-commerce web application.
    - Key technologies: React JS, Springboot
    """)
    st.image("C:/Users/Sherlyn Olalo/Downloads/CRANVAS.jpg")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(":art: Campus Eats")
    st.write("""
    - It is a localized delivery platform tailored specifically for the CIT-University community. 
    Campus Eats seeks to address the dining needs of faculty by providing a convenient and efficient
    food delivery service directly on campus.
    - Key technologies: React JS, Springboot
    """)
    st.image("C:/Users/Sherlyn Olalo/Downloads/CAMPUSEATS.png")

def show_skills():
    st.header("Skills")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(":star: Front-end development:")
    st.progress(90)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(":star: Back-end development:")
    st.progress(70)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(":star: Data Analysis:")
    st.progress(70)

def show_certifications():
    st.header("Certifications")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(":trophy: EFAM Training")
    st.write("Feb 2021 - Mar 2021")
    st.image("C:/Users/Sherlyn Olalo/Downloads/EFAM.png")


st.set_page_config(layout="wide")

st.sidebar.title("Navigation")
nav_selection = st.sidebar.radio(
    "",
    ("About Me", "Experience", "Education", "Projects", "Skills", "Certifications")
)

dark_mode = st.sidebar.checkbox("Dark Mode")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');

    .stApp {
        font-family: 'Poppins', sans-serif;
        background-color: #ffe4e6;
        color: #5f6368;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
    }

    h1, h2, h3, h4, h5, h6 {
        color: #ff69b4;
        margin-bottom: 20px;
    }

    h2, h3 {
        color: #ff8c94;
    }

    hr {
        border: 1px solid #ffb6c1;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    p, .stText, .stMarkdown {
        font-size: 16px;
        line-height: 1.6;
        color: #5f6368;
    }

    a {
        color: #ff69b4;
        text-decoration: none;
        font-weight: 500;
    }
    a:hover {
        color: #ff8c94;
    }

    img {
        border-radius: 15px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }

    .stButton button {
        background-color: #ff69b4;
        color: #ffffff;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #ff8c94;
    }

    .stColumns {
        gap: 2rem;
    }

    .dark-mode .stApp {
        background-color: #282c34;
        color: #e1e1e1;
    }
    .dark-mode hr {
        border: 1px solid #555555;
    }
    .dark-mode a {
        color: #ff69b4;
    }
    .dark-mode a:hover {
        color: #ff8c94;
    }

    </style>
    """,
    unsafe_allow_html=True
)

if dark_mode:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #282c34;
            color: #e1e1e1;
        }
        hr {
            border: 1px solid #555555;
        }
        a {
            color: #ff69b4;
            text-decoration: none;
        }
        a:hover {
            color: #ff8c94;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


Image1 = Image.open("C:/Users/Sherlyn Olalo/Pictures/XIEXIE2024/pictures/1991.jpg")

col1, col2 = st.columns([1, 3])

with col1:
    st.image(Image1, width=250)

with col2:
    st.title("Portfolio")

    st.markdown("**Name:** Sherlyn Olalo")
    st.markdown("**Email:** sherlyn.olalo@cit.edu")
    st.markdown("**Location:** Cebu City, Philippines")

    st.write("[GitHub](https://github.com/shexiee)")

st.write("")

if nav_selection == "About Me":
    show_about_me()

elif nav_selection == "Experience":
    show_experience()

elif nav_selection == "Education":
    show_education()

elif nav_selection == "Projects":
    show_projects()

elif nav_selection == "Skills":
    show_skills()

elif nav_selection == "Certifications":
    show_certifications()

import streamlit as st
from data import PROFILE

st.set_page_config(
    page_title=f"{PROFILE['name']} | Portfolio",
    page_icon="💼",
    layout="centered",
)

pages = [
    st.Page("views/home.py", title="Home", icon="🏠", default=True),
    st.Page("views/about.py", title="About", icon="👤"),
    st.Page("views/projects.py", title="Projects", icon="🗂️"),
    st.Page("views/project_detail.py", title="Project Detail", icon="🔍"),
    st.Page("views/resume.py", title="Résumé", icon="📄"),
    st.Page("views/contact.py", title="Contact", icon="✉️"),
]

page = st.navigation(pages)

# Sidebar shown on every page
st.sidebar.markdown(f"### {PROFILE['name']}\n{PROFILE['title']}")
st.sidebar.link_button("GitHub", PROFILE["github"])
st.sidebar.link_button("LinkedIn", PROFILE["linkedin"])

page.run()
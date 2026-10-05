import streamlit as st
from data import PROFILE, PROJECTS

st.title(f"Hi, I'm {PROFILE['name']} 👋")
st.subheader(PROFILE["title"])
st.write(PROFILE["tagline"])

col1, col2 = st.columns(2)
col1.page_link("views/projects.py", label="View my work", icon="🗂️")
col2.page_link("views/contact.py", label="Get in touch", icon="✉️")

st.header("Featured projects")
for p in PROJECTS[:3]:
    with st.container(border=True):
        st.markdown(f"**{p['title']}** · `{p['category']}`")
        st.write(p["summary"])
        if st.button("Read more →", key=f"home_{p['slug']}"):
            st.session_state["selected_project"] = p["slug"]
            st.switch_page("views/project_detail.py")
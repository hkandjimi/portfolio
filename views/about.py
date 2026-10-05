import streamlit as st
from data import PROFILE, SKILLS

st.title("About me")
st.write(PROFILE["bio"])

st.header("Skills")
for group, items in SKILLS.items():
    st.subheader(group)
    st.markdown("  ".join(f"`{skill}`" for skill in items))

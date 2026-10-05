from pathlib import Path
import streamlit as st
from data import EDUCATION, EXPERIENCE

st.title("Résumé")

pdf_path = Path(__file__).parent.parent / "assets" / "resume.pdf"
if pdf_path.exists():
    st.download_button("Download PDF", data=pdf_path.read_bytes(),
                       file_name="resume.pdf", mime="application/pdf")

st.header("Education")
for e in EDUCATION:
    st.markdown(f"**{e['degree']}**, {e['school']} ({e['years']})")
    st.caption(e["note"])

st.header("Experience")
for x in EXPERIENCE:
    st.markdown(f"**{x['role']}**, {x['org']} ({x['years']})")
    st.caption(x["note"])
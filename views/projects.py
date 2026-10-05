import streamlit as st
from data import PROJECTS

st.title("Projects")

col1, col2 = st.columns([2, 1])
query = col1.text_input("Search", placeholder="Title or technology...").strip().lower()
categories = ["All"] + sorted({p["category"] for p in PROJECTS})
category = col2.selectbox("Category", categories)

results = [
    p for p in PROJECTS
    if (category == "All" or p["category"] == category)
    and (not query
         or query in p["title"].lower()
         or query in p["summary"].lower()
         or any(query in t.lower() for t in p["tech"]))
]

st.caption(f"{len(results)} project(s) found.")
if not results:
    st.info("No projects match your search.")

for p in results:
    with st.container(border=True):
        st.markdown(f"**{p['title']}** · `{p['category']}` · {p['year']}")
        st.write(p["summary"])
        st.caption("Tech: " + ", ".join(p["tech"]))
        if st.button("View details →", key=f"btn_{p['slug']}"):
            st.session_state["selected_project"] = p["slug"]
            st.switch_page("views/project_detail.py")
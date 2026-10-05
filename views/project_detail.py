import streamlit as st
from data import PROJECTS

slugs = [p["slug"] for p in PROJECTS]
titles = {p["slug"]: p["title"] for p in PROJECTS}

# Use the project chosen on another page, or fall back to the first one
default = st.session_state.get("selected_project", slugs[0])
slug = st.selectbox("Choose a project", slugs,
                    index=slugs.index(default), format_func=titles.get)
st.session_state["selected_project"] = slug

project = next(p for p in PROJECTS if p["slug"] == slug)

st.title(project["title"])
st.caption(f"{project['category']} · {project['year']}")
st.write(project["description"])

st.subheader("Technologies")
st.markdown("  ".join(f"`{t}`" for t in project["tech"]))

st.link_button("View source code", project["link"])
import csv
import datetime
from pathlib import Path

import requests
import streamlit as st
from data import PROFILE

st.title("Contact me")
st.write(f"Or email me directly at {PROFILE['email']}.")


def save_message(name, email, message):
    endpoint = PROFILE["form_endpoint"]
    if endpoint:
        # Real mode: Formspree emails the message to you
        r = requests.post(
            endpoint,
            json={"name": name, "email": email, "message": message},
            headers={"Accept": "application/json"},
            timeout=10,
        )
        r.raise_for_status()
    else:
        # Demo mode: local file (is wiped whenever the app restarts online)
        with Path("messages.csv").open("a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(
                [datetime.datetime.now().isoformat(), name, email, message])


with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message", height=150)
    submitted = st.form_submit_button("Send message")

if submitted:
    if not (name.strip() and email.strip() and message.strip()) or "@" not in email:
        st.error("Please fill in all fields with a valid email.")
    else:
        try:
            save_message(name.strip(), email.strip(), message.strip())
            st.success("Thanks! Your message has been sent.")
        except Exception:
            st.error("Something went wrong. Please email me directly instead.")
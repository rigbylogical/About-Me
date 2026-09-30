import os
from pathlib import Path
import requests
import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Rigbylogical | Portfolio", layout="wide")

# 2. Dynamic Base Directory Resolution (Fixes FileNotFoundError)
BASE_DIR = Path(__file__).resolve().parent

# --- Header Section ---
with st.container():
    st.subheader("Hi, my name is Rigbylogical")
    st.title("About Me")
    st.write(
        """
    I am a GFS Food Service CDL Truck Driver. The job is very physically demanding and mentally taxing. However, it is very rewarding. 
    I am able to set my future up with the money I am bringing in! I have a goal to one day buy a home!!

    Outside of work my true identity is in my Lord and Savior Jesus Christ.
    I gave my life to Christ in 2020 during the Covid Lockdowns.

    I also used to make YT vids when I was heavily into gaming. The link is below!
    """
    )

    st.write("######")
    yt_logo, yt_play = st.columns([1, 2])

    # Safely load logo image across OS environments
    logo_path = BASE_DIR / "logo 1.png"
    with yt_logo:
        if logo_path.exists():
            st.image(str(logo_path))
        else:
            # Fallback if file is named with an underscore on GitHub
            alt_logo = BASE_DIR / "logo_1.png"
            if alt_logo.exists():
                st.image(str(alt_logo))
            else:
                st.info("🖼️ [logo image]")

    with yt_play:
        st.markdown(
            "[Old Youtube Channel >](https://www.youtube.com/@rigbylogical4001)"
        )

# --- Projects Section ---
with st.container():
    st.write("---")
    st.subheader("Here are some of projects I have made!!")
    st.write("##")

    # Project 1: Twins Bakery
    project_1, link_1 = st.columns([1, 2])
    bake_path = BASE_DIR / "bake.jpg"

    with project_1:
        if bake_path.exists():
            st.image(str(bake_path))
        else:
            st.info("🖼️ [bake.jpg]")

    with link_1:
        st.subheader(
            "[Twins Bakery](https://docs.google.com/spreadsheets/d/18QYe7zuLVc8OnVlYs3gujsGPDO1dowxtZp_UEYWXA2w/edit?gid=520005004#gid=520005004)"
        )
        st.write(
            """
        Twins Bakery project was my first real world project.
        I gathered data and put it into a spreadsheet and cleaned up the data to make it readable.
        When I was done gathering data I made a dashboard for her to see what sold the most and least and her total revenue from the sales.
        """
        )

    st.write("##")

    # Project 2: Job Project
    project_2, link_2 = st.columns([1, 2])
    lo_path = BASE_DIR / "lo.png"

    with project_2:
        st.markdown(
            """
            <style>
            img {
                border: 2px solid black;
                border-radius: 4px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        if lo_path.exists():
            st.image(str(lo_path))
        else:
            st.info("🖼️ [lo.png]")

    with link_2:
        st.subheader(
            "[Job Project](https://docs.google.com/spreadsheets/d/1lVtkfZD4ZUbOR4_-7ktqx2rHy36nELPkhNyLZGlcFFw/edit?gid=0#gid=0)"
        )
        st.write(
            """
        Here is my BIG project. It is for my job. Here I am making a better dashboard for food service drivers.
        I track cases, stops and other metrics for routes. The steps and calories aspects are for the 'Fit Plus' feature
        for drivers that like to track their health and fitness.
        """
        )

# --- Reliable Native Contact Form ---
st.write("---")
st.subheader("Contact Me!!")

left_column, right_column = st.columns([2, 1])

with left_column:
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name", placeholder="Enter your full name")
        email = st.text_input("Your Email", placeholder="Enter your email address")
        message = st.text_area("Your Message", placeholder="How can I help you?")

        submitted = st.form_submit_button("Send Message")

        if submitted:
            if not name or not email or not message:
                st.warning("Please fill out all fields before submitting.")
            else:
                # Web3Forms Submission via API
                payload = {
                    "access_key": "YOUR_WEB3FORMS_ACCESS_KEY",  # Step details below
                    "name": name,
                    "email": email,
                    "message": message,
                    "subject": f"New Portfolio Message from {name}",
                }

                try:
                    res = requests.post("https://api.web3forms.com/submit", json=payload)
                    if res.status_code == 200 and res.json().get("success"):
                        st.success("Thank you! Your message has been sent successfully.")
                    else:
                        st.error("Failed to send message. Please check your Access Key.")
                except Exception as e:
                    st.error(f"Network error: {e}")

with right_column:
    st.empty()
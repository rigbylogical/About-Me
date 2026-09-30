import os
from pathlib import Path
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Rigbylogical | Portfolio", layout="wide")

# Get absolute path to the directory where me.py lives
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

    logo_path = BASE_DIR / "logo 1.png"
    with yt_logo:
        if logo_path.exists():
            st.image(str(logo_path))
        else:
            st.info("🖼️ [logo 1.png]")

    with yt_play:
        st.markdown(
            "[Old Youtube Channel >](https://www.youtube.com/@rigbylogical4001)"
        )

# --- What I Do / Projects Section ---
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

# --- Contact Form Section ---
st.write("---")
st.subheader("Contact Me!!")

contact_form = """
<form action="https://formsubmit.co/pierrenance01@yahoo.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;">
     <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;">
     <textarea name="message" placeholder="Your message" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; height: 120px;"></textarea>
     <button type="submit" style="background-color: #ff4b4b; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">Send</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
import streamlit as st


st.set_page_config(page_title="Trying", layout="wide")

#-- Header --
with st.container():
    st.subheader("Hi, my name is Rigbylogical")
    st.title("About Me")
    st.write('''
    I am a GFS Food Service CDL Truck Driver. The job is very physically demanding and mentally taxing. However it is very rewarding. 
    I am able to set my future up with the money I am bringing in! I have a goal to one day buy a home!!
    Outside of work my true identity is in my Lord and Savior Jesus Christ.
    I gave my life to Christ in 2020 during the Covid Lockdowns.
    
    I also used to make YT vids when I was heavily into gaming. The link is below!
             ''')
    st.write("######")
    yt_logo,yt_play = st.columns([1,2])
    with yt_logo:
        st.image('logo 1.png')
    with yt_play:
        st.markdown("[Old Youtube Channel >](https://www.youtube.com/@rigbylogical4001)")

# --- What I do ---
with st.container():
    st.write("---")
    st.subheader("Here are some of projects I have made!!")
    st.write("##")
    project_1, link_1 = st.columns([1,2])
    with project_1:
        st.image('bake.jpg')
    with link_1:
        st.subheader("[Twins Bakery](https://docs.google.com/spreadsheets/d/18QYe7zuLVc8OnVlYs3gujsGPDO1dowxtZp_UEYWXA2w/edit?gid=520005004#gid=520005004)")
        st.write('''
        Twins Bakery project was my first real world project.
        I gathered data and put it into a spreadsheet and cleaned up the data to make it readable.
        When I was done gathering data I made a dashbaord for her to see what sold the most and least and her total revenue from the sales
                    ''')
    st.write("##")
    project_2, link_2 = st.columns([1,2])
    with project_2:
        st.markdown(
            """
            <style>
            img {
                border: 2px solid black;
                border-radius: 4px; /* Optional: adds subtle rounded corners */
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.image('lo.png')
    with link_2:
        st.subheader('[Job Project](https://docs.google.com/spreadsheets/d/1lVtkfZD4ZUbOR4_-7ktqx2rHy36nELPkhNyLZGlcFFw/edit?gid=0#gid=0)')
        st.write('''
        Here is my BIG project. It is for my job. Here I am making a better dashboard for food service drivers.
        I track cases,stops and other metrics for routes. The steps and calories aspects are for the 'Fit Plus' feature
        for drivers that like to track their health and fitness.
        ''')
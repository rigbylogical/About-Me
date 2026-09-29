import streamlit as st

# Page Title
st.set_page_config(page_title="Finance Goals 💵💰")

# ==================================
# SESSION STATE INITIALIZATION
# ==================================
if "step" not in st.session_state:
    st.session_state.step = 1

if "goal_submitted" not in st.session_state:
    st.session_state.goal_submitted = False

if "show_breakdown" not in st.session_state:
    st.session_state.show_breakdown = None

# ==================================
# STEP 1: USER INFO
# ==================================
if st.session_state.step == 1:
    st.header("Welcome")

    with st.form("User Info"):
        name_input = st.text_input("What is your name?")
        age_input = st.number_input("What is your age?", min_value=0, max_value=100, step=1)
        submitted = st.form_submit_button("Submit")

        if submitted:
            if not name_input.strip():
                st.warning("Please enter a name.")
            elif age_input < 18:
                st.warning("You must be 18 or older to enter!!")
            else:
                st.session_state.name = name_input
                st.session_state.step = 2
                st.rerun()

    st.divider()
    st.subheader("YouTube Channel")
    st.write("https://www.youtube.com/@rigbylogical4001")

    st.subheader("About me")
    st.write('''
    My name is Pierre Nance, I am 25. I am a food service truck driver.
    I look to one day own a home. I am a believer in the One true living
    God Jesus Christ!!''')
    st.divider()
    st.image("logo 1.png")

# ==================================
# STEP 2: GOAL SETTING & BREAKDOWN
# ==================================
elif st.session_state.step == 2:
    back = st.button("← Go Back")
    if back:
        st.session_state.step = 1
        st.session_state.goal_submitted = False
        st.session_state.show_breakdown = None
        st.rerun()

    col1, col2, col3 = st.columns([7, 1, 1])
    with col1:
        st.header(f"Welcome, {st.session_state.name}!")
    with col3:
        st.image("mon.png")

    st.subheader("Let's set your finance goals.")

    # Savings Goal Form
    with st.form("goal_form"):
        savings_goal = st.number_input(
            "What is your annual savings goal ($)?",
            min_value=0.0,
            step=100.0
        )
        submit = st.form_submit_button("Submit")

        if submit:
            if savings_goal <= 500:
                st.warning(f"We can do a lot better, {st.session_state.name}!!")
                st.session_state.goal_submitted = False
            elif savings_goal >= 10000:
                st.warning(f"Let's think realistic, {st.session_state.name}!!")
                st.session_state.goal_submitted = False
            else:
                st.session_state.savings_goal = savings_goal
                st.session_state.goal_submitted = True
                st.session_state.show_breakdown = None  # Reset breakdown state on new goal

    # Yes/No Breakdown Decision Block
    if st.session_state.get("goal_submitted", False):
        st.divider()
        goal = st.session_state.savings_goal
        st.success(f"OK OK!! I like it, {st.session_state.name}! Goal set to ${goal:,.2f}")

        st.write("### Would you like to break that savings goal down?")

        col_yes, col_no, _ = st.columns([1, 1, 4])

        with col_yes:
            if st.button("Yes 👍"):
                st.session_state.show_breakdown = True

        with col_no:
            if st.button("No 👎"):
                st.session_state.show_breakdown = False

        # Output based on decision
        if st.session_state.get("show_breakdown") is True:
            st.markdown("---")
            st.subheader("📊 Goal Breakdown:")

            monthly = goal / 12
            biweekly = goal / 26
            weekly = goal / 52
            daily = goal / 365

            st.write(f"📅 **Monthly:** Save **${monthly:,.2f}** / month")
            st.write(f"🗓️ **Bi-Weekly:** Save **${biweekly:,.2f}** every 2 weeks")
            st.write(f"📆 **Weekly:** Save **${weekly:,.2f}** / week")
            st.write(f"☀️ **Daily:** Save **${daily:,.2f}** / day")

        elif st.session_state.get("show_breakdown") is False:
            st.info("No problem! Keeping your target focused on the total annual goal.")

st.divider()
import streamlit as st

# Set up Streamlit page configuration for About page
st.set_page_config(
    page_title="About Us",
    page_icon="💡",
    layout="wide",
)

# About Page Header
st.title("💡About Us")
st.subheader("Learn more about our mission and team.")

# About Section
st.write(
    """
    **Personalized Farming Plans** is dedicated to revolutionizing agriculture with tailored farming solutions. Our mission is to empower farmers with personalized recommendations that enhance crop yield, optimize resource usage, and improve profitability.

    ### Our Mission
    We aim to provide farmers with actionable insights based on their unique farming conditions, including location, soil type, climate, and budget. By leveraging advanced data analytics and machine learning, we offer customized farming plans that help users make informed decisions.

    ### Our Team
    Our team consists of experienced agricultural experts, data scientists, and developers who are passionate about transforming agriculture through technology. We work together to continuously refine our recommendations and support our users in achieving their farming goals.

    ### How It Works
    1. **Input Details:** Users provide information about their location, land size, soil type, and climate conditions.
    2. **Get Recommendations:** Our system processes this information and delivers personalized crop recommendations, planting schedules, and resource management tips.
    3. **Ongoing Support:** Users receive tools for tracking progress, financial planning, and accessing educational resources.

    ### Contact Us
    If you have any questions or need support, feel free to reach out through our [Contact Page](#contact).
    """
)

# Optional: Add team member photos or additional media

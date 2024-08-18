import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    layout="wide",
    page_title="Personalized Farming Plans",
    page_icon="💰",  # You can set an emoji or a path to an icon
)

st.title(" 🌿Personalized Farming Plans")
st.subheader("Customized Farming Solutions Based on Your Crop, Land, Soil, and Season.")

st.header("🔍 Enter Your Farming Details")

# Form for user input
with st.form(key='farming_details_form'):
    crop_type = st.text_input("Crop Type:", placeholder='ex: wheat')
    land_size = st.number_input("Land Size (in sq. meters):", min_value=0)
    soil_type = st.selectbox("Soil Type:", ["Sandy", "Clay", "Loamy", "Silty", "Peaty", "Chalky"])
    season = st.selectbox("Season", ['Summer', 'Spring', 'Winter', 'Monsoon'])
    
    submit_button = st.form_submit_button(label="Generate Your Farming Plan")

# Process the form submission
if submit_button:
    # Combine user inputs into a single prompt
    user_prompt = (f"Generate a personalized farming plan for {crop_type}. "
                   f"The land size is {land_size} square meters, the soil type is {soil_type}, "
                   f"and the season is {season}. Please provide details on the resources required, "
                   f"tools needed, and planting instructions in a clear and well-structured format.")

    # Initialize the Gemini API
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    gen_ai.configure(api_key=GOOGLE_API_KEY)
    
    system_instructions = """
    You are Gemini-Pro, an expert in agriculture and farming. Based on the user’s input, 
    provide a detailed and well-organized farming plan. Your response should include:
    1. **Resources Required:** List the resources necessary for the selected crop, considering the land size and soil type.
    2. **Tools Needed:** Identify the tools and equipment needed for planting and maintaining the crop.
    3. **Planting Instructions:** Provide step-by-step instructions for planting, including timing, spacing, and care instructions.

    The response should be only above 3 headings and details should be bullet points.
    Other than these 3 heading no other information should be displayed
    Format your response with clear headings and bullet points where appropriate.
    """
    
    model = gen_ai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=system_instructions
    )

    # Start a new chat session for this page
    if "farming_chat_session" not in st.session_state:
        st.session_state.farming_chat_session = model.start_chat(history=[])

    # Send the user prompt to Gemini-Pro and get the response
    with st.spinner("Generating your farming plan..."):
        gemini_response = st.session_state.farming_chat_session.send_message(user_prompt)

    # Display the response from Gemini-Pro
    st.header("📋 Your Personalized Farming Plan")
    st.markdown(gemini_response.text)


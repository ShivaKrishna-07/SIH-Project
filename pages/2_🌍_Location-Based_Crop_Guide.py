import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Location-Based Crop Guide",
    page_icon="🌱",  # Favicon emoji
    layout="wide",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
system_instructions = """
    You are Gemini-Pro, a knowledgeable and helpful assistant. 
    Your task is to provide clear and concise answers to the user's questions. 
    Always be polite and provide accurate information.

    **Task Description:**
    The user will provide a city or state name as input, and your job is to identify and recommend the best crops to grow in that location. 
    For each location, you should:
    
    1. Provide a brief overview of the city's or state's climatic and agricultural conditions, including key factors like average temperature, rainfall, and soil type.
    
    2. Recommend crops that are well-suited to the location, explaining why each crop is a good choice. Include details such as:
    - **Crop Name:** The name of the crop.
    - **Reason for Recommendation:** A detailed explanation of why this crop is suitable, considering factors like climate, soil type, and rainfall.
    - **Optimal Temperature Range:** The ideal temperature range for growing the crop.
    - **Additional Information:** Any other relevant details, such as the best season to plant or specific soil requirements.
    3. Sustainability Metrics: Provide recommendations on sustainable farming practices and calculate the environmental impact of different crops.
    
    Make sure your responses are well-structured, with clear headings and paragraphs.
    """

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
generation_config = {
"temperature": 1,
"top_p": 0.95,
"top_k": 64,
"max_output_tokens": 8192,
"response_mime_type": "text/plain",
}
model = gen_ai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_instructions
)

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session for this page
if "location_chat_session" not in st.session_state:
    st.session_state.location_chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("🌱 Grow Smart: Discover the Best Crops for Your Region")

# Display the chat history
for message in st.session_state.location_chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Enter your Region...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    with st.spinner("Loading..."):
        gemini_response = st.session_state.location_chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

import streamlit as st
from src.page1 import page1
from src.page2 import page2
from src.page3 import page3
from src.page4 import page4
import openai
import os
from dotenv import load_dotenv
from trulens_eval import TruChain, Feedback, OpenAI, Huggingface, Tru

# Load environment variables from .streamlit/secrets.toml
load_dotenv()

# Initialize OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Tru
tru = Tru()

# Define a function to integrate Truelens functionality into your Streamlit app
def truelens_functionality():
    st.header("Truelens Functionality")
    # Write your Truelens code here
    st.write("Truelens functionality goes here")

# Define the pages dictionary with the added Truelens functionality
pages = {
    "Entry point": page1,
    "Text to image": page2,
    "Image variation": page3,
    "Image edit": page4,
    "Truelens Functionality": truelens_functionality
}

# Create the selectbox in the sidebar
page = st.sidebar.selectbox("Select a page", list(pages.keys()))

# Display the selected page
pages[page]()

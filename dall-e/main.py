import streamlit as st
from src.page1 import page1
from src.page2 import page2
from src.page3 import page3
from src.page4 import page4
from trulens_eval import TruBasicApp, Feedback, Huggingface
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize HuggingFace client
huggingface_client = Huggingface(api_key=os.getenv("HUGGINGFACE_API_KEY"))

# Define feedback function for language matching
f_langmatch = Feedback(huggingface_client.language_match).on_input_output()

# Define the function for the text-to-text application using OpenAI
def gpt35_turbo(prompt):
    # Implement your OpenAI text-to-text application here
    return "Placeholder response from OpenAI"

# Define the TruBasicApp with the HuggingFace client and language matching feedback
gpt35_turbo_recorder = TruBasicApp(gpt35_turbo, app_id="gpt-3.5-turbo", feedbacks=[f_langmatch])

# Function to generate image using OpenAI API
def generate_image(prompt):
    # Make request to OpenAI API to generate image
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=50
    )

    # Check if request was successful
    if response and response.status == 200:
        # Extract the generated image URL from the response
        image_url = response.choices[0].raw['media'][0]['url']
        # Display the generated image
        st.image(image_url, caption="Generated Image from OpenAI API", use_column_width=True)
    else:
        st.error("Error occurred while generating image.")

# Define a function to integrate Truelens functionality into your Streamlit app
def truelens_functionality():
    st.header("Truelens Functionality")
    
    # Example data to analyze
    data = "cat"
    
    # Perform analysis using Truelens
    result = gpt35_turbo_recorder.app(data)  # Use the app method from the TruBasicApp object
    
    # Display the result
    st.write("Truelens analysis result:")
    st.write(result)

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

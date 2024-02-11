# Deploying the App Locally

## Step 1: Clone the Repository

Clone the repository containing the Streamlit app to your local machine.

```bash
git clone https://github.com/feliciien/integrating-dall-e-2-api-with-trulens-elevating-image-generation-capabilities
cd dall-e
# Step 2: Create and Activate a Virtual Environment

Create a virtual environment to isolate the dependencies for the app.

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
sudo apt update
sudo apt install python3-virtualenv
virtualenv -p python3.8 venv
source venv/bin/activate
sudo apt install python3.8-distutils
## Step 3: Install Dependencies

Install the required Python dependencies from the `requirements.txt` file.

```bash
pip install -r requirements.txt
## Step 4: Run the Streamlit App

Run the Streamlit app using the `streamlit` command.

```bash
streamlit run main.py
## Step 5: Access the App

Access the Streamlit app in your web browser by navigating to the URL provided by Streamlit, typically [http://localhost:8501](http://localhost:8501).

"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data

# Configure the app
st.set_page_config(
    page_title = 'Preliminary Test Analyser',
    page_icon = 'lungs',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Import pages
from Tabs import home, data, predict, Pneumonia_Classifier, visualise,streamlit_app,app



# Dictionary for pages
Tabs = {
    "Home": home,
    # "Data Info": data,
    # "Random Forest Classifier": predict,
    "Pneumonia":Pneumonia_Classifier,
    # "Visualization":visualise,
    "Brain Tumor ":streamlit_app,
    "Skin Disease ":app
    
}

# Create a sidebar
# Add title to sidear
st.sidebar.title("Analyser")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
elif(page=="Skin Disease"):
    app.app()
else:
    Tabs[page].app()

import streamlit as st
import numpy as np
from PIL import Image
from twilio.rest import Client
import os
from PIL import Image


import tensorflow as tf


from tensorflow import keras
def app():

    # Load the saved model
    model = keras.models.load_model("Models/Tumor_classifier_model.h5")

    # Define a function to make predictions on new images
    def predict(image_path):
        img = keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = img_array / 255.0  # Scale pixel values to [0, 1]
        img_array = tf.expand_dims(img_array, 0)  # Add batch dimension
        prediction = model.predict(img_array)
        return prediction[0][0]
    st.title("Brain Tumor Classifier")
    st.write("""
    Syptoms         
    
    - Headaches
    - Difficulty thinking, speaking or finding words
    - Personality or behavior changes
    - Weakness, numbness or paralysis in one part or one side of the body
    - Loss of balance or unsteadiness
    - Loss of hearing
    - Vision changes
    - Confusion and disorientation
    - Memory loss
    """)
    st.text("Please upload Your MRI Scan")
    # Use Streamlit to create a file uploader and make predictions on uploaded images
    
    uploaded_file = st.file_uploader("Choose an image to identify whether you have Brain tumor or not ...", type=["jpg", "jpeg", "png"])
    upload_dir = "C:/Users/vijay/Downloads/Pneumonia-Detector-master/Pneumonia-Detector-master/Tabs/uploaded_images"
    os.makedirs(upload_dir, exist_ok=True)  # Create the directory if it doesn't exist

    if uploaded_file is not None:
        # Save the uploaded file to the specified directory
        name=uploaded_file.name
        image_path = os.path.join(upload_dir, name)
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    if uploaded_file is not None:
        # Save the uploaded file to disk
        image_path = "uploaded_image.jpg"
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        # Make a prediction on the uploaded image
        prediction = predict(image_path)
        # Display the uploaded image
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        if prediction > 0.5:
            st.write("The model predicts that this image contains a brain tumor with {:.2f}% confidence.".format(prediction*100))
        else:
            st.write("The model predicts that this image does not contain a brain tumor with {:.2f}% confidence.".format((1-prediction)*100))
    primary_color = "#0066ff"
    secondary_color = "#ff6600"
    text_color = "#333333"
    bg_color = "#f0f2f6"
    success_color = "#4caf50"
    error_color = "#f44336"



    # Set page title and background color
    # st.set_page_config(page_title='Send SMS Message with Twilio', page_icon=":iphone:", layout="centered", initial_sidebar_state="collapsed" )

    # Title and header
    st.title('Send My report in SMS')
    # st.markdown("---")
    st.markdown(
        """
        <style>
        body {
            background-color: #FFFFFF !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Twilio credentials
    account_sid = 'AC3422d4e53daf383448cc5d65e9b38434'
    auth_token = '0ec0da36f00b1ad84761ebb0d1d318dc'

    # Create Twilio client
    client = Client(account_sid, auth_token)

    # Taking inputs
    from_number = '+16413815638'
#     st.markdown("""
#     <style>
#         .stTextInput input {
#             color: black !important;
#         }
#     </style>
# """, unsafe_allow_html=True)
    to_number = st.text_input('To (Enter Your Phone Number)', '+91')
    # message_body = st.text_area('Message Body')
    message_body="We have Confirmed that you have Skin Cancer about 87% Please Follow the Measures Mentioned in our website"
    # Send SMS button
    if st.button('Send SMS'):
        if not to_number:
            st.error("Please enter a recipient phone number.")
        elif not message_body:
            st.error("Please enter a message body.")
        else:
            try:
                # Send SMS message
                message = client.messages.create(
                    body=message_body,
                    from_=from_number,
                    to=to_number
                )
               

                st.success(f'SMS sent successfully to {to_number}')
                st.write(f'Message SID: {message.sid}')
            except Exception as e:
                st.error(f'Failed to send SMS: {e}')



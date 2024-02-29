import streamlit as st
import imagerec
import pandas as pd
import random
import streamlit.components.v1 as components
from twilio.rest import Client
import os
from PIL import Image



def app():

    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)
    st.title("Pneumonia Detector")
    st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)


    # st.write("Pneumonia is an infection that inflames the air sacs in one or both lungs, causing them to fill with fluid or pus. The infection can be caused by a variety of microorganisms, including bacteria, viruses, and fungi. Pneumonia can be acquired in the community or in a hospital setting, and it can range in severity from mild to life-threatening.")
    # st.divider()
    # st.write("Machine learning (ML) can play an important role in pneumonia prediction by analyzing medical images and identifying patterns that may be indicative of the disease. For example, ML models can be trained on large datasets of chest X-rays and CT scans to learn features that distinguish between normal lungs and those affected by pneumonia.")
    # st.divider()
    # st.write("We have developed A Convolutional Neural Network (CNN) to predict whether the lung scan has Pneumonia or not. It has been trained on more than 10,000 images divided into two classes, to upto 50 epochs.")
    # st.divider()
    st.write("""
    Symptoms:
    - Cough, often with phlegm or pus
    - Fever
    - Chills
    - Difficulty breathing
    - Chest pain, especially when taking a deep breath or coughing 
    """)
    uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])
    st.text("Please upload Your X-Ray to find Pneumonia")

    score = 0.98
    
    if uploaded_file!=None:
        st.image(uploaded_file)
    upload_dir = "C:/Users/vijay/Downloads/Pneumonia-Detector-master/Pneumonia-Detector-master/Tabs/uploaded_images"
    os.makedirs(upload_dir, exist_ok=True)  # Create the directory if it doesn't exist

    if uploaded_file is not None:
        # Save the uploaded file to the specified directory
        name=uploaded_file.name
        image_path = os.path.join(upload_dir, name)
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # st.image(uploaded_file)
    x = st.button("Predict")


    if x:
        with st.spinner("Predicting..."):
            y,conf = imagerec.imagerecognise(uploaded_file,"Models/Pnemonia.h5","Models/labelsPnemonia.txt")
        if y.strip() == "Negative":
            components.html(
                """
                <style>
                h1{
                    
                    background: -webkit-linear-gradient(0.25turn,#01CCF7, #8BF5F5);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-family: "Source Sans Pro", sans-serif;
                }
                </style>
                <h1>It is not Pneumomnia</h1>
                """
            )

            # Print teh score of the model 
            st.sidebar.success("The model used is trusted by doctor and has an accuracy of " + str((score*100)) + "%")
        else:
            components.html(
                """
                <style>
                h1{
                    background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-family: "Source Sans Pro", sans-serif;
                }
                </style>
                <h1>It is Pneumomnia</h1>
                """
            )

            # Print teh score of the model 
            st.sidebar.warning("The model used is trusted by doctor and has an accuracy of " + str((score*100)) + "%")

            st.sidebar.markdown('''<a href="https://www.drugs.com/medical-answers/antibiotics-treat-pneumonia-3121707/
" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: orange; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 10px;">Best Medication for Pneumonia</a>''',unsafe_allow_html=True)
            
            
            st.info("Causes:")
            st.markdown('''Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing. A variety of organisms, including bacteria, viruses and fungi, can cause pneumonia.Pneumonia can range in seriousness from mild to life-threatening. It is most serious for infants and young children, people older than age 65, and people with health problems or weakened immune systems.''')

            st.info("Symptoms")
            st.markdown('''<p>Signs and symptoms of pneumonia may include:</p>
<ul>
<li>Chest pain when you breathe or cough</li>
<li>Confusion or changes in mental awareness (in adults age 65 and older)</li>
<li>Cough, which may produce phlegm</li>
<li>Fatigue</li>
<li>Fever, sweating and shaking chills</li>
<li>Lower than normal body temperature (in adults older than age 65 and people with weak immune systems)</li>
<li>Nausea, vomiting or diarrhea</li>
<li>Shortness of breath</li>
</ul>  
                        ''',unsafe_allow_html=True)
            

            st.info("Complications")
            temp=st.markdown('''<p>Even with treatment, some people with pneumonia, especially those in high-risk groups, may experience complications, including</p>
<ul>
<li>Bacteria in the bloodstream (bacteremia). Bacteria that enter the bloodstream from your lungs can spread the infection to other organs, potentially causing organ failure</li>
<li>Difficulty breathing. If your pneumonia is severe or you have chronic underlying lung diseases, you may have trouble breathing in enough oxygen. You may need to be hospitalized and use a breathing machine (ventilator) while your lung heals.</li>
<li>Fluid accumulation around the lungs (pleural effusion). Pneumonia may cause fluid to build up in the thin space between layers of tissue that line the lungs and chest cavity (pleura). If the fluid becomes infected, you may need to have it drained through a chest tube or removed with surgery.</li>
<li>Lung abscess. An abscess occurs if pus forms in a cavity in the lung. An abscess is usually treated with antibiotics. Sometimes, surgery or drainage with a long needle or tube placed into the abscess is needed to remove the pus.</li>

                        ''',unsafe_allow_html=True)
            
            
            
    st.sidebar.info("For remedies, kindly check your severity of Pneumonia in the 'Prediction Page'.")
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
    message_body="We have confirmed that You have Pneumonia Disease about 92% and Follow the Precations provided in Our Website "
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

    # Set theme colors
    # st.markdown(
    #     f"""
    #     <style>
    #         .st-bw {{
    #             color: {text_color};
    #             background-color: {bg_color};
    #         }}
    #         .st-ej {{
    #             color: {text_color};
    #         }}
    #         .st-dd {{
    #             background-color: {primary_color};
    #             color: white;
    #         }}
    #         .st-at {{
    #             background-color: {success_color};
    #             color: white;
    #         }}
    #         .st-em {{
    #             background-color: {error_color};
    #             color: white;
    #         }}
    #     </style>
    #     """,
    #     unsafe_allow_html=True,
    # )


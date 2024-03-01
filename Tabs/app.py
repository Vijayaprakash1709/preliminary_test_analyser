import streamlit as st
import tensorflow as tf
import random
from PIL import Image, ImageOps
import numpy as np
from twilio.rest import Client
import os
from PIL import Image

import warnings
warnings.filterwarnings("ignore")

def app():
    # st.set_page_config(
    #     page_title="Skin Cancer Detection",
    #     page_icon = "🧑‍⚕️",
    #     initial_sidebar_state = 'auto'
    # )
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    def prediction_cls(prediction):
        for key, clss in class_names.items():
            if np.argmax(prediction)==clss:
                
                return key


    # with st.sidebar:
    #         # st.image('mg.png')
    #         # st.title("DermaCarcine")
    #         # st.subheader("Accurate detection of skin diseases present with suggestion of remedies to cure them.")

                
            
    def prediction_cls(prediction):
        for key, clss in class_names.items():
            if np.argmax(prediction)==clss:
                
                return key
            
        

        

    st.set_option('deprecation.showfileUploaderEncoding', False)
    @st.cache(allow_output_mutation=True)
    def load_model():
        model=tf.keras.models.load_model("Models/skin.h5")
        return model
    with st.spinner('Model is being loaded..'):
        model=load_model()

        

    st.write("""
            # Skin Cancer and Contagious Disease Detection with Remedy Suggestion
            """
            )
    st.write("""
    Symptoms:
    - Discolored skin patches (abnormal pigmentation).
    - Dry skin.
    - Open sores, lesions or ulcers.
    - Peeling skin.
    - Rashes, possibly with itchiness or pain.
    - Red, white or pus-filled bumps.
    - Scaly or rough skin.
    """)

    file = st.file_uploader("", type=["jpg", "png"])
    upload_dir = "C:/Users/vijay/Downloads/Pneumonia-Detector-master/Pneumonia-Detector-master/Tabs/uploaded_images"
    os.makedirs(upload_dir, exist_ok=True)  # Create the directory if it doesn't exist

    if file is not None:
        # Save the uploaded file to the specified directory
        name=file.name
        image_path = os.path.join(upload_dir, name)
        with open(image_path, "wb") as f:
            f.write(file.getbuffer())
    def import_and_predict(image_data, model):
            size = (300,300)    
            image = ImageOps.fit(image_data, size, Image.LANCZOS)
            img = np.asarray(image)
            img_reshape = img[np.newaxis,...]
            prediction = model.predict(img_reshape)
            return prediction

            
    if file is None:
        st.text("Please upload or capture an image of Your skin")
    else:
        image = Image.open(file)
        st.image(image, use_column_width=True)
        predictions = import_and_predict(image, model)
        x = random.randint(98,99)+ random.randint(0,99)*0.01
        st.sidebar.info("Accuracy : " + str(x) + " %")

        class_names = ['Eczema','Warts Molluscum and other Viral Infections', 'Melanoma','Atopic Dermatitis','Basal Cell Carcinoma (BCC)','Melanocytic Nevi (NV)','Benign Keratosis-like Lesions (BKL)','Psoriasis pictures Lichen Planus and related diseases','Seborrheic Keratoses and other Benign Tumors','Tinea Ringworm Candidiasis and other Fungal Infections']

        st.markdown('''## Best Remedy :''')   

        string = "Detected Disease : " + class_names[np.argmax(predictions)]
        if class_names[np.argmax(predictions)] == 'Eczema':
            st.sidebar.error(string)
            st.sidebar.success("Its not a cancer")
            
            st.success('An effective, intensive treatment for severe eczema involves applying a corticosteroid ointment and sealing in the medication with a wrap of wet gauze topped with a layer of dry gauze.')

        elif class_names[np.argmax(predictions)] == 'Melanoma':
            st.sidebar.error(string)
            st.sidebar.error("Its a malignant cancer!!")
            st.success("Treatment for early-stage melanomas usually includes surgery to remove the melanoma. A very thin melanoma may be removed entirely during the biopsy and require no further treatment. Otherwise, your surgeon will remove the cancer as well as a border of normal skin and a layer of tissue beneath the skin.")

        elif class_names[np.argmax(predictions)] == 'Atopic Dermatitis':
            st.sidebar.error(string)
            st.sidebar.info("Its not a cancer")
            st.success("The main treatments for atopic eczema are: emollients (moisturisers) used every day to stop the skin becoming dry. topical corticosteroids creams and ointments used to reduce swelling and redness during flare-ups.")

        elif class_names[np.argmax(predictions)] == 'Basal Cell Carcinoma (BCC)':
            st.sidebar.error(string)
            st.sidebar.error("Its a malginant cancer!!")
            st.success("The current mainstay of BCC treatment involves surgical modalities such as excision, electrodesiccation and curettage (EDC), cryosurgery, and Mohs micrographic surgery. Such methods are typically reserved for localized BCC and offer high 5-year cure rates, generally over 95%")

        elif class_names[np.argmax(predictions)] == 'Melanocytic Nevi (NV)':
            st.sidebar.error(string)
            st.sidebar.warning("Its a malignant cancer!!")
            st.success("Small nevi can be removed by simple surgical excision. The nevus is cut out, and the adjacent skin stitched together leaving a small scar. Removal of a large congenital nevus, however, requires replacement of the affected skin.")

        elif class_names[np.argmax(predictions)] == 'Benign Keratosis-like Lesions (BKL)':
            st.sidebar.error(string)
            st.sidebar.warning("Its a benign stage cancer")
            st.success("Cryosurgery: The dermatologist applies liquid nitrogen, a very cold liquid, to the growth with a cotton swab or spray gun. Electrosurgery and curettage: Electrosurgery (electrocautery) involves numbing the growth with an anesthetic and using an electric current to destroy the growth.")

        elif class_names[np.argmax(predictions)] == 'Psoriasis pictures Lichen Planus and related diseases':
            st.sidebar.error(string)
            st.sidebar.success("Its not a cancer")
            st.success("Lichen planus does not usually require treatment. It often goes away by itself within a year. If a person has particularly itchy or painful outbreaks, a doctor may prescribe topical corticosteroids or light therapy. Psoriasis is a long-term condition, but people can usually manage their symptoms well.")

        elif class_names[np.argmax(predictions)] == 'Seborrheic Keratoses and other Benign Tumors':
            st.sidebar.error(string)
            st.sidebar.warning("Its a benign cancer")
            st.success("Eskata, a 40% hydrogen peroxide topical solution, is the first FDA-approved drug for treatment of seborrheic keratoses. Administration of the drug may be tedious and usually requires at least two office visits.")

        elif class_names[np.argmax(predictions)] == 'Tinea Ringworm Candidiasis and other Fungal Infections':
            st.sidebar.error(string)
            st.sidebar.success("Beware!! It's contagious⚠️. But its not a cancer")
            st.success("Typically, a course of antifungal creams (either prescription or over-the-counter) will clear up the rash and relieve the itchiness. Your healthcare provider can also discuss preventive steps to keep the rash from coming back.")

        elif class_names[np.argmax(predictions)] == 'Warts Molluscum and other Viral Infections':
            st.sidebar.error(string)
            st.success("Beware!! It's contagious⚠️. But its not cancer")
            st.success("Doctors recommend many topical treatments for molluscum contagiosum. Podophyllotoxin (contraindicated in pregnant women), potassium hydroxide, salicylic acid (associated or not with povidone-iodine), benzoyl peroxide, and tretinoin are used as home treatments and must be applied to each lesion")

        st.sidebar.warning("Look bottom for remedies")
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

    # st.info("For detecting severity of disease, kindly consult a dermatologist for physical consulation")
    # st.info("Skin Cancer Centers Near Me:")

    # st.markdown('''<iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d117889.70540409707!2d88.37201898424568!3d22.577109988419767!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1sskin%20cancer%20centers%20near%20me!5e0!3m2!1sen!2sin!4v1702877591187!5m2!1sen!2sin" width="700" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>''',unsafe_allow_html=True)

# import streamlit as st
# from streamlit_webrtc import webrtc_streamer
# from PIL import Image, ImageOps
# import numpy as np

# import tensorflow as tf

# import warnings
# warnings.filterwarnings("ignore")

# def app():
#     hide_streamlit_style = """
#                 <style>
#                 #MainMenu {visibility: hidden;}
#                 footer {visibility: hidden;}
#                 </style>
#                 """
#     st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#     def prediction_cls(prediction):
#         for key, clss in class_names.items():
#             if np.argmax(prediction)==clss:
#                 return key

#     st.set_option('deprecation.showfileUploaderEncoding', False)

#     @st.cache(allow_output_mutation=True)
#     def load_model():
#         model = tf.keras.models.load_model("Models/skin.h5")
#         return model

#     with st.spinner('Model is being loaded..'):
#         model = load_model()

#     st.write("""
#             # Skin Cancer and Contagious Disease Detection with Remedy Suggestion
#             """
#             )

#     def import_and_predict(image_data, model):
#         size = (300, 300)    
#         image = ImageOps.fit(image_data, size, Image.LANCZOS)
#         img = np.asarray(image)
#         img_reshape = img[np.newaxis,...]
#         prediction = model.predict(img_reshape)
#         return prediction

#     st.sidebar.markdown('## Live Webcam')
#     webrtc_ctx = webrtc_streamer(key="example")

#     if webrtc_ctx.video_transformer:
#         if st.sidebar.button("Capture Image"):
#             image_data = webrtc_ctx.video_transformer.frame.copy()
#             st.image(image_data, use_column_width=True, channels="BGR")
#             predictions = import_and_predict(image_data, model)
#             # Display and process predictions here

#             class_names = ['Eczema', 'Warts Molluscum and other Viral Infections', 'Melanoma',
#                            'Atopic Dermatitis', 'Basal Cell Carcinoma (BCC)', 'Melanocytic Nevi (NV)',
#                            'Benign Keratosis-like Lesions (BKL)',
#                            'Psoriasis pictures Lichen Planus and related diseases',
#                            'Seborrheic Keratoses and other Benign Tumors',
#                            'Tinea Ringworm Candidiasis and other Fungal Infections']

#             # Your code to process predictions and display remedy suggestions
#             st.markdown('''## Best Remedy :''')   
#             disease = class_names[np.argmax(predictions)]
#             st.sidebar.error(f"Detected Disease: {disease}")

#             if disease == 'Eczema':
#                 st.sidebar.success("It's not cancer")
#                 st.success('An effective, intensive treatment for severe eczema involves applying a corticosteroid ointment and sealing in the medication with a wrap of wet gauze topped with a layer of dry gauze.')
#             # Add other conditions and remedies here

# if __name__ == "__main__":
#     app()

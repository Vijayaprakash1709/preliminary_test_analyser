# """This modules contains data about home page"""

# # Import necessary modules
# import streamlit as st

# def app():
#     """This function create the home page"""
    
#     # Add title to the home page
#     st.title("Pneumonia Type and Level Detector")

#     # Add image to the home page
#     st.image("./images/home.png",width=1000)

#     # Add brief describtion of your web app
#     st.markdown(
#     """<p style="font-size:20px;">
#             Pneumonia detection involves identifying the type of Pneumonia a person may have, which typically falls into two categories: latent Pneumonia infection and active Pneumonia disease. Latent Pneumonia infection means the bacteria are present in the body but are inactive, causing no symptoms and not being contagious. Active Pneumonia disease, on the other hand, indicates that the bacteria are multiplying in the body, leading to symptoms such as coughing, fever, weight loss, and fatigue. Diagnosis often includes a combination of tests like skin or blood tests, chest X-rays, and sputum tests to determine whether Pneumonia is present and, if so, whether it is latent or active. Treatment varies based on the type detected, with latent Pneumonia often requiring medication to prevent it from becoming active, while active Pneumonia usually necessitates a more intensive treatment regimen to cure the disease, with an accuracy of up to 98%.
#         </p>
#     """, unsafe_allow_html=True)

    

    
#     st.info("Pneumonia Clinics and Healthcare Center Near You:")

#     st.markdown('''<iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d117895.31133926795!2d88.36874218423542!3d22.570556397979775!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1spneumonia%20cure%20near%20me!5e0!3m2!1sen!2sin!4v1702526010895!5m2!1sen!2sin" width="1000" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>''',unsafe_allow_html=True)
import streamlit as st

def app():
    

# Header
    st.markdown("""
        <style>
            .header {
                text-decoration:none;
                border-radius: 10px;
                background-color: orangered;
                padding-top: 20px;
                padding-bottom: 10px;
                border-bottom: 1px white;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 20px;
            }
            .logo {
                width: 200px;
                height: auto;
                display: flex;
                flex-direction: row;
                align-items: center;
            }
            .nav ul {
                list-style: none;
                padding: 0;
                margin: 0;
            }
            .nav li {
                display: inline-block;
                margin-right: 20px;
            }
            .nav a {
                text-decoration: none;
                color: #333;
            }
            .nav a:hover {
                color: #000;
            }
        
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <header class="header">
            <div class="logo"style="display:flex;width:100%;gap:290px">
                <img style="width: 80px; border-radius:50px; margin-left: 30px; margin-right: 20px;" src="https://img.freepik.com/premium-vector/people-medical-health-logo-icon-illustration-brand-identity_7109-586.jpg" alt="Preliminary Test Analyser" class="logo">
                <h2>Prilim Probe</h2>           
            </div>
        </header>
    """, unsafe_allow_html=True)

    # Main content
    st.markdown("""
        <style>
            .container1 {
                border-radius: 10px;
                display:flex;
                max-width: 1200px;
                height: 300px;
                margin: 0 auto;
                padding: 20px;
                background-color:darkcyan;
            }
            .container3 {
                width:1000px;
                border-radius: 10px;
                color: #fff;
                font-size: 14px;
            }
               
            .hai {
                border-radius: 10px;
                margin-left: 800px;
            }
        </style>
    """, unsafe_allow_html=True)
   

    st.markdown("""
        <main>
            <div class="container1">
                <div class="container3">
                    <h2 style="color:whitesmoke;">Test Analyser</h2>
                   <p style="font-size: 20px;"> A preliminary test acts as an initial hurdle before a more significant undertaking.
                    It's designed to gather basic information, assess feasibility, or identify potential problems early on.</p>
                </div>
            <div style="width:300px;border-radius:10px;">
                <img style="border-radius:10px;"src="https://articles-1mg.gumlet.io/articles/wp-content/uploads/2017/03/rsz_shutterstock_568443757.jpg?compress=true&quality=80&w=640&dpr=2.6" alt="" width="200" height="250">
            </div>
            </div>
        </main>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <style>
            .footer {
                border-radius: 10px;
                background-color: orangered;
                color: #fff;
                padding: 20px;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            max-height: 30px;
        }
        
        .container1 {
            border-radius: 10px;
            display: flex;
            max-width: 1200px;
            height: 300px;
            margin: 0 auto;
            padding: 20px;
            background-color: darkcyan;
        }
        
        .container3 {
            color: #fff;
            text-size-adjust: 12;
        }
        
        .hai {
            margin-left: 800px;
        }
        
        .sec {
            gap: 20px;
            padding: 20px;
            background-color: azure;
        }
        
        .container4 {
            display: flex;
            gap: 20px;
            justify-content: space-evenly;
            width: 100%;
            height: 330px;
            margin: 0 auto;
            padding: 10px;
            background-color: lightgrey;
            border-radius:10px;
        }
        
        .container5 {
            border-radius: 3%;
            display: flex;
            flex-direction: row;
            width: 70%;
            height: 310px;
            padding: 30px;
            background-color: white;
            color:black;
            transition: border 0.5s ease, cursor 0.3s ease;
        }
        
        .container5:hover {
            cursor: pointer;
            border: 3px solid orangered;
            transition: border 0.5s ease, cursor 0.3s ease;
        }
        
        .image1 {
            border-radius: 50%;
            border: 4px solid orange;
        }
        
        header {
            background-color: orangered;
            padding-top: 20px;
            padding-bottom: 10px;
            border-bottom: 1px white;
        }
        
        header img {
            width: 200px;
            height: auto;
        }
        
        header nav {
            float: right;
        }
        
        header nav ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        header nav li {
            display: inline-block;
            margin-right: 20px;
        }
        
        header nav a {
            text-decoration: none;
            color: #333;
        }
        
        header nav a:hover {
            color: #000;
        }
        
        header .get-started {
            background-color: #000;
            color: #fff;
            padding: 10px 20px;
            border-radius: 5px;
        }
        
        .hero {
            padding: 20px;
            background-color: whitesmoke;
        }
        
        .hero1 {
            padding: 20px;
            background-color: whitesmoke;
        }
        
        h1 {
            background-color: #007bff;
            color: #fff;
            padding: 10px 20px;
            text-align: center;
            font-weight: bold;
        }
        
        .footer {
            background-color: orangered;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
    </style>
        """, unsafe_allow_html=True)
    st.markdown("""
                <div class="container4">
                <div class="container5" onclick="scrollToBasixSection1()">
                <img class ="image1"src="https://th.bing.com/th/id/OIP.HDpBJ9w1fifhzWnUn2AjsgHaFj?w=207&h=180&c=7&r=0&o=5&pid=1.7" alt="" width="150" radius="20" height="150" margin-bottom="50" border-radius="30px"> 
                <center>
                <b style="color: red;">Brain Tumour</b>
                <p>
                    A brain tumor is a growth of cells in the brain or near it. Brain tumors can happen in the brain tissue.
                </p>
                </center> 
                </div>
                <div class="container5" onclick="scrollToBasixSection3()">
                <img class="image1" src="https://th.bing.com/th/id/OIP.dB19LcRjoSDKBsNz0xsVRwHaE7?w=269&h=180&c=7&r=0&o=5&pid=1.7" alt="" width="150" radius="20" height="150" margin-bottom="50"> 
                <center>
                <b style="color: red;">Pneumonia</b>
                <p>
                    Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material).
                </p>
                </center>
                </div>
                <div class="container5" onclick="scrollToBasixSection2()" >
                <img class="image1"  src="https://english-blog.s3.amazonaws.com/uploads/2018/01/Skin-disease_Blog.png" alt="" width="150" radius="20" height="150" margin-bottom="50"> 
                <center>
                <b style="color: red;"> Skin Disease</b>
                 <p>
                    Skin diseases are conditions that affect your skin. These diseases may cause rashes, inflammation, itchiness or other skin changes.
                 </p>
                </center> 
            </div>
            </div>
            <section class="hero1">
            </section>
            </main>
            <h1 id="braintumour">Brain Tumor</h1>
            <h2>What is a brain tumor?</h2>
            <p>
                A brain tumor is an abnormal growth of cells in the brain. The brain is a complex organ with different regions responsible for various functions of the nervous system. Brain tumors can develop anywhere in the brain or even in the surrounding areas, including the skull's lining, brainstem, sinuses, and nasal cavity. There are over 120 different types of brain tumors, categorized based on the tissue they originate from.
            </p>
            <img src="https://staticimg.amarujala.com/assets/images/2022/06/08/brain-tumor-demo_1654671737.jpeg?w=674&amp;dpr=1.0" alt="Brain tumor illustration">
            <h2>Precautions</h2>
            <p>To minimize the risk of brain tumors, consider the following:</p>
            <ul>
            <li>Minimize exposure to environmental hazards, such as smoking and excessive radiation exposure.</li>
            <li>Maintain a healthy diet rich in essential nutrients and antioxidants.</li>
            <li>Limit alcohol consumption.</li>
            <li>Consider genetic counseling if you have a family history of brain tumors.</li>
            </ul>
            <h2>Medicine</h2>
            <p>Please note that this information is not a substitute for professional medical advice. Always consult with a qualified healthcare professional for any questions or concerns you may have about brain tumors and their treatment.</p>
            <table>
           
            <tbody>
                <tr>
                <td>Alymsys (Bevacizumab)</td>
                </tr>
                <tr>
                <td>Temodar</td>
                </tr>
                <tr>
                <td>Everolimus</td>
                </tr>
                <tr>
                <td>Zirabev</td>
                </tr>
                <tr>
                <td>Welireg</td>
                </tr>
            </tbody>
            </table>
            <script>
                function scrollToBasixSection1() {
                    // Scroll smoothly to the basixSection
                    document.getElementById('braintumour').scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            </script>
            <h1 id="skin disease">Skin Diseases</h1>
            <h2>What are skin diseases?</h2>
            <p>
            Skin diseases are conditions that affect your skin, causing various symptoms such as rashes, inflammation, itchiness, or other changes in appearance. Some skin diseases can be genetic, while others arise due to lifestyle factors. Treatments for skin diseases can involve medications, creams or ointments, or lifestyle changes.
            </p>
            <img src="https://english-blog.s3.amazonaws.com/uploads/2018/01/Skin-disease_Blog.png" alt="Image of various skin conditions">
            <h2>Most Common Skin Diseases</h2>
            <ul>
            <li>Acne: Blocked skin follicles, causing oil, bacteria, and dead skin buildup in pores.</li>
            <li>Alopecia areata: Hair loss in small patches.</li>
            <li>Atopic dermatitis (eczema): Dry, itchy skin with potential swelling, cracking, or scaliness.</li>
            <li>Psoriasis: Scaly skin that may be swollen or feel hot.</li>
            <li>Raynaud's phenomenon: Reduced blood flow to fingers, toes, or other body parts, causing numbness or skin color changes.</li>
            <li>Rosacea: Flushed, thick skin with pimples, typically on the face.</li>
            <li>Skin cancer: Uncontrolled growth of abnormal skin cells.</li>
            <li>Vitiligo: Patches of skin losing pigment.</li>
            </ul>
            <h2>Precautions</h2>
            <ul>
            <li>Avoid sharing utensils, personal items, or cosmetics.</li>
            <li>Disinfect objects in public spaces (e.g., gym equipment).</li>
            <li>Maintain hydration and a balanced diet.</li>
            <li>Limit contact with irritants or harsh chemicals.</li>
            <li>Prioritize adequate sleep (7-8 hours).</li>
            <li>Use sun protection to prevent sunburn and other sun damage.</li>
            <li>Practice regular hand washing with soap and water.</li>
            </ul>
            <h2>Medicine (Disclaimer: Consult a Healthcare Professional)</h2>
            <table>
            <thead>
                <tr>
                <th>Medicine</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <td>Antibiotics</td>
                </tr>
                <tr>
                <td>Dicloxacillin</td>
                </tr>
                <tr>
                <td>Erythromycin</td> 
                </tr>
                <tr>
                <td>Tetracycline</td>
                </tr>
            </tbody>
            </table>
            <script>
                function scrollToBasixSection2() {
                    // Scroll smoothly to the basixSection
                    document.getElementById('skin disease').scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            </script>
            <h1 id="pneumonia">Pneumonia</h1>
            <h2>What is Pneumonia?</h2>
            <p>
                Pneumonia is an infection that primarily affects the alveoli, the tiny air sacs in your lungs responsible for gas exchange. When the alveoli become inflamed and filled with fluid or pus, it hinders oxygen intake and causes difficulty breathing.
            </p>
            <img src="https://t4.ftcdn.net/jpg/02/15/77/53/360_F_215775339_WE6fHlZ58FQyzytvH8xSAZE0CN2dhBo3.jpg" alt="Image of inflamed lungs with pneumonia">
            <h2>Symptoms</h2>
            <ul>
                <li>Cough, often with phlegm or pus</li>
                <li>Fever</li>
                <li>Chills</li>
                <li>Difficulty breathing</li>
                <li>Chest pain, especially when taking a deep breath or coughing</li>
            </ul>
            <h2>Precautions</h2>
            <ul>
                <li>Get vaccinated against pneumococcal pneumonia and influenza.</li>
                <li>Maintain good hand hygiene.</li>
                <li>Avoid smoking.</li>
                <li>Maintain a healthy lifestyle (balanced diet, regular exercise, adequate sleep).</li>
            </ul>
            <h2>Medicine (Disclaimer: Consult a Healthcare Professional)</h2>
            <p>
                **It is crucial to consult a healthcare professional** for diagnosis and treatment of any medical condition, including pneumonia. This information does not constitute medical advice.
            </p>
            <table>
                <thead>
                <tr>
                    <th>Medicine</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td>Levofloxacin</td>
                </tr>
                <tr>
                    <td>Doxycycline</td>
                </tr>
                <tr>
                    <td>Ceftriaxone</td>
                </tr>
                <tr>
                    <td>Clarithromycin</td>
                </tr>
                <tr>
                    <td>Azithromycin</td>
                </tr>
                </tbody>
            </table>
            <script>
                function scrollToBasixSection3() {
                    // Scroll smoothly to the basixSection
                    document.getElementById('pneumonia').scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            </script>""", unsafe_allow_html=True)

    st.markdown("""
        <footer class="footer">
            <p>Contact us</p>
                 <p>9025851189</p>
        </footer>
    """, unsafe_allow_html=True)

   
    # st.markdown('<h2 style="text-align: center;">Pneumonia Clinics and Healthcare Center Near You:</h2>', unsafe_allow_html=True)
    # st.markdown('''
    #     <div class="map">
    #         <!-- Replace the iframe with your Google Maps embed code -->
    #         <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3840.5158816848244!2d78.13215861482524!3d11.664325291762048!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3baa08f8ac49e4f3%3A0x6ecb5f57d93045fc!2sSalem%2C%20Tamil%20Nadu!5e0!3m2!1sen!2sin!4v1646630257855!5m2!1sen!2sin" width="1000" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    #     </div>
    # ''', unsafe_allow_html=True)
    # st.markdown("""
    #     <style>
    #         .description {
    #             margin-top: 20px;
    #             font-size: 16px;
    #             line-height: 1.5;
    #             color: #555;
    #         }

    #         .map {
    #             margin-top: 10px;
    #             text-align: center;
    #         }
    #     </style>
    # """, unsafe_allow_html=True)


if __name__ == "__main__":
    app()

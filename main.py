# streamlit_app.py

import streamlit as st
from PIL import Image
import pytesseract
import pandas as pd
import mysql.connector
from validation import create_new,login,extract_id_card_details
from user import dashboard



def main1():
    

 
    st.sidebar.title('AgriTechSmart')
    
    app=st.sidebar.selectbox('catogery',['Home','About','Sign up','Sign in'])
    

    if(app=='Home'):
        st.title('Welcome')
        st.subheader("AgriTechSmart")
        st.subheader("AgriTechSmart is a comprehensive solution that addresses the identified challenges in the Sri Lankan agricultural sector.")
        
    
    elif(app=='Sign up'):
      st.title('sign up page')
      uploaded_file = st.file_uploader("Choose an ID card image", type=["jpg", "jpeg", "png"],key="123456")

      if uploaded_file is not None:
    # Display the uploaded image
          st.image(uploaded_file, caption="Uploaded ID Card Image", use_column_width=True)

    # Extract details on button click
        #if st.button("Extract Details"):
          img = Image.open(uploaded_file)
          details = extract_id_card_details(img)


          name=st.text_input('Username',details["Name"],placeholder="Enter your name")
          DOB=st.text_input('Date of Birth', details["Date of Birth"],placeholder="Enter your Date of Birth")
          addre=st.text_input('Address',details["Address"],placeholder="Enter your Address")
          idnum=st.text_input('ID Number', details["ID Number"],placeholder="Enter your ID number")
          phone=st.text_input("Phone number",'',placeholder="Enter you Phone number")
          email=st.text_input("Email",'',placeholder="Enter you Email")
          passw=st.text_input("password",'',placeholder="Enter you password",type="password")

          btn=st.button('Submit')

          if(btn):

             create_new(name,DOB,addre,idnum,phone,email,passw)
            

    elif(app=='Sign in'):
           st.title('sign in page')
           email=st.text_input('Email','',placeholder="Enter your Email")
           passw=st.text_input('Password','',type="password",placeholder="Enter your password")
           btn=st.button('Submit')

           if(btn):

            login(email,passw)
                
                



def main():

    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False
    
    if not st.session_state.is_logged_in:
        
        main1()
    else:
        dashboard()

if __name__ == "__main__":
    main()









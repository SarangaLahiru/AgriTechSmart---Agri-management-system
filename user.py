import streamlit as st
from PIL import Image
import pytesseract
from streamlit_option_menu import option_menu
from cropRecomendation.recommendation import main
from diseasterManagement.main import diseaster
from QRcode.main import QR
from insectidentify.main import insect

def dashboard():
        
    
        st.title("Hi! "+st.session_state.name)
        
        selected=option_menu(
            menu_title="",
            options=["Home","About","More"],
            menu_icon="cast",
            icons=["house","book","envelope"],
            orientation="horizontal",
            
                            )
        if(selected=="Home"):
            st.title("Home page")
        elif(selected=="More"):
         st.title("see predictions")
         with st.sidebar:
           data=st.selectbox("select",["crop recommendation","diseaster management","crop identifier","Insect Prediction","QR code"])
         if(data=="crop recommendation"):
              main()
         elif(data=="diseaster management"):
              diseaster()
         elif(data=="QR code"):
              QR()
         elif(data=="Insect Prediction"):
              insect()
              
              
        
    
    
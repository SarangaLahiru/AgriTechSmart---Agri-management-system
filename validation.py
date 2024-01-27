import streamlit as st
import mysql.connector
from PIL import Image
import pytesseract


mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'AMS',
}






def create_new(name,DOB,addre,idnum,phone,email,passw):

  if not name or not email or not phone or not passw:
        st.error("All fields are require")
  else:
    

    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()
    query = "insert into user (id,name,IDnumber,DOB,address,phone,email,password,otp) values('',%s,%s,%s,%s,%s,%s,%s,'');"
    values=(name,idnum,DOB,addre,phone,email,passw)

    try:
        cursor.execute(query,values)
        conn.commit()
        
        st.success("successs")
        st.session_state.is_logged_in = True
        st.session_state.name = name
        st.session_state.email = email
        st.session_state.phone = phone
        st.session_state.address=addre
        st.session_state.idnum=idnum
        st.session_state.DOB=DOB
    except Exception as e:
        conn.rollback()
        st.error(f"Error: {e}")
    finally:
            cursor.close()
            conn.close()


def login(email,passw):


  if not email or not passw:
        st.error("All fields are require")
  else:
    

    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()
    query = "select * from test1 where email = %s AND password= %s;"
    values=(email,passw)
    
    cursor.execute(query,values)
       
    data=cursor.fetchall()

    for row in data:
        name=row[1]
        phone=row[3]

    if(data):
        st.success('Login success')
        st.session_state.is_logged_in = True
        st.session_state.name = name
        st.session_state.email = email
        st.session_state.phone = phone
        return True
        
        
        

    else:
        st.error("Something wrong")

def extract_id_card_details(img):
    text = pytesseract.image_to_string(img)
    details = {"Name": "", "Date of Birth": "", "Address": "", "ID Number": ""}
    address_lines = []

    for line in text.split('\n'):
        if "Name:" in line:
            details["Name"] = line.split(":")[1].strip()
        elif "Dos:" in line:  # Adjust based on the actual format in your OCR result
            details["Date of Birth"] = line.split(":")[1].strip()
        elif "Address:" in line:
            address_lines.append(line.split(":")[1].strip())
        elif "ID Number:" in line:
            details["ID Number"] = line.split(":")[1].strip()

    details["Address"] = " ".join(address_lines)
    return details

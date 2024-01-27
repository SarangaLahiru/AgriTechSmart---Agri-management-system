import streamlit as st
import qrcode
import io
from PIL import Image
from pyzbar.pyzbar import decode
import base64

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def read_qr_code(image):
    decoded_objects = decode(image)
    if decoded_objects:
        return decoded_objects[0].data.decode("utf-8")
    return None

# Function to create a download link for a file
def get_binary_file_downloader_html(bin_file, file_label, button_text):
    data = bin_file.getvalue()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_label}">{button_text}</a>'
    return href

def QR():
    st.title("QR Code Generator and Decoder")

    # User Input
    user_name = st.text_input("Enter User Name:",st.session_state.name)
    id_number = st.text_input("Enter ID Number:",st.session_state.idnum)
    address = st.text_input("Enter Address:",st.session_state.address)
    phone_number = st.text_input("Enter Phone Number:",st.session_state.phone)
    paddy_field_size = st.text_input("Enter Size of Paddy Field:")
    harvest_info = st.text_input("Enter Harvest Information:")
    food_category = st.text_input("Enter Food Category:")

    # Generate QR Code Button
    if st.button("Generate QR Code"):
        # Combine user inputs into a single string
        qr_data = f"Name: {user_name}\n Address: {address}\n ID: {id_number}\nPhone: {phone_number}\nSize of Paddy Field: {paddy_field_size}\nHarvest: {harvest_info}\nFood Category: {food_category}"

        # Generate QR Code
        qr_code = generate_qr_code(qr_data)

        # Save the QR code to a BytesIO object
        img_bytes = io.BytesIO()
        qr_code.save(img_bytes, format="PNG")

        # Display QR Code on the right side
        st.sidebar.image(img_bytes, caption="Generated QR Code", use_column_width=True)

        # Download button
        download_button = st.button("Download QR Code")
        if download_button:
            # Offer the file for download
            st.markdown(get_binary_file_downloader_html(img_bytes, "QR_Code.png", "Download QR Code"), unsafe_allow_html=True)

    # Decode QR Code from Image
    uploaded_image = st.file_uploader("Upload an image for QR code decoding:", type=["jpg", "png", "jpeg"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        decoded_data = read_qr_code(image)

        if decoded_data:
            st.success(f"Decoded QR Code Data: {decoded_data}")
        else:
            st.warning("No QR code found in the uploaded image.")



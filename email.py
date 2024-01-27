# pdf_download_with_user_info.py

import streamlit as st
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf_with_user_info(details):
    pdf_buffer = BytesIO()

    # Create a PDF document
    pdf = canvas.Canvas(pdf_buffer)

    # Set font for the title
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawCentredString(300, 750, "Details Document")
    pdf.drawString(100, 730, "-" * 200)  # Separator line
    pdf.drawCentredString(300, 720, "")  # Add a line break

    # Set font for the details
    pdf.setFont("Helvetica", 12)

    # Add details to the PDF in a table format
    x, y = 100, 700
    row_height = 20

    for key, value in details.items():
        pdf.drawString(x, y, key)
        pdf.drawString(x + 150, y, ":")
        pdf.drawString(x + 170, y, str(value))
        y -= row_height

    # Save the PDF to the buffer
    pdf.save()

    return pdf_buffer.getvalue()

# Streamlit UI
st.title("Details PDF Generator")

# Input form to get details
name = st.text_input("Enter Name:")
email = st.text_input("Enter Email:")
address = st.text_area("Enter Address:")

details = {
    "Name": name,
    "Email": email,
    "Address": address
}

# Generate PDF with user information and provide download button
pdf_output = generate_pdf_with_user_info(details)
st.download_button(label="Download PDF", data=pdf_output, key="download_pdf", file_name="details_document.pdf", mime="application/pdf")

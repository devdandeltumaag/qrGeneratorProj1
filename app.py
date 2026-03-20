import streamlit as st
import segno
import io

st.set_page_config(page_title="Quick QR Generator", page_icon="🎯")

st.title("🎯 Simple QR Generator")
st.write("Enter a URL or text below to generate a QR code.")

# User Input
url = st.text_input("Enter your content:", placeholder="https://example.com")

if url:
    # Generate QR code using Segno
    qr = segno.make(url)
    
    # Save to a buffer so Streamlit can display/download it
    out = io.BytesIO()
    qr.save(out, kind='png', scale=10)
    
    # Display the QR Code
    st.image(out.getvalue(), caption="Your Generated QR Code", width=300)
    
    # Download Button
    st.download_button(
        label="Download QR Code",
        data=out.getvalue(),
        file_name="qr_code.png",
        mime="image/png"
    )
else:
    st.info("Waiting for input...")
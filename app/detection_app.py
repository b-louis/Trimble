import streamlit as st
from model_app import predict

classes = ['field','road']
st.title("Road Or Field ?")
st.text("Upload an image to get your prediction.")
input_image = st.file_uploader(label="your image",accept_multiple_files=False)
if input_image :
    st.image(input_image,"Your input image",224)

def predict_class():
    output = predict(input_image)
    st.text("It's a "+classes[output],)
if st.button("Predict"):
    predict_class()

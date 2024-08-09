import google.generativeai as genai
import streamlit as st

GOOGLE_API_KEY = "AIzaSyCRcGr5HK8ltQzczWEg9Fc0aF0hTM0C8IM"
genai.configure(api_key= GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

st.title("Simple ChatBot")
st.write ("It uses Google API key")
user_input = st.text_input("Enter your prompt:")
if st.button("Response"):
    if user_input:
        output = getResponseFromModel(user_input)
        st.write(f"Chatbot Response: {output}")
    else:
        st.write("Please enter a prompt.")

import google.generativeai as genai
import streamlit as st

GOOGLE_API_KEY = "AIzaSyCRcGr5HK8ltQzczWEg9Fc0aF0hTM0C8IM"
genai.configure(api_key= GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

st.set_page_config(page_title = 'Simple ChatBot', layout = 'centered')

st.title("Simple ChatBot")
st.write ("Powered by Google Generative AI")

with st.form(key = "chat_form", clear_on_submit = True):
    user_input = st.text_input("", max_chars= 2000)
    submit_button = st.form_submit_button("send")
    if submit_button:
        if user_input:
            response = get_chatbot_response(user_input)
            st.write(response)
        else:
            st.warning("Please Enter a Prompt")

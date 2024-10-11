from dotenv import load_dotenv
load_dotenv() # take environment variables from .env
import streamlit as st
import os
from langchain import Cohere


llm = Cohere(cohere_api_key = os.getenv("COHERE_API_KEY"), temperature = 0.2)
def get_cohere_response(input, no_words, blog_style):
    temp = f"""
    write a blog for {blog_style} for a topic on {input} within {no_words} words."""
    response = llm(temp)

    return response

# intialize streamlit application
st.title("BlogCraft")
st.subheader("{Effortless Blog Creation Powered by AI}")


input = st.text_input("write your blog title here : ")
col1,col2 = st.columns([5,5])
with col1:
    no_words = st.text_input("Wordcounts :")
with col2:
    blog_style = st.selectbox("Blog Relevance :",("Research Field","Tech Field","General"), index = 0)

submit = st.button("Get the Blog")
if submit:
    st.write(get_cohere_response(input,no_words,blog_style))
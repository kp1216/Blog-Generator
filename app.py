import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


# function to get response from LLama 3 model
def get_llama_response(input_text, no_words, blog_style):
    # llama model
    llm = CTransformers(model="llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type="llama",
                        max_new_tokens=256,
                        temperature=0.01)

    # Prompt template
    template = """
    Write a blog in the style of a {blog_style} for the topic '{input_text}' within {no_words} words.
    """
    prompt = template.format(blog_style=blog_style, input_text=input_text, no_words=no_words)

    # Generate the response from LLama model
    response = llm(prompt)
    print(response)
    return response


st.set_page_config(page_title="Generate Blogs",
                   page_icon=":robot:",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate Blogs")
input_text = st.text_input("Enter the Blog Topic")

# Creating two more columns for additional 2 fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input("No of words")
    no_words = int(no_words) if no_words.isdigit() else 300  # Default to 300 words if not a number

with col2:
    blog_style = st.selectbox("Writing the blog for", ("Researchers", "Data Scientist", "Common People"))

submit = st.button("Generate")

# Final response
if submit:
    st.write(get_llama_response(input_text, no_words, blog_style))

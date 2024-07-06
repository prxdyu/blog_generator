import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


# function to get response from the LLAMA 2
def get_llama_response(input_test,no_of_words,blog_style):

    # loading the LLAma model in local
    llm = CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature':0.001})
    
    # defining the  template
    template= """ Write a blog for {blog_style} job profile for a topic {input_text} within {no_of_words} words"""

    # defining the prompt template
    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_of_words"],
                            template = template)
    # generate the response
    response = llm(prompt.format(blog_style=blog_style,input_text=input_test,no_of_words=no_of_words))

    print(response)
    return response





st.set_page_config (page_title="Generate Blogs",
                    page_icon="🤖" ,
                    layout='centered',
                    initial_sidebar_state="collapsed"
                    )
st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the topic of the blog")
col1,col2 = st.columns([5,5])

with col1:
    no_of_words = st.text_input('Enter the no of words')

with col2:
    blog_style = st.selectbox("Writing the blog for",
                             ('Researchers','Data Scientists','Common People'),
                             index=0)
submit = st.button("Generate")

if submit:
    # getting the response from llama
    response = get_llama_response(input_text,no_of_words,blog_style)
    st.write(response)

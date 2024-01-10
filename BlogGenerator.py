
#import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from dotenv import load_dotenv
import requests
import json
import os


load_dotenv()
key = os.getenv("OPENAI_API_KEY")


llm = OpenAI(openai_api_key=key, temperature=0.9)

def getBLOGLLamaresponse(input_text,no_words,blog_style):
    template = """
         You are a digital marketing and SEO expert and your task is to write article for {blog_style} on the topic: {input_text}. The article must be under {no_words} words.  
         """
    quiz_generation_prompt = PromptTemplate(
        input_variables = ["blog_style","input_text",'no_words'],
        template = template)
    
    formated_prompt = quiz_generation_prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words)
    result = llm(formated_prompt)
    #print(type(result))
    return result



# def load_llm(max_tokens, prompt_template):
#     # Load the locally downloaded model here
#     llm = CTransformers(
#         model = "./models/llama-2-7b-chat.ggmlv3.q8_0.bin",
#         model_type="llama",
#         max_new_tokens = max_tokens,
#         temperature = 0.7
#     )
    
#     llm_chain = LLMChain(
#         llm=llm,
#         prompt=PromptTemplate.from_template(prompt_template)
#     )
#     print(llm_chain)
#     return llm_chain


# def fun1():
#     prompt_template = """You are a digital marketing and SEO expert and your task is to write article so write an article on the given topic: {user_input}. The article must be under 800 words. The article should be be lengthy.               
#             """
#     llm_call = load_llm(max_tokens=800, prompt_template=prompt_template)
#     print(llm_call)
#     result = llm_call("Data science")
#     print(result)


#  ## Prompt Template
# def getBLOGLLamaresponse(input_text,no_words,blog_style):
#     ### LLama2 model
#     llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
#                       model_type='llama',
#                       config={'max_new_tokens':256,
#                               'temperature':0.7})
    
#     ## Prompt Template
#     template ="""
#         Write a blog for {blog_style} job profile for a topic {input_text}
#         within {no_words} words.
#             """
#     template1 = """
#         You are a digital marketing and SEO expert and your task is to write article for {blog_style} on the topic: {input_text}. The article must be under {no_words} words.  
#         """
#     print(input_text,no_words,blog_style)

#     prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
#                           template=template)
    
#     print(input_text,no_words,blog_style)

#     ## Generate the ressponse from the LLama 2 model
#     response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))

#     print(input_text,no_words,blog_style)

#     print(response)
#     print(input_text,no_words,blog_style)

#     return response


#     # prompt_template = """You are a digital marketing and SEO expert and your task is to write article so write an article on the given topic: {user_input}. The article must be under 800 words. The article should be be lengthy.               
#     #         """
#     # llm_call = load_llm(max_tokens=800, prompt_template=prompt_template)
        
#     # llm = CTransformers(
#     #     model = "llama-2-7b-chat.ggmlv3.q8_0.bin",
#     #     model_type="llama",
#     #     max_new_tokens = max_tokens,
#     #     temperature = 0.7
#     # )
    
#     # llm_chain = LLMChain(
#     #     llm=llm,
#     #     prompt=PromptTemplate.from_template(prompt_template)
#     # )
#     # print(llm_chain)
#     # return llm_chain

#     # print(llm_call)
#     # result = llm_call(user_input)

# print("Calling function")
#show_me = getBLOGLLamaresponse("Data", 804, "Data Scienctist")
#print(show_me)

# fun1()
# print("Calling Done")
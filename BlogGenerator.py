
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

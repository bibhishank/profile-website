
import os

# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
# from langchain.chains import SequentialChain
# #from langchain.callbacks import get_openai_callback
# from langchain_community.callbacks import get_openai_callback
# from langchain_community.llms import OpenAI

from langchain import HuggingFaceHub 
from dotenv import load_dotenv

#load_dotenv() # Reads variables from .env file
#key = os.getenv("OPENAI_API_KEY")

#======Sime OpenAI call (working)=========================================
#key = "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"
#Working fine
# llm = OpenAI(openai_api_key=key, temperature=0.9)
# text = 'What is the capital of India'
# print(llm.predict(text))
#======Sime OpenAI call (working) =========================================


#==== Hugging face test (working)  =========================================
# hf_key = "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"
# #HUGGINGFACEHUB_API_TOKEN
# llm_huggingface = HuggingFaceHub(huggingfacehub_api_token="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", repo_id="google/flan-t5-base" , model_kwargs={"temperature": 0, "max_length":64} )
# output = llm_huggingface.predict("can you tell me the capital of Japan")
# print("\nAnswer: " + output)
#==== Hugging face test (working )  =========================================

#Prompt template with Chain examples (working )  =========================================
# key = "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"
# llm = OpenAI(openai_api_key=key, temperature=0.9)
# prompt_template = PromptTemplate(input_variables=['country'],
# template = "Tell me the capital of {country}")
# prompt_template.format(country="India")
# chain=LLMChain(llm=llm, prompt=prompt_template)
# print(chain.run("Sri Lanka"))
#Prompt template examples (working )  =========================================

#Prompt template  project examples (working )  =========================================

template = """
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz  of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}
"""

response_json  = {
    "1": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        "correct": "correct answer"
    },
    "2": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        "correct": "correct answer"
    },
    "3": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        "correct": "correct answer"
    }
}

text = """
Data science combines math and statistics, specialized programming, advanced analytics, artificial intelligence (AI), and machine learning with specific subject matter expertise to uncover actionable insights hidden in an organization’s data. These insights can be used to guide decision making and strategic planning.

The accelerating volume of data sources, and subsequently data, has made data science is one of the fastest growing field across every industry. As a result, it is no surprise that the role of the data scientist was dubbed the “sexiest job of the 21st century” by Harvard Business Review (link resides outside of IBM). Organizations are increasingly reliant on them to interpret data and provide actionable recommendations to improve business outcomes.

The data science lifecycle involves various roles, tools, and processes, which enables analysts to glean actionable insights. Typically, a data science project undergoes the following stages:

Data ingestion: The lifecycle begins with the data collection--both raw structured and unstructured data from all relevant sources using a variety of methods. These methods can include manual entry, web scraping, and real-time streaming data from systems and devices. Data sources can include structured data, such as customer data, along with unstructured data like log files, video, audio, pictures, the Internet of Things (IoT), social media, and more.
Data storage and data processing: Since data can have different formats and structures, companies need to consider different storage systems based on the type of data that needs to be captured. Data management teams help to set standards around data storage and structure, which facilitate workflows around analytics, machine learning and deep learning models. This stage includes cleaning data, deduplicating, transforming and combining the data using ETL (extract, transform, load) jobs or other data integration technologies. This data preparation is essential for promoting data quality before loading into a data warehouse, data lake, or other repository.
Data analysis: Here, data scientists conduct an exploratory data analysis to examine biases, patterns, ranges, and distributions of values within the data. This data analytics exploration drives hypothesis generation for a/b testing. It also allows analysts to determine the data’s relevance for use within modeling efforts for predictive analytics, machine learning, and/or deep learning. Depending on a model’s accuracy, organizations can become reliant on these insights for business decision making, allowing them to drive more scalability.
Communicate: Finally, insights are presented as reports and other data visualizations that make the insights—and their impact on business—easier for business analysts and other decision-makers to understand. A data science programming language such as R or Python includes components for generating visualizations; alternately, data scientists can use dedicated visualization tools.
"""

key = "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"
llm = OpenAI(openai_api_key=key, temperature=0.9)

def getMCQData(mcq_input_data, mcq_number, mcq_subject, mcq_tone):
    quiz_generation_prompt = PromptTemplate(
        input_variables = ["text", "number", "subject", "tone", "response_json"],
        template = template)
    
    formated_prompt = quiz_generation_prompt.format(text=mcq_input_data, number=mcq_number, subject=mcq_subject, tone=mcq_tone, response_json=response_json)
    result = llm(formated_prompt)
    #print(type(result))
    return result

#Prompt template chain project examples (working )  =========================================
  #quiz_chain = LLMChain(llm=llm, prompt= quiz_generation_prompt, output_key="generated_quiz", verbose=True)
#Prompt template chain project examples (working )  =========================================
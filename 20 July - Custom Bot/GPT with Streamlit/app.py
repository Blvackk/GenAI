from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# Load API key
load_dotenv()

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("user", "{question}")
])

# Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.7
)

# Output Parser
parser = StrOutputParser()

# Chain
chain = prompt | llm | parser

# Streamlit UI
st.set_page_config(page_title="Gemini Chatbot")

st.title("Gemini AI Chatbot")

question = st.text_input("Ask anything...")

if question:
    try:
        response = chain.invoke({"question": question})
        st.success(response)

    except Exception as e:
        st.error(e)
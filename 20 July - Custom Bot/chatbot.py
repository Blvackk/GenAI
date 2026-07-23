from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ["OPENAI_API_KEY"] = "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"

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Question: {question}")
])

llm = ChatOpenAI(
    model="gpt-5.4-mini",
    temperature=1
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

response = chain.invoke(
    {"question": "Who won the FIFA World Cup 2022?"}
)

print(response)
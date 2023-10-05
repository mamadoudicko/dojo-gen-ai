import os

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

from utils.vector_store import vector_store

api_key = os.environ["OPENAI_API_KEY"]

llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0, openai_api_key=api_key )

def get_answer(question: str):

    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vector_store.as_retriever()
        
        # chain_type_kwargs={"prompt": ""}

    )
    result = qa_chain({"query": question})
    return result["result"]
    

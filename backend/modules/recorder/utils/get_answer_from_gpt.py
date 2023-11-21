import os

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

from backend.modules.recorder.utils.vector_store import vector_store

api_key = os.environ["OPENAI_API_KEY"]

gpt_client = ChatOpenAI(
    model_name="gpt-3.5-turbo", temperature=0, openai_api_key=api_key
)


def get_answer_from_gpt(question: str):
    """
    Send question to the model and return the answer
    """
    qa_chain = RetrievalQA.from_chain_type(
        gpt_client, retriever=vector_store.as_retriever()
    )
    result = qa_chain({"query": question})
    return result["result"]

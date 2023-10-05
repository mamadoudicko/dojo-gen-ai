import os

from utils.vector_store import vector_store

api_key = os.environ["OPENAI_API_KEY"]


def save_embeddings(texts: list[str]):
    vector_store.add_texts(texts)
    vector_store.similarity_search("hello")
from backend.modules.recorder.utils.vector_store import vector_store


def save_embeddings(texts: list[str]):
    """
    Save the embeddings of the given texts to the vector store
    """
    vector_store.add_texts(texts)

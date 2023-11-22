from backend.modules.recorder.utils.get_vector_store import get_vector_store


def get_relevant_chunks(question: str, number_of_chunks: int = 5) -> str:
    vector_store = get_vector_store()
    vector_store_retriever = vector_store.as_retriever()
    relevant_documents = vector_store_retriever.get_relevant_documents(question)
    relevant_documents[:number_of_chunks]

    chunks_contents = [
        document.page_content for document in relevant_documents[:number_of_chunks]
    ]

    return "\n".join(chunks_contents)

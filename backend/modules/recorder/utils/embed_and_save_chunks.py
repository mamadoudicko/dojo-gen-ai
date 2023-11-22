from backend.modules.recorder.utils.get_vector_store import get_vector_store


def embed_and_save_chunks(chunks: list[str]):
    vector_store = get_vector_store()
    vector_store.add_texts(chunks)

import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import SupabaseVectorStore
from supabase.client import create_client


def get_vector_store() -> SupabaseVectorStore:
    """
    Return the vector store
    """
    api_key = os.environ["OPENAI_API_KEY"]
    supabase_url = os.environ["SUPABASE_URL"]
    supabase_key = os.environ["SUPABASE_KEY"]

    embeddings_model = OpenAIEmbeddings(openai_api_key=api_key)

    supabase_client = create_client(supabase_url, supabase_key)

    vector_store = SupabaseVectorStore(
        client=supabase_client,
        embedding=embeddings_model,
        table_name="vectors",
        query_name="match_vectors",
    )

    return vector_store


vector_store = get_vector_store()

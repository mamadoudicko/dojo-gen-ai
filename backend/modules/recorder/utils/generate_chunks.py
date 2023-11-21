from langchain.text_splitter import CharacterTextSplitter


def generate_chunks(text: str):
    """Generate chunks of text from a string."""

    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=100, chunk_overlap=0
    )
    texts = text_splitter.split_text(text)
    return texts

from langchain.text_splitter import CharacterTextSplitter


def generate_chunks(text) -> list[str]:
    """Generate chunks of text from a string."""

    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0,
    )

    return text_splitter.split_text(text)

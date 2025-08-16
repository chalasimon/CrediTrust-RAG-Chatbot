from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_text_splitter():
    """Configure optimal chunking for financial complaints"""
    return RecursiveCharacterTextSplitter(
        chunk_size=256,  # Increased from 150 for better context
        chunk_overlap=64,  # Increased overlap for better continuity
        length_function=len,
        separators=['\n\n', '\n', '. ', '! ', '? ', ' ', ''],
        is_separator_regex=False
    )
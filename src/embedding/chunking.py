from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_text_splitter():
    """Configure optimal chunking for financial complaints"""
    return RecursiveCharacterTextSplitter(
        chunk_size=150,
        chunk_overlap=30,
        length_function=len,
        separators=['\n\n', '\n', '. ', '! ', '? ', ' ', '']
    )
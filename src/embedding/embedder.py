from sentence_transformers import SentenceTransformer
import numpy as np

class Embedder:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        """Initialize the embedding model"""
        self.model = SentenceTransformer(model_name)
        
    def embed_text(self, texts):
        """Embed a list of text chunks"""
        if isinstance(texts, str):
            texts = [texts]
        return self.model.encode(texts, convert_to_tensor=False)
        
    def get_embedding_dimension(self):
        """Get the dimension of the embeddings"""
        # all-MiniLM-L6-v2 has 384 dimensions
        return self.model.get_sentence_embedding_dimension()
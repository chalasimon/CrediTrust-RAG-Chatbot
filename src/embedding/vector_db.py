import faiss
import numpy as np
from typing import List, Dict
import pickle
import os

class VectorDB:
    def __init__(self, embedding_dim: int):
        """Initialize FAISS index and metadata store"""
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.metadata = []
        
    def add_embeddings(self, embeddings: np.ndarray, metadata: List[Dict]):
        """Add embeddings and associated metadata to the database"""
        if len(embeddings) != len(metadata):
            raise ValueError("Number of embeddings must match number of metadata entries")
            
        self.index.add(embeddings)
        self.metadata.extend(metadata)
        
    def search(self, query_embedding: np.ndarray, k: int = 5):
        """Search for similar vectors"""
        distances, indices = self.index.search(np.array([query_embedding]), k)
        
        results = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx >= 0:  # FAISS returns -1 for invalid indices
                results.append({
                    "metadata": self.metadata[idx],
                    "distance": float(distance)
                })
        return results
    
    def save(self, directory: str):
        """Save the index and metadata to disk"""
        os.makedirs(directory, exist_ok=True)
        faiss.write_index(self.index, f"{directory}/index.faiss")
        with open(f"{directory}/metadata.pkl", "wb") as f:
            pickle.dump(self.metadata, f)
            
    @classmethod
    def load(cls, directory: str):
        """Load the index and metadata from disk"""
        index = faiss.read_index(f"{directory}/index.faiss")
        with open(f"{directory}/metadata.pkl", "rb") as f:
            metadata = pickle.load(f)
            
        vector_db = cls(index.d)
        vector_db.index = index
        vector_db.metadata = metadata
        return vector_db
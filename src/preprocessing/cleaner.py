import re

def clean_text(text: str) -> str:
    """Normalize complaint text for embedding"""
    if not isinstance(text, str):
        return ""
    
    # Standard cleaning pipeline
    text = text.lower()
    text = re.sub(r'\bXX+\b', '', text)  # Remove redacted portions
    text = re.sub(r'[^a-z0-9\s.,!?]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text
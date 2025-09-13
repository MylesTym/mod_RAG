import numpy as np
from typing import List, Dict
from sentence_transformers import SentenceTransformer


def load_embedder(model_name: str):
    model = SentenceTransformer(model_name)
    return model

def embed_chunks(chunks: List[str], model):
    
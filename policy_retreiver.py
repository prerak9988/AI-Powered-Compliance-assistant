import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from config import POLICY_DB_PATH, CHROMA_DB_PATH

def load_policies():
    """Load GDPR/CCPA policies into ChromaDB"""
    policy_texts = []
    for file in os.listdir(POLICY_DB_PATH):
        with open(os.path.join(POLICY_DB_PATH, file), "r", encoding="utf-8") as f:
            policy_texts.append(f.read())

    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_texts(policy_texts, embedding=embeddings, persist_directory=CHROMA_DB_PATH)
    return vector_store

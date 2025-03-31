import fitz  # PyMuPDF
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from backend.policy_retriever import load_policies

def extract_text_from_pdf(pdf_path):
    """Extract text from an uploaded PDF"""
    doc = fitz.open(pdf_path)
    return " ".join([page.get_text("text") for page in doc])

def analyze_compliance(pdf_text):
    """Compare document text with GDPR/CCPA policies to detect risks"""
    vector_store = load_policies()
    retriever = vector_store.as_retriever()
    llm = ChatOpenAI(model_name="gpt-3")
    qa_chain = RetrievalQA(llm=llm, retriever=retriever)

    query = "Identify any GDPR/CCPA compliance risks in this document: " + pdf_text[:2000]
    return qa_chain.run(query)

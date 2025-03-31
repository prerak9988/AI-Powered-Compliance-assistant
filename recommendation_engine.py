from langchain.chat_models import ChatOpenAI

def generate_compliance_fixes(risk_analysis):
    """Suggest improvements to make a document GDPR/CCPA compliant"""
    llm = ChatOpenAI(model_name="gpt-3")

    query = f"Provide recommendations to fix these compliance risks: {risk_analysis}"
    response = llm.predict(query)
    return response
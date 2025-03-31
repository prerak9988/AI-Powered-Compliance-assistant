import streamlit as st
import tempfile
from document_analyzer import extract_text_from_pdf, analyze_compliance
from recommendation_engine import generate_compliance_fixes

st.title("🛡️ AI Compliance Assistant")
st.write("Ensure your documents comply with GDPR & CCPA")

uploaded_file = st.file_uploader("📄 Upload a document", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        pdf_text = extract_text_from_pdf(temp_file.name)

        st.info("Analyzing document for compliance risks...")
        risk_analysis = analyze_compliance(pdf_text)
        st.write("⚠️ **Compliance Risks:**", risk_analysis)

        st.info("Generating recommendations to fix compliance issues...")
        recommendations = generate_compliance_fixes(risk_analysis)
        st.write("✅ **Recommended Fixes:**", recommendations)

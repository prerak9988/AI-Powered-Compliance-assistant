The AI-Powered Compliance Assistant is designed to ensure that the internal documents comply with GDPR (General Data Protection Regulation) and CCPA (California Consumer Privacy Act). Instead of manually reviewing documents, this AI-driven solution:

- Retrieves governance policies from a knowledge base.
- Analyzes uploaded documents to detect compliance risks. 
- Generates actionable recommendations to make documents compliant.

                        +--------------------------------+
                        |   🖥️ User Uploads a PDF       |
                        +--------------------------------+
                                      │
                                      ▼
                  +--------------------------------------+
                  |  🎛️ Streamlit Frontend UI           |
                  |  - File uploader                     |
                  |  - Displays risks & recommendations  |
                  +--------------------------------------+
                                      │
                                      ▼
   ┌───────────────────────────────────────────────────────────┐
   │                      Backend API (Flask, if needed)       │
   │                                                           │
   │    - Receives PDF → Extracts text                         │
   │    - Calls AI model to analyze compliance                │
   │    - Returns risks & recommended fixes                   │
   └───────────────────────────────────────────────────────────┘
                                      │
                                      ▼
        ┌────────────────────────────────────────────┐
        |     PDF Processing (PyMuPDF)               |
        |  - Extracts text from PDF files            |
        |  - Prepares data for analysis              |
        └────────────────────────────────────────────┘
                                      │
                                      ▼
       ┌───────────────────────────────────────────────┐
       |     Compliance Knowledge Base (ChromaDB)      |
       |  - Stores GDPR & CCPA policies as embeddings  |
       |  - Enables fast retrieval of relevant policies|
       └───────────────────────────────────────────────┘
                                      │
                                      ▼
    ┌────────────────────────────────────────────────────┐
    |     AI Model (OpenAI GPT-3 via LangChain)         |
    |  - Compares document with policies                |
    |  - Identifies compliance risks                    |
    |  - Suggests improvements                          |
    └────────────────────────────────────────────────────┘
                                      │
                                      ▼
        ┌──────────────────────────────────────┐
        |     Cloud Deployment (GCP Cloud Run) |
        |  - Serverless hosting for the app    |
        |  - Scalable & cost-efficient         |
        └──────────────────────────────────────┘



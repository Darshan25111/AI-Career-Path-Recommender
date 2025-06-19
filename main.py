from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub
from langchain.schema import Document
import os

# Set HuggingFace API Key
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "HUGGINGFACEHUB_API_TOKEN"

# 1. Define your career knowledge base (can be expanded or loaded from file)
career_data = [
    {"career": "Software Engineer", "description": "I enjoy solving problems with code, building applications, and working with new technologies."},
    {"career": "Doctor", "description": "I want to help people by improving their health, understanding the human body, and providing care."},
    {"career": "Teacher", "description": "I love sharing knowledge, working with students, and helping others learn and grow."},
    {"career": "Artist", "description": "I enjoy drawing, painting, creating things, and expressing myself visually."},
    {"career": "Mechanical Engineer", "description": "I like building machines, solving real-world mechanical problems, and working with physical systems."},
    {"career": "Psychologist", "description": "I'm interested in human behavior, emotions, and helping others through listening and therapy."}
]

# 2. Convert to LangChain Documents
docs = [Document(page_content=career["description"], metadata={"career": career["career"]}) for career in career_data]

# 3. Use HuggingFace SentenceTransformer for Embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 4. Create FAISS vector store
vectorstore = FAISS.from_documents(docs, embedding_model)

# 5. Ask for user interest
user_input = input("Tell me about your interests or what you enjoy doing: ").strip()

# 6. Fallback prompt if user input is too vague
if len(user_input.split()) < 5:
    user_input += " " + input("Can you please explain your interests a bit more? For example, teaching, building things, helping others: ").strip()

# 7. Use retriever to get best match
retriever = vectorstore.as_retriever(search_type="similarity", k=1)
result = retriever.get_relevant_documents(user_input)

# 8. Output prediction
if result:
    print("\nBased on your interests, a suitable career path might be: ")
    print("🎯", result[0].metadata['career'])
else:
    print("Sorry, we couldn't find a career match. Please try describing your interests differently.")

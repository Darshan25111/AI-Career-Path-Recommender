# 🔮 AI Career Path Recommender

An intelligent, interactive assistant that recommends a suitable career path based on your preferences, using natural language understanding and vector similarity.

This project simulates how AI can guide career counseling by analyzing user inputs with semantic embeddings and returning matched paths with clear explanations.

---

## 🧰 Tools & Libraries Used

| Tool / Library         | Purpose                                                                 |
|------------------------|-------------------------------------------------------------------------|
| **LangChain**          | Framework to manage language model workflows and retrieval pipelines   |
| **HuggingFace Embeddings** | Converts sentences into vector embeddings for semantic search      |
| **FAISS (Facebook AI Similarity Search)** | Fast nearest-neighbor search among high-dimensional vectors |
| **Python `dotenv`**    | Loads API keys and environment variables securely                       |
| **Optional: OpenAI**   | Can be used to replace local embeddings for higher-quality suggestions  |

---

## 🎯 Project Objective

- Ask users guided **multiple-choice questions**
- Use their combined selections to **guess a suitable career**
- Perform **semantic similarity search** to find the best match
- Return a detailed **career explanation**
- Use **fallback free-text input** if unsure

---

## 🚀 Features

- 🧩 5-option user interaction (MCQs)
- 🔍 Smart matching using vector similarity (FAISS)
- 🧠 Personalized explanation generator
- 🛠️ Plug-and-play embedding engine (HuggingFace or OpenAI)
- 📚 Easily extensible with more career paths or preferences

---

## 📦 Installation

```bash
pip install langchain faiss-cpu sentence-transformers python-dotenv
# Optional if using OpenAI
pip install openai

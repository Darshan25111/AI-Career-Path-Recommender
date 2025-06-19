# 🎓 Student Career Pathway Recommender (LLM + FAISS + HuggingFace)

This is a simple AI-powered project that recommends suitable career paths for students based on their interests, hobbies, and goals using free, open-source tools like FAISS and Hugging Face models.

---

## 🚀 Overview

The app takes a student's input (e.g., "I like solving problems and using AI") and uses vector similarity to find the most relevant career option, then optionally explains the reasoning using an LLM.

---

## 🛠️ Tech Stack & Tools

| Component      | Tool Used                                  |
| -------------- | ------------------------------------------ |
| Language Model | `HuggingFaceHub` (e.g., FLAN-T5, optional) |
| Embedding      | `sentence-transformers/all-MiniLM-L6-v2`   |
| Vector DB      | `FAISS` (in-memory similarity search)      |
| Framework      | `LangChain`, `Python`                      |
| Deployment     | Local / Replit / Colab                     |

---

## 📦 Installation

### 🔧 Dependencies

Run this in your terminal or Replit shell:

```bash
pip install -U sentence-transformers faiss-cpu langchain huggingface-hub
```

---

### 🔐 Hugging Face Token Setup

1. Go to [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Generate a **read access token**
3. Save it in your `.env` file or directly in your Python code:

```bash
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

---

## 🧠 How It Works

1. **User Input**: The student describes their interests (e.g., "I like working with machines").
2. **Fallback Prompt**: If the input is too short or vague, we ask a follow-up question.
3. **Embedding**: We convert user input and each career profile into vectors.
4. **FAISS Search**: We use cosine similarity to find the most similar career document.
5. **LLM Explanation** *(optional)*: If enabled, we use a Hugging Face LLM to explain why that career fits.

---

## ✅ Example

**Input:**

```
I like solving problems with data and logic.
```

**Output:**

```
🎯 Recommended Career: Software Engineer
🧠 Why: You enjoy problem-solving, data, and building applications—ideal for a software engineering career.
```

---

## 📁 Project Structure

```
career-recommender/
├── main.py
├── requirements.txt
└── README.md
```

---

## 💡 Assumptions

* Users may enter short or vague inputs, so fallback questions are added.
* Career profiles are simplified and can be extended.
* No OpenAI or paid tools are used by default.

---

## 💸 Accuracy Note

This app uses **free** models and tools. For better accuracy:

* ✅ Use OpenAI GPT-4 or GPT-3.5 with `ChatOpenAI`
* ✅ Use `OpenAIEmbeddings` for more semantic understanding
* ✅ Add more detailed career descriptions and a larger FAISS knowledge base

To switch, just change the embedding and LLM sections in `main.py`.

---

## 🧪 Troubleshooting

| Issue                     | Solution                                              |
| ------------------------- | ----------------------------------------------------- |
| `RateLimitError` (OpenAI) | You're on free tier. Use Hugging Face or add billing. |
| `ModuleNotFoundError`     | Run `pip install` for missing packages.               |
| No career matched         | Try giving more descriptive input.                    |

---

## 👏 Contributions

This project was created as part of the Brainwonders AI Intern assignment.

Feel free to fork, extend, or integrate with a chatbot UI.

---

## 📬 Contact

If you're stuck or need help:

* ChatGPT (LLM Support 😄)
* Hugging Face docs: [https://huggingface.co/docs](https://huggingface.co/docs)
* LangChain docs: [https://docs.langchain.com](https://docs.langchain.com)

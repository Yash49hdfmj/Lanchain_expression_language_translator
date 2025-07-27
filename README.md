# Lanchain_expression_language_translator
Here’s a clean and concise **GitHub `README.md`** (without full code), highlighting the most **important snippets**, instructions, and sections from your LECL translation project:

---

# 🌍 English to Marathi Translator using LangChain + Groq

Fast, batch-supported LLM translation API powered by Groq’s ultra-low latency LPU models via LangChain Expression Language (LECL).

---

## 🚀 Features

* 🔗 **LangChain + Groq** integration (`Gemma2-9b-it`)
* 🧠 **LECL** chaining for prompt → model → parser
* 📦 **Batch translation support**
* 🌐 **REST API via FastAPI + LangServe**
* 🧪 Tested via **Postman**
* 📝 Built-in **feedback logging**

---

## 📁 Project Structure

```
├── serve.py                # FastAPI app with chain and feedback endpoint
├── .env                    # Secure API keys
├── requirements.txt        # All dependencies
├── simple.ipynb            # Playground & testing
└── feedback_log.jsonl      # Logged user feedback
```

---

## 📦 Sample `.env` Variables

```env
GROQ_API_KEY=your_groq_key
LANGCHAIN_API_KEY=your_langchain_key
OPENAI_API_KEY=your_openai_key
```

---

## 🧠 Chaining Prompt → Model → Parser

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "Translate the following into {language}:"),
    ("user", "{text}")
])

chain = prompt | model | parser
```

---

## 🧪 Postman Test Input

**POST** `http://127.0.0.1:8000/chain/invoke`

```json
{
  "input": [{
    "language": "Marathi",
    "text": "How are you?"
  }],
  "config": {},
  "kwargs": {}
}
```

✅ **Response:**

```json
{
  "output": [
    "कसे आहात? (Kese aahat?)"
  ]
}
```

---

## 📝 Feedback Submission

**POST** `/feedback`

```json
{
  "input": [{"language": "Marathi", "text": "How are you?"}],
  "output": ["कसे आहात?"],
  "feedback": ["Accurate translation."]
}
```

---

## 🔧 Run Locally

```bash
uvicorn serve:app --reload
```

---

## 📚 Tech Stack

* [LangChain](https://www.langchain.com/)
* [Groq](https://groq.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [LangServe](https://docs.langchain.com/langserve/)
* [Postman](https://www.postman.com/)

---

> Built for blazing fast Marathi translations using open-source LLMs and LPUs.

---

Let me know if you’d like a badge-style header, GitHub Actions CI, or a demo GIF section too.

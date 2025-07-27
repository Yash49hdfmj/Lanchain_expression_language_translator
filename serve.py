from fastapi import FastAPI, Request
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda
from langserve import add_routes
from dotenv import load_dotenv
from typing import List
import os
import json
from datetime import datetime

# Load environment variables
load_dotenv()

# Get GROQ API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq model
model = ChatGroq(model="Gemma2-9b-it", groq_api_key=groq_api_key)

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Translate the following into {language}:"),
    ("user", "{text}")
])

# Parser and base chain
parser = StrOutputParser()
base_chain = prompt | model | parser

# Batch handler
def translate_many(batch: List[dict]) -> List[str]:
    return [base_chain.invoke(item) for item in batch]

# RunnableLambda chain
chain = RunnableLambda(translate_many)

# FastAPI app
app = FastAPI(
    title="Langchain + Groq Translation API",
    version="1.0",
    description="Chain API using LangServe v0.3.1 with batch support"
)

# LangServe route
add_routes(app, chain, path="/chain")

# Feedback route
@app.post("/feedback")
async def log_feedback(request: Request):
    data = await request.json()

    feedback_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": data.get("input"),
        "output": data.get("output"),
        "user_feedback": data.get("feedback")
    }

    # Append to log file
    with open("feedback_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(feedback_entry) + "\n")

    return {"status": "logged", "entry": feedback_entry}

# Run locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("serve:app", host="127.0.0.1", port=8000, reload=True)

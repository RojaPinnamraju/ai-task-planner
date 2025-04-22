# backend.py
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_ai_agent

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

ALLOWED_MODEL_NAMES = ["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app = FastAPI(title="AI Task Planner Assistant")

@app.post("/chat")
def task_planner_endpoint(request: RequestState):
    """
    Organize, prioritize, and expand user's task list using an AI assistant.
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}

    llm_id = request.model_name
    task_list = "\n".join(request.messages)
    allow_search = request.allow_search
    system_prompt = request.system_prompt or (
        "You are a smart and helpful personal assistant. Organize the tasks, prioritize them, "
        "and suggest any improvements or additions. Present the output in a clear, structured list."
    )
    provider = request.model_provider

    response = get_response_from_ai_agent(llm_id, task_list, allow_search, system_prompt, provider)
    return {"structured_plan": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)

# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()

#Step1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ai_agent import get_response_from_ai_agent
import traceback
import logging
import sys
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: Optional[str] = ""
    messages: List[str]
    allow_search: bool = False

ALLOWED_MODEL_NAMES=["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]  # Groq models

app = FastAPI(title="LangGraph AI Agent")

# Add CORS middleware with more permissive settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "AI Task Planner API is running",
        "endpoints": {
            "chat": "/chat",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0"
    }

@app.options("/chat")
async def options_chat():
    return {"status": "ok"}

@app.post("/chat")
async def chat_endpoint(request: RequestState): 
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    try:
        logger.info(f"Received request: {request}")
        
        if request.model_name not in ALLOWED_MODEL_NAMES:
            logger.error(f"Invalid model name: {request.model_name}")
            return {"error": "Invalid model name. Kindly select a valid AI model"}
        
        llm_id = request.model_name
        query = request.messages
        allow_search = request.allow_search
        system_prompt = request.system_prompt or "Act as an AI chatbot who is smart and friendly"
        provider = request.model_provider

        logger.info(f"Calling AI agent with params: llm_id={llm_id}, provider={provider}, allow_search={allow_search}")
        
        # Create AI Agent and get response from it! 
        response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
        logger.info(f"Successfully got response from AI agent: {response[:100]}...")  # Log first 100 chars
        return {"response": response}
    except Exception as e:
        error_traceback = traceback.format_exc()
        logger.error(f"Error processing request: {str(e)}\n{error_traceback}")
        return {"error": f"Server error: {str(e)}"}

#Step3: Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")

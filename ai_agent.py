# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()

#Step1: Setup API Keys for Groq, OpenAI and Tavily
import os
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Changed to DEBUG for more detailed logging
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Get API keys from environment
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

# Log API key status (without exposing the actual key)
logger.debug(f"GROQ_API_KEY is {'set' if GROQ_API_KEY else 'not set'}")
logger.debug(f"TAVILY_API_KEY is {'set' if TAVILY_API_KEY else 'not set'}")

#Step2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, END

# Initialize tools
search_tool=TavilySearchResults(max_results=2)

#Step3: Setup AI Agent with Search tool functionality
system_prompt="Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    try:
        logger.info(f"Initializing AI agent with model: {llm_id}, provider: {provider}")
        
        if not GROQ_API_KEY:
            logger.error("GROQ_API_KEY is not set in environment variables")
            raise ValueError("GROQ_API_KEY is not set in environment variables")
        
        if provider=="Groq":
            try:
                logger.debug(f"Attempting to initialize ChatGroq with model: {llm_id}")
                llm=ChatGroq(
                    model=llm_id,
                    api_key=GROQ_API_KEY,
                    temperature=0.7,  # Added temperature parameter
                    max_tokens=1024   # Added max_tokens parameter
                )
                logger.info("Successfully initialized ChatGroq")
            except Exception as e:
                logger.error(f"Error initializing ChatGroq: {str(e)}")
                if "Invalid API Key" in str(e):
                    logger.error("The provided Groq API key appears to be invalid. Please check your API key.")
                raise ValueError(f"Failed to initialize Groq model: {str(e)}")
        else:
            raise ValueError("Only Groq provider is supported")

        tools=[TavilySearchResults(max_results=2)] if allow_search else []
        
        # Create messages list with system prompt and user query
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query[0] if isinstance(query, list) else query)
        ]
        
        logger.debug(f"Sending request to model with messages: {messages}")
        
        # Get response from the model
        try:
            response = llm.invoke(messages)
            logger.debug(f"Received response from model: {response}")
        except Exception as e:
            logger.error(f"Error getting response from model: {str(e)}")
            if "Invalid API Key" in str(e):
                logger.error("The provided Groq API key appears to be invalid. Please check your API key.")
            raise ValueError(f"Failed to get response from model: {str(e)}")
        
        if not response or not hasattr(response, 'content'):
            logger.error("Invalid response format from model")
            raise ValueError("Invalid response from model")
            
        return response.content
    except Exception as e:
        logger.error(f"Error in get_response_from_ai_agent: {str(e)}")
        raise ValueError(f"Error getting response from AI agent: {str(e)}")


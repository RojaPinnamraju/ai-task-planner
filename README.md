# 🧠 AI Task Planner & Personal Assistant

A powerful AI-powered task planning and personal assistant application that helps you organize, prioritize, and get smart suggestions for your tasks. Built with Streamlit for the frontend and FastAPI for the backend, this application leverages cutting-edge AI models from Groq and OpenAI to provide intelligent task management solutions.

## ✨ Features

- **Smart Task Planning**: Get AI-generated structured plans for your tasks
- **Multiple AI Providers**: Choose between Groq and OpenAI models
- **Customizable Assistant**: Define your assistant's behavior through system prompts
- **Web Search Integration**: Enable web search for enhanced task planning
- **Modern UI**: Clean and intuitive interface built with Streamlit
- **Flexible Model Selection**: Support for various AI models:
  - Groq: llama-3.3-70b-versatile, mixtral-8x7b-32768
  - OpenAI: gpt-4o-mini

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip or pipenv for package management

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd ai-agent-chatbot-copy
```

2. Install dependencies:
```bash
# Using pip
pip install -r requirements.txt

# Or using pipenv
pipenv install
```

3. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

### Running the Application

1. Start the backend server:
```bash
python backend.py
```

2. In a new terminal, start the frontend:
```bash
streamlit run frontend.py
```

3. Open your browser and navigate to `http://localhost:8501`

## 🛠️ Project Structure

- `frontend.py`: Streamlit-based user interface
- `backend.py`: FastAPI backend server
- `ai_agent.py`: Core AI agent implementation
- `styles.css`: Custom styling for the application
- `requirements.txt`: Python dependencies
- `.env`: Environment variables configuration

## 🤖 How to Use

1. Define your assistant's behavior in the system prompt text area
2. Select your preferred AI provider (Groq or OpenAI)
3. Choose a specific model from the available options
4. Enable web search if needed
5. Enter your tasks (one per line)
6. Click "Generate Plan" to get AI-generated task planning suggestions

## 📝 Example

Input tasks:
```
- Finish project proposal
- Buy groceries
- Schedule team meeting
```

The AI will generate a structured plan with:
- Prioritized tasks
- Suggested timeframes
- Additional recommendations
- Potential dependencies between tasks

## 🔧 Technologies Used

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **AI Integration**: 
  - Groq API
  - OpenAI API
  - LangChain
- **Styling**: CSS
- **Environment Management**: python-dotenv
# frontend.py
import streamlit as st
import requests

st.set_page_config(page_title="AI Task Planner", layout="centered")
st.title("🧠 AI Task Planner & Personal Assistant")
st.write("Organize, prioritize, and get smart suggestions for your tasks.")

system_prompt = st.text_area("Define the assistant's behavior:", height=70, placeholder="You are a smart planner...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select AI Provider:", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Enable Web Search")

task_input = st.text_area("📝 Enter your tasks (one per line):", height=200, placeholder="Example:\n- Finish project proposal\n- Buy groceries\n- Schedule team meeting")

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Generate Plan"):
    if task_input.strip():
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": task_input.strip().split("\n"),
            "allow_search": allow_web_search
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            try:
                data = response.json()
                if "error" in data:
                    st.error(data["error"])
                else:
                    st.subheader("📋 Your Smart Plan:")
                    st.markdown(data["structured_plan"])
            except Exception as e:
                st.error("⚠️ Failed to parse response")
                st.code(response.text)
        else:
            st.error(f"❌ API call failed with status code: {response.status_code}")

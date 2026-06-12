import streamlit as st
from openai import OpenAI

# ✅ Connect to local Ollama
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

# ✅ App title
st.set_page_config(page_title="Chat LLM Using Ollama")
st.title("💬 Chat LLM Using Ollama")

# ✅ Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "Give short, clear, and quick answers."
        }
    ]

# ✅ Input
user_input = st.text_input("You:")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="phi3",                # ✅ fast model
        messages=st.session_state.messages,
        max_tokens=100               # ✅ limits response → faster
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

# ✅ Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"👤 You: {msg['content']}")
    elif msg["role"] == "assistant":
        st.write(f"🤖 Bot: {msg['content']}")
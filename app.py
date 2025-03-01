import streamlit as st
from groq import Groq

# Set up the Groq client
client = Groq(api_key="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")

# Streamlit app UI
st.set_page_config(page_title="💰 Finance & Banking Chatbot", layout="wide")

# System prompt to enforce finance-related responses
SYSTEM_PROMPT = (
    "You are an expert financial assistant. Your role is to answer ONLY finance-related topics, including banking, investments, "
    "loans, credit cards, budgeting, and economic trends. "
    "If a user asks a question unrelated to finance, you MUST respond with: "
    "'I'm here to assist with financial topics only. Please ask me something related to banking, investments, or finance. 💰'"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I can help you with financial questions. How can I assist? 💳"}
    ]

# Main chat interface
st.title("💳 Finance & Banking Chatbot 🤵")

# Display previous messages in the chat area
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=("👦🏻" if msg["role"] == "user" else "🤵")):
        st.markdown(msg["content"])

# User input field
user_input = st.chat_input("Ask me about finance, banking, investments, etc. 📈")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="👦🏻"):
        st.markdown(user_input)

    # Get response from Groq API
    response = client.chat.completions.create(
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages,
        model="llama-3.3-70b-versatile",
        max_tokens=200,
    )

    bot_reply = response.choices[0].message.content

    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant", avatar="🤵"):
        st.markdown(bot_reply)

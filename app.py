import streamlit as st
import os
from dotenv import load_dotenv

# LangChain imports
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -------- LOAD ENV --------
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Missing GROQ_API_KEY")
    st.stop()

# -------- LLM --------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=api_key
)

# -------- PROMPT TEMPLATE --------
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Give clear and concise answers."),
    ("user", "{question}")
])

# -------- CHAIN --------
chain = prompt_template | llm | StrOutputParser()

# -------- PAGE CONFIG --------
st.set_page_config(page_title="AI Chatbot", layout="wide")

st.title("🤖 AI Chatbot")
st.caption("Your AI assistant powered by Groq + LLaMA 3.3")

# -------- SESSION --------
if "chats" not in st.session_state:
    st.session_state.chats = {}
    st.session_state.current_chat = None

# -------- SIDEBAR --------
with st.sidebar:
    st.title("💬 Chats")

    if st.button("➕ New Chat"):
        st.session_state.current_chat = None
        st.rerun()

    st.markdown("### Recents")

    for title in st.session_state.chats:
        if st.button(title, key=title):
            st.session_state.current_chat = title
            st.rerun()

# -------- CURRENT CHAT --------
if st.session_state.current_chat:
    messages = st.session_state.chats[st.session_state.current_chat]
else:
    messages = []

# -------- CSS --------
st.markdown("""
<style>
.chat-container {
    max-width: 900px;
    margin: auto;
}
.user-msg {
    background-color: #2563eb;
    color: white;
    padding: 12px;
    border-radius: 12px;
    margin: 10px 0;
    max-width: 70%;
    margin-left: auto;
}
.bot-msg {
    background-color: #1f2937;
    color: white;
    padding: 12px;
    border-radius: 12px;
    margin: 10px 0;
    max-width: 70%;
    margin-right: auto;
}
</style>
""", unsafe_allow_html=True)

# -------- DISPLAY --------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in messages:
    if isinstance(msg, HumanMessage):
        st.markdown(f'<div class="user-msg">{msg.content}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg.content}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# -------- INPUT --------
user_input = st.chat_input("Type your message...")

if user_input:

    # Create new chat if none exists
    if st.session_state.current_chat is None:
        title = user_input[:40] + ("..." if len(user_input) > 40 else "")
        st.session_state.current_chat = title
        st.session_state.chats[title] = []

    # Save user message
    st.session_state.chats[st.session_state.current_chat].append(
        HumanMessage(content=user_input)
    )

    try:
        # 🔥 Use chain instead of raw LLM
        response = chain.invoke({"question": user_input})

        st.session_state.chats[st.session_state.current_chat].append(
            AIMessage(content=response)
        )

    except Exception as e:
        st.error(str(e))

    st.rerun()
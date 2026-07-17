# My ChatBot

import streamlit as st
from openai import OpenAI

# -----------------------------------------------------------------------------
# Page Config
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Mini ChatGPT - Mistral",
    page_icon="🐯",
    layout="centered"
)

st.title("🐯 Sukku Mini ChatGPT (Mistral AI)")

# -----------------------------------------------------------------------------
# API Key
# -----------------------------------------------------------------------------
api_key = "fZekcLdoI27lYfG6WZDRNj8OCxK2H3v1"

# -----------------------------------------------------------------------------
# Initialize Mistral Client
# -----------------------------------------------------------------------------
client = OpenAI(
    api_key=api_key,
    base_url="https://api.mistral.ai/v1"
)

# -----------------------------------------------------------------------------
# Initialize Chat History
# -----------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]

# -----------------------------------------------------------------------------
# Display Previous Messages
# -----------------------------------------------------------------------------
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# -----------------------------------------------------------------------------
# Chat Input
# -----------------------------------------------------------------------------
prompt = st.chat_input("Type your message...")

if prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="mistral-small-latest",
                    messages=st.session_state.messages
                )

                reply = response.choices[0].message.content

                st.markdown(reply)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": reply
                    }
                )

            except Exception as e:
                st.error(f"Error: {e}")

# -----------------------------------------------------------------------------
# Sidebar
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("Options")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        ]
        st.rerun()

    st.markdown("---")
    st.write("**Model:** mistral-small-latest")

#---------------------------------------------------------------------------------

















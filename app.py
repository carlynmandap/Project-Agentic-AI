import streamlit as st
import ollama


st.set_page_config(page_title="Local Chat", page_icon="💬", layout="centered")

if "messages" not in st.session_state:
	st.session_state.messages = []

with st.sidebar:
	st.subheader("Local model")
	st.caption("Ollama connection will be added after setup.")

	if st.button("New chat", icon=":material/add_comment:", use_container_width=True):
		st.session_state.messages = []
		st.rerun()

st.title("Local Chat")
st.caption("A simple chat interface for your local model.")

for message in st.session_state.messages:
	with st.chat_message(message["role"]):
		st.markdown(message["content"])

prompt = st.chat_input("Message")

if prompt:
	st.session_state.messages.append({"role": "user", "content": prompt})
	with st.chat_message("user"):
		st.markdown(prompt)

with st.chat_message("assistant"):
    with st.spinner("Thinking..."):
        response = ollama.chat(
            model="qwen3:4b",
            messages=st.session_state.messages,
        )
        reply = response.message.content
        st.markdown(reply)

st.session_state.messages.append({"role": "assistant", "content": reply})

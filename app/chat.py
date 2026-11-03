
import logging

import streamlit as st
from google.genai.errors import ClientError, ServerError

st.set_page_config(
    page_title="Emporio da Musica AI",
    page_icon="🎸"
)

st.title("🎸 Empório da Música")
st.caption("AI-powered customer support assistant")

logger = logging.getLogger(__name__)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input(
    "Ask about instruments, orders or promotions..."
)

if question:
    history = st.session_state.messages.copy()

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Checking store information..."):
            try:
                from agent import chat

                answer = chat(question, history)

            except ServerError as error:
                logger.warning(
                    "Gemini service error: %s", error.code
                )
                st.warning(
                    "The AI service is temporarily unavailable. "
                    "Please try again shortly."
                )
                st.stop()

            except ClientError as error:
                logger.warning(
                    "Gemini client error: %s", error.code
                )
                st.error(
                    "The AI request could not be completed. "
                    "Please contact the application administrator."
                )
                st.stop()

            except Exception:
                logger.exception("Unexpected assistant error")
                st.error(
                    "An unexpected error occurred. "
                    "Please try again."
                )
                st.stop()

        st.markdown(answer)

    st.session_state.messages.extend([
        {"role": "user", "content": question},
        {"role": "assistant", "content": answer}
    ])

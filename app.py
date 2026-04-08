import streamlit as st

import praxa_rag


st.set_page_config(page_title="PraxaApp", page_icon=":performing_arts:", layout="centered")

st.title("PraxaApp")
st.caption("Ask questions about theater using the completed RAG backend.")

with st.sidebar:
    st.subheader("Setup")
    st.write("Set `OPENROUTER_API_KEY` in your shell before launching the app.")
    st.write("The app uses the local `chromadb` vector store already present in the repo.")

question = st.text_input(
    "Question",
    placeholder="What Broadway shows have had more than 10,000 performances?",
)

ask = st.button("Ask", type="primary")

if ask:
    if not question.strip():
        st.warning("Enter a question first.")
    else:
        with st.spinner("Searching context and generating an answer..."):
            try:
                result = praxa_rag.answer_and_sources(question.strip())
            except Exception as exc:
                st.error(str(exc))
            else:
                st.subheader("Answer")
                st.write(result["answer"])
                st.subheader("Sources")
                st.text(result["sources"] or "No sources returned.")

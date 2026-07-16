import streamlit as st

from utils.session_manager import initialize_session
from utils.document_processor import process_document

from ui.sidebar import show_sidebar
from ui.document_uploader import show_document_uploader
from ui.components.document_card import show_document_card
from ui.components.summary import show_summary
from ui.components.keywords import show_keywords
from ui.components.quiz import show_quiz

from ui.components.flashcards import show_flashcards
# from ui.components.translator import show_translation
# from ui.components.rag import show_chat

def run_dashboard():
    initialize_session()

    st.set_page_config(
        page_title="EduAssist",
        page_icon="📚",
        layout="wide"
    )

    show_sidebar()

    st.title("📚 EduAssist")
    st.caption(
        "Multilingual AI Learning Assistant"
    )
# calling uploader file
    uploaded_file = show_document_uploader()

    if uploaded_file is None:
        return
    if uploaded_file.name != st.session_state.get("current_file"):
        st.session_state.current_file = uploaded_file.name

        st.session_state.summary = None
        st.session_state.keywords = None
        st.session_state.quiz = None
        st.session_state.translation = None
        st.session_state.flashcards = None
        st.session_state.mindmap = None
        st.session_state.chat_history = []
        st.session_state.active_tool = "summary"

        data = process_document(uploaded_file)

        st.session_state.extracted_text = data["extracted_text"]
        st.session_state.cleaned_text = data["cleaned_text"]
        st.session_state.language_code = data["language_code"]
        st.session_state.language_name = data["language_name"]
        st.session_state.processing_time = data["processing_time"]


    show_document_card(uploaded_file)


    st.divider()

    st.subheader("🧠 AI Learning Tools")
    st.caption("Choose a feature to generate learning resources.")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button(
            "📝 Summary",
            use_container_width=True
        ):
            st.session_state.active_tool = "summary"

    with col2:
        if st.button(
            "🔑 Keywords",
            use_container_width=True
        ):
            st.session_state.active_tool = "keywords"

    with col3:
        if st.button(
            "📝 Quiz",
            use_container_width=True
        ):
            st.session_state.active_tool = "quiz"

    with col4:
        if st.button(
            "🗂 Flashcards",
            use_container_width=True
        ):
            st.session_state.active_tool = "flashcards"

    st.divider()

    st.subheader("📖 Output")
    tool = st.session_state.active_tool

    if tool == "summary":
        show_summary()

    elif tool == "keywords":
        show_keywords()

    elif tool == "quiz":
        show_quiz()

    elif tool == "flashcards":
        show_flashcards()
import streamlit as st

from flashcards.flashcard_generator import generate_flashcards
from ui.components.translation import show_translation


def show_flashcards():

    # --------------------------------------------------
    # Generate Flashcards
    # --------------------------------------------------

    if st.button(
        "🗂 Generate Flashcards",
        use_container_width=True
    ):

        if st.session_state.summary is None:

            st.warning("Please generate the summary first.")
            return

        if st.session_state.flashcards is None:

            with st.spinner("Generating Flashcards..."):

                st.session_state.flashcards = generate_flashcards(
                    st.session_state.summary
                )

            st.success("Flashcards Generated Successfully!")

        else:

            st.info("Flashcards already generated.")

    # --------------------------------------------------
    # Display Flashcards
    # --------------------------------------------------

    if st.session_state.flashcards is None:
        return

    flashcards = st.session_state.flashcards

    st.subheader("🃏 Flashcards")

    cols = st.columns(2)

    for i, card in enumerate(flashcards):

        with cols[i % 2]:

            with st.expander(f"Flashcard {i + 1}", expanded=False):

                st.markdown("**❓ Question**")
                st.write(card["question"])

                st.markdown("**✅ Answer**")
                st.success(card["answer"])

    # --------------------------------------------------
    # Translation
    # --------------------------------------------------

    flashcard_text = "\n\n".join(
        f"Question: {card['question']}\nAnswer: {card['answer']}"
        for card in flashcards
    )

    st.divider()

    show_translation(
        text=flashcard_text,
        key="flashcards"
    )
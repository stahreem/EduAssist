import streamlit as st


def display_flashcards(flashcards):

    """
    Display flashcards.
    """

    if not flashcards:

        st.warning("No flashcards generated.")

        return

    st.subheader("🃏 Flashcards")

    for i, card in enumerate(flashcards):

        with st.expander(f"Flashcard {i+1}"):

            st.markdown("### ❓ Question")

            st.write(card["question"])

            st.markdown("---")

            st.markdown("### ✅ Answer")

            st.success(card["answer"])
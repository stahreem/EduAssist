import streamlit as st

from flashcards.flashcard_generator import generate_flashcards
from flashcards.formatter import display_flashcards
from ui.components.translation import show_translation

def show_flashcards():

    if st.button(
        "🗂 Generate Flashcards",
        use_container_width=True
    ):

        if st.session_state.summary is None:

            st.warning(
                "Please generate the summary first."
            )
            return

        if st.session_state.flashcards is None:

            with st.spinner(
                "Generating Flashcards..."
            ):

                cards = generate_flashcards(
                    st.session_state.summary
                )

                st.session_state.flashcards = cards

            st.success(
                "Flashcards Generated Successfully!"
            )

        else:

            st.info(
                "Flashcards already generated."
            )

    if st.session_state.flashcards is not None:

        display_flashcards(st.session_state.flashcards)

    # st.write(type(st.session_state.flashcards))
    # st.write(st.session_state.flashcards)

        flashcards = st.session_state.flashcards
        flashcard_text = ""

        for card in flashcards:

            flashcard_text += (
                f"Question: {card['question']}\n"
                f"Answer: {card['answer']}\n\n"
            )

        show_translation(
            text=flashcard_text,
            key="flashcards"
        )
    
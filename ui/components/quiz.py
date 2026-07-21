import streamlit as st

from quiz.quiz_generator import generate_quiz
from quiz.parser import parse_quiz
from quiz.formatter import display_quiz
from ui.components.translation import show_translation


def show_quiz():

    if st.button(
        "📝 Generate Quiz",
        use_container_width=True
    ):

        if st.session_state.summary is None:

            st.warning("Please generate the summary first.")

        elif st.session_state.quiz is None:

            with st.spinner("Generating Quiz..."):

                raw_quiz = generate_quiz(
                    st.session_state.summary
                )

                quiz = parse_quiz(raw_quiz)

                st.session_state.quiz = quiz

            st.success("Quiz Generated Successfully!")

        else:

            st.info("Quiz already generated.")

    # ------------------------------------

    if st.session_state.quiz is not None:

        display_quiz(st.session_state.quiz)

        quiz_text = "\n\n".join(

            f"""Question: {q['question']}

{chr(10).join(q['options'])}

Answer: {q['answer']}"""

            for q in st.session_state.quiz
        )

        st.divider()

        show_translation(
            text=quiz_text,
            key="quiz"
        )
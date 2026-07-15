import streamlit as st


def display_quiz(quizzes):

    """
    Display quiz nicely.
    """

    if not quizzes:
        st.warning("No quiz generated.")
        return

    st.subheader("📝 Quiz")

    for i, quiz in enumerate(quizzes):

        st.markdown(f"### Question {i+1}")

        st.write(quiz["question"])

        choice = st.radio(

            label="",

            options=quiz["options"],

            key=f"quiz_{i}"

        )

        if st.button(

            f"Check Answer {i+1}",

            key=f"btn_{i}"

        ):

            if choice.startswith(quiz["answer"]):

                st.success("✅ Correct")

            else:

                st.error(

                    f"❌ Correct Answer: {quiz['answer']}"

                )

        st.divider()
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

            correct_letter = quiz["answer"].strip().upper()

            correct_option = next(
                (
                    option
                    for option in quiz["options"]
                    if option.startswith(correct_letter + ".")
                ),
                correct_letter
            )

            if choice.startswith(correct_letter + "."):
                st.success("✅ Correct")
            else:
                st.error(f"❌ Correct Answer: {correct_option}")

        st.divider()
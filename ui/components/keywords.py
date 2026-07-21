import streamlit as st

from keywords.keyword_extractor import extract_keywords
from ui.components.translation import show_translation


def show_keywords():

    if st.button(
        "🔑 Generate Keywords",
        use_container_width=True
    ):

        if st.session_state.summary is None:

            st.warning("Please generate the summary first.")
            return

        if st.session_state.keywords is None:

            with st.spinner("Extracting Keywords..."):

                st.session_state.keywords = extract_keywords(
                    st.session_state.cleaned_text
                )

            st.success("Keywords Generated Successfully!")

        else:

            st.info("Keywords already generated.")

    # -------------------------------------

    if st.session_state.keywords is None:
        return

    st.subheader("🔑 Extracted Keywords")

    cols = st.columns(4)

    for i, keyword in enumerate(st.session_state.keywords):

        with cols[i % 4]:
            st.success(keyword)

    keyword_text = ", ".join(
        st.session_state.keywords
    )

    st.divider()

    show_translation(
        text=keyword_text,
        key="keywords"
    )
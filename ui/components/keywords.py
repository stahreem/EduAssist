import streamlit as st

from keywords.keyword_extractor import extract_keywords


def show_keywords():

    if st.button("🔑 Generate Keywords", use_container_width=True):

        if st.session_state.summary is None:

            st.warning("Please generate the summary first.")

        elif st.session_state.keywords is None:

            with st.spinner("Extracting Keywords..."):

                keywords = extract_keywords(
                    st.session_state.cleaned_text
                )

                st.session_state.keywords = keywords

            st.success("Keywords Generated Successfully!")

        else:

            st.info("Keywords already generated.")

    # --------------------------

    if st.session_state.keywords is not None:

        st.subheader("🔑 Extracted Keywords")

        cols = st.columns(4)

        for i, keyword in enumerate(st.session_state.keywords):

            cols[i % 4].success(keyword)
import streamlit as st

def show_tabs(extracted_text, cleaned_text, summary):

    tab1, tab2, tab3 = st.tabs([
        "📝 AI Summary",
        "📄 Extracted Text",
        "🧹 Cleaned Text"
    ])

    with tab1:
        st.markdown("### AI Generated Summary")
        st.markdown(summary)

    with tab2:
        st.text_area(
            "Extracted Text",
            extracted_text,
            height=500
        )

    with tab3:
        st.text_area(
            "Cleaned Text",
            cleaned_text,
            height=500
        )
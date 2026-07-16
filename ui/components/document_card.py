import streamlit as st

def show_document_card(uploaded_file):

    st.success("📄 Document Processed Successfully")

    with st.expander("📄 Document Information", expanded=True):
        c1, c2, c3 = st.columns(3) 
        c1.metric( "Language", st.session_state.language_name ) 
        c2.metric( "Extracted Words", len(st.session_state.extracted_text.split()) ) 
        c3.metric( "Cleaned Words", len(st.session_state.cleaned_text.split()) ) 
        st.info(f"📁 {uploaded_file.name}")
        # st.write("**📁 File Name:**",uploaded_file.name)
        # st.write()

        # st.write("**🌍 Language:**",st.session_state.language_name)
        # st.write()

        # st.write("**📄 Extracted Words:**",len(st.session_state.extracted_text.split()))
        # st.write()

        # st.write("**🧹 Cleaned Words:**",len(st.session_state.cleaned_text.split()))
        # st.write()
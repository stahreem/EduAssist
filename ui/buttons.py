import streamlit as st

def summary_button():
    return st.button(
        "🚀 Generate Summary",
        use_container_width=True,
        type="primary"
    )


def future_buttons():

    st.markdown("### 🚀 Upcoming AI Features")

    c1, c2 = st.columns(2)

    with c1:
        st.button("🔑 Keywords", disabled=True, use_container_width=True)
        st.button("🧠 Flashcards", disabled=True, use_container_width=True)
        st.button("📝 Quiz", disabled=True, use_container_width=True)

    with c2:
        st.button("🗺 Mind Map", disabled=True, use_container_width=True)
        st.button("🌐 Translate", disabled=True, use_container_width=True)
        st.button("💬 Ask AI", disabled=True, use_container_width=True)
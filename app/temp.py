import sys
from pathlib import Path
import time

# ======================================================
# Add Project Root
# ======================================================

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# ======================================================
# Imports
# ======================================================

import streamlit as st

from preprocessing.pdf_reader import extract_text_from_pdf
from preprocessing.cleaner import clean_text
from preprocessing.language_detector import detect_language

from summarization.summarizer import summarize_text
from summarization.chunker import split_into_chunks

from evaluation.evaluator import evaluate_summary

from ui.sidebar import show_sidebar
from ui.buttons import summary_button
from ui.progress import ProgressTracker

# ======================================================
# Page Configuration
# ======================================================

st.set_page_config(
    page_title="EduAssist",
    page_icon="📚",
    layout="wide"
)

# ======================================================
# Session State
# ======================================================

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "metrics" not in st.session_state:
    st.session_state.metrics = None

if "language" not in st.session_state:
    st.session_state.language = ""

if "chunks" not in st.session_state:
    st.session_state.chunks = 0

# ======================================================
# Sidebar
# ======================================================

show_sidebar()

# ======================================================
# Header
# ======================================================

st.title("📚 EduAssist")

st.subheader("Multilingual AI Learning Assistant")

st.markdown("""
Upload a PDF document to

- 📄 Extract Text
- 🌍 Detect Language
- 🧹 Clean Text
- ✂ Chunk Large Documents
- 🤖 Generate AI Summary
""")

# ======================================================
# Upload PDF
# ======================================================

uploaded_file = st.file_uploader(
    "Choose a PDF File",
    type=["pdf"]
)

# ======================================================
# Main Pipeline
# ======================================================

if uploaded_file:

    st.success("✅ PDF Uploaded Successfully")

    st.write(f"**Filename:** {uploaded_file.name}")

    file_size = round(uploaded_file.size / 1024, 2)

    st.info(f"📦 File Size : {file_size} KB")

    st.divider()

    if summary_button():

        tracker = ProgressTracker()

        try:

            # ===========================================
            # Extraction
            # ===========================================

            tracker.update(10, "📄 Extracting text...")

            start = time.time()

            extracted_text = extract_text_from_pdf(uploaded_file)

            extraction_time = time.time() - start

            if not extracted_text.strip():

                tracker.error("No readable text found.")

                st.error(
                    "This appears to be a scanned PDF.\n\n"
                    "OCR Support will be added in Phase 5."
                )

                st.stop()

            # ===========================================
            # Language Detection
            # ===========================================

            tracker.update(25, "🌍 Detecting Language...")

            start = time.time()

            language_code, language_name = detect_language(extracted_text)

            detection_time = time.time() - start

            # ===========================================
            # Cleaning
            # ===========================================

            tracker.update(40, "🧹 Cleaning Text...")

            start = time.time()

            cleaned_text = clean_text(extracted_text)

            cleaning_time = time.time() - start

            # ===========================================
            # Chunking
            # ===========================================

            tracker.update(55, "✂ Splitting into Chunks...")

            chunks = split_into_chunks(cleaned_text)

            st.session_state.chunks = len(chunks)

            # ===========================================
            # Summarization
            # ===========================================

            tracker.update(
                65,
                f"🤖 Summarizing {len(chunks)} Chunks..."
            )

            start = time.time()
            print("===== BEFORE summarize_text =====")
            summary = summarize_text(cleaned_text)
            print("Summary length:", len(summary))
            print("Summary preview:")
            print(summary[:500])
            print("===== AFTER summarize_text =====")
            print("Summary type:", type(summary))
            print("Summary repr:", repr(summary))
            print("Summary length:", len(summary) if summary is not None else "None")
            summary_time = time.time() - start

            # ===========================================
            # Evaluation
            # ===========================================

            tracker.update(
                90,
                "📊 Evaluating Summary..."
            )

            metrics = evaluate_summary(
                extracted_text,
                summary
            )

            tracker.success(
                "✅ Summary Generated Successfully"
            )

            # ===========================================
            # Save Results
            # ===========================================

            st.session_state.summary = summary
            print("Saved to session state")
            print("Session summary length:", len(st.session_state.summary))

            st.session_state.metrics = metrics

            st.session_state.language = language_name

            st.session_state.extracted_text = extracted_text

            st.session_state.cleaned_text = cleaned_text

            st.session_state.processing_time = {
                "Extraction": extraction_time,
                "Detection": detection_time,
                "Cleaning": cleaning_time,
                "Summary": summary_time
            }

        except Exception as e:

            tracker.error("Something went wrong.")

            st.exception(e)

            st.stop()
            # ======================================================
# Display Results
# ======================================================
print("Checking session state...")
print("summary key exists:", "summary" in st.session_state)

if "summary" in st.session_state:
    print("Session summary length:", len(st.session_state.summary))
    
if "summary" in st.session_state and st.session_state.summary:

    st.divider()

    # ==================================================
    # Processing Time
    # ==================================================

    st.subheader("⚡ AI Processing Time")

    t1, t2, t3, t4 = st.columns(4)

    times = st.session_state.processing_time

    t1.metric(
        "Extraction",
        f"{times['Extraction']:.2f}s"
    )

    t2.metric(
        "Language",
        f"{times['Detection']:.2f}s"
    )

    t3.metric(
        "Cleaning",
        f"{times['Cleaning']:.2f}s"
    )

    t4.metric(
        "Summary",
        f"{times['Summary']:.2f}s"
    )

    st.divider()

    # ==================================================
    # Document Statistics
    # ==================================================

    from ui.statistics import show_statistics

    show_statistics(
        st.session_state.metrics,
        st.session_state.language,
        st.session_state.chunks,
        pages="Unknown",
        model="Qwen3:1.7B"
    )

    st.divider()

    # ==================================================
    # Summary Quality
    # ==================================================

    st.subheader("📈 Summary Evaluation")

    metrics = st.session_state.metrics

    quality = 100 - abs(metrics["compression"] - 70)

    quality = max(0, min(100, quality))

    q1, q2 = st.columns(2)

    q1.metric(
        "Summary Quality",
        f"{quality:.1f}%"
    )

    q2.metric(
        "Compression",
        f"{metrics['compression']}%"
    )

    st.progress(quality / 100)

    if quality >= 85:

        st.success("Excellent summary quality.")

    elif quality >= 70:

        st.info("Good summary quality.")

    else:

        st.warning("Summary may be too short or too long.")

    st.divider()

    # ==================================================
    # AI Output
    # ==================================================

    st.subheader("🤖 AI Results")

    from ui.tabs import show_tabs

    show_tabs(
        st.session_state.summary,
        st.session_state.extracted_text,
        st.session_state.cleaned_text
    )

    st.divider()

    # ==================================================
    # Future AI Features
    # ==================================================

    from ui.buttons import future_buttons

    future_buttons()

    st.divider()

    # ==================================================
    # Roadmap
    # ==================================================

    with st.expander("🚀 EduAssist Development Roadmap"):

        st.markdown("""
### ✅ Completed

- PDF Upload
- Text Extraction
- Language Detection
- Text Cleaning
- Chunk-based Summarization
- Summary Merging
- Local AI using Ollama
- Summary Evaluation
- Modern Dashboard UI

---

### 🔄 In Progress

- OCR for Scanned PDFs
- Keyword Extraction
- Translation

---

### 🛠 Planned

- Flashcards
- Quiz Generator
- Mind Maps
- AI Tutor
- PDF Question Answering (RAG)
- Export Summary (PDF/DOCX)
- Multi-language Interface
""")

    # ==================================================
    # Footer
    # ==================================================

    st.divider()

    st.caption(
        "EduAssist v0.2 • Built with Streamlit, Ollama, and Qwen3"
    )
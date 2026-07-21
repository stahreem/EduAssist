import pdfplumber


def extract_text_from_pdf(uploaded_file):

    pages = []

    try:

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:

                    pages.append(page_text)

        return "\n".join(pages)

    except Exception as e:

        raise RuntimeError(
            f"PDF Extraction Failed: {e}"
        )
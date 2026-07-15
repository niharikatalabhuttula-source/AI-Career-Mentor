import fitz  # PyMuPDF


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF file.
    Returns the extracted text as a string.
    """

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text
from fpdf import FPDF
from datetime import datetime
import os
import tempfile

def create_pdf_report(summary_text: str, inspector_name: str = "Anonymous") -> str:
    """
    Generates a PDF file from summary text.
    Returns the full path to the generated PDF.
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Mining Equipment Inspection Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Inspector: {inspector_name}", ln=True)
    pdf.cell(0, 10, f"Generated: {now}", ln=True)
    pdf.ln(10)

    # Add summary text
    pdf.multi_cell(0, 10, summary_text)

    # Save to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        pdf.output(tmp.name)
        return tmp.name

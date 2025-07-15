# main.py

import streamlit as st
from audio_utils.recorder import upload_audio
from transcriber.whisper_engine import transcribe_audio
from config import USE_CLOUD, GROQ_API_KEY
from summarizers import groq_api, phi3_local
from reports.report_generator import create_pdf_report

if "summary" not in st.session_state:
    st.session_state.summary = None



st.title("🛠️ Mining Inspection Assistant")
st.markdown("Upload an inspection voice note. The app will transcribe it.")

# Audio upload
audio_path = upload_audio()

if audio_path:
    st.success(f"Audio received ✅\n\nTranscribing...")
    transcript = transcribe_audio(audio_path, model_size="base")
    st.markdown("### 📝 Transcription Result:")
    st.text(transcript)

    if st.button("🧠 Generate Summary"):
        st.markdown("## 📋 Summary Report")

        if USE_CLOUD:
            st.session_state.summary = groq_api.summarize_with_groq(transcript, GROQ_API_KEY)
        else:
            st.session_state.summary = phi3_local.summarize_with_phi3(transcript)

        st.success("Summary generated successfully.")

# ✅ Move this part outside the button so it persists across reruns
if st.session_state.summary:
    st.text_area("Summary", st.session_state.summary, height=300)

    if st.button("📄 Download PDF Report"):
        pdf_path = create_pdf_report(
            summary_text=st.session_state.summary, 
            inspector_name="Field Engineer"
        )
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Click to Download PDF",
                data=f,
                file_name="inspection_report.pdf",
                mime="application/pdf"
            )

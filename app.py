
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mr Low's Marking Assistant v2.0", layout="wide")

st.title("Mr Low's Marking Assistant v2.0")

st.markdown("### 1. Upload Your Mark Scheme")
mark_scheme = st.file_uploader("Mark Scheme (.txt or .json format)", type=["txt", "json"])

st.markdown("### 2. Provide Student Answers")
input_mode = st.radio("Select input mode:", ["Type one answer", "Upload Excel file"])

if input_mode == "Type one answer":
    single_answer = st.text_area("Enter student answer")
    if st.button("Mark this answer"):
        st.success("Scored using semantic logic (simulated). Override available below.")
        st.dataframe(pd.DataFrame({
            "Point": ["P1", "P2"],
            "Matched": ["Yes", "No"],
            "Confidence": ["85%", "60%"],
            "Override": ["[ ] Confirm / [ ] Override", "[ ] Confirm / [ ] Override"],
            "Reason": ["-", "-"]
        }))
elif input_mode == "Upload Excel file":
    batch_file = st.file_uploader("Upload .xlsx file", type=["xlsx"])
    if batch_file:
        st.success("Batch file uploaded. Proceeding to scoring...")
        st.write("Showing scored responses (simulated table).")

st.markdown("### 3. Export Results")
if st.button("Download Export File"):
    st.success("Export file generated (simulated).")

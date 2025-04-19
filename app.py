
import streamlit as st

st.title("Mr Low's Marking Assistant v2.0")

st.markdown("### Upload your mark scheme and student answers")

uploaded_mark_scheme = st.file_uploader("Upload Mark Scheme", type=["txt"])
uploaded_answers = st.file_uploader("Upload Student Answers (.xlsx)", type=["xlsx"])

if uploaded_mark_scheme and uploaded_answers:
    st.success("Files received. Proceeding to mark based on semantic scoring...")
    st.info("This is a demo scaffold. Real logic should be implemented here.")

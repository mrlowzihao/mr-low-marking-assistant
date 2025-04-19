
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mr Low's Marking Assistant v2.0.1", layout="wide")

st.title("Mr Low's Marking Assistant v2.0.1")

st.markdown("## 1. Input Your Mark Scheme")

option = st.radio("Choose method:", ["Manual Entry", "Upload Mark Scheme File"])

if option == "Manual Entry":
    st.subheader("Manual Mark Scheme Entry")
    p1_text = st.text_input("Expected Idea (P1)")
    p1_weight = st.number_input("Weight for P1", min_value=0.0, step=0.5)
    p1_logic = st.selectbox("Logic (optional) for P1", ["None", "AND", "OR"])
    if p1_logic != "None":
        p1_alt = st.text_input(f"Second condition for P1 ({p1_logic})")

    show_p2 = st.checkbox("Add P2")
    if show_p2:
        p2_text = st.text_input("Expected Idea (P2)")
        p2_weight = st.number_input("Weight for P2", min_value=0.0, step=0.5)
        p2_logic = st.selectbox("Logic (optional) for P2", ["None", "AND", "OR"])
        if p2_logic != "None":
            p2_alt = st.text_input(f"Second condition for P2 ({p2_logic})")

    nullify_list = st.text_area("NULLIFY: Enter misconceptions (one per line)")
    penalty_list = st.text_area("PENALTY: Enter penalising facts (one per line)")

    if st.button("Submit Mark Scheme"):
        st.success("Mark scheme recorded.")

else:
    uploaded_scheme = st.file_uploader("Upload Mark Scheme File (.txt or .json)", type=["txt", "json"])
    if uploaded_scheme:
        st.success("Mark scheme uploaded successfully.")

st.markdown("---")
st.markdown("## 2. Input Student Responses")

student_input_mode = st.radio("Input Mode", ["Type One Answer", "Upload Excel (.xlsx)"])

if student_input_mode == "Type One Answer":
    student_answer = st.text_area("Enter Student Answer")
    if st.button("Mark Answer"):
        st.markdown("### Marking Result")
        result = {
            "Point": ["P1", "P2"],
            "Matched": ["Yes", "No"],
            "Confidence": ["85%", "60%"],
            "Override": ["[ ] Confirm / [ ] Override", "[ ] Confirm / [ ] Override"],
            "Reason": ["-", "-"]
        }
        st.dataframe(pd.DataFrame(result))

elif student_input_mode == "Upload Excel (.xlsx)":
    student_file = st.file_uploader("Upload file", type=["xlsx"])
    if student_file:
        st.success("Student responses uploaded. Placeholder for batch scoring.")

st.markdown("### Export")
if st.button("Download Export File"):
    st.success("Export file generated (simulated).")

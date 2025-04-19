
import streamlit as st

st.set_page_config(page_title="Mr Low's Marking Assistant v2.0.1", layout="wide")

st.title("Mr Low's Marking Assistant v2.0.1")

st.markdown("## Choose How to Input Your Mark Scheme")

option = st.radio("Select input method:", ["Manual Entry", "Upload Mark Scheme File"])

if option == "Manual Entry":
    st.subheader("Manual Mark Scheme Entry")

    st.markdown("### P1 (Required)")
    p1_text = st.text_input("Expected Idea (P1)")
    p1_weight = st.number_input("Weight for P1", min_value=0.0, step=0.5)
    p1_logic = st.selectbox("Logic (optional)", ["None", "AND", "OR"])
    if p1_logic != "None":
        p1_alt = st.text_input(f"Second condition for P1 ({p1_logic})")

    show_p2 = st.checkbox("Add P2")
    if show_p2:
        st.markdown("### P2")
        p2_text = st.text_input("Expected Idea (P2)")
        p2_weight = st.number_input("Weight for P2", min_value=0.0, step=0.5)
        p2_logic = st.selectbox("Logic for P2 (optional)", ["None", "AND", "OR"])
        if p2_logic != "None":
            p2_alt = st.text_input(f"Second condition for P2 ({p2_logic})")

    show_p3 = st.checkbox("Add P3")
    if show_p3:
        st.markdown("### P3")
        p3_text = st.text_input("Expected Idea (P3)")
        p3_weight = st.number_input("Weight for P3", min_value=0.0, step=0.5)
        p3_logic = st.selectbox("Logic for P3 (optional)", ["None", "AND", "OR"])
        if p3_logic != "None":
            p3_alt = st.text_input(f"Second condition for P3 ({p3_logic})")

    show_p4 = st.checkbox("Add P4")
    if show_p4:
        st.markdown("### P4")
        p4_text = st.text_input("Expected Idea (P4)")
        p4_weight = st.number_input("Weight for P4", min_value=0.0, step=0.5)
        p4_logic = st.selectbox("Logic for P4 (optional)", ["None", "AND", "OR"])
        if p4_logic != "None":
            p4_alt = st.text_input(f"Second condition for P4 ({p4_logic})")

    st.markdown("### NULLIFY")
    nullify_list = st.text_area("Enter misconceptions (one per line)")

    st.markdown("### PENALTY")
    penalty_list = st.text_area("Enter penalising facts (one per line)")

    if st.button("Submit Mark Scheme"):
        st.success("Mark scheme submitted. Proceed to student answer input.")

else:
    st.subheader("Upload Mark Scheme File")
    uploaded_file = st.file_uploader("Upload .txt or .json", type=["txt", "json"])
    if uploaded_file:
        st.success("File uploaded successfully. Proceed to student answer input.")

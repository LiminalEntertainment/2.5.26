import streamlit as st

st.write("What's 1 + 1?")
a1 = st.text_input("Enter answer:", key="q1")
if a1:
    st.write("Correct!" if a1 == "2" else "Wrong")

st.write("What's 2 × 5?")
a2 = st.text_input("Enter answer:", key="q2")
if a2:
    st.write("Correct!" if a2 == "10" else "Wrong")

st.write("What's 100 ÷ 10?")
a3 = st.text_input("Enter answer:", key="q3")
if a3:
    st.write("Correct!" if a3 == "10" else "Wrong")

st.write("What's 2⁵?")
a4 = st.text_input("Enter answer:", key="q4")
if a4:
    st.write("Correct!" if a4 == "32" else "Wrong")

st.write("What is x if: 2x + 5x = 161?")
a5 = st.text_input("Enter answer:", key="q5")
if a5:
    st.write("Correct!" if a5 == "23" else "Wrong")


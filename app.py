import streamlit as st
st.write("whats 1 + 1?")
answer = st.text_input("enter answer: ")
if answer == "2":
    st.write("Correct!")
elif answer != "2":
    st.write("Wrong")
st.write("whats 2 * 5?")
answer = st.text_input("enter answer: ")
if answer == "10":
    st.write("Correct!")
elif answer != "10":
    st.write("Wrong")
st.write("whats 100 / 10?")
answer = st.text_input("enter answer: ")
if answer == "10":
    st.write("Correct!")
elif answer != "10":
    st.write("Wrong")
st.write("whats 2^5?")
answer = st.text_input("enter answer: ")
if answer == "32":
    st.write("Correct!")
elif answer != "32":
    st.write("Wrong")
st.write("whats x equal to if: 2x + 5x = 161?")
answer = st.text_input("enter answer: ")
if answer == "23":
    st.write("Correct!")
elif answer != "23":
    st.write("Wrong")

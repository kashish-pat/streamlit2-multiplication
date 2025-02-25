import streamlit as st
a = st.number_input("enter number")
for i in range(1,11):
    st.write(i*a)
import streamlit as st
import groq as Groq
st.set_page_config(page_title='Student Profile',page_icon='👩‍🎓',layout='centered')
st.title("🎓Student Profile Application")
st.caption("Developed by Akshata Ganesh")

st.text_input('Student Name',' ')
st.text_input('USN/RollNumber',' ')


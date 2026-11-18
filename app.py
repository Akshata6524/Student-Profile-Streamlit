
import streamlit as st
import groq as Groq
st.set_page_config(page_title='Student Profile',page_icon='👩‍🎓',layout='centered')
st.title("🎓Student Profile Application")
st.caption("Developed by Akshata Ganesh")

st.text_input('Student Name',' ')
st.text_input('USN/RollNumber',' ')
st.selectbox('Department',['CSE','AI','ISE','EC','EEE','Cyber'])
st.radio('Current Year',['1st year','2nd year','3rd year','4th year'])
st.button('View My Profile')


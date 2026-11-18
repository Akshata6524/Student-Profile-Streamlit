
import streamlit as st

st.set_page_config(page_title='Student Profile',page_icon='👩‍🎓',layout='centered')
st.title("🎓Student Profile Application")
st.caption("Developed by Akshata Ganesh")

name=st.text_input('Student Name',' ')
usn=st.text_input('USN/RollNumber',' ')
dep=st.selectbox('Department',['CSE','AI','ISE','EC','EEE','Cyber'])
year=st.radio('Current Year',['1st year','2nd year','3rd year','4th year'])
st.button('View My Profile')
if st.button('View My Profile'):
  if name.strip() and usn.strip():
  st.success("Profile Created Successfully")

st.write("Student Name :",name)
st.write("USN :",usn)
st.write("Department :",dep)
st.write("Year :",year)


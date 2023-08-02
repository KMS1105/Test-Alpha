import streamlit as st

"""https://www.youtube.com/watch?v=8u2PngR2xpM, Terminal=streamlit run (File Path)"""

st.title("Test")

with st.form("form"):
    User_input = st.text_input("ID")
    User_input2 = st.text_input("PassWord")
    submit = st.form_submit_button("Submit")


if submit and User_input:
    with st.spinner("Wait..."):
        if User_input == 'abc' and User_input2 == 'abc':
            st.write('pass')
    
        else:
            st.write('ID나 PW가 일치 하지 않음')


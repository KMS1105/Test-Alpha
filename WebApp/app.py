import streamlit as st

"""https://www.youtube.com/watch?v=8u2PngR2xpM, Terminal=streamlit run (File Path)"""

tab1, tab2= st.tabs(['Tab A' , 'Tab B'])  
IDPW = []

with tab1:
    st.title("Test") 
    
    with st.form("MY_form"):
        User_setting = st.text_input("ID")
        User_setting2 = st.text_input("PassWord")
        submit = st.form_submit_button("Submit")


    if submit and User_setting and User_setting2:
        with st.spinner("Saving..."):
            IDPW.append([User_setting, User_setting2])
      
with tab2:   
    st.title("Test") 
    
    with st.form("form"):
        User_input = st.text_input("ID")
        User_input2 = st.text_input("PassWord")
        submit = st.form_submit_button("Submit")
             
    if submit and User_input and User_input2:
        with st.spinner("Saving..."):
            if [User_input, User_input2] == IDPW[0]:
                st.write('Pass')    
        
            else:
                st.write('ID나 PW가 일치 하지 않음')
                
                


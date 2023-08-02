import streamlit as st
import time

"""https://www.youtube.com/watch?v=8u2PngR2xpM, Terminal=streamlit run (File Path)"""

tab1, tab2= st.tabs(['Tab A' , 'Tab B'])  
IDPW = []

with tab1:
    st.title("Test") 
    
    with st.form("form1"):
        User_setting = st.text_input("ID")
        User_setting2 = st.text_input("PassWord")
        submit = st.form_submit_button("Submit")


    if submit and User_setting and User_setting2:
        with st.spinner("Saving..."):
            IDPW.append(User_setting)
            IDPW.append(User_setting2)
            time.sleep(0.1)
            st.write("Save!")
            st.write(IDPW)
      
with tab2:   
    st.title("Test") 
    
    with st.form("form2"):
        User_input = st.text_input("ID")
        User_input2 = st.text_input("PassWord")
        submit = st.form_submit_button("Submit")
             
    if submit and User_input and User_input2:
        with st.spinner("Wait..."):
            if User_input == IDPW[0] and User_input2 == IDPW[1]:
                st.write('Pass')    
        
            else:
                st.write('ID나 PW가 일치 하지 않음')
                
                


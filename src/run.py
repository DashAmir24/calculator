import streamlit as st


if 'result' not in st.session_state:
    st.session_state.result = '0'

st.title(':abacus: CALCULATOR')
box = st.empty()
''
col1, col2, col3, col4, col5, col6, *args= st.columns(12)
with col1:
    if st.button('1', use_container_width=True):
        st.session_state.result = '1'
    if st.button('4', use_container_width=True):
        st.session_state.result = '4'
    if st.button('7', use_container_width=True):
        st.session_state.result = '7'
    if st.button('=', use_container_width=True):
        st.session_state.result = '='

with col2:
    if st.button('2', use_container_width=True):
        st.session_state.result = '2'
    if st.button('5', use_container_width=True):
        st.session_state.result = '5'
    if st.button('8', use_container_width=True):
        st.session_state.result = '8'    
    if st.button('0', use_container_width=True):
        st.session_state.result = '0'

with col3:
    if st.button('3', use_container_width=True):
        st.session_state.result = '3'
    if st.button('6', use_container_width=True):
        st.session_state.result = '6'
    if st.button('9', use_container_width=True):
        st.session_state.result = '9'
    if st.button('.', use_container_width=True):
        st.session_state.result = '.'

with col5:
    if st.button('+', use_container_width=True):
        st.session_state.result = '+'
    if st.button('-', use_container_width=True):
        st.session_state.result = '-'
    if st.button('*', use_container_width=True):
        st.session_state.result = '*'
    if st.button('/', use_container_width=True):
        st.session_state.result = '/'

box.text_input('',value=st.session_state.result ,disabled=True)



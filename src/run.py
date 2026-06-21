import streamlit as st
from main import calculate
# st.markdown("""
#     <style>
#     html {zoom: 100%;}
#     </style>
# """, unsafe_allow_html=True)

if 'result' not in st.session_state:
    st.session_state.result = '0'
    input_number = ''
    st.session_state.point_checker = True
    st.session_state.operator = ''
    st.session_state.operation = False
    st.session_state.first_number = ''
    st.session_state.rank = 8

st.title(':abacus: CALCULATOR')
box = st.empty()
''
col1, col2, col3, col4, col5, col6, *args= st.columns(12)
with col1:
    if st.button('1', use_container_width=True):
        if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
        if len(st.session_state.result) < 8:
            st.session_state.result += '1'
        st.session_state.operation = False

    if st.button('4', use_container_width=True):
        if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
        if len(st.session_state.result) < 8:
            st.session_state.result += '4'
        st.session_state.operation = False

    if st.button('7', use_container_width=True):
        if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
        if len(st.session_state.result) < 8:
            st.session_state.result += '7'
        st.session_state.operation = False

    if st.button('=', use_container_width=True):
        st.session_state.result = '='

with col2:
    if st.button('2', use_container_width=True):
        if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
        if len(st.session_state.result) < 8:
            st.session_state.result += '2'
        st.session_state.operation = False

    if st.button('5', use_container_width=True):
        if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
        if len(st.session_state.result) < 8:
            st.session_state.result += '5'
        st.session_state.operation = False

    if st.button('8', use_container_width=True):
        if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
        if len(st.session_state.result) < 8:
            st.session_state.result += '8'
        st.session_state.operation = False

    if st.button('0', use_container_width=True):
        if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
        if len(st.session_state.result) < 8:
            st.session_state.result += '0'
        st.session_state.operation = False

with col3:
    if st.button('3', use_container_width=True):
        if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
        if len(st.session_state.result) < 8:
            st.session_state.result += '3'
        st.session_state.operation = False

    if st.button('6', use_container_width=True):
        if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
        if len(st.session_state.result) < 8:
            st.session_state.result += '6'
        st.session_state.operation = False

    if st.button('9', use_container_width=True):
        if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
        if len(st.session_state.result) < 8:
            st.session_state.result += '9'
        st.session_state.operation = False
    
    if st.button('.', use_container_width=True) and st.session_state.point_checker:
        st.session_state.point_checker = False
        st.session_state.result += '.'


with col5:
    if st.button('+', use_container_width=True):
        if st.session_state.operation:
            st.session_state.result = st.session_state.result[:-4]
        elif st.session_state.first_number:
            st.session_state.second_number = st.session_state.result
            st.session_state.result = calculate(st.session_state.first_number, st.session_state.operator, st.session_state.second_number)
            st.session_state.second_number = ''
            st.session_state.first_number = st.session_state.result
        else:
            st.session_state.first_number = st.session_state.result
        st.session_state.operation = True
        st.session_state.operator = '+'
        st.session_state.result += '   +'
    
    
    if st.button('-', use_container_width=True):
        if st.session_state.operation:
            st.session_state.result = st.session_state.result[:-4]
        elif st.session_state.first_number:
            st.session_state.second_number = st.session_state.result
            st.session_state.result = calculate(st.session_state.first_number, st.session_state.operator, st.session_state.second_number)
            st.session_state.second_number = ''
            st.session_state.first_number = st.session_state.result
        else:
            st.session_state.first_number = st.session_state.result
        st.session_state.operation = True
        st.session_state.operator = '-'
        st.session_state.result += '   -'

    if st.button('*', use_container_width=True):
        if st.session_state.operation:
            st.session_state.result = st.session_state.result[:-4]
        elif st.session_state.first_number:
            st.session_state.second_number = st.session_state.result
            st.session_state.result = calculate(st.session_state.first_number, st.session_state.operator, st.session_state.second_number)
            st.session_state.second_number = ''
            st.session_state.first_number = st.session_state.result
        else:
            st.session_state.first_number = st.session_state.result
        st.session_state.operation = True
        st.session_state.operator = '*'
        st.session_state.result += '   *'

    if st.button('/', use_container_width=True):
        if st.session_state.operation:
            st.session_state.result = st.session_state.result[:-4]
        elif st.session_state.first_number:
            st.session_state.second_number = st.session_state.result
            st.session_state.result = calculate(st.session_state.first_number, st.session_state.operator, st.session_state.second_number)
            st.session_state.second_number = ''
            st.session_state.first_number = st.session_state.result
        else:
            st.session_state.first_number = st.session_state.result
        st.session_state.operation = True
        st.session_state.operator = '/'
        st.session_state.result += '   /'

box.text_input('',value=st.session_state.result ,disabled=True,width=320)


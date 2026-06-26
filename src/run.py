import streamlit as st

from main import calculate


def num_input(number):
    if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
    if len(st.session_state.result) < 8:
            st.session_state.result += number
    st.session_state.operation = False

def opt_input(operator):
    if st.session_state.operation:
        st.session_state.result = st.session_state.result[:-4]
    elif st.session_state.first_number:
        st.session_state.second_number = st.session_state.result
        st.session_state.result = calculate(st.session_state.first_number, st.session_state.operator, st.session_state.second_number)
        st.session_state.second_number = ''
        st.session_state.first_number = st.session_state.result
    else:
        st.session_state.first_number = st.session_state.result
    if list(st.session_state.result)[-1] == '.':
        st.session_state.result = st.session_state.result[:-1]
    st.session_state.operation = True
    st.session_state.operator = operator
    st.session_state.result += '   ' + operator

if 'result' not in st.session_state:
    st.session_state.result = '0'
    st.session_state.operation = False
    st.session_state.first_number = ''

st.title(':abacus: CALCULATOR')
box = st.empty()
''
col1, col2, col3, col4, col5, col6, *args= st.columns(12)
with col1:
    if st.button('1', use_container_width=True):
        num_input('1')

    if st.button('4', use_container_width=True):
        num_input('4')

    if st.button('7', use_container_width=True):
        num_input('7')

    if st.button('=', use_container_width=True) and st.session_state.first_number and not st.session_state.operation:
        st.session_state.result = calculate(st.session_state.first_number, st.session_state.operator, st.session_state.result)
        st.session_state.first_number = ''

with col2:
    if st.button('2', use_container_width=True):
        num_input('2')

    if st.button('5', use_container_width=True):
        num_input('5')

    if st.button('8', use_container_width=True):
        num_input('8')

    if st.button('0', use_container_width=True):
        if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
        if len(st.session_state.result) < 8:
            st.session_state.result += '0'
        st.session_state.operation = False

with col3:
    if st.button('3', use_container_width=True):
        num_input('3')

    if st.button('6', use_container_width=True):
        num_input('6')

    if st.button('9', use_container_width=True):
        num_input('9')

    if st.button('.', use_container_width=True):
        if st.session_state.operation:
            st.session_state.result = '0.'
            st.session_state.operation = False
        elif '.' not in st.session_state.result:
            st.session_state.result += '.'

with col5:
    if st.button('+', use_container_width=True):
        opt_input('+')
    
    if st.button('-', use_container_width=True):
        opt_input('-')        

    if st.button('*', use_container_width=True):
        opt_input('*')        

    if st.button('/', use_container_width=True):
        opt_input('/')

with col6:
    if st.button('c', use_container_width=True):
         st.session_state.result = '0'
         st.session_state.operation = False
         st.session_state.first_number = ''
    if st.button('<-', use_container_width=True):
        if st.session_state.operation:
            st.session_state.result = st.session_state.result[:-4]
            st.session_state.operation = False
            st.session_state.first_number = ''
        elif st.session_state.result:
            st.session_state.result = st.session_state.result[:-1]
            if not st.session_state.result:
                st.session_state.result = '0'

if 'N' in list(st.session_state.result):
    st.session_state.result = st.session_state.result[:-1]
    box.text_input('',value=st.session_state.result ,disabled=True,width=320)
    st.session_state.result = '0'
    st.session_state.operation = False
    st.session_state.first_number = ''
else:
    box.text_input('',value=st.session_state.result ,disabled=True,width=320)

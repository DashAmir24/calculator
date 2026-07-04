import streamlit as st

from main import calculate

def storing_numbers(new_number: str):
    """
    Store the latest calculated result in the history list.

    Keeps only the last 10 calculated results.
    
    Args:
        new_number (str): The calculated result to be stored.
    """
    if len(st.session_state.history_num) > 10:
        del st.session_state.history_num[0]
    st.session_state.history_num.append(new_number)

def num_input(number: str):
    """
    Handle numeric button input.

    Clears the current display if a new operation has started
    or the display contains only the default value.
    """

    if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
    if len(st.session_state.result) < 8:
            st.session_state.result += number
            st.session_state.history_counter = -1
    st.session_state.operation = False

def opt_input(operator):
    """
    Handle arithmetic operator selection.

    If a previous operation exists, compute the intermediate
    result before storing the new operator.
    """
    if st.session_state.operation:
        st.session_state.result = st.session_state.result[:-4]
    elif st.session_state.first_number:
        st.session_state.second_number = st.session_state.result
        st.session_state.result = calculate(st.session_state.first_number, st.session_state.operator, st.session_state.second_number)
        storing_numbers(st.session_state.result)
        st.session_state.second_number = ''
        st.session_state.first_number = st.session_state.result
    else:
        st.session_state.first_number = st.session_state.result
    if list(st.session_state.result)[-1] == '.':
        st.session_state.result = st.session_state.result[:-1]
    st.session_state.operation = True
    st.session_state.operator = operator
    st.session_state.result += '   ' + operator
    st.session_state.history_counter = -1

def reset_cal():
    """
    Reset calculator state for a new calculation.
    """
    st.session_state.operation = False
    st.session_state.first_number = ''
    st.session_state.history_counter = -1

if 'result' not in st.session_state:
    st.session_state.result = '0'
    st.session_state.history_num = list()
    reset_cal()

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
        storing_numbers(st.session_state.result)
        st.session_state.history_counter = -1

with col2:
    if st.button('2', use_container_width=True):
        num_input('2')

    if st.button('5', use_container_width=True):
        num_input('5')

    if st.button('8', use_container_width=True):
        num_input('8')

    if st.button('0', use_container_width=True):
        num_input('0')

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
        st.session_state.history_counter = -1

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
        reset_cal()
    if st.button('<-', use_container_width=True):
        st.session_state.history_counter = -1
        if st.session_state.operation:
            st.session_state.result = st.session_state.result[:-4]
            reset_cal()
        elif st.session_state.result:
            st.session_state.result = st.session_state.result[:-1]
            if not st.session_state.result:
                st.session_state.result = '0'
    if st.button('H', use_container_width=True) and st.session_state.history_num:
        if len(st.session_state.history_num) >= abs(st.session_state.history_counter):
            st.session_state.result = st.session_state.history_num[st.session_state.history_counter]
            st.session_state.history_counter -= 1
        st.session_state.first_number = ''
        st.session_state.operation = False
    if st.button('Pi', use_container_width=True):
        if st.session_state.result == '0' or st.session_state.operation:
            st.session_state.result = ''
        if len(st.session_state.result) < 8:
            st.session_state.result = '3.141592'
        st.session_state.operation = False
        st.session_state.history_counter = -1

if 'N' in list(st.session_state.result):
    st.session_state.result = st.session_state.result[:-1]
    box.text_input('',value=st.session_state.result ,disabled=True,width=320)
    st.session_state.result = '0'
    reset_cal()
else:
    box.text_input('',value=st.session_state.result ,disabled=True,width=340)

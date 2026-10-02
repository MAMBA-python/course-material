import streamlit as st

if "count" not in st.session_state:
    st.session_state['count'] = 0

if st.button("Verhoog teller"):
    st.session_state['count'] += 1

st.write("Teller:", st.session_state['count'])

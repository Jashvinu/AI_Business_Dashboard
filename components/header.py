import streamlit as st

def render_header():
    """Render the application header"""
    col1, col2 = st.columns([6, 1])
    with col1:
        st.markdown("## Business Dashboard")
    with col2:
        st.selectbox("Select Company", ["Company 1", "Company 2", "Company 3"])
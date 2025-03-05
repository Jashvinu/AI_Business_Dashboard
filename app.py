import streamlit as st
from utils.page_config import setup_page_config, init_session_state, apply_custom_css
from components.header import render_header
from components.home import render_home
from components.project_tab import render_project_tab
from components.finance_tab import render_finance_tab
from components.data_tab import render_data_tab
from components.chat import render_chat_component

def main():
    # Setup page configuration
    setup_page_config()
    init_session_state()
    apply_custom_css()
    
    # Render header
    render_header()
    
    # Navigation tabs - now including Home as the first tab
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Home", "Project Management", "Finance & Reports", "Data Table"])
    
    # Render chat component in the sidebar
    render_chat_component()
    
    with tab1:
        render_home()
        
    with tab2:
        render_project_tab()
    
    with tab3:
        render_finance_tab()
    
    with tab4:
        render_data_tab()

if __name__ == "__main__":
    main()
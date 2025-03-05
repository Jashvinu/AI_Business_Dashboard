import streamlit as st

def setup_page_config():
    """Set up the page configuration"""
    st.set_page_config(layout="wide")
    if 'plotly_config' not in st.session_state:
        st.session_state.plotly_config = {
            'displayModeBar': False,
            'responsive': True
        }

def init_session_state():
    """Initialize all session state variables"""
    # Chat history for the chat tab only
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Ensure exports directory exists for image outputs
    import os
    os.makedirs("exports/charts", exist_ok=True)

def apply_custom_css():
    """Apply custom CSS styles to the application"""
    st.markdown("""
        <style>
        .stApp {
            background-color: #FAFAFA;
        }
        
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
        }
        
        .metric-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            margin: 10px 0;
        }
        
        .project-card {
            background-color: white;
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .status-badge {
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 12px;
        }
        
        .on-track {
            background-color: #E5F7F0;
            color: #047857;
        }
        
        .delayed {
            background-color: #FEF3C7;
            color: #B45309;
        }
        
        .meeting-item {
            display: flex;
            align-items: center;
            padding: 10px 0;
        }
        
        .meeting-dot {
            width: 8px;
            height: 8px;
            background-color: #E5E7EB;
            border-radius: 50%;
            margin-right: 10px;
        }

        .document-item {
            display: flex;
            align-items: center;
            padding: 15px;
            background-color: white;
            border-radius: 8px;
            margin: 10px 0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .filter-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            margin: 10px 0;
        }

        .data-table-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)